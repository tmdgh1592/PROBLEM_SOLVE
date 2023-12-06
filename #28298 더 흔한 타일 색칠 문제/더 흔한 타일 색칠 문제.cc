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

int n, m, k, res;
string str;
char graph[501][501];
unordered_map<char, int> char_map;

bool comp(pair<char, int> p1, pair<char, int> p2) {
    return p1.second > p2.second;
}

char get_many_char() {
    vector<pair<char, int>> vec(all(char_map));
    sort(all(vec), comp);
    return vec[0].first;
}


int main(){
    FAST_IO;
#ifndef ONLINE_JUDGE
    clock_t start = clock();
    freopen("input.txt", "r", stdin);
#endif

    cin >> n >> m >> k;
    rep(i, 0, n) {
        cin >> str;
        rep(j, 0, m) {
            graph[i][j] = str[j];
        }
    }

    rep(w, 0, k) {
        rep(q, 0, k) {
            for (int i = w; i < n; i += k) {
                for (int j = q; j < m; j += k) {
                    char_map[graph[i][j]] += 1;
                }
            }
            char c = get_many_char();
            res += n * m / k / k - char_map[c];
            for (int i = w; i < n; i += k) {
                for (int j = q; j < m; j += k) {
                    graph[i][j] = c;
                }
            }
            
            char_map.clear();
        }
    }

    cout << res << endl;
    rep(i, 0, n) {
        rep(j, 0, m) {
            cout << graph[i][j];
        }
        cout << endl;
    }

#ifndef ONLINE_JUDGE
    cout << endl << "elapsed time: " << static_cast<double>(clock() - start) / CLOCKS_PER_SEC << "ms" << endl;
#endif
    return 0;
}