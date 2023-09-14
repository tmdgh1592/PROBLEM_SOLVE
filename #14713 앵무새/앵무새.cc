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
string str;
stack<string> stacks[100];

stack<string> split(string str, char delimeter) {
    istringstream iss(str);
    string buffer;

    stack<string> stk;

    while(getline(iss, buffer, delimeter)) {
        stk.push(buffer);
    }

    return stk;
}

int main(){
    FAST_IO;
#ifndef ONLINE_JUDGE
    clock_t start = clock();
    freopen("input.txt", "r", stdin);
#endif

    cin >> n;
    cin.ignore();
    rep(i, 0, n) {
        getline(cin, str);
        stacks[i] = split(str, ' ');
    }

    getline(cin, str, '\n');
    stack<string> mStack = split(str, ' ');
    

    while (!mStack.empty()) {
        string& cur = mStack.top();

        bool flag = 0;
        rep(i, 0, n) {
            if (stacks[i].empty()) continue;
            if (stacks[i].top() == cur) {
                stacks[i].pop();
                mStack.pop();
                flag = 1;
                break;
            }
        }

        if (flag == 0) {
            cout << "Impossible" << endl;
            return 0;
        }
    }

    if (mStack.empty()) {
        cout << "Possible" << endl;
    } else {
        cout << "Impossible" << endl;
    }

#ifndef ONLINE_JUDGE
    cout << endl << "elapsed time: " << static_cast<double>(clock() - start) / CLOCKS_PER_SEC << "ms" << endl;
#endif
    return 0;
}