#include <bits/stdc++.h>

using namespace std;

// You are given two positive integers x and y, denoting the number of coins with values 75 and 10 respectively.
// Alice and Bob are playing a game. Each turn, starting with Alice, the player must pick up coins with a 
// total value 115. If the player is unable to do so, they lose the game.
// Return the name of the player who wins the game if both players play optimally.

class Solution {
public:
    string losingPlayer(int x, int y) {
        bool cnt = 0;
        while (x>=1 && y >=4) {
            x-=1;
            y-=4;
            cnt = !cnt;
        }
        if (cnt) return "Alice"; 
        return "Bob";
        
    };
};

int main() {
    Solution obj;
    string ans  = obj.losingPlayer(3,12);
    printf("The winner is %s\n", ans.c_str());
    return 0;
};

