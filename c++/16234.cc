#include <iostream>
#include <vector>
using namespace std;

vector<vector<int>> pi;

int bfs(vector<vector<int>> &graph, vector<vector<bool>> &visited, int n, int l, int r, int fx, int fy){
    vector<vector<int>>li= {{fx,fy}};
    int val=0;
    int nx[4] = {1,-1,0,0};
    int ny[4] = {0,0,1,-1};
    pi={{fx,fy}};
    val+=graph[fx][fy];
    visited[fx][fy]=true;
    while (li.size()!=0) {
        int x;
        int y;
        x=li[0][0];
        y=li[0][1];
        li.erase(li.begin());
        for (int k=0; k<4; k++) {
            int xi=x+nx[k];
            int yi=y+ny[k];
            if (0<=xi && xi<n && 0<=yi && yi<n) {
                if (!visited[xi][yi] && l<=abs(graph[x][y]-graph[xi][yi]) && abs(graph[x][y]-graph[xi][yi])<=r) {
                    li.push_back({xi,yi});
                    pi.push_back({xi,yi});
                    val+=graph[xi][yi];
                    visited[xi][yi]=true;
                }
            }
        }        
    }
    val/=pi.size();
    return val;
}


int main() {
    int n,l,r;
    cin>>n>>l>>r;
    vector<vector<int>> vs;
    vector<vector<int>> graph(n,vector<int>(n));
    for (int i=0; i<n; i++) {
        for (int ii=0; ii<n; ii++) {
            int p;
            cin>>p;
            graph[i][ii]=p;
        }
    }
    int result=0;
    while(1) {
        vector<vector<bool>> visited(n,vector<bool>(n, false));
        bool is=false;
        for (int i=0; i<n; i++) {
            for (int j=0; j<n; j++) {
                pi={};
                if (!visited[i][j]) {
                    int val = bfs(graph, visited, n, l, r, i , j);
                    if (pi.size()!=1) {
                        is = true;
                        for (int k=0; k<pi.size(); k++) {
                            graph[pi[k][0]][pi[k][1]]=val;
                        }
                    }
                }
            }
        }
        if (!is) {
            break;
        }
        result++;
            
    }

    cout<< result<<'\n';

    return 0;
}