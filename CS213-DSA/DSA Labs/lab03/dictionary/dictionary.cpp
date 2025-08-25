#include "dictionary.h"

//Implement dictionary here

Dictionary::Dictionary(){
    N = DICT_SIZE;
    A = new Entry[N];
    for (int i=0; i<N; i++) {
        A[i].key = NULL;
        A[i].value = 0;
    }
};

Dictionary::~Dictionary(){
    for (int i=0; i<N; i++) {
        if (A[i].key != NULL && A[i].key != (char*)-1) {
            free(A[i].key);
        }
    }
    delete[] A;
}


int Dictionary::hashValue(char key[]){
    
    /*** For testcases compliance use factor: 31
    and alpha: 0.6180339887 in your implementation 
    but you are free to use other values and see variation in hash plots ***/
    
    // compute hash
    double hash = 0;
    double const_A = 0.6180339887;

    int n;
    for (int i=0; key[i] != '\0'; i++) n = i;
    
    for (int i=n-1; i>=0; i--) {
        hash = hash*31 + key[i]*const_A;
        hash -= int(hash);
    }
    return (int)(N*(hash - int(hash)));
}

int Dictionary::findFreeIndex(char key[]){
    int hash = hashValue(key);
    for (int i=0; i<N; i++) {
        int index = (hash + i)%N;
        if (A[index].key == NULL || strcmp(A[index].key, "TOMBSTONE") == 0 || strcmp(A[index].key, key) == 0) return index;
    }
    return -1;
}

struct Entry* Dictionary::get(char key[]){
    int hash = hashValue(key);
    for (int i=0; i<N; i++) {
        int index = (hash + i)%N;
        if (A[index].key == NULL) return NULL;
        if (strcmp(A[index].key, key) == 0) return &A[index]; 
    }
    return NULL;
}

bool Dictionary::put(Entry e) {
    int index = findFreeIndex(e.key);
    if (index == -1) return false;
    A[index].key = strdup(e.key);
    A[index].value = e.value;
    return true; // Dummy return
}

bool Dictionary::remove(char key[]){
    int hash = hashValue(key);
    for (int i=0; i<N; i++) {
        int index = (hash + i)%N;
        if (A[index].key == NULL) return false;
        if (strcmp(A[index].key, key) == 0) {
            free(A[index].key);
            A[index].key = strdup("TOMBSTONE");
            return true;
        } 
    }
    return false; // Dummy return
}



