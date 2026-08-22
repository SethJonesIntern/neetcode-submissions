class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int,int> m;
        vector<int> res;
        for(int i = 0; i < nums.size(); i++){
            int curtar = target - nums[i];
            if(m.find(curtar) != m.end()){
                res.push_back(m[curtar]);
                res.push_back(i);
                return res;
            }
            m[nums[i]] = i;
        }
        return res;       
    }
};
