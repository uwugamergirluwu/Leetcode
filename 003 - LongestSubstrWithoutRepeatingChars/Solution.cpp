#include <iostream>
#include <unordered_map>
#include <string>
using namespace std;

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        if (s.length()<=1){
            return s.length();
        }
        int maxLength = 0;
        int left = 0;
        unordered_map<char, int> charMap;
        for (int right = 0; right < s.length(); right++){
            char c = s[right];
            if (charMap.find(c) != charMap.end()){
                left = max(left, charMap[c]+1);
            }
            charMap[c] = right;
            maxLength = max(maxLength, right - left + 1);
        }
        return maxLength;
    }
};
