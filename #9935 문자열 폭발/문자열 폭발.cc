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

string line, bomb;
vector<char> vec;
char trigger;

int main(){
    FAST_IO;
#ifndef ONLINE_JUDGE
    clock_t start = clock();
    freopen("input.txt", "r", stdin);
#endif
    cin >> line >> bomb;
    trigger = *--bomb.end();
    int bombLen = bomb.sz;
    
    for(char c : line) {
        vec.pb(c);
        if (c == trigger && vec.sz >= bombLen) {
            vector<char> subVector(vec.end() - bombLen, vec.end());

            string str;
            rep(i, 0, bombLen) str += subVector[i];
            if (str == bomb) rep(i, 0, bombLen) vec.pop_back();
        }
    }

    if (vec.sz == 0) {
        cout << "FRULA";
    } else {
        for (char c : vec) cout << c;
    }
#ifndef ONLINE_JUDGE
    cout << endl << "elapsed time: " << static_cast<double>(clock() - start) / CLOCKS_PER_SEC << "ms" << endl;
#endif
    return 0;
}