#include <iostream>
#include <string>
using namespace std;

class Solution {
public:
    string longestPalindrome(const string& s) {
        string longest = "";
        for (int i=0; i < s.length(); i++){
            string odd = returnPalindrome(s, i ,i);
            string even = returnPalindrome(s, i, i+1);
            string substring = (odd.length()>even.length()) ? odd : even;
            longest = (substring.length()>longest.length()) ? substring : longest;
        }
        return longest;
    }

    string returnPalindrome(const string& s, int left, int right){
        while (left >= 0 && right < s.length() && s[left]==s[right]){
            left--;
            right++;
        }
        return(s.substr(left+1, right-left-1));
    }
};
