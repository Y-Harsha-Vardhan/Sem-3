
## Big-O Notation:

We count memory accesses, arithmetic operations (including comparisons), assignments, and jumps.
Time =  nT_Read + (3n+2)T_Arith + (2n+1)T__jump + T_return
Example:
```
int search(int* S, int n, int e) {
	// n is the length of the array S
	// We are looking for element e in S
	for (int i=0; i<n; i++) {
		if (S[i]==e) {return i;}
	}
	return -1; //Not found
}
```
The loop in the program will iterate n times. In each iteration, there will be:
one memory access S\[i], three arithmetic operations (i<n, S\[i]\==e, and i++), and two jumps.
At the initialization, there is an assignment i=0. For the loop exit , there will be one more comparison and jump.

##### A Better Search : Binary Search
-  *Input specification:* a **non-decreasing array** S and an element e
-  *Output specification:* Position of e in S. If not found, return -1.

```
int BinarySearch(int* S, int n, int e){
	// S is a sorted array
	int first = 0, last = n;
	int mid = (first + last)/2;
	while (first < last){
		if (S[mid] == e) return mid;
		if (S[mid] > e) last = mid;
		else first = mid + 1;
		mid = (last + first)/2;
	}
	return -1;
}
```
There will be k iterations, in each iteration the function follows the same path, there will be:
-  a memory access, S\[mid]
-  five arithmetic operations (first < last, S\[mid] \== e, S\[i] > e, first + last, and . ./2,)
-  one assignment, last = mid
-  three jumps because of two ifs and a loop exit
For loop exit there will be one additional comparison and a jump at the loop head.
In the initialization section, we have two assignments and two arithmetic operations.

Time = kT_Read + (6k+5)T_Arith + (3k+1)T_jump + T_return

![[Pasted image 20250617151028.png]]
![[Pasted image 20250617151104.png]]
![[Pasted image 20250617151817.png]]
![[Pasted image 20250617151839.png]]
![[Pasted image 20250617151902.png]]



## Tutorial Problems:

1. *The following is the code for insertion sort. Compute the exact worst-case running time of the code in terms of n and the cost of doing various machine operations.*
```
for(int j=1; j<n; j++){
	int key = A[j];
	int i = j-1;
	while(i>=0){
		if(A[i]>key){A[i+1]=A[i];}
		else break;
		i--;
	}
	A[i+1]=key;
}
```

2. *What is the time complexity of binary addition and multiplication ? How much time does it take to do unary addition ?*

3. 
![[Pasted image 20250617151312.png]]

4. 
![[Pasted image 20250617151514.png]]

5. *Prove that  O(log(n!)) = O(nlogn)*.

6. *In the dead of night, a master jewel thief is plotting the heist of a lifetime-stealing the most valuable Faberge Egg from a towering 100-story museum. Each floor of the building has an identical egg, but the higher the floor, the more valuable the egg becomes. However, there’s a catch. The thief can steal only one egg and she knows that the most valuable egg at the top may not survive a drop from such a great height. To avoid smashing her prized loot, she must identify the highest floor from which an egg can be dropped without breaking. Armed with two replica eggs from the museum’s gift shop-perfectly identical but utterly worthless-the thief devises a plan. These two eggs will be her test subjects, sacrificed in the pursuit of the perfect drop. But time is of the essence, and the thief can not afford to be caught by the museum guards. She needs to figure out the minimum number of test drops required to guarantee finding the highest safe floor. Once an egg is broken, it’s gone for good-no replacements, no second chances. She cannot use any other method to determine the sturdiness of the eggs.*
   *Give an algorithm for the thief to determine, with the least number of drops in the worst case, the highest floor from which an egg can be safely dropped without breaking?*


****

## Containers in C++

***A collection of C++ objects:***
```
- array
- vector<T>
- set<T>
- map<T,T>
- unordered_set<T>
- unordered_map<T,T>
```

##### Some examples of containers:
```
set<T>
- Unique element
- insert/erase/contains interface
- collection has implicit ordering among elements

map<T,T>
- Unique key-value pairs
- insert/erase interface
- collection has implicit orderin gamong keys
- Finding a key-value pair is not the same as accessing it
- Throws an exception if accessed using a non-existing key
```

***Axioms of abstract data type set***
```
- std::set<int> s; s.contains(v) == false
- s.insert(v); s.contains(v) == true
- x = s.contains(u); s.insert(v); s.contains(u) == x, where u != v
- s.erase(v); s.contains(v) == false
- x = s.contains(u); s.erase(v); s.contains(u) == x, where u != v
```


***Why write exceptions instead of handling the "unexpected" cases ?***
To avoid cumbersome code!
If no catch is written, the exception flows to the top, and the program fails.
Exceptions provide a succinct mechanism to handle all possible errors, with a few catches.

#### Vector vs. Array:
| ***Vector***                  | ***Array***         |
| ----------------------------- | ------------------- |
| Variable length               | Fixed length        |
| Primarily stack-like access   | Random access       |
| Allows random access          | Difficult to search |
| Difficult to search           | Low overhead        |
| Overhead of memory management |                     |

![[Pasted image 20250617160000.png]]
![[Pasted image 20250617160028.png]]
## Tutorial Problems:

1.  *What is the difference between "at" and "..\[..]" accesses in C++ maps ?*

2.  *C++ does not provide active memory management. However, smart pointers in C++ allow us the capability of  a garbage collector. The smart pointer classes in C++ are:*
```
- shared_ptr       - weak_ptr
- unique_ptr       - auto_ptr
```
Write programs that illustrate the differences among the above smart pointers.

3.  *Why do the following three writes cause compilation errors in the C++ 20 compiler ?*
```
class Node {
public:
	Node() : value(0) { }
	const Node& foo( const Node* x) const {
		value = 3;          // Not allowed because of _______
		x[0].value = 4;     // Not allowed because of _______
		return x[0];
	}
	int value;
};

int main() {
	Node x[3], y;
	auto& z = y.foo(x);
	z.value = 5;  // Not allowed because of _______
}
```

4. *Some of these containers have named requirements in their description. For example, "std::vector (for T other than bool) meets the requirements of Container, AllocatorAwareContainer (since C++11), SequenceContainer, ContiguousContainer (since C++17), and ReversibleContainer."                                                                      What are these ? Can you describe the meaning of these ? How are these conditions checked ?*

5.  *Can we write auto within the catch parameter ?*
```
int foo(int x) {
	try {throw 20;}
	catch (auto e) {
		cout << "An int exception occured. " << e << "\n";
	}
	return 0;
}
```

****
