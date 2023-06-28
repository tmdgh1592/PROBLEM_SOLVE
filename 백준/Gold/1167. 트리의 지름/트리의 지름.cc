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
using namespace std;

#ifdef ONLINE_JUDGE
constexpr bool ndebug = true;
#else
constexpr bool ndebug = false;
#endif
#define FAST_IO \
    if constexpr (ndebug) { cin.tie(nullptr); ios::sync_with_stdio(false); }
#define debug(x) \
    if constexpr (!ndebug) cout << "[DEBUG] " << #x << " == " << x << '\n';
#define debugf(...) \
    if constexpr (!ndebug) { cout << "[DEBUG] "; printf(__VA_ARGS__); }
#define debugc(c) \
    if constexpr (!ndebug) { cout << "[DEBUG] "<< #c << ": "; for (const auto& elem : c) cout << elem << ", "; cout << '\n'; }

typedef long long ll;
typedef unsigned long long ull;

int n;
int a, b, c;
vector<pii> graph[100001];
bool visited[100001];
int max_dist, max_node;

void f(int node, int dist) {
    if (visited[node]) return;
    if (max_dist < dist) {
        max_dist = dist;
        max_node = node;
    }

    visited[node] = true;
    for (auto data : graph[node]) {
        f(data.first, dist + data.second);
    }
}

int main(){
    FAST_IO;
#ifndef ONLINE_JUDGE
    clock_t start = clock();
    freopen("input.txt", "r", stdin);
#endif
    
    cin >> n;
    rep(i, 0, n) {
        cin >> a;
        while(1) {
            cin >> b;
            if (b == -1) break;
            cin >> c;
            graph[a].pb({b, c});
            graph[b].pb({a, c});
        }
    }

    f(1, 0);
    memset(visited, false, sizeof(visited));
    max_dist = 0;
    f(max_node, 0);
    cout << max_dist << endl;

#ifndef ONLINE_JUDGE
    cout << endl << "elapsed time: " << static_cast<double>(clock() - start) / CLOCKS_PER_SEC << "ms" << endl;
#endif
    return 0;
}