#include <iostream>
#include <vector>

using namespace std;
int dx[4]={1,-1,0,0};
int dy[4]={0,0,1,-1};
int m_count=0;

void melting(vector<vector<int>> &graph, vector<vector<int>> &minus, int n, int m,int x, int y) {
    if (graph[x][y]==0) {
        return;
    }
    int z_count=0;
    for (int i=0; i<4; i++) {
        int xi= x+dx[i];
        int yi= y+dy[i];
        if (xi>=0 && xi<n && yi>=0 && yi<m) {
            if (graph[xi][yi]==0) {
                z_count++;
            }
        }
    }
    minus[x][y]=z_count;
    
}

void ice_counter(vector<vector<int>> &graph, vector<vector<bool>> &visited, int n, int m, int x, int y) {
    if (graph[x][y]==0) {
        return;
    }
    if (!visited[x][y]) {
        visited[x][y]=true;
        m_count++;
    }
    for (int i=0; i<4; i++) {
        int xi= x+dx[i];
        int yi= y+dy[i];
        if (xi>=0 && xi<n && yi>=0 && yi<m) {
            if (graph[xi][yi]!=0 && !visited[xi][yi]) {
            
                ice_counter(graph, visited, n, m, xi, yi);
            }
        }
    }
}

int main() {
    int n,m;
    cin>>n>>m;
    vector<vector<int>> graph(n, vector<int>(m));
    for (int i=0; i<n; i++) {
        for (int j=0; j<m; j++) {
            int p;
            cin>>p;
            graph[i][j]=p;
        }
    }

    int ttime=0;
    while (true) {
    
    bool all_zero=true;
    for (int i=0; i<n; i++) {
        for (int j=0; j<m; j++) {
            if (graph[i][j]!=0) {
                all_zero=false;
            }
        }
    }

    if (all_zero) {
        cout<<0;
        break;
    }

    vector<vector<int>> minus(n, vector<int>(m,0));
    vector<vector<bool>> visited(n, vector<bool>(m, false));
    int all_ice_count=0;

    for (int i=0; i<n; i++) {
        for (int j=0; j<m; j++) {
            int prev_counter=m_count;
            ice_counter(graph, visited, n, m, i, j);
            if (prev_counter!=m_count) {
                
                all_ice_count++;
            }

        }
        
    }

    if (all_ice_count>=2) {
        cout<<ttime;
        break;   
    }
    
    for (int i=0; i<n; i++) {
        for (int j=0; j<m; j++) {
            melting(graph, minus, n, m, i, j);
        }
    }

    for (int i=0; i<n; i++) {
        for (int j=0; j<m; j++) {
            if (minus[i][j]!=0) {
                int r= graph[i][j]-minus[i][j];
                if (r<0) {
                    graph[i][j]=0;
                } else{
                    graph[i][j]=r;
                }
            }    
        }
    }
    ttime++;
    }

    return 0;
}