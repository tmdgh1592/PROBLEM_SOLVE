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

int n;
string line;
char c, cmd;
list<char> mList;

int main(){
    FAST_IO;
#ifndef ONLINE_JUDGE
    clock_t start = clock();
    freopen("input.txt", "r", stdin);
#endif

    cin >> line >> n;
    for(char x : line) mList.pb(x);
    auto cursor = mList.end();

    rep(i, 0, n) {
        cin >> cmd;

        if (cmd == 'P') {
            cin >> c;
            mList.insert(cursor, c);
        }
        else if (cmd == 'L') {
            if (cursor != mList.begin()) --cursor;
        }
        else if (cmd == 'D') {
            if (cursor != mList.end()) ++cursor;
        }
        else if (cmd == 'B') {
            if (cursor != mList.begin()) {
                cursor = mList.erase(--cursor);
            }
        }
    }

    for(char x : mList) cout << x;

#ifndef ONLINE_JUDGE
    cout << endl << "elapsed time: " << static_cast<double>(clock() - start) / CLOCKS_PER_SEC << "ms" << endl;
#endif
    return 0;
}