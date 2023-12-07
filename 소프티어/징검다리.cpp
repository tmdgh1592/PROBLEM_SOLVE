#include<bits/stdc++.h>
using namespace std;

int n;
vector<int> vec;
vector<int> lis;

int main(int argc, char** argv)
{
  ios_base::sync_with_stdio(0);
  cin.tie(NULL);
  cout.tie(NULL);

  cin >> n;
  int height;
  for (int i=0; i<n; i++) {
    cin >> height;
    vec.push_back(height);
  }
  lis.push_back(vec[0]);
  int idx = 1;

  for (int i=1; i<n; i++) {
    if (lis.back() < vec[i]) {
      lis.push_back(vec[i]);
    } else {
      int last_idx = lower_bound(lis.begin(), lis.end(), vec[i]) - lis.begin();
      lis[last_idx] = vec[i];
    }
  }

  cout << lis.size();
  
  
  return 0;
}