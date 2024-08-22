#include <bits/stdc++.h>

struct Node {
    int data;
    Node* left;
    Node* right;

    Node (int val): data(val), left(nullptr), right(nullptr){};
};

/* 
LevelOrder(tree)

Create an empty queue Q
Enqueue the root node of the tree to Q
Loop while Q is not empty
Dequeue a node from Q and visit it
Enqueue the left child of the dequeued node if it exists
Enqueue the right child of the dequeued node if it exists
*/

void levelOrder(Node* root) {
    if (root == nullptr)return;
    std::queue<Node*> q;
    q.push(root);
    while (!q.empty()) {
        Node* curr = q.front();
        std::cout<< curr->data<<"\n";
        q.pop();
        if (curr->left)q.push(curr->left);
        if (curr->right)q.push(curr->right);
    };
};


int main() {
    Node* root = new Node(4);
    root->left = new Node(6);
    root->right = new Node(8);
    root->left->left = new  Node(9);
    root->left->right  = new Node(3);
    root->right->left = new Node(1);
    root->right->right = new Node(2);


    std::cout<< "this is level Order Traversal:"<<"\n";
    levelOrder(root);
};