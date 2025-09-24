import java.util.HashMap;

class Solution {
    public int lengthOfLongestSubstring(String s) {
        if (s.length()<=1){
            return s.length();
        }
        int maxLength = 0;
        int left = 0;
        HashMap<Character, Integer> map = new HashMap<>();

        for (int right = 0; right<s.length(); right++){
            char c = s.charAt(right);

            if (map.containsKey(c)){
                left = Math.max(left, map.get(c)+1);
            }

            map.put(c, right);
            maxLength = Math.max(maxLength, right - left+1);
        }
        return maxLength;
    }
}
