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

int n, s;
int seq = 0;
vector<int> vec;
bool flag = 0;

void f(int cost) {
    if (cost == n) {
        if (++seq == s) {
            flag = 1;
            for (int i = 0; i < vec.sz; i++) {
                if (i == vec.sz - 1) {
                    cout << vec[i];
                } else {
                    cout << vec[i] << "+";
                }
            }
            return;
        }
    }

    REP(i, 1, 3) {
        if (cost + i > n) continue;
        vec.pb(i);
        f(cost + i);
        vec.pop_back();
    }
}

int main(){
    FAST_IO;
#ifndef ONLINE_JUDGE
    clock_t start = clock();
    freopen("input.txt", "r", stdin);
#endif
    cin >> n >> s;
    f(0);
    if (flag == 0) cout << -1;

#ifndef ONLINE_JUDGE
    cout << endl << "elapsed time: " << static_cast<double>(clock() - start) / CLOCKS_PER_SEC << "ms" << endl;
#endif
    return 0;
}