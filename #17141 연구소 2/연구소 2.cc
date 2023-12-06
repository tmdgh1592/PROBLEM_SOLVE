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

int n, m, res = INF, want_virus_cnt;
int graph[51][51];
vector<pii> viruses;
vector<pii> cur_viruses;
bool virus_visited[51];
pii opers[4] = {{-1, 0}, {0, 1}, {1, 0}, {0, -1}};

struct node {
    int x, y, round;
};

bool in_range(int x, int y) {
    return 0 <= x && x < n && 0 <= y && y < n;
}

int bfs() {
    queue<node> q;
    bool visited[51][51];
    memset(visited, 0, sizeof(visited));

    for (auto [x, y] : cur_viruses) {
        q.push({x, y, 0});
        visited[x][y] = 1;
    }
    int cur_virus_cnt = q.sz;
    if (cur_virus_cnt == want_virus_cnt) return 0;

    while (!q.empty()) {
        auto [x, y, round] = q.front();
        q.pop();

        for (auto [dx, dy] : opers) {
            int nx = x + dx;
            int ny = y + dy;

            if (!in_range(nx, ny)) continue;
            if (visited[nx][ny]) continue;
            if (graph[nx][ny] == 1) continue;

            q.push({nx, ny, round + 1});
            visited[nx][ny] = 1;
            ++cur_virus_cnt;

            if (cur_virus_cnt == want_virus_cnt) return round + 1;
        }
    }
    return INF;
}

void dfs(int now) {
    if (cur_viruses.sz == m) {
        res = min(res, bfs());
        return;
    }

    rep(i, now, viruses.sz) {
        virus_visited[i] = 1;
        cur_viruses.pb(viruses[i]);
        dfs(i + 1);
        virus_visited[i] = 0;
        cur_viruses.pop_back();
    }
}

int main(){
    FAST_IO;
#ifndef ONLINE_JUDGE
    clock_t start = clock();
    freopen("input.txt", "r", stdin);
#endif

    cin >> n >> m;
    rep(i, 0, n) {
        rep(j, 0, n) {
            cin >> graph[i][j];
            if (graph[i][j] == 2) {
                viruses.pb({i, j});
                ++want_virus_cnt;
            }
            if (graph[i][j] == 0) {
                ++want_virus_cnt;
            }
        }
    }

    dfs(0);

    if (res == INF) {
        cout << -1;
    } else {
        cout << res;
    }

#ifndef ONLINE_JUDGE
    cout << endl << "elapsed time: " << static_cast<double>(clock() - start) / CLOCKS_PER_SEC << "ms" << endl;
#endif
    return 0;
}