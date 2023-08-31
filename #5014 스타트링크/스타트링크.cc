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

int f, s, g, u, d;
bool visited[1000001];

int bfs() {
    queue<pii> q;
    q.push({s, 0});
    memset(visited, 0, sizeof(visited));

    while(!q.empty()) {
        const auto [pos, cost] = q.front();
        q.pop();

        if (pos == g) return cost;
        
        if(pos + u <= f && !visited[pos + u]) {
            q.push({pos + u, cost + 1});
            visited[pos + u] = 1;
        }
        if(pos - d >= 1 && !visited[pos - d]) {
            visited[pos - d] = 1;
            q.push({pos - d, cost + 1});
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

    cin >> f >> s >> g >> u >> d;
    int res = bfs();
    if (res == -1) {
        cout << "use the stairs";
    } else {
        cout << res;
    }

#ifndef ONLINE_JUDGE
    cout << endl << "elapsed time: " << static_cast<double>(clock() - start) / CLOCKS_PER_SEC << "ms" << endl;
#endif
    return 0;
}