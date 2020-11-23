// --- Directions
// Given a string, return the character that is most
// commonly used in the string.
// --- Examples
// maxChar("abcccccccd") === "c"
// maxChar("apple 1231111") === "1"

function maxChar(str) { return s2(str);}

// O(2n)
function s1(str) {
    var maxFreq = 0;
    var maxChar = '';
    dict = {};
    for (i = 0; i < str.length; i++) {
        if (str[i] in dict)
            dict[str[i]] = dict[str[i]] + 1;
        else
            dict[str[i]] = 1;
    }
    for(var key in dict) {
        if (dict[key] > maxFreq) {
            maxFreq = dict[key];
            maxChar = key;
        }
    }
    console.log(dict)
    return maxChar
}

// O(n)
function s2(str) {
    var maxFreq = 0;
    var maxChar = '';
    dict = {};
    for (i = 0; i < str.length; i++) {
        if (str[i] in dict) {
            var count = dict[str[i]] + 1;
            dict[str[i]] = count;
            if (count > maxFreq) {
                maxFreq = count;
                maxChar = str[i];
            }
        }  
        else {
            dict[str[i]] = 1;
            if (1 > maxFreq) {
                maxFreq = 1;
                maxChar = str[i];
            }
        }            
    }
    console.log(dict)
    return maxChar
}

module.exports = maxChar;
