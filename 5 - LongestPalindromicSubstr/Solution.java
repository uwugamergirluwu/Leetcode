class Solution {
    public String longestPalindrome(String s) {
        String longest = "";
        for (int i = 0; i < s.length(); i++){
            String odd = returnPalindrome(s, i, i);
            String even = returnPalindrome(s, i, i+1);
            
            String longer = odd.length() > even.length() ? odd : even;
            if (longer.length() > longest.length()){
                longest = longer;
            }
        }
        return longest;
    
    }

    private String returnPalindrome(String s, int left, int right){
        while (left >=0 && right < s.length() && s.charAt(left)==s.charAt(right)){
            left--;
            right++;
        }
        return (s.substring(left + 1, right));
    }
}
