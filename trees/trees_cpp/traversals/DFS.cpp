#include <bits/stdc++.h>


struct Node {
    int data;
    Node* left;
    Node* right;

    Node (int val): data(val),left(nullptr), right(nullptr) {};
};

void Preorder(Node* root) {
    if (root == nullptr) {
        return;
    };
    std::cout<< root->data<<"\n";
    Preorder(root->left);
    Preorder(root->right);
};


void Inorder( Node* root) {
    if (root == nullptr) {
        return;
    }
    Inorder(root->left);
    std::cout<< root->data<<"\n";
    Inorder(root->right);
};

void Postorder(Node* root) {
    if (root == nullptr) {
        return;
    };
    Postorder(root->left);
    Postorder(root->right);
    std::cout<< root->data<<"\n";
};


int main () {
    Node* root = new Node(4);
    root->left = new Node(6);
    root->right = new Node(8);
    root->left->left = new  Node(9);
    root->left->right  = new Node(3);
    root->right->left = new Node(1);
    root->right->right = new Node(2);


    std::cout<< "this is Inorder:"<<"\n";
    Inorder(root);
    std::cout<< "\n";
    std::cout<< "this is Postorder:"<<"\n";
    Postorder(root);
    std::cout<< "\n";
    std::cout<< "this is Preorder:"<<"\n";
    Preorder(root);
}

