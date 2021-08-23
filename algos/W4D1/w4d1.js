function sigma(n) {

    if (n <= 1) {
        console.log('base case reached');
        return 1;
    }

    console.log(`making recursive call to sigma with value ${n - 1}`)
    var sigma_result = sigma(n - 1);
    console.log(`recursive call to sigma with value ${n - 1} complete`)
    return n + sigma_result;
}

console.log(sigma(4));


// do these recursively, alright?

// factorial(n) - return factorial n, i.e. n * n - 1 * n - 2 ...  * 1
// written out as n!
// factorial(5) -> 120  (5 * 4 * 3 * 2 * 1)
// factorial(6) -> 720  (6 * 5 * 4 * 3 * 2 * 1)
function factorial(n) {

}

// console.log(factorial(5))

// fibonacci(n)
// return the nth number in the Fibonacci sequence
// https://en.wikipedia.org/wiki/Fibonacci_number
// fibonacci(0) -> 0
// fibonacci(1) -> 1
// fibonacci(2) -> 1
// fibonacci(3) -> 2
// fibonacci(4) -> 3
// fibonacci(5) -> 5
// fibonacci(6) -> 8
// keep n less than like, 30

function fibonacci(n) {

}