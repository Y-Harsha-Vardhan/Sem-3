// WRITE IMPLEMENTATIONS OF METHODS BELOW
#include <stdexcept>
#include "queue.h"

template <typename T>
Queue<T>::Queue() { }

template <typename T>
Queue<T>::~Queue() { }

template <typename T>
void Queue<T>::enqueue(T value) {
    first_stack.push(value);
}

template <typename T>
T Queue<T>::dequeue() {
    if (isEmpty()) throw std::invalid_argument("Empty Queue Dequeue Error");

    if (second_stack.isEmpty()) {
        while (!first_stack.isEmpty()) {
            second_stack.push(first_stack.pop());
        }
    }

    return second_stack.pop();
}

template <typename T>
T Queue<T>::peek() {
    if (isEmpty()) throw std::invalid_argument("Empty Queue Peek Error");

    if (second_stack.isEmpty()) {
        while (!first_stack.isEmpty()) {
            second_stack.push(first_stack.pop());
        }
    }

    return second_stack.peek();
}

template <typename T>
bool Queue<T>::isEmpty() {
    // CORRECT: check both stacks
    return first_stack.isEmpty() && second_stack.isEmpty();
}

template <typename T>
size_t Queue<T>::getSize() {
    // CORRECT: size is the sum of both stacks
    return first_stack.getSize() + second_stack.getSize();
}
