#include <iostream>
#include <string>
using namespace std;

class Solution {
public:
    bool isPalindrome(int x) {
        string s = to_string(x);
        if (s.length() <=1){
            return true;
        }
        int left = s.length()-1;
        for (int right = 0; right < s.length(); right++){
            if (s[right]!=s[left]){
                return false;
            }
            left--;
        }
        return true;
    }
};
