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

int n, m, x, y, d, res, exclude_node = 0;
int dist[1001];
int prevs[1001];
vector<pii> graph[1001];

int dijkstra() {
    priority_queue<pii> q;
    q.push({0, 1});
    dist[1] = 0;

    while(!q.empty()) {
        auto [cost, now] = q.top();
        cost = -cost;
        q.pop();

        if (dist[now] < cost) continue;

        for (auto [next, next_cost] : graph[now]) {
            if ((next == exclude_node && now == prevs[next])) continue;

            if (cost + next_cost < dist[next]) {
                dist[next] = cost + next_cost;
                q.push({-(cost + next_cost), next});
                if (exclude_node == 0) prevs[next] = now;
            }
        }
    }
    return dist[n];
}

int main(){
    FAST_IO;
#ifndef ONLINE_JUDGE
    clock_t start = clock();
    freopen("input.txt", "r", stdin);
#endif

    cin >> n >> m;
    fill(dist, dist + 1001, INF);

    rep(i, 0, m) {
        cin >> x >> y >> d;
        graph[x].pb({y, d});
        graph[y].pb({x, d});
    }
    res = dijkstra();

    exclude_node = n;
    while (exclude_node != 1) {
        fill(dist, dist + 1001, INF);
        res = max(res, dijkstra());
        exclude_node = prevs[exclude_node];
    }

    cout << res << endl;

#ifndef ONLINE_JUDGE
    cout << endl << "elapsed time: " << static_cast<double>(clock() - start) / CLOCKS_PER_SEC << "ms" << endl;
#endif
    return 0;
}