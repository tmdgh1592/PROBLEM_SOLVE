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

string common_line = "어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.";
string begin_line1 = "\"재귀함수가 뭔가요?\"";
string begin_line2 = "\"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.";
string begin_line3 = "마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.";
string begin_line4 = "그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어.\"";

string top_line1 = "\"재귀함수가 뭔가요?\"";
string top_line2 = "\"재귀함수는 자기 자신을 호출하는 함수라네\"";

string end_line = "라고 답변하였지.";

int n;

void print_underline(int cnt) {
    rep(i, 0, cnt) cout << "____";
}

void f(int cnt) {
    if (cnt == n) {
        print_underline(cnt);
        cout << top_line1 << endl;
        print_underline(cnt);
        cout << top_line2 << endl;
        print_underline(cnt);
        cout << end_line << endl;
        return;
    }

    print_underline(cnt);
    cout << begin_line1 << endl;
    print_underline(cnt);
    cout << begin_line2 << endl;
    print_underline(cnt);
    cout << begin_line3 << endl;
    print_underline(cnt);
    cout << begin_line4 << endl;

    f(cnt + 1);

    print_underline(cnt);
    cout << end_line << endl;
}

int main(){
    FAST_IO;
#ifndef ONLINE_JUDGE
    clock_t start = clock();
    freopen("input.txt", "r", stdin);
#endif

    cin >> n;
    cout << common_line << endl;
    f(0);

#ifndef ONLINE_JUDGE
    cout << endl << "elapsed time: " << static_cast<double>(clock() - start) / CLOCKS_PER_SEC << "ms" << endl;
#endif
    return 0;
}