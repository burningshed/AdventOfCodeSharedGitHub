function lookandsay(str) {
    return str.replace(/(.)\1*/g, function(seq, p1){return seq.length.toString() + p1})
}

var num = "1113222113";

let start = new Date();
for (var i = 50; i > 0; i--) {
    num = lookandsay(num);
}
let end = new Date();

console.log(num.length, 'in', (end - start) / 1000, 'seconds');