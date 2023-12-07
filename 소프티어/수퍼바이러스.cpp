#include<bits/stdc++.h>
#define MOD 1000000007;
using namespace std;

long long int k, p, n;

long long f(long long a, long long b) {
  if (b == 1) return a;
  long long res = f(a, b / 2);
  res = res * res % MOD;

  if (b % 2 == 1) res = res * a % MOD;
  return res;
}

int main(int argc, char** argv)
{
  ios_base::sync_with_stdio(0);
  cin.tie(NULL);
  cout.tie(NULL);
  cin >> k >> p >> n;

  cout << (k * f(p, 10 * n)) % MOD;

  return 0;
}