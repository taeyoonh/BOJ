#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int furthestNode = 0;
int maxDistance = 0;

void dfs(int node, int distance, vector<vector<pair<int, int>>> &graph, vector<bool> &visited) {
    visited[node] = true;
    if (distance > maxDistance) {
        maxDistance = distance;
        furthestNode = node;
    }
    for (auto [nextNode, edgeWeight] : graph[node]) {
        if (!visited[nextNode]) {
            dfs(nextNode, distance+edgeWeight, graph, visited);
        }
    }
}

int main() {    
    int n;
    cin>>n;

    vector<vector<pair<int, int>>> graph(n+1);


    for (int i=0; i<n; i++) {
        int a;
        cin>>a;
        while (true) {
            int b,c;
            cin>>b;
            if (b==-1) {
                break;
            }
            cin>>c;
            graph[a].push_back({b,c});            
        }
    }
    

    vector<bool> visited(n+1, false);
    dfs(1,0, graph, visited);

    visited = vector<bool>(n+1, false);

    maxDistance = 0;
    dfs(furthestNode, 0, graph, visited);
    cout<<maxDistance<<'\n';
  
    return 0;

}