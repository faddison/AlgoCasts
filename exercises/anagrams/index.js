// --- Directions
// Check to see if two provided strings are anagrams of eachother.
// One string is an anagram of another if it uses the same characters
// in the same quantity. Only consider characters, not spaces
// or punctuation.  Consider capital letters to be the same as lower case
// --- Examples
//   anagrams('rail safety', 'fairy tales') --> True
//   anagrams('RAIL! SAFETY!', 'fairy tales') --> True
//   anagrams('Hi there', 'Bye there') --> False

function anagrams(stringA, stringB) { return s1(stringA, stringB); }

// iterate through one string, for each character remove it from the other. seconds string should be empty at end.
function s1(stringA, stringB) {
    for (a = 0; a < stringA.length; a++) {
        for (b = 0; b < stringB.length; b++) {
            if (stringA[a] === stringB[b])
                stringB = stringB.substring(0,b)+stringB.substring(b+1, stringB.length);
        }
    }
    return stringB.length === 0;
}

module.exports = anagrams;
