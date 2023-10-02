#include <bits/stdc++.h>
#define endl "\n"
#define rep(i, a, b) for(auto i = a; i < b; ++i)
#define rrep(i, a, b) for(auto i = a; i > b; --i)
#define REP(i, a, b) for(auto i = a; i <= b; ++i)
#define RREP(i, a, b) for(auto i = a; i >= b; --i)
#define pii pair<int, int>
#define all(v) (v).begin(), (v).end()
#define pb push_back
#define INF numeric_limits<int>::max()
#define sz size()
#define PIV (1 << 20)
#define FAST_IO ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
using namespace std;

typedef long long ll;
typedef unsigned long long ull;

int visited[100000 + 1001];
vector<int> graph[100000 + 1001];
int n, k, m, x;

int bfs() {
    queue<int> q;
    q.push(1);
    visited[1] = 1;

    while(!q.empty()) {
        int node = q.front();
        q.pop();

        if (node == n) return visited[node];

        for (auto next : graph[node]) {
            if (visited[next] != 0) continue;
            q.push(next);
            if (next > 100000) {
                visited[next] = visited[node];
            } else {
                visited[next] = visited[node] + 1;
            }
        }
    }

    return -1;
}

int main(){
    FAST_IO;
#ifndef ONLINE_JUDGE
    clock_t start = clock();
    freopen("input.txt", "r", stdin);
#endif

    cin >> n >> k >> m;
    memset(visited, 0, sizeof(visited));
    REP(i, 1, m) {
        rep(j, 0, k) {
            cin >> x;
            graph[100000 + i].pb(x);
            graph[x].pb(100000 + i);
        } 
    }
    cout << bfs();

#ifndef ONLINE_JUDGE
    cout << endl << "elapsed time: " << static_cast<double>(clock() - start) / CLOCKS_PER_SEC << "ms" << endl;
#endif
    return 0;
}