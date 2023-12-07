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

int n, x, ans = 0;
int mmin = INF, mmax = -INF;
vector<int> vec;
unordered_map<int, int> mp;

bool is_banseok(int a, int b) {
    return abs(a - b) <= 2;
}

void set_min_max() {
    int mx = -INF;
    int mn = INF;
    for (auto& [value, count] : mp) {
        if (count == 0) continue;
        mn = min(mn, value);
        mx = max(mx, value);
    }
    mmin = mn;
    mmax = mx;
}

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

    int endd = 0;
    mp[vec[0]] = 1;
    rep(startt, 0, n) {
        while (endd < n - 1 && is_banseok(min(mmin, vec[endd + 1]), max(mmax, vec[endd + 1]))) {
            mp[vec[++endd]] += 1;
            ans = max(ans, endd - startt + 1);
            
            set_min_max();
        }
        mp[vec[startt]] -= 1;
        set_min_max();
    }
    cout << ans << endl;

#ifndef ONLINE_JUDGE
    cout << endl << "elapsed time: " << static_cast<double>(clock() - start) / CLOCKS_PER_SEC << "ms" << endl;
#endif
    return 0;
}