// --- Directions
// Write a function that accepts a positive number N.
// The function should console log a pyramid shape
// with N levels using the # character.  Make sure the
// pyramid has spaces on both the left *and* right hand sides
// --- Examples
//   pyramid(1)
//       '#'
//   pyramid(2)
//       ' # '
//       '###'
//   pyramid(3)
//       '  #  '
//       ' ### '
//       '#####'
//   pyramid(4)
//       '   #   ' 1 4-1=3; j > n - i+1 && j < width - n - i + 1
//       '  ###  ' 2 4-2=2; j > 2 || i < length - 2
//       ' ##### ' 3 4-3=1
//       '#######' 4; 4-4=0

// width = 2*n-1
// activation = 


function pyramid(n) { return s1(n); }

function s1(n) {
    width = 2 * n - 1
    for (i = 0; i < n; i++) {
        var stepStr = ''
        for (j = 0; j < width; j++) {
            if (j >= n - (i + 1)) {
                //console.log('left true')
                if (j <= width - n - (i + 1)) {
                    //console.log('right true')
                    stepStr += '#';
                }
                else
                    stepStr += ' '
            }
            else
                stepStr += ' '
        }
        console.log(stepStr)
    }
}

module.exports = pyramid;
