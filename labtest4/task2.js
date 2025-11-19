// JavaScript: Filter even numbers using filter()
const numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
const evenNumbers = numbers.filter(x => x % 2 === 0);
console.log(evenNumbers);  // Output: [2, 4, 6, 8, 10]
// JavaScript: Using map with conditional (less efficient)
const evenNumber = numbers.map(x => x % 2 === 0 ? x : null).filter(x => x !== null);
console.log(evenNumbers);  // Output: [2, 4, 6, 8, 10]
// JavaScript: Traditional for loop approach
const evenNum = [];
for (let x of numbers) {
    if (x % 2 === 0) {
        evenNum.push(x);
    }
}
console.log(evenNum);  // Output: [2, 4, 6, 8, 10]