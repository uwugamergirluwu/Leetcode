/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {
    if (s.length <=1){
        return s.length;
    }
    let charSet = {};
    maxLength = 0;
    let left = 0;
    for(let right=0; right < s.length; right++){
        let c = s.charAt(right);
        if (c in charSet){
            left = Math.max(left, charSet[c] + 1);
        }
        charSet[c] = right;
        maxLength = Math.max(maxLength, right - left + 1);
    }
    return maxLength;
};
