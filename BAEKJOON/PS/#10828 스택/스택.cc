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
string oper;
stack<int> stk;

void command(string cmd) {
    if (cmd == "push") stk.push(x);
    if (cmd == "pop") {
        if (stk.empty()) cout << -1 << endl;
        else {
            cout << stk.top() << endl;
            stk.pop();
        }
    }
    if (cmd == "size") cout << stk.sz << endl;
    if (cmd == "empty") {
        if (stk.empty()) cout << 1 << endl;
        else cout << 0 << endl;
    }
    if (cmd == "top") {
        if (stk.empty()) cout << -1 << endl;
        else cout << stk.top() << endl;
    }
}

int main(){
    FAST_IO;
#ifndef ONLINE_JUDGE
    clock_t start = clock();
    freopen("input.txt", "r", stdin);
#endif

    cin >> n;
    rep(i, 0, n) {
        cin >> oper;
        if (oper == "push") cin >> x;
        command(oper);
    }


#ifndef ONLINE_JUDGE
    cout << endl << "elapsed time: " << static_cast<double>(clock() - start) / CLOCKS_PER_SEC << "ms" << endl;
#endif
    return 0;
}