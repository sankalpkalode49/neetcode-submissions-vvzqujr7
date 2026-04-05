#include <unordered_map>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int,int> mp;

        // Step 1: Count frequency
        for (int num : nums) {
            mp[num]++;
        }

        // Step 2: Move map to vector
        vector<pair<int,int>> vec(mp.begin(), mp.end());

        // Step 3: Sort by frequency (descending)
        sort(vec.begin(), vec.end(), [](auto &a, auto &b) {
            return a.second > b.second;
        });

        // Step 4: Take top k elements
        vector<int> res;
        for (int i = 0; i < k; i++) {
            res.push_back(vec[i].first);
        }

        return res;
    }
};