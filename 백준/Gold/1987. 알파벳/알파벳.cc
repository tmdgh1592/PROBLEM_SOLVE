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

int n, m, ans;
string line;
char graph[21][21];
bool visited[21][21];
bool checked[1000];
pii opers[4] = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};

bool in_range(int x, int y) {
    return 1 <= x && x <= n && 1 <= y && y <= m;
}

void f(int x, int y, int cnt) {
    ans = max(ans, cnt);

    for (const auto& [dx, dy] : opers) {
        int nx = x + dx, ny = y + dy;

        if (!in_range(nx, ny)) continue;
        if (visited[nx][ny]) continue;
        
        char& next_char = graph[nx][ny];
        if (checked[next_char]) continue;

        checked[next_char] = true;
        visited[nx][ny] = true;
        f(nx, ny, cnt + 1);
        checked[next_char] = false;
        visited[nx][ny] = false;
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
        rep(j, 0, m) graph[i + 1][j + 1] = line[j];
    }

    visited[1][1] = 1;
    checked[graph[1][1]] = 1;
    f(1, 1, 1);
    cout << ans << endl;

#ifndef ONLINE_JUDGE
    cout << endl << "elapsed time: " << static_cast<double>(clock() - start) / CLOCKS_PER_SEC << "ms" << endl;
#endif
    return 0;
}