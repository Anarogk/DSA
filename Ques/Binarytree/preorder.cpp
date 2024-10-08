#include <bits/stdc++.h>
using namespace std;


struct TreeNode { 
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {};
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {};
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {};
};

vector<int> preorderTraversal(TreeNode* root) {
    vector<int> li;
    if (!root) return li;
    li.push_back(root->val);
    if (root->left) preorderTraversal(root->left);
    if (root-> right) preorderTraversal(root->right);
    return li;
};