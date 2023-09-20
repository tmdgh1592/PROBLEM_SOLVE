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

int n, m, x;
int graph[1001][1001];

int main(){
    FAST_IO;
#ifndef ONLINE_JUDGE
    clock_t start = clock();
    freopen("input.txt", "r", stdin);
#endif

    cin >> n >> m;
    REP(i, 1, n) {
        cin >> graph[i][0];
    }
    REP(i, 1, m) {
        cin >> graph[0][i];
    }
    REP(i, 1, n) {
        REP(j, 1, m) {
            if (graph[i - 1][j] == graph[i][j - 1]) {
                graph[i][j] = 0;
            } else {
                graph[i][j] = 1;
            }
        }
    }
    cout << graph[n][m] << endl;

#ifndef ONLINE_JUDGE
    cout << endl << "elapsed time: " << static_cast<double>(clock() - start) / CLOCKS_PER_SEC << "ms" << endl;
#endif
    return 0;
}