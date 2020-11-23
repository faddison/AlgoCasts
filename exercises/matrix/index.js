// --- Directions
// Write a function that accepts an integer N
// and returns a NxN spiral matrix.
// --- Examples
//   matrix(2)
//     [[1, 2],
//     [4, 3]]
//   matrix(3)
//     [[1, 2, 3], | [[1, 2, 3] | [[0,0; 0,1; 0,2]
//     [8, 9, 4],  |  [4, 5, 6] |  [1,0; 1,1; 1,2]
//     [7, 6, 5]]  |  [7, 8, 9] |  [2,0; 2,1; 2,2]
//  matrix(4)
//     [[1,  2,  3, 4],
//     [12, 13, 14, 5],
//     [11, 16, 15, 6],
//     [10,  9,  8, 7]]

// box method
// numBoxes = ceiling(root(n))
// count = 0
// for (b = 0; b < numBoxes; b++)
// row 0+b:0+b->n-b, column n-b:0+b->n-b, row n-b:n-b->0+b, column 0+b:n-b->0+b

function matrix(n) { return s1(n); }

function s1(n) {
    var size = n;
    var groups = n;
}

module.exports = matrix;
