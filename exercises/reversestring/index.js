// --- Directions
// Given a string, return a new string with the reversed
// order of characters
// --- Examples
//   reverse('apple') === 'leppa'
//   reverse('hello') === 'olleh'
//   reverse('Greetings!') === '!sgniteerG'

function reverse(str) {
    return s1(str);
}

function s1(str) {
    var newStr = ""
    for (i = 0; i < str.length; i++) {
        newStr += str[str.length-i-1];
    }
    return newStr;
}

module.exports = reverse;
