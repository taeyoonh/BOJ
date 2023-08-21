#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
vector<int> max_arr;
int dfs(int start,int set, vector<vector<int>> &graph, vector<bool> &visited, vector<vector<int>> &arr) {
    if (start==set) {
        visited[set]=true;
        for (int ri: graph[set]) {
            max_arr.push_back(arr[start][ri]+dfs(ri,set, graph, visited,arr));
        }
    }

    else {
        visited[start]=true;
        int co_max=0;
        int co=0;
        for (int ti: graph[start]) {
            if (!visited[ti]) {
                co++;
                co_max = max(co_max, arr[ti][start]+dfs(ti, set, graph, visited,arr));
                
            }    
        }

        if (co==0) {
            return 0;
        }
        
        return co_max;
        

    }
}


int main() {

    int n;
    cin>>n;
    vector<vector<int>> graph(n+1);
    vector<vector<int>> arr(n+1, vector<int>(n+1, 0));
    for (int i=0; i<n-1; i++) {
        int a,b,c;
        cin>>a>>b>>c;
        graph[a].push_back(b);
        graph[b].push_back(a);
        arr[a][b]=c;
        arr[b][a]=c;
    }   
    int p=1;
    int max_result=0;
    while (true) {
        
        if (p==12) {
            break;
        }
        p++;
        vector<bool> visited(n+1, false);
        dfs(p, p, graph, visited,arr);

        
        sort(max_arr.begin(), max_arr.end());
        if (max_arr.size()>1) {
            max_result=max(max_result, max_arr[max_arr.size()-1]+max_arr[max_arr.size()-2]);
        } else {
            max_result= max(max_result, max_arr[0]);
        }
        max_arr.clear();
    }

    cout<<max_result;

    return 0;
}