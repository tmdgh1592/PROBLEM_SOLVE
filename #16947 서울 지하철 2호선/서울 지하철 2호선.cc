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

int n, s, e;
vector<int> graph[3001];
bool visited[3001];
bool type[3001]; // 1 : 순환선 / 0 : 지선

bool f(int start, int now, int cnt) {
    for (int next : graph[now]) {
        if (visited[next]) continue;
        if (cnt >= 3 && start == next) return true;

        visited[next] = 1;
        if (f(start, next, cnt + 1)) return true;
        visited[next] = 0;
    }
    return false;
}

int bfs(int start) {
    if (type[start]) return 0;
    queue<pii> q;
    q.push({start, 0});
    visited[start] = 1;

    while (!q.empty()) {
        auto [now, cnt] = q.front();
        q.pop();

        if (type[now]) return cnt;

        for (int next : graph[now]) {
            if (visited[next]) continue;
            visited[next] = 1;
            q.push({next, cnt + 1});
        }
    }

    return 0;
}

int main(){
    FAST_IO;
#ifndef ONLINE_JUDGE
    clock_t start = clock();
    freopen("input.txt", "r", stdin);
#endif
    cin >> n;
    rep(i, 0, n) {
        cin >> s >> e;
        graph[s].pb(e);
        graph[e].pb(s);
    }

    REP(i, 1, n) {
        memset(visited, 0, sizeof(visited));
        type[i] = f(i, i, 1);
    }
    REP(i, 1, n) {
        memset(visited, 0, sizeof(visited));
        cout << bfs(i) << " ";
    }



#ifndef ONLINE_JUDGE
    cout << endl << "elapsed time: " << static_cast<double>(clock() - start) / CLOCKS_PER_SEC << "ms" << endl;
#endif
    return 0;
}