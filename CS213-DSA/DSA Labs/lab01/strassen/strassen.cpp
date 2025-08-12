#include "common.h"

// Add two matrices
Matrix add(const Matrix &A, const Matrix &B) {
  int n = A.size();
  Matrix C(n, vector<int>(n));
  // TODO
  for (int i = 0; i<n; i++) {
    for (int j=0; j<n; j++) {
      C[i][j] = A[i][j] + B[i][j];
    }
  } 
  return C;
}

// Subtract two matrices
Matrix subtract(const Matrix &A, const Matrix &B) {
  int n = A.size();
  Matrix C(n, vector<int>(n));
  // TODO
  for (int i = 0; i<n; i++) {
    for (int j=0; j<n; j++) {
      C[i][j] = A[i][j] - B[i][j];
    }
  } 
  return C;
}

// Naive O(N^3) matrix multiplication
Matrix naiveMultiply(const Matrix &A, const Matrix &B) {
  int n = A.size();
  Matrix C(n, vector<int>(n));
  // TODO
  for (int i = 0; i<n; i++) {
    for (int j=0; j<n; j++) {
      for (int k=0; k<n; k++) {
        C[i][j] += A[i][k]*B[k][j];
      }
    }
  } 
  return C;
}

// Strassen's matrix multiplication, use the reference for the algorithm
Matrix strassenMultiply(const Matrix &A, const Matrix &B, int threshold) {
  int n = A.size();
  Matrix C(n, vector<int>(n));
  // TODO
  if (n <= threshold) return naiveMultiply(A, B);

  int k = n/2;
  Matrix A11(k, vector<int>(k)), A12(k, vector<int>(k)), A21(k, vector<int>(k)), A22(k, vector<int>(k));
  Matrix B11(k, vector<int>(k)), B12(k, vector<int>(k)), B21(k, vector<int>(k)), B22(k, vector<int>(k));
  for (int i=0; i<k; i++) {
    for (int j=0; j<k; j++) {
      A11[i][j] = A[i][j];
      A12[i][j] = A[i][j+k];
      A21[i][j] = A[i+k][j];
      A22[i][j] = A[i+k][j+k];
    
      B11[i][j] = B[i][j];
      B12[i][j] = B[i][j+k];
      B21[i][j] = B[i+k][j];
      B22[i][j] = B[i+k][j+k];
    }
  }

  Matrix M1 = strassenMultiply(add(A11, A22), add(B11, B22), threshold);
  Matrix M2 = strassenMultiply(add(A21, A22), B11, threshold);
  Matrix M3 = strassenMultiply(A11, subtract(B12, B22), threshold);
  Matrix M4 = strassenMultiply(A22, subtract(B21, B11), threshold);
  Matrix M5 = strassenMultiply(add(A11, A12), B22, threshold);
  Matrix M6 = strassenMultiply(subtract(A21, A11), add(B11, B12), threshold);
  Matrix M7 = strassenMultiply(subtract(A12, A22), add(B21, B22), threshold);

  Matrix C11 = add(subtract(add(M1, M4), M5), M7);
  Matrix C12 = add(M3, M5);
  Matrix C21 = add(M2, M4);
  Matrix C22 = add(subtract(add(M1, M3), M2), M6);

  for (int i = 0; i < k; ++i) {
      for (int j = 0; j < k; ++j) {
          C[i][j] = C11[i][j];
          C[i][j + k] = C12[i][j];
          C[i + k][j] = C21[i][j];
          C[i + k][j + k] = C22[i][j];
      }
  }

  return C;
}


bool equal(const Matrix &A, const Matrix &B) {
    /*
        Returns True if the input matrices are equal and false otherwise
    */
    // TODO
  bool ans = true;
  int n = A.size();
  for (int i = 0; i<n; i++) {
    for (int j=0; j<n; j++) {
      if (A[i][j] != B[i][j]) {ans = false; return ans;}
    }
  } 
  return ans; 
}

