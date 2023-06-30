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

int n;
ll dp[1001][2][4][2];
const int MOD = 1000000007;

int f(int pos, int cnt, int sum_h, bool is_two) {
    if (pos == n) return is_two && sum_h < 4 && cnt <= 2;
    if (cnt > 2 || sum_h >= 4) return 0;
    if (dp[pos][cnt][sum_h][is_two] != -1) return dp[pos][cnt][sum_h][is_two] % MOD;

    dp[pos][cnt][sum_h][is_two] = 0;
    dp[pos][cnt][sum_h][is_two] += f(pos + 1, 0, 0, is_two) % MOD;
    dp[pos][cnt][sum_h][is_two] += f(pos + 1, cnt + 1, sum_h + 1, is_two) % MOD;
    dp[pos][cnt][sum_h][is_two] += f(pos + 1, cnt + 1, sum_h + 2, true) % MOD;

    return dp[pos][cnt][sum_h][is_two] % MOD;
}

int main(){
    FAST_IO;
#ifndef ONLINE_JUDGE
    clock_t start = clock();
    freopen("input.txt", "r", stdin);
#endif

    cin >> n;
    memset(dp, -1, sizeof(dp));
    cout << f(1, 0, 0, false) << endl;

#ifndef ONLINE_JUDGE
    cout << endl << "elapsed time: " << static_cast<double>(clock() - start) / CLOCKS_PER_SEC << "ms" << endl;
#endif
    return 0;
}