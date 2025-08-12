#include "linked-list.h"

void LinkedList::reverse() {
    if (!head || !head->next) return;

    ListNode* prev = nullptr;   
    ListNode* curr = head;
    tail = head; 

    while (curr) {
        ListNode* nextNode = curr->next;
        curr->next = prev;
        prev = curr;
        curr = nextNode;
    }
    head = prev;
}

