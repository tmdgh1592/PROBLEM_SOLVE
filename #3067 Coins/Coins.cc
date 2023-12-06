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

int t, n, x, money;
vector<int> coins;
int dp[10001][21];

int f(int cost, int used) {
    if (cost == money) return 1;
    if (dp[cost][used] != -1) return dp[cost][used];

    dp[cost][used] = 0;
    rep(i, used, n) {
        int coin = coins[i];
        if (cost + coin <= money) {
            dp[cost][used] += f(cost + coin, i);
        }
    }
    return dp[cost][used];
}

int main(){
    FAST_IO;
#ifndef ONLINE_JUDGE
    clock_t start = clock();
    freopen("input.txt", "r", stdin);
#endif

    cin >> t;
    while(t--) {
        coins.clear();
        memset(dp, -1, sizeof(dp));
        cin >> n;
        rep(i, 0, n) {
            cin >> x;
            coins.pb(x);
        }
        cin >> money;
        cout << f(0, 0) << endl;
    }

#ifndef ONLINE_JUDGE
    cout << endl << "elapsed time: " << static_cast<double>(clock() - start) / CLOCKS_PER_SEC << "ms" << endl;
#endif
    return 0;
}