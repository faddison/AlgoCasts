// --- Directions
// Given an array and chunk size, divide the array into many subarrays
// where each subarray is of length size
// --- Examples
// chunk([1, 2, 3, 4], 2) --> [[ 1, 2], [3, 4]]
// chunk([1, 2, 3, 4, 5], 2) --> [[ 1, 2], [3, 4], [5]]
// chunk([1, 2, 3, 4, 5, 6, 7, 8], 3) --> [[ 1, 2, 3], [4, 5, 6], [7, 8]]
// chunk([1, 2, 3, 4, 5], 4) --> [[ 1, 2, 3, 4], [5]]
// chunk([1, 2, 3, 4, 5], 10) --> [[ 1, 2, 3, 4, 5]]

function chunk(array, size) { return s1(array, size); }

Object(n)
function s1(array, size) {
    var length = array.length
    var groups = Math.floor(length/size)
    var remainder = length % size
    var newArray = []

    for (g = 0; g < groups; g++) {
        newArray[g] = []
        for (s = 0; s < size; s++) {
            newArray[g][s] = array[(g * size) + s]
        }
    }
    if (remainder > 0) {
        newArray[groups] = []
        for (r = 0; r < remainder; r++) {
            newArray[groups][r] = array[((groups) * size) + r]
        }
    }
    console.log(array.length+', '+size+', '+groups+', '+remainder)
    console.log(newArray)
    return newArray
}

module.exports = chunk;
