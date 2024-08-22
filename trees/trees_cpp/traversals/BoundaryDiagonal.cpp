#include <bits/stdc++.h>

using namespace std;

struct Node {
    int data;
    Node* left;
    Node* right;

    Node( int val): data(val), left(nullptr), right(nullptr){};
};


void Boundary(Node* root) {
    if (!root) return;
    cout<<root->data<<"\n";
    


};



int main() {
    Node* root = new Node(4);
    root->left = new Node(6);
    root->right = new Node(8);
    root->left->left = new  Node(9);
    root->left->right  = new Node(3);
    root->right->left = new Node(1);
    root->right->right = new Node(2);


    std::cout<< "this is Inorder:"<<"\n";
    Boundary(root);

    return 0;
};