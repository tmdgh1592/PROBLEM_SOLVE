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

struct node {
    int x, y, cost;
};

int n;
int graph[101][101];
pii dirs[4] = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
int cnt = 2;
int res = INF;

bool in_range(int x, int y) {
    return 0 <= x && x < n && 0 <= y && y < n;
}

void check_bfs(int ix, int iy, int cnt) {
    queue<pii> q;
    q.push({ix, iy});
    graph[ix][iy] = cnt;

    while (!q.empty()) {
        auto [x, y] = q.front();
        q.pop();

        for (auto [dx, dy] : dirs) {
            int nx = x + dx;
            int ny = y + dy;

            if (!in_range(nx, ny)) continue;
            if (graph[nx][ny] != 1) continue;

            graph[nx][ny] = cnt;
            q.push({nx, ny});
        }
    }
}

void bfs(int ix, int iy) {
    int color = graph[ix][iy];
    queue<node> q;
    q.push({ix, iy, 0});

    int visited[101][101];
    memset(visited, 0, sizeof(visited));
    visited[ix][iy] = 1;

    while (!q.empty()) {
        auto [x, y, cost] = q.front();
        q.pop();

        for (auto [dx, dy] : dirs) {
            int nx = x + dx;
            int ny = y + dy;

            if (!in_range(nx, ny)) continue;
            if (visited[nx][ny]) continue;

            if(graph[nx][ny] != 0 && graph[nx][ny] != color) {
                res = min(res, cost);
                return;
            }

            if (graph[nx][ny] == 0) q.push({nx, ny, cost + 1});
            else q.push({nx, ny, cost});
            visited[nx][ny] = 1;
        }
    }
}

int main(){
    FAST_IO;
#ifndef ONLINE_JUDGE
    clock_t start = clock();
    freopen("input.txt", "r", stdin);
#endif

    cin >> n;
    rep(i, 0, n) rep(j, 0, n) cin >> graph[i][j];

    int cnt = 2;
    rep(i, 0, n) rep(j, 0, n) {
        if (graph[i][j] == 1) {
            check_bfs(i, j, cnt);
            ++cnt;
        }
    }

    rep(i, 0, n) rep(j, 0, n) if (graph[i][j] != 0) bfs(i, j);
    cout << res << endl;

#ifndef ONLINE_JUDGE
    cout << endl << "elapsed time: " << static_cast<double>(clock() - start) / CLOCKS_PER_SEC << "ms" << endl;
#endif
    return 0;
}