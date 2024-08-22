#include <bits/stdc++.h>

using namespace std;

int minCost(vector<int> cost) {
    int len = cost.size();
    cost.push_back(0);
    cost.push_back(0);
    for (int i= 0; i< len; ++i) {
        len -=1;
        cost[len] = min(cost[len+1],cost[len+2]) + cost[len];
    }
    return min(cost[0],cost[1]);
};


int main() {
    vector<int> cost = {10,15,20};
    vector<int> cost_1 = {1,100,1,1,1,100,1,1,100,1};

    cout<<"This is the min cost to climb stairs:"<<minCost(cost)<<"\n";
    cout<<"This is the min cost to climb stairs:"<<minCost(cost_1)<<"\n";
}