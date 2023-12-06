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

int n, cmd, x;
deque<int> q;

int main(){
    FAST_IO;
#ifndef ONLINE_JUDGE
    clock_t start = clock();
    freopen("input.txt", "r", stdin);
#endif

    cin >> n;
    rep(i, 0, n) {
        cin >> cmd;
        if (cmd == 1) {
            cin >> x;
            q.push_front(x);
        }
        if (cmd == 2) {
            cin >> x;
            q.pb(x);
        }
        if (cmd == 3) {
            if (q.empty()) cout << -1 << endl;
            else {
                cout << q.front() << endl;
                q.pop_front();
            }
        }
        if (cmd == 4) {
            if (q.empty()) cout << -1 << endl;
            else {
                cout << q.back() << endl;
                q.pop_back();
            }
        }
        if (cmd == 5) {
            cout << q.sz << endl;
        }
        if (cmd == 6) {
            cout << q.empty() << endl;
        }
        if (cmd == 7) {
            if (q.empty()) cout << -1 << endl;
            else cout << q.front() << endl;
        }
        if (cmd == 8) {
            if (q.empty()) cout << -1 << endl;
            else cout << q.back() << endl;
        }
    }

#ifndef ONLINE_JUDGE
    cout << endl << "elapsed time: " << static_cast<double>(clock() - start) / CLOCKS_PER_SEC << "ms" << endl;
#endif
    return 0;
}