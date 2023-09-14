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

int t;
int n, want_index;
int x;
deque<pii> q;

bool is_bigger_than(int priority) {
    rep(i, 0, q.sz) {
        auto& [pri, idx] = q[i];
        if (pri > priority) {
            return true;
        }
    }
    return false;
}

int main(){
    FAST_IO;
#ifndef ONLINE_JUDGE
    clock_t start = clock();
    freopen("input.txt", "r", stdin);
#endif

    cin >> t;
    rep(i, 0, t) {
        q.clear();
        cin >> n >> want_index;
        rep(j, 0, n) {
            cin >> x;
            q.pb({x, j});
        }

        int cnt = 0;
        while(true) {
            auto [priority, idx] = q.front();
            if (is_bigger_than(priority)) {
                q.pb({priority, idx});
                q.pop_front();
            } else {
                q.pop_front();
                cnt++;
                if (idx == want_index) {
                    cout << cnt << endl;
                    break;
                }
            }
       }
    }

#ifndef ONLINE_JUDGE
    cout << endl << "elapsed time: " << static_cast<double>(clock() - start) / CLOCKS_PER_SEC << "ms" << endl;
#endif
    return 0;
}