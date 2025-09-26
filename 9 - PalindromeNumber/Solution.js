/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
    if (0 < x && x < 10){
        return true;
    }
    let num = String(x);
    let right = num.length-1;
    for (let left = 0; left < num.length; left++){
        if (num[right] != num[left]){
            return false;
        }
        right--;
    }
    return true;
};
