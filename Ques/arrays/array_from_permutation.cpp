#include<bits/stdc++.h>
using namespace std;

class Solution {
public:

    // Given a zero-based permutation nums (0-indexed), build an array ans of the 
    // same length where ans[i] = nums[nums[i]] for each 0 <= i < nums.length and return it.
    // A zero-based permutation nums is an array of distinct integers from 0 to nums.length - 1 (inclusive).
    vector<int> buildArray(vector<int>& nums) {
        vector<int> ans(nums.size());
        for (int i : nums) {
            ans[i] = nums[nums[i]];
        };
        return ans;
        
    };
};


int main() {
    vector<int> nums = {0, 3, 1, 4, 6, 5, 7, 2};
    Solution obj;
    vector<int> ans = obj.buildArray(nums);
    printf("The array is: ");
    for (int i : ans) {
        printf("%d ", i);
    };
    // output: "The array is: 0 4 3 6 7 5 2 1"
    return 0;
}