// --- Directions
// Write a function that accepts a string.  The function should
// capitalize the first letter of each word in the string then
// return the capitalized string.
// --- Examples
//   capitalize('a short sentence') --> 'A Short Sentence'
//   capitalize('a lazy fox') --> 'A Lazy Fox'
//   capitalize('look, it is working!') --> 'Look, It Is Working!'

function capitalize(str) { return s1(str); }

function s1(str) {
    var tmpStr = ''
    for (i = 0; i < str.length; i++) {
        if (i == 0 || str[i-1] === ' ')
            tmpStr += str[i].toUpperCase();
        else
            tmpStr += str[i]
    }
    return tmpStr;
}

module.exports = capitalize;
