/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
    if (0 < x && x < 10){
        return true;
    }
    if (x < 0 || (x % 10 == 0 && x != 0)){
        return false;
    }
    let half = 0;
    while (x > half){
        half = half * 10 + x % 10;
        x = Math.floor(x /= 10);
    }

    return(x == half || x == Math.floor(half / 10));
};
