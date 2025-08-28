# Problem: reverse-linked-list

We have a `LinkedList` class (defined in `list-node.h` and `reverse-linked-list.h`) that supports basic operations. Your goal is to implement its in-place `reverse()` method so that the list’s order is flipped, and both `head` and `tail` pointers remain correct.

# Your Task
In **linked-list.cpp**:
- Complete the body of `LinkedList::reverse()` so that it reverses the list in O(n) time and O(1) extra space.

# Input/Output

The provided `main.cpp` (do **not** edit) does the following:
- **Input** (stdin):
  1. An integer `n` (the number of nodes, `n ≥ 0`).
  2. `n` space-separated integers (the node values in insertion order).
- **Behavior**:
  1. Builds a `LinkedList` by calling `push_back` on each input value.
  2. Prints `Original: ` then the list contents.
  3. Calls your `reverse()`.
  4. Prints `Reversed: ` then the reversed list.
- **Output** (stdout):
  - Two lines starting with `Original: ` and `Reversed: ` followed by space-separated values (or a blank line if the list is empty).

# Files to Edit [Do not edit any other files]

- **reverse.cpp**  
  Locate the `// TODO: Implement the linked list reversal function` marker and fill in the `reverse()` method there.
  
  You cannot allocate any memory on heap in reverse.cpp.

_All other files (`main.cpp`, `list-node.h`, `linked-list.cpp`, `linked-list.h`, etc.) are provided and should remain unchanged._  
