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

int t, n;
int x, y;
vector<pii> vec;

int f() {
    cin >> n;
    vec.clear();

    rep(i, 0, n) {
        cin >> x >> y;
        vec.pb({x, y});
    }
    sort(all(vec));

    int ans = 1;
    int other_index = 0;

    rep(i, 1, n) {
        int my = vec[i].second;
        int other = vec[other_index].second;

        if (my < other) {
            other_index = i;
            ans++;
        }
    }
    return ans;
}

int main(){
    FAST_IO;
#ifndef ONLINE_JUDGE
    clock_t start = clock();
    freopen("input.txt", "r", stdin);
#endif

    cin >> t;
    while(t--) {
        cout << f() << endl;
    }

#ifndef ONLINE_JUDGE
    cout << endl << "elapsed time: " << static_cast<double>(clock() - start) / CLOCKS_PER_SEC << "ms" << endl;
#endif
    return 0;
}