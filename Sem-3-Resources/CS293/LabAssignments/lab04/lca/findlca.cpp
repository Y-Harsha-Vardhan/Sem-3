#include "tree.h"

// helper: compute depth of a node from root
int depth(TreeNode* node) {
    int d = 0;
    while (node != nullptr) {
        d++;
        node = node->parent;
    }
    return d;
}

// Function which returns lca node of given nodes 'a' and 'b'
TreeNode* TREE::findlca(TreeNode* a, TreeNode* b) {
    if (a == nullptr || b == nullptr) return nullptr;

    // Step 1: compute depths
    int da = depth(a);
    int db = depth(b);

    // Step 2: bring deeper one up
    while (da > db) {
        a = a->parent;
        da--;
    }
    while (db > da) {
        b = b->parent;
        db--;
    }

    // Step 3: climb together until meet
    while (a != b) {
        a = a->parent;
        b = b->parent;
    }

    return a; // LCA found
}
