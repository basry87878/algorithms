#include <bits/stdc++.h> 
#include<iostream>
using namespace std;

// greedy algorithm code in c++ 
int D[] = { 1, 5,12,25 };
int n = sizeof(D) / sizeof(D[0]);

void findMin(int V)
{
	// Initialize result 
	vector<int> ans;

	// Traverse through all denomination 
	for (int i = n - 1; i >= 0; i--)  // Loops n times
	{
		// Find denominations 
		while (V >= D[i])
		{
			V -= D[i];
			ans.push_back(D[i]);
		}
	}

	// Print result 
	for (int i = 0; i < ans.size(); i++)
		cout << ans[i] << "  ";
}

// main function
int main()
{
	int n = 16;
	cout << " min number: " << n << ": ";
	findMin(n);
	return 0;
}