// link - https://practice.geeksforgeeks.org/problems/subarray-with-given-sum-1587115621/1?page=1&company[]=Google&sortBy=submissions

//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;
// } Driver Code Ends

class Solution
{
    public:
    //Function to find a continuous sub-array which adds up to a given number.
    vector<int> subarraySum(int arr[], int n, long long s)
    {
        // Your code here
        int left =0, right = 0;
        long long sum =arr[0];
        vector<int> ans(2,0);
        while (right < n){
            // cout << "sum "<<sum <<endl;
            if (left >right) {
                
            }
            if (sum == s) break;
            else if (sum < s) {
                right++;
                sum += arr[right];
            }
            else {
                if (left == right) {
                    if  (right == n-1) break;
                    left++;
                    right++;
                    sum = arr[right];
                }
                else {
                    sum -= arr[left];
                    left++;
                }
            }
        }
        if (sum != s) return vector<int> (1,-1);
        // cout << left << " " << right<<endl;
        ans[0] = left+1;
        ans[1] = right+1;
        
        return ans;
        
    }
};

//{ Driver Code Starts.

int main()
 {
    int t;
    cin>>t;
    while(t--)
    {
        int n;
        long long s;
        cin>>n>>s;
        int arr[n];
        const int mx = 1e9;
        for(int i=0;i<n;i++)
        {
            cin>>arr[i];
        }
        Solution ob;
        vector<int>res;
        res = ob.subarraySum(arr, n, s);
        
        for(int i = 0;i<res.size();i++)
            cout<<res[i]<<" ";
        cout<<endl;
        
    }
	return 0;
}
// } Driver Code Ends