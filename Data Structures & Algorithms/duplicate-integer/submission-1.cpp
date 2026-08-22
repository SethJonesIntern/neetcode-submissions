class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_map<int,bool> m;
        for (int i: nums){
            if (m[i] == true) return true;
            else m[i] = true;
        }


        return false;
        
    }
};