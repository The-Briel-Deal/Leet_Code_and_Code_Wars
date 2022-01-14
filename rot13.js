function rot13(message) {
    var alphabet = "abcdefghijklmnopqrstuvwxyz".split('');
    message = message.split('');
    var capitals = Array();
    for (index = 0; index < message.length; index++) {
        if (!alphabet.includes(message[index])) {
            if ("ABCDEFGHIJKLMNOPQRSTUVWXYZ".includes(message[index])) {
                capitals.push(index);
                message[index] = message[index].toLowerCase();
            } else {
                continue;
            }
        }
        message[index] = alphabet[(alphabet.indexOf(message[index]) + 13) % 26]
        if (capitals.includes(index)) {
            message[index] = message[index].toUpperCase();
        }
    }
    return message.join("");
}