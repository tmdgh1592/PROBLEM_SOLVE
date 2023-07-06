#include <bits/stdc++.h>
#define endl "\n"
#define REP(i, a, b) for(auto i = a; i <= b; ++i)
using namespace std;

#define FAST_IO \
    if constexpr (true) { cin.tie(nullptr); ios::sync_with_stdio(false); }

int n;
pair<string, string> arr[100001];
string op1, op2;
int dp[100001][2];

int calc(int a, string& b) {
    if (b[0] == '+') return a + (b[1] - '0');
    if (b[0] == '-') return a - (b[1] - '0');
    if (b[0] == '*') return a * (b[1] - '0');
    return a / (b[1] - '0');
}

int f(int round, bool chance) {
    if (round == 0) return 1;
    if (dp[round][chance] != -1) return dp[round][chance];

    int& ret = dp[round][chance];
    ret = f(round - 1, chance);

    if (ret > 0) {
        int left = calc(ret, arr[round].first);
        int right = calc(ret, arr[round].second);
        ret = max(left, right);
    }

    if (chance == 0) ret = max(ret, f(round - 1, 1));
    if (ret <= 0) return 0;
    return ret;
}

int main() {
    FAST_IO;
#ifndef ONLINE_JUDGE
    clock_t start = clock();
    freopen("input.txt", "r", stdin);
#endif

    cin >> n;
    memset(dp, -1, sizeof(dp));
    REP(i, 1, n) {
        cin >> op1 >> op2;
        arr[i] = {op1, op2};
    }

    int res = max(f(n, 1), f(n, 0));
    if (res <= 0) cout << "ddong game";
    else cout << res;

    return 0;
}