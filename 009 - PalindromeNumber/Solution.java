class Solution {
    public boolean isPalindrome(int x) {
        String s = String.valueOf(x);
        int left = s.length()-1;
        for (int right = 0; right < s.length(); right++){
            if (s.charAt(right)!=s.charAt(left)){
                return false;
            }
            left--;
        }
        return true;
    }
}
