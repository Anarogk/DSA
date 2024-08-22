#include <bits/stdc++.h>
using std::vector, std::cout, std::queue;

// func to add an edge between x and y
void addEdge(int x, int y, vector<vector<int>>& adj)
{
    adj[x].push_back(y);
    adj[y].push_back(x);
};

// function to print parent of a node
void printParents(int node, vector<vector<int>>& adj, int parent)
{
    if (parent == 0)
    {
        cout << node << "-> Root" << "\n";
    }
    else
    {
        cout << node << " -> " << "\n";
    };

    // use DFS
    for (auto curr : adj[node])
    {
        if (curr != parent)
        {
            printParents(curr, adj, node);
        };
    }
};

void printChildren(int node, vector<vector<int>>& adj)
{
    queue<int> q{};
    q.push(node);

    int visit[adj.size()]{};

    // BFS
    while (!q.empty())
    {
        int node = q.front();
        q.pop();
        visit[node] = 1;
        std::cout << node << "->";

        for (auto curr : adj[node])
        {
            if (visit[curr] == 0)
            {
                cout << curr << " ";
                q.push(curr);
            }
        }
        cout << "\n";
    }
};

void printLeafNodes(int node, vector<vector<int>>& adj) {
    for (int i{1}; i < adj.size(); i++)
    {
        if (adj[i].size()== 1 && i != node)
        {
            cout <<i << " ";
        }
    }
    cout << "\n";
};

void printDegrees(int node, vector<vector<int>>& adj)
{
    for (int i = 0; i < adj.size(); i++)
    {
        cout << i << ": ";

        if (i == node)
        {
            cout << adj[i].size() << "\n";
        }
        else
        {
            cout << adj[i].size() - 1 << "\n";
        }
    }

};

int main()
{

    int N = 7, Root = 1;

    // Adjacency list to store the tree
    vector<vector<int>> adj(N + 1, vector<int>());

    // Creating the tree
    addEdge(1, 2, adj);
    addEdge(1, 3, adj);
    addEdge(1, 4, adj);
    addEdge(2, 5, adj);
    addEdge(2, 6, adj);
    addEdge(4, 7, adj);

    // Printing the parents of each node
    cout << "The parents of each node are:" << "\n";
    printParents(Root, adj, 0);

    // Printing the children of each node
    cout << "The children of each node are:" << "\n";
    printChildren(Root, adj);

    // Printing the leaf nodes in the tree
    cout << "The leaf nodes of the tree are:" << "\n";
    printLeafNodes(Root, adj);

    // Printing the degrees of each node
    cout << "The degrees of each node are:" << "\n";
    printDegrees(Root, adj);

    for ( int i = 0 ; i< N+1; i++ ) 
    {
        cout << "The adj: " << adj[i][i]<< "\n";
    }
    return 0;
};