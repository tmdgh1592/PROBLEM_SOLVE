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
using namespace std;

#ifdef ONLINE_JUDGE
constexpr bool ndebug = true;
#else
constexpr bool ndebug = false;
#endif
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

int t, n, cls, ans, prev_total;
unordered_map<int, vector<int>> mp;
vector<int> vec;
vector<int> players;

int main(){
    FAST_IO;
#ifndef ONLINE_JUDGE
    clock_t start = clock();
    freopen("input.txt", "r", stdin);
#endif

    cin >> t;
    rep(i, 0, t) {
        cin >> n;
        prev_total = INF;
        vec.clear(); players.clear(); mp.clear();

        rep(j, 0, n) {
            cin >> cls;
            vec.pb(cls);
        }
        copy_if(all(vec), back_inserter(players), [](int num) { return count(all(vec), num) == 6; });

        for (auto i = 0; i < players.size(); i++) {
            mp[players[i]].pb(i + 1);
        }

        for (auto team : mp) {
            ll sum = accumulate(team.second.begin(), team.second.begin() + 4, 0);

            if (sum < prev_total || (sum == prev_total && team.second[4] < mp[ans][4])) {
                ans = team.first;
                prev_total = sum;
            }
        }

        cout << ans << endl;
    }

#ifndef ONLINE_JUDGE
    cout << endl << "elapsed time: " << static_cast<double>(clock() - start) / CLOCKS_PER_SEC << "ms" << endl;
#endif
    return 0;
}