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

int n, a, b, high;
deque<int> q;

int main(){
    FAST_IO;
#ifndef ONLINE_JUDGE
    clock_t start = clock();
    freopen("input.txt", "r", stdin);
#endif
    
    cin >> n >> a >> b;
    
    rep(i, 1, a) q.pb(i);
    q.pb(max(a, b));
    RREP(i, b - 1, 1) q.pb(i);

    if (q.size() > n) {
        cout << -1; 
        return 0;
    }

    int front = q.front();
    q.pop_front();
    
    rep(i, 0, n - q.sz - 1) q.push_front(1);
    q.push_front(front);

    for (auto e : q) cout << e << " ";

#ifndef ONLINE_JUDGE
    cout << endl << "elapsed time: " << static_cast<double>(clock() - start) / CLOCKS_PER_SEC << "ms" << endl;
#endif
    return 0;
}