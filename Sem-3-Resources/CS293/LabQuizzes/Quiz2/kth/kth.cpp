#include "bst.h"
//
// You may use the following function to view the BST
//
//void printBST(Node* root);

struct NodeStack {
    Node* arr[1000];   // adjust size if tree can be bigger
    int top;
    NodeStack() : top(-1) {}
    void push(Node* n) { arr[++top] = n; }
    Node* pop() { return arr[top--]; }
    bool empty() { return top < 0; }
    Node* peek() { return arr[top]; }
};

int findKthSmallest(Node* root, int k) {
    NodeStack st;
    Node* curr = root;
    while (curr || !st.empty()) {
        while (curr) {
            st.push(curr);
            curr = curr->left;
        }
        curr = st.pop();
        if (--k == 0) return curr->data;
        curr = curr->right;
    }
    return -1;
}

int findKthLargest(Node* root, int k) {
    NodeStack st;
    Node* curr = root;
    while (curr || !st.empty()) {
        while (curr) {
            st.push(curr);
            curr = curr->right;
        }
        curr = st.pop();
        if (--k == 0) return curr->data;
        curr = curr->left;
    }
    return -1;
}
