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

int n, t;
ull dp[65][10]; // i번째 자리 수가 j일 때 증가수

ull f(int i, int j) {
    if (i == 1) return 1;
    if (dp[i][j] != -1) return dp[i][j];
    
    dp[i][j] = 0;
    REP(k, 0, j) {
        dp[i][j] += f(i - 1, k);
    }

    return dp[i][j];
}

int main(){
    FAST_IO;
#ifndef ONLINE_JUDGE
    clock_t start = clock();
    freopen("input.txt", "r", stdin);
#endif

    cin >> t;
    memset(dp, -1, sizeof(dp));

    while(t--) {
        cin >> n;
        ull res = 0;
        REP(i, 0, 9) res += f(n, i);
        cout << res << endl;
    }

#ifndef ONLINE_JUDGE
    cout << endl << "elapsed time: " << static_cast<double>(clock() - start) / CLOCKS_PER_SEC << "ms" << endl;
#endif
    return 0;
}