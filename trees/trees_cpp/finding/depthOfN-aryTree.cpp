#include <bits/stdc++.h>
using namespace std;

// finding depth of the N-ary tree;

struct NaryNode
{
    char val;
    vector<NaryNode *> child;
};


NaryNode *newNode(int key)
{
    NaryNode *temp = new NaryNode;
    temp->val = key;
    return temp;
};


int depthOfNaryTree(NaryNode *ptr)
{
    if (ptr == nullptr) return 0;
    int maxdepth{};
    for (vector<NaryNode *>::iterator it = ptr->child.begin() ;
         it != ptr->child.end(); it++)
    {
        maxdepth = max(maxdepth, depthOfNaryTree(*it));
    };

    return maxdepth +1;
};

// Driver program 
int main() 
{ 
   /*   Let us create below tree 
   *             A 
   *          / /\ \
   *         / /  \  \ 
   *       B  F   D   E 
   *      / \    /   /|\ 
   *     K  J   G   C H I 
   *     /\              \ 
   *    N  M              L 
   */
  
   NaryNode *root = newNode('A'); 
   (root->child).push_back(newNode('B')); 
   (root->child).push_back(newNode('F')); 
   (root->child).push_back(newNode('D')); 
   (root->child).push_back(newNode('E')); 
   (root->child[0]->child).push_back(newNode('K')); 
   (root->child[0]->child).push_back(newNode('J')); 
   (root->child[2]->child).push_back(newNode('G')); 
   (root->child[3]->child).push_back(newNode('C')); 
   (root->child[3]->child).push_back(newNode('H')); 
   (root->child[3]->child).push_back(newNode('I')); 
   (root->child[0]->child[0]->child).push_back(newNode('N')); 
   (root->child[0]->child[0]->child).push_back(newNode('M')); 
   (root->child[3]->child[2]->child).push_back(newNode('L')); 
  
   cout << depthOfNaryTree(root) << endl; 
  
   return 0; 
};