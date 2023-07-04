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

int n, m;
string line;
char graph[51][51];
char org_graph[51][51];
bool visited[51][51];
int sx, sy;
pii opers[4] = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};

bool in_range(int x, int y) {
    return 0 <= x && x < n && 0 <= y && y < m;
}

void fill_water(int iter) {
    rep(i, 0, n) rep(j, 0, m) graph[i][j] = org_graph[i][j];
    vector<pii> water;

    REP(k, 0, iter) {
        water.clear();
        rep(i, 0, n) {
            rep(j, 0, m) {
                if (graph[i][j] == '*') water.pb({i, j});
            }
        }

        for (auto [i, j] : water) {
            for (const auto& [dx, dy] : opers) {
                int nx = i + dx;
                int ny = j + dy;

                if (graph[nx][ny] == 'D') continue;
                if (graph[nx][ny] == 'X') continue;
                if (in_range(nx, ny)) graph[nx][ny] = '*';
            }
        }
    }
}

int bfs() {
    queue<node> q;
    q.push({sx, sy, 0});

    while (!q.empty()) {
        auto [x, y, cost] = q.front();
        q.pop();

        if (graph[x][y] == 'D') return cost;

        fill_water(cost);
        for (const auto& [dx, dy] : opers) {
            int nx = x + dx;
            int ny = y + dy;

            if (!in_range(nx, ny)) continue;
            if (visited[nx][ny]) continue;
            if (graph[nx][ny] == '*') continue;
            if (graph[nx][ny] == 'X') continue;

            q.push({nx, ny, cost + 1});
            visited[nx][ny] = 1;
        }
    }

    return INF;
}

int main(){
    FAST_IO;
#ifndef ONLINE_JUDGE
    clock_t start = clock();
    freopen("input.txt", "r", stdin);
#endif

    cin >> n >> m;
    rep(i, 0, n) {
        cin >> line;
        rep(j, 0, m) {
            if (line[j] == 'S') {
                sx = i, sy = j;
                graph[i][j] = '.';
                org_graph[i][j] = '.';
                continue;
            }
            graph[i][j] = line[j];
            org_graph[i][j] = line[j];
        }
    }

    int res = bfs();
    if (res == INF) cout << "KAKTUS";
    else cout << res;

#ifndef ONLINE_JUDGE
    cout << endl << "elapsed time: " << static_cast<double>(clock() - start) / CLOCKS_PER_SEC << "ms" << endl;
#endif
    return 0;
}