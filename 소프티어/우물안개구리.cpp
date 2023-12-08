#include<bits/stdc++.h>


using namespace std;

int n, m, power, a, b;
vector<int> vec;
map<int, bool> mp;
int ans;

int main(int argc, char** argv)
{
  ios_base::sync_with_stdio(0);
  cin.tie(NULL);
  cout.tie(NULL);

  cin >> n >> m;
  vec.push_back(0);
  for(int i=0; i<n; i++) {
    cin >> power;
    mp[i+1] = true;
    vec.push_back(power);
  }

  for(int i=0; i<m; i++) {
    cin >> a >> b;
    int a_power = vec[a];
    int b_power = vec[b];

    if (a_power <= b_power) {
      mp[a] = false;
    }
    if (b_power <= a_power) {
      mp[b] = false;
    }
  }

  for(int i=1; i<=n; i++) {
    if (mp[i]) ans++;
  }

  cout << ans;
  
  return 0;
}