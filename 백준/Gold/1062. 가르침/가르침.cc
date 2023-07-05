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

int n, k, ans;
string s;
string arr[51];
bool used[26];

int check() {
    int res = 0;
    
    rep(i, 0, n) {
        bool flag = false;
        for (auto c : arr[i]) {
            if (!used[c - 'a']) {
                flag = true;
                break;
            }
        }
        if (!flag) res++;
    }
    return res;
}

void f(int can_use, int start) {
    if (can_use == 0) {
        ans = max(ans, check());
        return;
    }

    rep(i, start, 26) {
        if (used[i]) continue;
        used[i] = 1;
        f(can_use - 1, i);
        used[i] = 0;
    }
}

int main(){
    FAST_IO;
#ifndef ONLINE_JUDGE
    clock_t start = clock();
    freopen("input.txt", "r", stdin);
#endif

    cin >> n >> k;
    rep(i, 0, n) {
        cin >> s;
        arr[i] = s.substr(4, s.size() - 8);
    }
    used[0] = 1;
    used[2] = 1;
    used[8] = 1;
    used[13] = 1;
    used[19] = 1;
    k -= 5;

    if (k < 0) cout << 0 << endl;
    else {
        f(k, 0);
        cout << ans << endl;
    }

#ifndef ONLINE_JUDGE
    cout << endl << "elapsed time: " << static_cast<double>(clock() - start) / CLOCKS_PER_SEC << "ms" << endl;
#endif
    return 0;
}