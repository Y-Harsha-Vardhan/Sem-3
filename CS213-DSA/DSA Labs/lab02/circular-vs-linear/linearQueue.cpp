#include "queue.h"

using namespace std;

template <typename T> bool DynamicQueue<T> :: isEmpty() {
  return head == tail; 
}

template <typename T> bool DynamicQueue<T> :: isFull() {
  return size() == N; 
}

template <typename T> void DynamicQueue<T> :: grow() {
  unsigned int newSize = nextSize();
  T* newArray = new T[newSize];

  unsigned int count = size();
  for (unsigned int i=0; i<count; i++) newArray[i] = A[head + i];
  delete[] A;
  A = newArray;
  head = 0;
  tail = count;
  N = newSize;
}

template <typename T> unsigned int DynamicQueue<T> :: size() {
  return tail - head; 
}

template <typename T> void DynamicQueue<T> :: QInsert(T x) {
  if (isFull()) {
        grow();
    } else if (tail == N && head > 0) {
        // shift only when we've reached end but still have free space at front
        unsigned int count = size();
        for (unsigned int i = 0; i < count; i++) {
            A[i] = A[head + i];
        }
        head = 0;
        tail = count;
    }
    A[tail++] = x;
}

template <typename T> bool DynamicQueue<T> :: QDelete(T* x) {
  if (isEmpty()) return false;
  *x = A[head++];
  return true;
}
