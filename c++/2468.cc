#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int dx[4] = {1,-1,0,0};
int dy[4] = {0,0,1,-1};
int mcount=0;
void dfs(vector<vector<int>> &graph, vector<vector<bool>> &visited, int n, int x, int y , int height) {
    
    if (graph[x][y]<=height || visited[x][y]) {
        return;
    } 
    if(graph[x][y]>height && !visited[x][y]) {
        visited[x][y]=true;
        mcount++;
    }

    for (int i=0; i<4; i++) {
        int xi=x+dx[i];
        int yi=y+dy[i];
        if (xi>=0 && xi<n && yi<n && yi>=0) {
            if (!visited[xi][yi]) {
                dfs(graph, visited, n, xi, yi, height);
            }
        }
    }
}

int main() {

    int n; 
    cin>>n;
    vector<vector<int>> graph(n, vector<int>(n));
    for (int i=0; i<n; i++) {
        for (int ii=0; ii<n; ii++) {
            int p;
            cin>>p;
            graph[i][ii]=p;
        }
    }




    vector<int> k;
    int prev_count=0;
    for (int i=0; i<101; i++) {
        vector<vector<bool>> visited(n, vector<bool>(n, false));
    
        int result=0;
        for (int j=0; j<n; j++) {
            for (int k=0; k<n; k++) {
                prev_count = mcount;
                dfs(graph, visited, n, j, k,i);
                if (prev_count!=mcount) {
                    result++;
                }
            }
        }
        k.push_back(result);
    }
    sort(k.begin(), k.end());
    cout<<k[k.size()-1];
    return 0;
}