
---

### 🎤  Script for Kasai's Algorithm

> Hello everyone. My name is Harsha and today I am going to talk about a few interesting algorithms that I have studied during this Summer's SoS under CS02: Advanced Algorithms for CP. The topics that I am going to talk about are: Kasai's Algorithm, HLD Algorithm, Centroid Decomposition and Li Chao Tree.  

>  First I’ll be explaining **Kasai’s Algorithm**, a powerful linear-time algorithm to compute the **Longest Common Prefix (LCP) array** from the **Suffix Array** of a string.

> First, a quick recap — a **suffix array** sorts all suffixes of a string lexicographically. The **LCP array** tells us how many characters two adjacent suffixes in this array share as a prefix.

> For example, for the string “banana”, suffixes like “anana” and “ana” have an LCP of “ana”, which is of length 3. Computing this naively takes O(n²), but Kasai’s algorithm brings it down to **O(n)** using a clever trick.

> The core idea is to avoid recomputing prefixes from scratch. We build an auxiliary array called `Rank[]`, which stores the position of each suffix in the suffix array. Then, for each suffix starting at position `i`, we find the previous suffix in sorted order and compare their characters. Once we find an LCP of length `k`, we store it, and for the next suffix, we start the comparison from `k-1`, since we already know the previous characters matched.

> This reuse of previously matched characters is what makes Kasai’s algorithm so efficient. Each character in the string is compared at most twice, leading to an overall time complexity of **O(n)**.

> This LCP array is extremely useful in applications like **string pattern matching**, **data compression**, and even in constructing **suffix trees** efficiently.

---

## 🎙️ ** Script for HLD**

> " Next I’ll be explaining an important tree decomposition technique known as **Heavy-Light Decomposition**, or HLD.

> Trees often come up in problems where we need to answer queries about paths—like finding the maximum value between two nodes, or updating a path. The problem is, such operations are hard to do efficiently unless we break the tree down smartly—and that’s exactly what HLD does.

> Here’s how it works: First, we look at the size of every subtree. For each node, we choose the child with the largest subtree as the **heavy child**, and the edge to it is a **heavy edge**. All other edges are **light edges**. This ensures that any time we move through a light edge, we significantly reduce the size of the remaining subtree.

> Because of this design, we can prove that from any node to the root, we’ll only cross **O(log N)** light edges. So if we decompose our tree into paths along heavy edges, we get a collection of disjoint paths where each path can be represented using a segment tree.

> Using this, we can reduce complex tree path queries to a series of range queries on a segment tree. For example, to get the maximum value between two nodes, we simply move up from both ends along heavy paths until we reach their lowest common ancestor, querying the segment tree along the way.

> This method has many applications, including efficient LCA finding, path sum queries, and dynamic programming on trees. It’s a go-to technique in competitive programming when dealing with large trees and dynamic operations.

> On the next slide, I’ve shown a visual of how a tree is broken into heavy and light edges, and how the paths are formed. This visual can help understand the recursive nature of HLD and how it's converted into a linear structure suitable for fast queries.

---
## 🎙️ ** Script for Centroid Decomposition **

> "Next I’ll walk you through an important tree decomposition technique called **Centroid Decomposition**.

> Unlike other techniques that process paths, centroid decomposition focuses on breaking down the tree by identifying _central balancing points_ called **centroids**.

> A **centroid** is a node which, when removed, splits the tree into smaller subtrees, none of which is larger than half the size of the original. This balancing property allows us to apply **divide-and-conquer** efficiently on trees.

> So how do we find the centroid? First, we compute the size of each subtree using a DFS. Then, starting from any node, we move to the largest child until no child has more than half the total size. That node is our centroid.

> After finding it, we remove it from the tree and repeat the process recursively on each resulting subtree. This forms a new hierarchical structure called the **centroid tree**. The centroid tree has a depth of O(log N), so it’s quite efficient.

> Why is this useful? Because many tree problems—like counting paths of certain lengths, computing distances with constraints, or answering range queries—can be solved much faster if we use this decomposition strategy instead of naïvely traversing the tree each time.

> On the next slide, you'll see a tree being decomposed step-by-step. First we calculate subtree sizes, then find the centroid, split the tree, and build the centroid tree. Visually, this helps understand how the original tree is simplified layer by layer.

> Centroid decomposition is widely used in competitive programming and research problems dealing with trees, especially where path constraints or efficient divide-and-conquer is needed.

---
## 🎙️ ** Script for Li Chao Tree **

> "Next I’ll be presenting a powerful data structure called the **Li Chao Tree**.

> It’s designed to handle a dynamic set of **linear functions** and efficiently answer queries like: _What is the minimum value among all these lines at some x?_

> This is particularly useful in **dynamic programming optimizations** where transitions involve linear costs, or in problems where the cost function is a straight line.

> The idea is to build a **segment tree** over a fixed x-coordinate range. Each node of this tree represents a segment of the x-axis and stores the best line for that segment.

> When we insert a new line, we compare it with the currently stored line at the midpoint of the segment. The better line stays at the current node, and the other line is recursively inserted into the half where it performs better.

> When we query the minimum or maximum y-value at a point x, we simply traverse down the segment tree. At each node, we evaluate the stored line at x and keep track of the best answer.

> The beauty of the Li Chao Tree is in its efficiency—both insertion and query are done in O(log X), which is very fast for large data.

> On the next slide, I’ve shown a diagram where two lines are inserted and compared, and how a query walks through the segment tree to find the optimal line for a given x.

> Li Chao Tree is a brilliant example of combining geometry with data structures to solve advanced optimization problems.

> Thank you!"

---
