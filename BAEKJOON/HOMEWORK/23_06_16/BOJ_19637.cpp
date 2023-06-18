#include <bits/stdc++.h>
#define endl "\n"
#define FAST ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL)
#define rep(i, a, b) for(auto i = a; i < b; ++i)
#define REP(i, a, b) for(auto i = a; i <= b; ++i)
#define pii pair<int, int>
#define all(v) (v).begin(), (v).end()
#define pb push_back
#define INF numeric_limits<int>::max()
#define mp make_pair

using namespace std;

#define FAST_IO \
    if constexpr (ndebug) { cin.tie(nullptr); ios::sync_with_stdio(false); }
#define debug(x) \
    if constexpr (!ndebug) cout << "[DEBUG] " << #x << " == " << x << '\n';
#define debugf(...) \
    if constexpr (!ndebug) { cout << "[DEBUG] "; printf(__VA_ARGS__); }
#define debugc(c) \
    if constexpr (!ndebug) { cout << "[DEBUG] "<< #c << ": "; for (const auto& elem : c) cout << elem << ", "; cout << '\n'; }

typedef long long ll;
typedef unsigned long long ull;

int main(){
    FAST;
#ifndef ONLINE_JUDGE
    clock_t start = clock();
    freopen("input.txt", "r", stdin);
#endif

int n, m;
cin >> n >> m;
vector<int> scores;
vector<string> rates;

rep(i, 0, n) {
    string rate;
    int value;
    cin >> rate >> value;
    
    scores.pb(value);
    rates.pb(rate);
}

rep(i, 0, m) {
    int score;
    int l = 0, h = n - 1;
    int mid = -1;
    cin >> score;
    
    while(l <= h) {
        mid = (l + h) / 2;

        if (score <= scores[mid]) {
            h = mid - 1;
        } else {
            l = mid + 1;
        }
    }

    cout << rates[l] << endl;
}


#ifndef ONLINE_JUDGE
    cout << endl << "elapsed time: " << static_cast<double>(clock() - start) / CLOCKS_PER_SEC << "ms" << endl;
#endif
    return 0;
}