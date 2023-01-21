/**
 * 7. Reverse Integer
 * https://leetcode.com/problems/reverse-integer/
 * 
 * @param {number} x
 * @return {number}
 */
var reverse = function (x) {
  let sign = x < 0 ? -1 : 1;
  let num = Math.abs(x);
  let toReverse = num.toString().split("");
  let reverse = toReverse.reverse();
  let finalString = reverse.join("");
  let number = +finalString;
  return number > 0x7FFFFFFF ? 0 : (number * sign);
};

reverse(123);
