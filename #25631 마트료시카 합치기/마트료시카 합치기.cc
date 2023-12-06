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

int n, x, res = 0;
vector<int> mList;
vector<int> clear_indicies;

int main(){
    FAST_IO;
#ifndef ONLINE_JUDGE
    clock_t start = clock();
    freopen("input.txt", "r", stdin);
#endif

    cin >> n;
    rep(i, 0, n) {
        cin >> x;
        mList.pb(x);
    }
    sort(all(mList), greater<int>());

    int processed = 0;
    int cur_idx = 0;
    while(processed != n) {
        while(mList[cur_idx] == -1) cur_idx++;
        int now = mList[cur_idx];
        mList[cur_idx] = -1;
        ++processed;
        rep(i, 1, mList.sz) {
            int next = mList[i];
            if (next == -1) continue;
            if (now > next) {
                mList[i] = -1;
                ++processed;
                now = next;
            }
        }
        res++;
    }

    cout << res;
#ifndef ONLINE_JUDGE
    cout << endl << "elapsed time: " << static_cast<double>(clock() - start) / CLOCKS_PER_SEC << "ms" << endl;
#endif
    return 0;
}