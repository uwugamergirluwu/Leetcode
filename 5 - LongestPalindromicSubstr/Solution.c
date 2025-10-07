#include <stdio.h>
#include <stdlib.h>
#include <string.h>


char* returnPalindrome(char* s, int s_length, int left, int right){
    while(left >= 0 && right < s_length && s[left]==s[right]){
        left--;
        right++;
    }
    int len = right - left - 1;
    char *substring = (char *)malloc((len + 1) * sizeof(char));
    strncpy(substring, s + left + 1, len);
    substring[len] = '\0';
    return (substring);
}

char* longestPalindrome(char* s) {
    int s_length = strlen(s);
    char *longest = (char *)malloc(1);
    longest[0] = '\0';
    for (int i = 0; i < s_length; i++){
        char *odd = returnPalindrome(s, s_length, i, i);
        char *even = returnPalindrome(s, s_length, i, i+1);
        char *substring = (strlen(odd) > strlen(even)) ? odd : even;
        if (strlen(substring) > strlen(longest)){
            free(longest);
            longest=substring;
        }else{
            free(substring);
        }
        if (substring == odd) free (even);
        else free(odd);
    }
    return longest;
}
