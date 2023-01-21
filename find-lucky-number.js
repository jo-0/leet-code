/**
 * 1394. Find Lucky Integer in an Array
 * https://leetcode.com/problems/find-lucky-integer-in-an-array/
 * 
 * @param {int[]} arr An integer array
 * @returns the biggest lucky number or -1
 */
function findLucky(arr) {
  const splitObj = arr.reduce((m, v) => (m[v] = m[v] || []).push(v) && m, {});
  const splitArr = Object.values(splitObj);
  let results = [];
  for (let items of splitArr) {
    if (items.length == items[0]) {
      results.push(items.length);
    }
  }
  return results.length ? Math.max(...results) : -1;
}


console.log("Result = ", findLucky([5]));
