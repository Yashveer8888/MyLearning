// The assert module provides a set of assertion functions for verifying invariants.
// The assert.deepStrictEqual() function tests for deep equality between the actual 
// and expected parameters.If the condition is true it will not produce an output 
// else an assertion error is raised.

// Parameters: This function accepts the following parameters as mentioned above and described below: 
// actual: This parameter holds the actual value that need to be evaluated. It is of any type.
// expected: This parameter holds the expected value which is matched against actual value. It is of any type.
// message: This parameter holds the error message of string or error type. It is an optional parameter.

// Return Value: This function returns assertion error of object type. 



const assert = require('assert').strict;

try {
   assert.deepStrictEqual({ a: '1' }, { a: '1' });
   console.log("No Error Occurred")
} catch (error) {
   console.log("Error: ", error)
}


try {
   assert.deepStrictEqual({ a: 5 }, { a: '5' });
   console.log("No Error Occurred")
} catch (error) {
   console.log("Error: ", error)
}