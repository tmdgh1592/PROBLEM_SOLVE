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

string line;
vector<char> vec;

int main(){
    FAST_IO;
#ifndef ONLINE_JUDGE
    clock_t start = clock();
    freopen("input.txt", "r", stdin);
#endif

    while(true) {
        getline(cin, line);
        if (line == ".") break;
        bool flag = 0;
        vec.clear();

        for(char c : line) {
            if (c != '[' && c != '(' && c != ']' && c != ')') continue;
            else if (c == '(' || c == '[') vec.pb(c);
            else if (c == ')' && !vec.empty() && vec.back() =='(') vec.pop_back();
            else if (c == ']' && !vec.empty() && vec.back() =='[') vec.pop_back();
            else {
                flag = 1;
                break;
            }
        }

        if (flag || !vec.empty()) cout << "no" << endl;
        else cout << "yes" << endl;
    }

#ifndef ONLINE_JUDGE
    cout << endl << "elapsed time: " << static_cast<double>(clock() - start) / CLOCKS_PER_SEC << "ms" << endl;
#endif
    return 0;
}