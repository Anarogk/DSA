#include <bits/stdc++.h>

using namespace std;

int kadane(vector<int> arr, int size){
    int max_sum = INT_MIN;
    int curr_sum = 0;
    if(max_sum < curr_sum){
        max_sum = curr_sum;
    };
    if (curr_sum<0){
        curr_sum = 0;
    }

    return curr_sum;
};


int main() {

}