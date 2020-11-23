// --- Directions
// Given a string, return true if the string is a palindrome
// or false if it is not.  Palindromes are strings that
// form the same word if it is reversed. *Do* include spaces
// and punctuation in determining if the string is a palindrome.
// --- Examples:
//   palindrome("abba") === true
//   palindrome("abcdefg") === false

function palindrome(str) {
    return s3(str);
}

// reversal option one liner
function s3(str) {
    return str.split('').reverse().join('') === str;
}

// reverse letter comparison with O(n/2))
function s2(str) {
    var iterations = str.length / 2
    if (str.length % 2 == 1)
        iterations = (str.length+1)/2
    for (i = 0; i < iterations; i++) {
        if (str[i] != str[str.length - i - 1])
            return false;
    }
    return true;
}

// reverse word comparison (linear time)
function s1(str) {
    var newStr = ""
    for (i = 0; i < str.length; i++) {
        newStr += str[str.length - i - 1];
    }
    return str == newStr;
}

module.exports = palindrome;
