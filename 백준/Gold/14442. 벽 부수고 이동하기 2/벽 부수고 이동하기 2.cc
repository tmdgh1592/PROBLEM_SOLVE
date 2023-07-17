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
    int x, y, cost, use_opportunity;
};

int r, c, k;
string line;
int graph[1001][1001];
bool visited[1001][1001][11];
pii opers[4] = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};

bool in_range(int x, int y) {
    return 1 <= x && x <= r && 1 <= y && y <= c;
}

int bfs() {
    queue<node> q;
    q.push({1, 1, 1, 0});
    visited[1][1][0] = 1;

    while (!q.empty()) {
        auto [x, y, cost, use_opportunity] = q.front();
        q.pop();

        if (x == r && y == c) return cost;

        for(auto& [dx, dy] : opers) {
            int nx = x + dx;
            int ny = y + dy;

            if (!in_range(nx, ny)) continue;
            if (graph[nx][ny] == 1 && use_opportunity < k) {
                if (visited[nx][ny][use_opportunity + 1]) continue;
                visited[nx][ny][use_opportunity + 1] = 1;
                q.push({nx, ny, cost + 1, use_opportunity + 1});
            } else if (graph[nx][ny] == 0) {
                if (visited[nx][ny][use_opportunity]) continue;
                visited[nx][ny][use_opportunity] = 1;
                q.push({nx, ny, cost + 1, use_opportunity});
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

    cin >> r >> c >> k;
    REP(i, 1, r) {
        cin >> line;
        REP(j, 1, c) graph[i][j] = line[j - 1] - '0';
    }
    memset(visited, 0, sizeof(visited));
    cout << bfs() << endl;

#ifndef ONLINE_JUDGE
    cout << endl << "elapsed time: " << static_cast<double>(clock() - start) / CLOCKS_PER_SEC << "ms" << endl;
#endif
    return 0;
}