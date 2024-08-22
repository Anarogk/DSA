#include<bits/stdc++.h>
using namespace std;
// Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].
// Return the array in the form [x1,y1,x2,y2,...,xn,yn].
vector<int> shuffle(vector<int>& nums, int n) {
    int j = n;
    vector<int> ans;
    for( int i = 0; i< n; i++) {
        printf("%d %d\n", i, j);
        ans.push_back(nums[i]);
        ans.push_back(nums[j]);
        j+=1;
    }
    return ans;
}


int main() {
    int n = 3;
    vector<int> nums = {1,2,3,4,5,6};
    vector<int> ans = shuffle(nums, n);
    for(int i = 0; i< 2*n; i++) {
        cout<<ans[i]<<" ";
    }
    return 0;
}