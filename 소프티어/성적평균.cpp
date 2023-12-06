#include <bits/stdc++.h>

using namespace std;

int n, k, score, prefix_sum;
vector<int> score_sums;

int main(int argc, char** argv)
{
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);

  cin >> n >> k;
  score_sums.push_back(0);
  for(int i=0; i<n; i++) {
    cin >> score;
    prefix_sum += score;
    score_sums.push_back(prefix_sum);
  }

  cout << fixed;
  cout.precision(2);
  int s, e;
  for (int i=0; i<k; i++) {
    cin >> s >> e;
    int partitial_sum = score_sums[e] - score_sums[s - 1];
    float count = e - s + 1;
    float result = partitial_sum / count;
    cout << result << endl;
  }

  return 0;
}