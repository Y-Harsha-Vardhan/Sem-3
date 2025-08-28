#include <bits/stdc++.h>
using namespace std;

// Function provided to calculate modulo inverse of a wrt a prime P if needed
long long modulo_inverse(long long a, long long P) {
  return a <= 1 ? a : P - (long long)(P/a) * modulo_inverse(P % a, P) % P;
}

string permute_k(string s, long long k) {
  long long n = s.size();
  k %= n;
  return s.substr(k) + s.substr(0, k);
}

long long cyclic_shifts(string s){
    // Complete this function
    unordered_map<string, vector<long long>> perm;
    long long n = s.length();
    for (long long k=0; k<n; k++) {
      string p = permute_k(s, k);
      if (perm.find(p) != perm.end()) perm[p].push_back(k);
      else {
        vector<long long> a;
        a.push_back(k);
        perm[p] = a;
      }
    }
    return perm[s].size();
}

