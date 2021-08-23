// generateCoinChange(input)
// input is an integer representing an amount of money
// output is an object representing the most optimal
// (i.e. fewest coins) way to represent that amount
// with standard U.S. coins
// if the input is 74 cents, the output would be:
// {quarters: 2, dimes: 2, nickels: 0, pennies: 4}
// if the input is 109 cents, the output would be:
// {quarters: 4, dimes: 0, nickels: 1, pennies: 4}

function generateCoinChange(input) {
    var quarter = 25
    var dime = 10
    var nickel = 5
    var penny = 1
    remainder = input;

    numQuarters = 0;
    numDime = 0;
    numNickel = 0;
    numPenny = 0;

    numQuarters = Math.floor(remainder/quarter);
    console.log('quarter: ' + numQuarters);
    remainder = remainder%quarter;
    console.log('remainder: ' + remainder);

    numDime = Math.floor(remainder/dime);
    console.log('dime: ' + numDime);
    remainder = remainder%dime;
    console.log('remainder: ' + remainder);

    numPenny = Math.floor(remainder/penny);
    console.log('penny: ' + numPenny);
    remainder = remainder%penny;
    console.log('remainder: ' + remainder);

    numNickel = Math.floor(remainder/nickel);
    console.log('nickel: ' + numNickel);
    remainder = remainder%nickel;
    console.log('remainder: ' + remainder);
    
    var output = {'quarter': numQuarters, 'dime' : numDime, 'penny' : numDime, 'penny' : numPenny};
    return output;
}
// try out your own cases!
console.log(generateCoinChange(74))


// generateCoinChangeWithGivenValues(input, values)
// input is an integer representing an amount of money
// values is an array of arrays - each array represents a
// denomination of currency (string) and its value (integer)
// (a denomination of 1 will always be present)
// that array is in order of denomination
// the output is an object representing the most optimal
// way to represent that amount given the denominations
// if the input is 127 cents, and the values are:
// [ ['metadime', 15],
//  ['supernickel', 6]
//  ['very regular penny', 1]]
// the output would be:
// {metadimes: 8, supernickels: 1, very regular pennys: 1}
// (note the pluralization)
// if the input was 127, but the values were:
// [ ['halfquarter', 12],
//  ['greater nickel', 8],
//  ['lesser dime', 3]
//  ['just-a-penny', 1]]
// the output would be:
// {halfquarters: 10, greater nickels: 0, lesser dimes: 2, just-a-pennys: 0}
// if the input was 127, but the values were:
// [ ['half-dollar', 50],
//  ['dime', 10],
//  ['nickel', 5]
//  ['penny', 1]]
// the output would be:
// {'half-dollars': 2, 'dimes': 2, 'nickels': 1, 'pennys': 2}
// (these values -could- be an object, a set of key-value pairs,
// but I want to get you used to the concept of arrays within arrays
// and accessing that data within them)
//
// bonus: what would you do if we couldn't guarantee a denomination of 1
// being present? there are a few different answers, none strictly 'correct'

// function generateCoinChangeWithGivenValues(input, values) {

// }

function generateCoinChangeWithGivenValues(input, values);
var remainder = input;
var output = {};
for (var i = 0; i < values.length ; ++i){
    output[value[i][0]] = Math.floor(remainder/values[i][1]);
    remainder = remainder % values[i][1];
    return output;
}
generateCoinChangeWithGivenValues(52, [['halfquarter', 12], ['greater nickel', 8], ['lesser dime', 3], ['just-a-penny', 1]]);
