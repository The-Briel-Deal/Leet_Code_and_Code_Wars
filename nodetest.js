function getCount(str) {
    var vowelsCount = 0;

    for (const c of str) {
        if (c == "a" || c == "e" || c == "i" || c == "o" || c == "u") { vowelsCount++ }
    }
    return vowelsCount;
}
console.log(getCount("cute"));