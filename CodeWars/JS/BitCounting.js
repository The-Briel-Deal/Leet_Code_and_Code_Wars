/*
 Write a function that takes an integer as input, and returns the number of bits that are equal to one in the binary representation of that number. You can guarantee that input is non-negative.

Example: The binary representation of 1234 is 10011010010, so the function should return 5 in this case
*/

var countBits = function(n) {
    current_square = 1;
    bit_lst = Array();
    while (n >= current_square) {
        bit_lst.push(current_square);
        current_square = current_square * 2;
    };
    for (index = 0; index < bit_lst.length; index++) {
        // console.log(bit_lst[bit_lst.length - index - 1])
        if (n - bit_lst[bit_lst.length - index - 1] >= 0) {
            n = n - bit_lst[bit_lst.length - index - 1];
            bit_lst[bit_lst.length - index - 1] = 1;
        } else {
            bit_lst[bit_lst.length - index - 1] = 0;
        }
    };
    var incre = 0;
    for (index = 0; index < bit_lst.length; index++) {
        if (bit_lst[index] == 1) {
            incre++;
        }
    }
    console.log(bit_lst);
    return incre;
};

console.log(countBits(1234));

// It passed!!!!!