#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int dx[4] = {1,-1,0,0};
int dy[4] = {0,0,1,-1};
int mcount=0;
void dfs(vector<vector<int>> &graph, vector<vector<bool>> &visited, int n,int m, int x, int y) {
    
    if (graph[x][y]==-1 || visited[x][y]) {
        return;
    } 
    if(!visited[x][y]) {
        visited[x][y]=true;
        mcount++;
    }

    for (int i=0; i<4; i++) {
        int xi=x+dx[i];
        int yi=y+dy[i];
        if (xi>=0 && xi<n && yi<m && yi>=0) {
            if (!visited[xi][yi]) {
                dfs(graph, visited, n,m, xi, yi);
            }
        }
    }
}

int main() {

    int n,m,k; 
    cin>>m>>n>>k;
    vector<vector<int>> graph(n, vector<int>(m,0));
    
    for (int i=0; i<k; i++) {
        int x,y,xi,yi;
        cin>>x>>y>>xi>>yi;
        for (int ax=x; ax<xi; ax++) {
            for (int ay=y; ay<yi; ay++) {
                graph[ax][ay]=-1;
            }
        }
    }
    /*
    for (int ax=0; ax<n; ax++) {
        for (int ay=0; ay<m; ay++) {
                cout<<graph[ax][ay]<<' ';
        }
        cout<<'\n';
    }
    */
    
    vector<vector<bool>> visited(n, vector<bool>(n, false));
    


    vector<int> kt;
    int prev_count=0;
    int result=0;
    for (int j=0; j<n; j++) {
        for (int k=0; k<m; k++) {
            prev_count = mcount;
            dfs(graph, visited, n,m, j, k);
            if (prev_count!=mcount) {
                result++;
                kt.push_back(mcount-prev_count);
            }
        }
    }

    sort(kt.begin(), kt.end());
    cout<<result<<'\n';
    for (int r: kt) {
        cout<<r<<' ';
    }
    
    return 0;
}