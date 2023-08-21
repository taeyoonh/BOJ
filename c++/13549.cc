#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
vector<int> arr(100001, 0);

int bfs(vector<int> &arr, int si, int ed) {
    vector<int> p;
    vector<bool> visited(100001, false);
    visited[si]=true;
    p.push_back(si);
    while (p.size()!=0) {
        int st= p[0];
        p.erase(p.begin());
        if (st==ed) {
            return arr[st];
        }
        int ar[3]={st-1, st*2, st+1};
        for (int ki: ar) {
            if (0<=ki && ki<100001 && !visited[ki]) {
                if (ki==st*2) {
                    arr[ki] = arr[st];
                } else{
                    arr[ki] = arr[st]+1;
                }
                visited[ki]=true;
                p.push_back(ki);
            }
        }
    }   

}

int main() {

    int n,k;
    cin>>n>>k;

    int result=bfs(arr,n,k);
    cout<<result;



    return 0;
}