 const assert = require('assert').strict; 
  
// let x = 4; 
// let y = 5; 
// try { 
//     // Checking condition 
//     assert(x == y); 
// } 
// catch { 
//     // Error output 
//     console.log( `${x} is not equal to ${y}`); 
// } 


// try {
//    assert(0);
// } 
// catch(error) {
//    console.log("Error:", error);
// }

//assert.deepStrictEqual(actual, expected[, message])
// try {
//    assert.deepStrictEqual({ a: 1 }, { a: '1' });
// } catch(error) {
//    console.log("Error: ", error)
// }

try {
   assert.deepStrictEqual({ a: '5' }, { a: '5' });
   console.log("No Error Occurred")
} catch(error) {
   console.log("Error: ", error)
}