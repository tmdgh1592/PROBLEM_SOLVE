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

int n, t;
int sx, sy, dx, dy;
pii opers[8] = {{-2, 1}, {-1, 2}, {1, 2}, {2, 1}, {-2, -1}, {-1, -2}, {1, -2}, {2, -1}};

struct node {
    int x, y, cost;
};

bool in_range(int x, int y) {
    return 0 <= x && x < n && 0 <= y && y < n;
}

int bfs() {
    bool visited[301][301];
    memset(visited, 0, sizeof(visited));
    queue<node> q;
    q.push({sx, sy, 0});
    visited[sx][sy] = 1;

    while(!q.empty()) {
        auto [x, y, cost] = q.front();
        q.pop();

        if (x == dx && y == dy) return cost;

        for(auto [ddx, ddy] : opers) {
            int nx = x + ddx;
            int ny = y + ddy;

            if (!in_range(nx, ny)) continue;
            if (visited[nx][ny]) continue;

            visited[nx][ny] = 1;
            q.push({nx, ny, cost + 1});
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

    cin >> t;
    rep(i, 0, t) {
        cin >> n >> sx >> sy >> dx >> dy;
        cout << bfs() << endl;
    }

#ifndef ONLINE_JUDGE
    cout << endl << "elapsed time: " << static_cast<double>(clock() - start) / CLOCKS_PER_SEC << "ms" << endl;
#endif
    return 0;
}