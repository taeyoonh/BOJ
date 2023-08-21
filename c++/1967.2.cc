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
            dfs(nextNode, distance + edgeWeight, graph, visited);
        }
    }
}

int main() {
    int n;
    cin >> n;
    vector<vector<pair<int, int>>> graph(n+1);
    for (int i=0; i<n-1; i++) {
        int a, b, c;
        cin >> a >> b >> c;
        graph[a].push_back({b, c});
        graph[b].push_back({a, c});
    }

    vector<bool> visited(n+1, false);
    dfs(1, 0, graph, visited);  // 임의의 노드에서 시작

    visited = vector<bool>(n+1, false);  // visited 배열 초기화
    maxDistance = 0;
    dfs(furthestNode, 0, graph, visited);  // 가장 먼 노드에서 시작

    cout << maxDistance << endl;
    return 0;
}
