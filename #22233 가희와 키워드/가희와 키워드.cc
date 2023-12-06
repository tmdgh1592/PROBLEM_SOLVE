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

vector<string> split(string str) {
    stringstream ss(str);
    string buffer;
    vector<string> vec;

    while(getline(ss, buffer, ',')) {
        vec.pb(buffer);
    }
    return vec;
}

int n, t;
string s;
unordered_set<string> mset;

int main(){
    FAST_IO;
#ifndef ONLINE_JUDGE
    clock_t start = clock();
    freopen("input.txt", "r", stdin);
#endif

    cin >> n >> t;
    rep(i, 0, n) {
        cin >> s;
        mset.insert(s);
    }

    while(t--) {
        cin >> s;
        vector<string> vec = split(s);
        for(auto cur_s : vec) {
            if (mset.find(cur_s) != mset.end()) {
                mset.erase(cur_s);
            }
        }
        cout << mset.sz << endl;
    }


#ifndef ONLINE_JUDGE
    cout << endl << "elapsed time: " << static_cast<double>(clock() - start) / CLOCKS_PER_SEC << "ms" << endl;
#endif
    return 0;
}