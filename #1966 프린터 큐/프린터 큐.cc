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

int t;
int n, want_seq, x;
deque<pii> q;

int main(){
    FAST_IO;
#ifndef ONLINE_JUDGE
    clock_t start = clock();
    freopen("input.txt", "r", stdin);
#endif

    cin >> t;
    while(t--) {
        cin >> n >> want_seq;
        q.clear();
        int res = 0;
        rep(i, 0, n) {
            cin >> x;
            q.pb({x, i});
        }

        // 더 큰 값이 있으면
        // queue의 뒤로 보내기
        // 없으면 pop 해서 want_seq인지 비교
        while(true) {
            auto [value, seq] = q.front();
            bool found_bigger = 0;

            for (auto [valuee, seqq] : q) {
                if (valuee > value) {
                    q.pb({value, seq});
                    q.pop_front();
                    found_bigger = 1;
                    break;
                }
            }
            if(!found_bigger) {
                res++;
                q.pop_front();
                if (seq == want_seq) {
                    cout << res << endl;
                    break;
                }
            }
        }
    }

#ifndef ONLINE_JUDGE
    cout << endl << "elapsed time: " << static_cast<double>(clock() - start) / CLOCKS_PER_SEC << "ms" << endl;
#endif
    return 0;
}