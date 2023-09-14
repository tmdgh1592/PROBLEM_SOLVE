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

int n, x, cur, move_amount;
deque<int> q;
const int MARK = -10000;

int get_next_cur() {
    int move_count = 0;
    while(move_count < abs(move_amount)) {
        if (move_amount < 0) {
            --cur;
            if (cur == -1) cur = n - 1;
            if (q[cur] == MARK) continue;
        } else {
            ++cur;
            if (cur == n) cur = 0;
            if (q[cur] == MARK) continue;
        }
        ++move_count;
    }
    return cur;
}

int main(){
    FAST_IO;
#ifndef ONLINE_JUDGE
    clock_t start = clock();
    freopen("input.txt", "r", stdin);
#endif

    cin >> n;

    cur = 0;
    rep(i, 0, n) {
        cin >> x;
        q.pb(x);
    }

    move_amount = q[cur];
    q[cur] = MARK;
    cout << cur + 1 << " ";

    rep(i, 0, n - 1) {
        cur = get_next_cur();
        move_amount = q[cur];
        q[cur] = MARK;
        cout << cur + 1 << " ";
    }

#ifndef ONLINE_JUDGE
    cout << endl << "elapsed time: " << static_cast<double>(clock() - start) / CLOCKS_PER_SEC << "ms" << endl;
#endif
    return 0;
}