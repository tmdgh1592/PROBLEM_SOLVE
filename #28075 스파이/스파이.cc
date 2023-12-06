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

int n, m;
int arr[2][3];
int res;

void f(int score, int day, int prev_place) {
    if (day == n) {
        if (score >= m) ++res;
        return;
    }

    rep(i, 0, 2) {
        rep(j, 0, 3) {
            if (j == prev_place) {
                f(score + arr[i][j] / 2, day + 1, j);
            } else {
                f(score + arr[i][j], day + 1, j);
            }
        }
    }
}

int main(){
    FAST_IO;
#ifndef ONLINE_JUDGE
    clock_t start = clock();
    freopen("input.txt", "r", stdin);
#endif

    cin >> n >> m;
    rep(i, 0, 2) rep(j, 0, 3) cin >> arr[i][j];
    f(0, 0, -1);
    cout << res;

#ifndef ONLINE_JUDGE
    cout << endl << "elapsed time: " << static_cast<double>(clock() - start) / CLOCKS_PER_SEC << "ms" << endl;
#endif
    return 0;
}