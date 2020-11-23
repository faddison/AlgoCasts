// --- Directions
// Given an integer, return an integer that is the reverse
// ordering of numbers.
// --- Examples
//   reverseInt(15) === 51
//   reverseInt(981) === 189
//   reverseInt(500) === 5
//   reverseInt(-15) === -51
//   reverseInt(-90) === -9

function reverseInt(n) {return s1(n);}

function s1(n) {
    var sign = 1;
    if (n < 0)
        sign = -1;
        n = n * sign;
    var str = n.toString();
    var newStr = str.split('').reverse().join('');
    var newN = parseInt(newStr);
    if (sign < 0) 
    newN *= sign
    return newN;
}

module.exports = reverseInt;
