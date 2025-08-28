# Problem: alloc
Let’s revisit vectors. When a vector is declared without specifying a size, it starts empty. However, it still allocates some initial space in anticipation of new elements being added. As we continue adding elements, there will come a point when the allocated memory is exhausted. At that point, the vector needs to allocate more memory.

Your task is to write code that detects the size at which new allocations occur and determines the amount of additional memory being allocated.

Keep in mind that when a vector reallocates memory:

It not only requires extra space,

- But also relocates all existing elements to ensure contiguous memory.
- This reallocation takes time, which we can measure.

We can also estimate the cost associated with each memory allocation.

# Your Task
In alloc.cpp, write the body of the specified function to perform this analysis.

# Input/Output

Input (stdin):
Two non-negative numbers:
- The maximum size of the vector to grow to
- The number of repetitions of the experiment for averaging

Output (stdout):
- A table of vector sizes and the corresponding average clock cycles taken to insert an element.


# Files to Edit [Do not edit any other files]

alloc.cpp
