let string = '1113222113';

function iterate(line)
{
    let newLine = '';

    while (line.length) {
        let digit = line[0];

        let regex = new RegExp(i = '^(' + digit  + '+)');
        let result = regex.exec(line);
        let total = result[0].length;

        newLine += total.toString() + digit.toString();
        line = line.substring(total);
    }

    return newLine;
}

let start = new Date();
for (let i=0; i<60; i++) {
    string = iterate(string);
}
let end = new Date();

console.log(string.length, 'in', (end - start) / 1000, 'seconds');