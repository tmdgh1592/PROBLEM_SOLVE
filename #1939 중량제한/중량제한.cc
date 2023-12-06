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

int n, m;
int a, b, c;
int stt, dest;

vector<pii> graph[10001];
bool visited[10001];

bool f(int weight) {
    queue<int> q;
    q.push(stt);
    memset(visited, 0, sizeof(visited));
    visited[stt] = 1;

    while(!q.empty()) {
        int now = q.front();
        q.pop();

        if (now == dest) return 1;

        for (auto [next, limit] : graph[now]) {
            if (visited[next]) continue;
            if (weight > limit) continue;
            
            visited[next] = 1;
            q.push(next);
        }
    }
    return 0;
}

int main(){
    FAST_IO;
#ifndef ONLINE_JUDGE
    clock_t start = clock();
    freopen("input.txt", "r", stdin);
#endif

    cin >> n >> m;
    rep(i, 0, m) {
        cin >> a >> b >> c;
        graph[a].pb({b, c});
        graph[b].pb({a, c});
    }
    cin >> stt >> dest;

    int lo = 1, hi = 1000000001;
    while(lo + 1 < hi) {
        int mid = (lo + hi) >> 1;
        if (f(mid)) lo = mid;
        else hi = mid;
    }
    cout << lo;

#ifndef ONLINE_JUDGE
    cout << endl << "elapsed time: " << static_cast<double>(clock() - start) / CLOCKS_PER_SEC << "ms" << endl;
#endif
    return 0;
}