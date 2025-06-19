#### Following are the implementations of the above mentioned Algorithms:
<br>

### Merge Sort:
**Features:** Divide-and-Conquer, Stable, O(nlogn)
Merge Sort recursively splits the array into halves, sorts them, and merges the sorted halves.
**Implementation:**
```
#include<bits/stdc++.h>
using namespace std;

void merge(vector<int>& arr, int left, int mid, int right) {
	int n1 = mid-left+1;
	int n2 = right-mid;
	vector<int> L(n1), R(n2);

	for(int i=0; i<n1; i++) L[i] = arr[left+1];
	for(int j=0; j<n2; j++) R[j] = arr[mid+1+j];
	int i=0, j=0, k=left;
	while(i < n1 && j < n2){
		if(L[i] <= R[j]) {arr[k] = L[i]; i++;}
		else {arr[k] = R[j]; j++;}
		k++;
	}
	while(i < n1){
		arr[k] = L[i];
		i++; k++;	
	}
	while(j < n2){
		arr[k] = R[j];
		j++; k++;
	}
}

void mergeSort(vector<int>& arr, int left, int right){
	if (left >= right) return;
	int mid = left + (right-left)/2;
	mergeSort(arr, left, mid);
	mergeSort(arr, mid+1, right);
	merge(arr, left, mid, right);
}

void mergeSort(vector<int>& arr) {mergeSort(arr, 0, arr.size()-1);}
```

<br><br>

### Binary Search:
There are two implementations, one is *iterative* and the other is *recursive*
**Features:** Average Time Complexity is O(logn), Space Complexity is O(1) for *iterative* and it is O(logn) for *recursive*.
**Iterative Implementation:**
```
#include<bits/stdc++.h>
using namespace std;

int binarySearch (const vector<int>& arr, int target){
	int left = 0;
	int right = arr.size() - 1;
	while (left <= right){
		int mid = left + (right - left)/2;
		if (arr[mid] == target) return mid;
		else if (arr[mid] < target) left = mid + 1;
		else right = mid - 1;
	}
	return -1;
}
```

**Recursive Implementation:**
```
#include<bits/stdc++.h>
using namespace std;

int binarySearch(const vector<int>& arr, int target, int left, int right){
	if (left > right) return -1;
	int mid = left + (right - left)/2;
	if (arr[mid] == target) return mid;
	else if (arr[mid] < target){
	return binarySearch(arr, target, mid+1, right);}
	else {
	return binarySearch(arr, target, left, mid-1);}
}

int binarySearch(const vector<int>& arr, int target) {
	return binarySearch(arr, target, 0, arr.size() - 1);
}
```

<br><br>

### Dijkstra Algorithm:
**Problem Statement:**
Given a graph and a source node, find the shortest path from the source to all other nodes.
**Features:**
O((V+E)logV) is the *Time Complexity* with a priority queue (where V = nodes, E = edges).
O(V) is the *Space Complexity*.
**Implementation:**
```
#include<bits/stdc++.h>
using namespace std;
typedef vector<vector<pair<int, int>>> Graph;

vector<int> dijkstra(const Graph& graph, int src) {
	int n = graph.size();
	vector<int> dist(n, INT_MAX);
	dist[src] = 0;

	priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
	pq.push({0, src});

	while (!pq.empty()) {
		int u = pq.top().second;
		int current_dist = pq.top().first;
		pq.pop();

		if (current_dist > dist[u]) continue;

		for (const auto& edge : graph[u]) {
			int v = edge.first;
			int weight = edge.second;

			if (dist[u] + weight < dist[v]) {
				dist[v] = dist[u] + weight;
				pq.push({dist[v], v});
			}
		}
	}
	
	return dist;
}
```

<br><br>

### Binary Lifting for LCA:
**Problem Statement:**
Given a tree (acyclic undirected graph) and multiple queries of the form (u, v), find the lowest common ancestor of nodes u and v.
**Features:**
Time Complexity:
	-  *Preprocessing:* O(NlogN) 
	-  *LCA Query:* O(logN) per query.
Space Complexity: O(NlogN)

**Implementation:**
```
#include<bits/stdc++.h>
using namespace std;

class BinaryLiftingLCA {
	int n, log_max;
	vector<vector<int>> up;
	vector<int> depth;
public:
	BinaryLiftingLCA(const vector<vector<int>>& tree, int root) {
		n = tree.size();
		log_max = log2(n) + 1;
		up.assign(n, vector<int>(log_max, -1));
		depth.resize(n);
		dfs(tree, root, -1);
	}

	void dfs(const vector<vector<int>>& tree, int u, int parent) {
		up[u][0] = parent;
		for (int k=1; k<log_max; k++) {
			if (up[u][k-1] != -1) {
				up[u][k] = up[ up[u][k-1] ][k-1];}
		}
		for (int v : tree[u]) {
			if (v != parent) {
				depth[v] = depth[u] + 1;
				dfs(tree, v, u);
			}	
		}
	}

	int lift(int u, int steps) {
		for (int k=0; k<log_max; k++) {
			if (steps& (1 << k)) {
				u = up[u][k];
				if (u == -1) break;
			}
		}
		return u;
	}

	int lca(int u, int v) {
		if (depth[u] < depth[v]) swap(u, v);
		u = lift(u, depth[u] - depth[v]);
		if (u == v) return u;
		for (int k=log_max-1; k>=0; k--) {
			if (up[u][k] != up[v][k]) {
				u = up[u][k];
				v = up[v][k];
			}
		}
		return up[u][0];
	}
}
```

