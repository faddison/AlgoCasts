// --- Directions
// Write a function that accepts a positive number N.
// The function should console log a step shape
// with N levels using the # character.  Make sure the
// step has spaces on the right hand side!
// --- Examples
//   steps(2)
//       '# '
//       '##'
//   steps(3)
//       '#  '
//       '## '
//       '###'
//   steps(4)
//       '#   '
//       '##  '
//       '### '
//       '####'

function steps(n) { return s1(n); }

function s1(n) {
    for (i = 0; i < n; i++) {
        var stepStr = ''
        for (j = 0; j < n; j++) {
            if (j <= i)
                stepStr += '#';
            else
                stepStr += ' '
        }
        console.log(stepStr)
    }
}

module.exports = steps;
