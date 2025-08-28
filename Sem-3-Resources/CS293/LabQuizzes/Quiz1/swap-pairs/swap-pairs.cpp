#include "swap-pairs.h"

// In this question, you have to reverse the adjacent nodes of a singly linked list.
// The nodes will have only the data and the link of the link node.
// In last node, the link part of the node will be nullptr.
// 'head' is a pointer that holds the address of the first node of the linked list.
// If the linked list is empty or contains one element you don't need to reverse.
// You have to reverse the adjacent nodes and do not swap the values of the adjacent nodes.

// For example:
// If a linked list contains:
// 22 50 17 95 62 31 79 34 53 66 86 87 48 25 4
// The resulting linked list should contain:
// 50 22 95 17 31 62 34 79 66 53 87 86 25 48 4

// For more examples, please look at testcases folder

void reverseAdjacentNodes(Node*& head) {
    if (head == nullptr || head->link == nullptr) return;

    Node dummy(0) ;   // helper node before head
    dummy.link = head;
    Node* prev = &dummy;

    while (prev->link != nullptr && prev->link->link != nullptr) {
        Node* first = prev->link;
        Node* second = first->link;

        // swap
        first->link = second->link;
        second->link = first;
        prev->link = second;

        // move forward
        prev = first;
    }

    head = dummy.link;
  
}
