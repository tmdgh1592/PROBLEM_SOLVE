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
#define FAST_IO ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
using namespace std;

typedef long long ll;
typedef unsigned long long ull;

int n, x, y;
ll res = 0, ans = 0;
vector<pii> vec;

int main(){
    FAST_IO;
#ifndef ONLINE_JUDGE
    clock_t start = clock();
    freopen("input.txt", "r", stdin);
#endif
    cin >> n;
    rep(i, 0, n) {
        cin >> x >> y;
        vec.pb({x, y});
    }

    REP(my_price, 0, 1000000) {
        ll total = 0;
        for (auto [other_price, tip] : vec) {
            if (my_price > other_price) continue;
            if (my_price - tip <= 0) continue;
            total += my_price - tip;
        }
        if (res < total) {
            res = total;
            ans = my_price;
        }
    }
    cout << ans << endl;

#ifndef ONLINE_JUDGE
    cout << endl << "elapsed time: " << static_cast<double>(clock() - start) / CLOCKS_PER_SEC << "ms" << endl;
#endif
    return 0;
}