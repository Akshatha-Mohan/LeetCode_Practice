#include <iostream>
#include <vector>
#include <queue>

using namespace std;

// Function to perform BFS on a graph starting from a given node
void BFS(const vector<vector<int>>& graph, int start) {
    // Create a queue to manage the BFS process
    queue<int> q;
    
    // Create a visited array and initialize all nodes as not visited
    int N = graph.size();
    vector<bool> visited(N, false);
    
    // Mark the start node as visited and enqueue it
    visited[start] = true;
    q.push(start);
    
    // While there are nodes in the queue
    while (!q.empty()) {
        // Dequeue the front node
        int node = q.front();
        q.pop();
        
        // Process the current node (for example, print it)
        cout << node << " ";
        
        // Get all the neighbors of the current node
        for (int neighbor : graph[node]) {
            // If the neighbor has not been visited
            if (!visited[neighbor]) {
                // Mark the neighbor as visited
                visited[neighbor] = true;
                // Enqueue the neighbor
                q.push(neighbor);
            }
        }
    }
}

int main() {
    // Example graph represented as an adjacency list
    vector<vector<int>> graph = {
        {1, 2},    // Node 0 is connected to nodes 1 and 2
        {0, 3, 4}, // Node 1 is connected to nodes 0, 3, and 4
        {0, 4},    // Node 2 is connected to nodes 0 and 4
        {1, 5},    // Node 3 is connected to nodes 1 and 5
        {1, 2, 5}, // Node 4 is connected to nodes 1, 2, and 5
        {3, 4}     // Node 5 is connected to nodes 3 and 4
    };
    
    // Perform BFS starting from node 0
    cout << "BFS starting from node 0: ";
    BFS(graph, 0);
    cout << endl;

    return 0;
}





//BFS PseudoCode
