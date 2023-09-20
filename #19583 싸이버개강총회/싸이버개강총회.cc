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

int start, end1, end2, ans;
unordered_map<string, int> enter;

int getTime(string time) {
    int total = 0;
    stringstream ss(time);
    string buffer;

    int weight = 60;
    while(getline(ss, buffer, ':')) {
        total += stoi(buffer) * weight;
        weight = 1;
    }
    return total;
}

int main(){
    FAST_IO;
#ifndef ONLINE_JUDGE
    clock_t start = clock();
    freopen("input.txt", "r", stdin);
#endif

    string time, name;
    cin >> time;
    start = getTime(time);
    cin >> time;
    end1 = getTime(time);
    cin >> time;
    end2 = getTime(time);

    while(!cin.eof()) {
        cin >> time >> name;
        if (getTime(time) <= start) {
            if (enter[name] == 0) {
                enter[name] = 1;
            }
            continue;
        }

        int exitTime = getTime(time);
        if (end1 <= exitTime && exitTime <= end2) {
            if (enter[name] == 1) enter[name] = 2;
        }
    }

    for (auto [name, count] : enter) {
        if (count == 2) ans++;
    }
    cout << ans;


#ifndef ONLINE_JUDGE
    cout << endl << "elapsed time: " << static_cast<double>(clock() - start) / CLOCKS_PER_SEC << "ms" << endl;
#endif
    return 0;
}