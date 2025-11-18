#include <iostream>
#include <string>
using namespace std;

class Solution {
    //Solution does not use typecasting
public:
    bool isPalindrome(int x) {
        if (x < 0 || x % 10 == 0 && x!=0){
            return false;
        }
        int reversedHalf = 0;
        while (x > reversedHalf){
            reversedHalf = reversedHalf * 10 + x % 10;
            x /= 10;
        }
        return (x == reversedHalf || x == reversedHalf / 10);
    }
};
