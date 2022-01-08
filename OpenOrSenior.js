function openOrSenior(data) {
    lst = Array();
    for (index = 0; index < data.length; index++) {
        if (data[index][0] >= 55 && data[index][1] > 7) {
            lst.push("Senior");
        } else {
            lst.push("Open");
        }
    }
}

openOrSenior([(18, 20), (45, 2), (61, 12), (37, 6), (21, 21), (78, 9)]);