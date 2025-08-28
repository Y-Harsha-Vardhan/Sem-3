#include "common.h"

int BinarySearch ( int * S , int n , int e ) {
  int first = 0, last = n, mid = (first + last) / 2;
  int iteration = 0;
  while (first < last) {
    iteration++ ;
    if (S[mid] == e) {
      // std::cout << "iteration = " << iteration << "\n";
      return iteration;
    }
    if (S[mid] < e) {
      last = mid;
    } else {
      first = mid + 1;
    }
    mid = (first + last) / 2;
  }
  return iteration;
}

double drive_binary_search(unsigned size) {
  //int S[size];
  // int* S = (int*)malloc(sizeof(int)*size );
  int* S = new int[size];
  for( unsigned i = 0; i < size; i++ ) {
    S[i] = size-i;
  }
  long long sum = 0;
  for(unsigned i = 0; i < size; i++) {
    unsigned result = BinarySearch ( S , size , S[i] );
    sum = result + sum;
  }
  return ((double)sum)/((double)size);
}

