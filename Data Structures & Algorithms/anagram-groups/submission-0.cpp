class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string,vector<string>> map;
        vector<vector<string>> res;
        for(string s: strs){
            string key = s;
            sort(s.begin(),s.end());
            map[s].push_back(key);
        }

        for(auto[x,s]: map){
            res.push_back(s);
        }

        return res;
        
    }
};
