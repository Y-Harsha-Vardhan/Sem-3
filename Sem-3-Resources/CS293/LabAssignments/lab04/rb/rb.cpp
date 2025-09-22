#include "rb.h"
using ptr = RedBlackTree::ptr;

RedBlackTree::RedBlackTree() : root(nullptr) {}  
// ❌ before: root was uninitialized
// ✅ now: explicitly initialized to nullptr

const ptr RedBlackTree::getRoot() const
{ 
    return root; 
}

ptr RedBlackTree::insert(int data)
{
    ptr newnodePtr = new node(data);
    if (!root) {
        root = newnodePtr;
        root->color = 0; // set root color as black
        return newnodePtr;
    }
    // only does BST insert, no fixup
    insert(root, newnodePtr);
    return newnodePtr;
}

// auxiliary function to perform RBT insertion of a node
// ❌ before: you called fixup here as well, causing double fixup
// ✅ now: only performs BST insert (fixup will be called by main)
void RedBlackTree::insert(ptr start, ptr newnodePtr)
{
    ptr y = nullptr;
    ptr x = start;
    int a = newnodePtr->data;

    while (x != nullptr) {
        y = x;
        if (a < x->data) x = x->left;
        else x = x->right;
    }

    newnodePtr->parent = y;

    if (y == nullptr) root = newnodePtr;
    else if (a < y->data) y->left = newnodePtr;
    else y->right = newnodePtr;

    // ❌ removed fixup(newnodePtr) from here
    // ✅ because public insert() or main() should decide when to call it
}

// Credits to Adrian Schneider
// Use ASCII '|' (0x7C) instead of Unicode box-drawing '│' to avoid invisible codepoint mismatch
void RedBlackTree::printRBT(ptr start, const std::string& prefix, bool isLeftChild) const
{
    if (!start) return;

    std::cout << prefix;
    std::cout << (isLeftChild ? "|--" : "|__");
    // print value and color, then newline
    std::cout << start->data << "(" << start->color << ")" << (char)10;

    // NOTE: use "|   " (ASCII vertical bar + three spaces) not the Unicode '│' character
    printRBT(start->left,  prefix + (isLeftChild ? "|   " : "    "), true);
    printRBT(start->right, prefix + (isLeftChild ? "|   " : "    "), false);
}



// Function performing right rotation
void RedBlackTree::rightrotate(ptr x)
{
    ptr y = x->left;  
    // ❌ before: you nulled pointers and reassigned in a dangerous way
    // ✅ now: standard right rotation

    x->left = y->right;
    if (y->right != nullptr)
        y->right->parent = x;

    y->parent = x->parent;
    if (x->parent == nullptr)
        root = y;
    else if (x == x->parent->left)
        x->parent->left = y;
    else
        x->parent->right = y;

    y->right = x;
    x->parent = y;
}

// Function performing left rotation
void RedBlackTree::leftrotate(ptr x)
{
    ptr y = x->right;  
    // ❌ before: you nulled g->left / g->right which destroyed subtrees
    // ✅ now: standard left rotation

    x->right = y->left;
    if (y->left != nullptr)
        y->left->parent = x;

    y->parent = x->parent;
    if (x->parent == nullptr)
        root = y;
    else if (x == x->parent->left)
        x->parent->left = y;
    else
        x->parent->right = y;

    y->left = x;
    x->parent = y;
}

// This function fixes violations caused by RBT insertion
void RedBlackTree::fixup(ptr loc)
{
    while (loc != root && loc->parent->color == 1) {
        ptr p = loc->parent;
        ptr g = p->parent;

        if (p == g->left) {
            ptr u = g->right; // uncle
            if (u != nullptr && u->color == 1) {
                // ❌ before: no nullptr check on uncle
                // ✅ now: check u != nullptr
                g->color = 1;
                p->color = 0;
                u->color = 0;
                loc = g;
            } else {
                if (loc == p->right) {
                    loc = p;
                    leftrotate(loc);
                }
                p->color = 0;
                g->color = 1;
                rightrotate(g);
            }
        } else {
            // mirror case
            ptr u = g->left;
            if (u != nullptr && u->color == 1) {
                g->color = 1;
                p->color = 0;
                u->color = 0;
                loc = g;
            } else {
                if (loc == p->left) {
                    loc = p;
                    rightrotate(loc);
                }
                p->color = 0;
                g->color = 1;
                leftrotate(g);
            }
        }
    }
    root->color = 0;
}

void RedBlackTree::inorder(ptr start) const
{
    if (!start) return;
    inorder(start->left);
    std::cout << start->data << " ";
    inorder(start->right);
}

int main()
{
    int n; std::cin >> n;
    assert(n < 10000 && n >= 0);
    int a[10000];
    RedBlackTree tree;

    for (int i = 0; i < n; i++) {
        std::cin >> a[i];
        auto newnodePtr = tree.insert(a[i]);
        tree.fixup(newnodePtr);  // ✅ now called exactly once
    }
    tree.printRBT(tree.getRoot());

    return 0;
}
