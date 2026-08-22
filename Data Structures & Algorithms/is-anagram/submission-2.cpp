class Solution {
public:
    bool isAnagram(string s, string t) {

        unordered_map<int,int> m;

        for(char c : s){
            m[c]++;
        }
        for(char c : t){
            m[c]--;
            if(m[c] < 0) return false;
        }
        for(char c : s){
            if(m[c] != 0) return false;
        }
        return true;
    }
};
