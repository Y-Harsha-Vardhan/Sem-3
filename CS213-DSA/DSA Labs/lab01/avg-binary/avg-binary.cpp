#include "common.h"

int BinarySearch ( int * S , int n , int e ) {
  int iteration_count = 0;
  // Implement binary search here
  // instead of returning position return the number
  // of executed iterations of binary search.
  int left = 0, right = n-1;
  int mid = (left + right)/2;

  while(left < right) { 

    if (S[mid] == e) {
      break;
    }

    if (S[mid] > e) {
      left = mid+1;
      iteration_count++;
    }

    else {right = mid; iteration_count++;}

    mid = (left + right)/2;
  }
  
  return iteration_count+1;
}

double drive_binary_search(unsigned size) {
  // Initialize an array with distinct elements
  int S[size];
  for (unsigned i=0; i<size; i++){
    S[i] = size - i;
  }
  // search all elements stored in S and compute
  // the average number of iterations in binary search
  double val = 0;
  for (unsigned i=0; i<size; i++){
    val += BinarySearch(S, size, i+1);
  }
  double ans = val/size;
  return ans; 
}

