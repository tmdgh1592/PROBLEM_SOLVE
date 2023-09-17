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

int n, x, cnt;
deque<pii> q; // 값, id

int main(){
    FAST_IO;
#ifndef ONLINE_JUDGE
    clock_t start = clock();
    freopen("input.txt", "r", stdin);
#endif

    cin >> n;
    rep(i, 0, n) {
        cin >> x;
        q.pb({x, i});
    }
    sort(all(q), greater<pii>());

    while(!q.empty()) {
        int prev_id = -1;
        cnt++;

        auto [value, id] = q.front();
        q.pop_front();
        if (value - 1 > 0) {
            q.push_front({value - 1, id});
        }
        
        if (q.sz == 0) continue; // 1개밖에 없거나 빈 경우 스킵
        if (q.sz == 1) {
            auto [tv, tid] = q.front();
            if (tid == id) continue;
        }

        auto [v1, id1] = q[0];
        auto [v2, id2] = q[1];
        q.pop_front();
        q.pop_front();

        if (v2 - 1 > 0) {
            q.push_front({v2 - 1, id2});
        }
        q.push_front({v1, id1});
        sort(all(q), greater<pii>());
    }

    if (cnt > 1440) {
        cout << -1 << endl;
    } else {
        cout << cnt;
    }

#ifndef ONLINE_JUDGE
    cout << endl << "elapsed time: " << static_cast<double>(clock() - start) / CLOCKS_PER_SEC << "ms" << endl;
#endif
    return 0;
}