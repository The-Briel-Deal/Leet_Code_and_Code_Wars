
/* 
Jaden Smith, the son of Will Smith, is the star of films such as The Karate Kid (2010) and After Earth (2013). Jaden is also known for some of his philosophy that he delivers via Twitter. When writing on Twitter, he is known for almost always capitalizing every word. For simplicity, you'll have to capitalize each word, check out how contractions are expected to be in the example below.

Your task is to convert strings to how they would be written by Jaden Smith. The strings are actual quotes from Jaden Smith, but they are not capitalized in the same way he originally typed them.

Example:

Not Jaden-Cased: "How can mirrors be real if our eyes aren't real"
Jaden-Cased:     "How Can Mirrors Be Real If Our Eyes Aren't Real"


I just learned that strings are immutable you cannot change them like you can in python
I refreshed on the format of for loops
I learned how to slice strings
And I learned about prototype functions and that it is not a thing in python.
(This stackoverflow post was very informative https://stackoverflow.com/questions/4650513/why-is-javascript-prototyping)
*/
String.prototype.toJadenCase = function() {
    str = this.toString();
    split_str = str.split(" ");
    for (index = 0; index < split_str.length; index++) {
        split_str[index] = split_str[index][0].toUpperCase() + split_str[index].slice(1, );
        console.log(split_str[index][0].toUpperCase())
    }
    console.log(split_str);
    str = split_str.join(' ');
    return str;
};
var sentance = "How can mirrors be real if our eyes aren't real";
console.log(sentance.toJadenCase());
// The function passed!!!!!!!!!