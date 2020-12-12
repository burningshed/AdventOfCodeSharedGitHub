let input = '1113222113';

function recurse(str) {
    let size = str.length;
    let mid = Math.floor(size / 2);
    let midChar = str[mid];
    let split = false;
    let i = mid + 1;

    for (; i < size; i++) {
        if (midChar !== str[i]) {
            split = true;
            break;
        }
    }

    // Went to end and didn't find another char
    if (!split) {
        for (i = mid; i >= 0; i--) {
            if (midChar !== str[i]) {
                split = true;
                i++;
                break;
            }
        }
    }

    // All chars match
    if (!split) {
        return size.toString() + midChar.toString();
    }

    let left = str.substr(0, i);
    let right = str.substr(i);

    return recurse(left) + recurse(right);
}

let start = new Date();
for (let i = 0; i < 50; i++) {
    input = recurse(input);
}
let end = new Date();

console.log(input.length, 'in', (end - start) / 1000, 'seconds');
