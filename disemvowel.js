function disemvowel(str) {
    list_str = str.split("");
    for (letter in list_str) {
        if (["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"].includes(str[letter])) {
            delete list_str[letter];
        }

    }
    return list_str.join("");


}
console.log(disemvowel("cute dog!"));