#include <iostream>
#include <vector>

using namespace std;

void bfs(vector<vector<int>> &graph, vector<bool> &visited, vector<int> &ci,int st, int ed) {

    
    vector<int> p;
    p.push_back(st);
    while (true){
        if (p.size()==0) {
            return ;
        }
        int fi=p[0];
        p.erase(p.begin());
        for (int k: graph[fi]) {
            if (!visited[k]) {
                visited[k]=true;
                ci[k]=ci[fi]+1;
                p.push_back(k);
            }
        }
    }

}

int main() {
    int ni;
    cin>>ni;
    int n,m;
    cin>>n>>m;
    int re;
    cin>>re;

    vector<vector<int>> graph(ni+1, vector<int>(ni+1));
    vector<int> ci(ni+1,0);
    
    vector<bool> visited(ni, false);
    for (int i=0; i<re; i++) {
        int a,b;
        cin>>a>>b;
        graph[a].push_back(b);
        graph[b].push_back(a);
    }

    bfs(graph, visited, ci, n, m);

    if (ci[m]==0) {
        cout<<-1;
    } else {
        cout<<ci[m];
    }

    return 0;
}