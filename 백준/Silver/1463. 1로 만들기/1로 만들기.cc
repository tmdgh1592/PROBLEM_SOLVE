#include <bits/stdc++.h>
#define FAST ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL)
#define endl "\n"
#define rep(i, a, b) for(auto i = a; i < b; ++i)
#define REP(i, a, b) for(auto i = a; i <= b; ++i)
#define pii pair<int, int>
#define all(v) (v).begin(), (v).end()
#define pb push_back
#define INF 987654321

using namespace std;
typedef long long ll;
typedef unsigned long long ull;

int n;
vector<int> cache;

int f(int now) {
    if (now == 1) return 0;
    if (cache[now] != -1) return cache[now];

    cache[now] = f(now - 1) + 1;
    if (now % 3 == 0) cache[now] = min(cache[now], f(now / 3) + 1);
    if (now % 2 == 0)cache[now] = min(cache[now], f(now / 2) + 1);

    return cache[now];
}

int main(){
    FAST;
#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
#endif

    cin >> n;
    cache = vector<int>(n + 1, -1);
    cout << f(n);

    return 0;
}