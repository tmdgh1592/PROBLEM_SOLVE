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

int n, white, black;
int arr[129][129];
int color;

bool is_same_color(int sx, int sy, int size) {
    int standard_color = arr[sx][sy];
    rep (i, sx, sx + size) {
        rep (j, sy, sy + size) {
            if (standard_color != arr[i][j]) return 0;
        }
    }
    return 1;
}

void f(int sx, int sy, int size) {
    if (size == 1) {
        if (arr[sx][sy]) black++;
        else white++;
        return;
    }
    if (is_same_color(sx, sy, size)) {
        if (arr[sx][sy]) black++;
        else white++;
        return;
    }
    f(sx, sy, size / 2);
    f(sx + size / 2, sy, size / 2);
    f(sx, sy + size / 2, size / 2);
    f(sx + size / 2, sy + size / 2, size / 2);
}

int main(){
    FAST_IO;
#ifndef ONLINE_JUDGE
    clock_t start = clock();
    freopen("input.txt", "r", stdin);
#endif

    cin >> n;
    rep(i, 0, n) rep(j, 0, n) cin >> arr[i][j];
    f(0, 0, n);
    cout << white << endl << black;

#ifndef ONLINE_JUDGE
    cout << endl << "elapsed time: " << static_cast<double>(clock() - start) / CLOCKS_PER_SEC << "ms" << endl;
#endif
    return 0;
}