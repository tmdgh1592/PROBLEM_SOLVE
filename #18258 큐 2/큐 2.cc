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

int n, x;
string cmd;
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
        if (cmd == "push") {
            cin >> x;
            q.pb(x);
        }
        if (cmd == "pop") {
            if (q.empty()) cout << "-1" << endl;
            else {
                cout << q.front() << endl;
                q.pop_front();
            }
        }
        if (cmd == "size") cout << q.sz << endl;
        if (cmd == "empty") cout << q.empty() << endl;
        if (cmd == "front") {
            if (q.empty()) cout << "-1" << endl;
            else cout << q.front() << endl;
        }
        if (cmd == "back") {
            if (q.empty()) cout << "-1" << endl;
            else cout << q.back() << endl;
        }
    }

#ifndef ONLINE_JUDGE
    cout << endl << "elapsed time: " << static_cast<double>(clock() - start) / CLOCKS_PER_SEC << "ms" << endl;
#endif
    return 0;
}