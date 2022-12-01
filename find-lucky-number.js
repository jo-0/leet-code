/**
 * Ex 1:
 * arr = [1, 1, 2, 3, 3, 3, 4, 4, 4, 5]
 * Answer = 3; since it occurs exactly 3 times.
 * 
 * Ex 2:
 * arr = [5]
 * Answer = -1
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
