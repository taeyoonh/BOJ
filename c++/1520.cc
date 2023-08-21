#include <iostream>
#include <vector>
using namespace std;
int nx[4]={1,-1,0,0};
int ny[4]={0,0,1,-1};
int dp[501][501]={};


int dfs(vector<vector<int>> graph, int x, int y, int n, int m) { 
    if (x==n-1 && y==m-1) {
        return 1;
    }
    if (dp[x][y]) {
        return dp[x][y];
    }
    for (int i=0; i<4; i++) {
        int xi=x+nx[i];
        int yi=y+ny[i];
        if (xi>=0 && xi<n && yi<m && yi>=0) {
            if (graph[x][y]>graph[xi][yi] ) {

                dp[x][y]+=dfs(graph, xi, yi, n, m);
            }
            
        }
    }
    return dp[x][y];

}


int main() {
    ios_base :: sync_with_stdio(false); 
    cin.tie(NULL); 
    cout.tie(NULL);
    int n, m;
    cin>>n>>m;
    vector<vector<int>> graph(n, vector<int>(m));
    for (int i=0; i<n; i++) {
        for (int j=0; j<m; j++) {
            int p;
            cin>>p;
            graph[i][j]=p;
        }
    }
    
    dfs(graph, 0, 0, n, m);

    

    return 0;
}