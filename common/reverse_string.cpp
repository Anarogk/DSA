#include <bits/stdc++.h>
using namespace std;

std::string reverse_func(string st) {
    reverse(st.begin(), st.end());
    return st;
};

string reverse_swap(string st) {
    int n = st.length();
    for (int i =0; i< n/2; ++i) {
        swap(st[i], st[n-i-1]);
    }
    return st;
};

string reverse_two_pointers(string st) {
    int i = 0;
    int j = st.length()-1;

    while (i<j){
        swap(st[i], st[j]);
        i++;
        j--;
    };
    return st;
}

int main() {
    string str = "this is the string.";
    cout<< reverse_func(str);
    cout<<"\n";
    cout<< reverse_swap(str);
    cout<<"\n";
    cout<< reverse_two_pointers(str);


}