#include "linked-list.h"

void LinkedList::reverse()
{
  // TODO: Implement the linked list reversal function
  // Don't forget to set tail ptr correctly as well !

  // DO NOT ALLOCATE ANY MEMORY

    if (!head || !(head->next)) return;
    tail = head;

    ListNode* prev = nullptr;
    ListNode* curr = head;
    while (curr) {
        auto nxt = curr->next;
        curr->next = prev;
        prev = curr;
        curr = nxt;
    }
    head = prev;
}
