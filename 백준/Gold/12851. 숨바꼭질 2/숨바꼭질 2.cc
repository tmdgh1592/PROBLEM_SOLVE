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

int n, k;
int ans = INF, cnt;
queue<pii> q;
int visited[100001];

bool in_range(int pos) {
    return 0 <= pos && pos <= 100000;
}

int main(){
    FAST_IO;
#ifndef ONLINE_JUDGE
    clock_t start = clock();
    freopen("input.txt", "r", stdin);
#endif

    cin >> n >> k;
    q.emplace(n, 0);

    while (!q.empty()) {
        pii item = q.front();
        int pos = item.first, cost = item.second;
        q.pop();
        visited[pos] = true;

        if (pos == k) {
            ans = min(ans, cost);
            if (ans == cost) cnt++;
		}

        if (in_range(pos * 2) && !visited[pos * 2]) q.emplace(pos * 2, cost + 1);
        if (in_range(pos - 1) && !visited[pos - 1]) q.emplace(pos - 1, cost + 1);
        if (in_range(pos + 1) && !visited[pos + 1]) q.emplace(pos + 1, cost + 1);
    }
    
    cout << ans << endl << cnt;

#ifndef ONLINE_JUDGE
    cout << endl << "elapsed time: " << static_cast<double>(clock() - start) / CLOCKS_PER_SEC << "ms" << endl;
#endif
    return 0;
}