function isPangram(string) {
    let letters_in_sentence = Array();
    let alphabet = "abcdefghijklmnopqrstuvwxyz"
    for (letter of string) {
        if (!letters_in_sentence.includes(letter.toLowerCase()) && alphabet.includes(letter.toLowerCase())) {
            letters_in_sentence += letter.toLowerCase();
        }

    }
    console.log(letters_in_sentence.length)
    console.log(letters_in_sentence)
    if (letters_in_sentence.length == 26) { return true } else {
        return false
    }
}
console.log(isPangram("The quick brown fox jumps over the lazy dog"));