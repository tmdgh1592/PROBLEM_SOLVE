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

int n, x, res;
vector<int> vec;

int main(){
    FAST_IO;
#ifndef ONLINE_JUDGE
    clock_t start = clock();
    freopen("input.txt", "r", stdin);
#endif

    cin >> n;
    rep(i, 0, n) {
        cin >> x;
        vec.pb(x);
    }

    int i_sum = 1;
    rep(i, 0, n - 3) {
        i_sum *= vec[i];
        int j_sum = 1;
        rep(j, i + 1, n - 2) {
            j_sum *= vec[j];
            int k_sum = 1;
            rep(k, j + 1, n - 1) {
                k_sum *= vec[k];
                int l_sum = 1;
                rep(l, k + 1, n) {
                    l_sum *= vec[l];
                }
                res = max(res, i_sum + j_sum + k_sum + l_sum);
            }
        }
    }
    cout << res << endl;

#ifndef ONLINE_JUDGE
    cout << endl << "elapsed time: " << static_cast<double>(clock() - start) / CLOCKS_PER_SEC << "ms" << endl;
#endif
    return 0;
}