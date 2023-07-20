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

int n, m;
int arr[101][101];
string line;
pii opers[4] = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};

struct node {
    int x, y, cost;
};

bool in_range(int x, int y) {
    return 0 <= x && x < n && 0 <= y && y < m;
}

int bfs() {
    queue<node> q;
    bool visited[101][101];
    memset(visited, 0, sizeof(visited));
    visited[0][0] = 1;
    q.push({0, 0, 1});

    while(!q.empty()) {
        auto [x, y, cost] = q.front();
        q.pop();

        if (x == n - 1 && y == m - 1) return cost;

        for (auto& [dx, dy] : opers) {
            int nx = x + dx;
            int ny = y + dy;

            if (!in_range(nx, ny)) continue;
            if (!arr[nx][ny]) continue;
            if (visited[nx][ny]) continue;

            visited[nx][ny] = 1;
            q.push({nx, ny, cost + 1});
        }
    }
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
        rep(j, 0, m) arr[i][j] = line[j] - '0';
    }

    cout << bfs() << endl;

#ifndef ONLINE_JUDGE
    cout << endl << "elapsed time: " << static_cast<double>(clock() - start) / CLOCKS_PER_SEC << "ms" << endl;
#endif
    return 0;
}