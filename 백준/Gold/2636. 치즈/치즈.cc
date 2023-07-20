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

int n, m, res, prev_cheese;
int arr[101][101];
pii opers[4] = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};

bool in_range(int x, int y) {
    return 0 <= x && x < n && 0 <= y && y < m;
}

bool bfs() {
    queue<pii> q;
    q.push({0, 0});
    bool visited[101][101];
    visited[0][0] = 1;
    memset(visited, 0, sizeof(visited));

    int cheese = 0;
    while(!q.empty()) {
        auto [x, y] = q.front();
        q.pop();

        for(auto [dx, dy] : opers) {
            int nx = x + dx;
            int ny = y + dy;

            if (!in_range(nx, ny)) continue;
            if(visited[nx][ny]) continue;            

            if (arr[nx][ny] == 0) q.push({nx, ny});
            else {
                arr[nx][ny] = 0;
                ++cheese;
            }
            visited[nx][ny] = 1;
        }
    }

    if (cheese == 0) {
        cout << res << endl << prev_cheese;
    } else {
        prev_cheese = cheese;
        ++res;
    }
    return cheese > 0;
}

int main(){
    FAST_IO;
#ifndef ONLINE_JUDGE
    clock_t start = clock();
    freopen("input.txt", "r", stdin);
#endif

    cin >> n >> m;
    rep(i, 0, n) rep(j, 0, m) cin >> arr[i][j];

    while(true) {
        if (!bfs()) break;
    }

#ifndef ONLINE_JUDGE
    cout << endl << "elapsed time: " << static_cast<double>(clock() - start) / CLOCKS_PER_SEC << "ms" << endl;
#endif
    return 0;
}