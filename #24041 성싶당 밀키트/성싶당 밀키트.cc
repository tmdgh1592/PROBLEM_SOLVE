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

struct node {
    ll speed, limit;
    bool can_exclude;
};

ll n, g, k;
ll s, l;
bool exc;
ll exclude_cnt = 0;
vector<node> nodes;
vector<node> bactes;

ll calc_bacteria(ll speed, ll now_day, ll limit) {
    return speed * max(1ll, now_day - limit);
}

bool f(int day) {
    vector<ll> vec;
    vec.clear();

    ll bacteria_sum = 0;
    ll bacte_cnt = 0;
    for (auto [s, l, can_exclude] : nodes) {
        ll bacteria = calc_bacteria(s, day, l);
        bacteria_sum += bacteria;
        if (can_exclude) {
            vec.pb(bacteria);
        }
    }

    sort(all(vec), greater<ll>());
    rep(i, 0, exclude_cnt) {
        bacteria_sum -= vec[i];
    }
    return bacteria_sum <= g;
}

int main(){
    FAST_IO;
#ifndef ONLINE_JUDGE
    clock_t start = clock();
    freopen("input.txt", "r", stdin);
#endif

    cin >> n >> g >> k;
    rep(jjjj, 0, n) {
        cin >> s >> l >> exc;
        nodes.pb({s, l, exc});
        if(exc) ++exclude_cnt;
    }
    exclude_cnt = min(exclude_cnt, k);

    ll lo = 1;
    ll hi = 2000000001;

    while (lo + 1 < hi) {
        ll mid = (lo + hi) >> 1;
        if (f(mid)) {
            lo = mid;
        } else {
            hi = mid;
        }
    }
    cout << lo << endl;

#ifndef ONLINE_JUDGE
    cout << endl << "elapsed time: " << static_cast<double>(clock() - start) / CLOCKS_PER_SEC << "ms" << endl;
#endif
    return 0;
}