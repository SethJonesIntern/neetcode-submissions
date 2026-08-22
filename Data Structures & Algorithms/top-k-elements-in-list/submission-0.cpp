#include <unordered_map>

class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int,int> map;
        vector<vector<int>> freq(nums.size() + 1);

        for(int x : nums){
            if(map.find(x) != map.end()){
                map[x]++;
            } else map[x] = 1;
        }
        for(auto[n,c]: map){
            freq[c].push_back(n);
        }

        vector<int> res;
        for(int i = freq.size() - 1; i > 0; i--){
            for(int x: freq[i]){
                res.push_back(x);
                if(res.size() == k) return res;
            }
        }

    return res;
    }
};
