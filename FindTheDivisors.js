/*
I learned to append to lists in JS you use the .push method
*/

function divisors(integer) {
    var lst = Array();
    for (index = 2; index < integer; index++) {
        if (integer % index == 0) {
            lst.push(index);
            console.log(index + " divides");
        } else {
            console.log(index + " does not divide");
        }
    }
    if (lst.length > 0) {
        return lst;
    } else {
        return integer + ' is prime';
    }
};
console.log(divisors(27));

// It passed!!!!