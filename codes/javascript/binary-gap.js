// you can write to stdout for debugging purposes, e.g.
// console.log('this is a debug message');

function solution(N) {
    // Implement your solution here
    const binary = N.toString(2);
    let resCounter = 0;
    let tempCounter = 0;

    for (let i = 0; i < binary.length; i++) {
        if (binary[i] === '1') {
        if (tempCounter > resCounter) resCounter = tempCounter;

        tempCounter = 0;
        } else {
        tempCounter++;
        }
    }

    return resCounter
}
