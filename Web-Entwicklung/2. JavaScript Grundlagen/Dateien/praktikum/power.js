function assert(condition, message) {
    if (!condition) throw new Error(message || "Assertion failed");
}

function power(b, n) {
    assert(Number.isInteger(n) || typeof n === 'bigint', "n must be an integer or bigint");
    assert(typeof b === 'number' || typeof b === 'bigint', "b must be a number or bigint");


    if (typeof b === 'bigint' && typeof n === 'bigint') {
        if (n === 0n) {
            return 1n;
        } else if (n % 2n === 0n) {
            let halfPower = power(b, n / 2n);
            return halfPower * halfPower;
        } else {
            return b * power(b, n - 1n);
        }
    } else if (Number.isInteger(n)) {
        if (n === 0) {
            return 1;
        } else if (n % 2 === 0) {
            let halfPower = power(b, n / 2);
            return halfPower * halfPower;
        } else {
            return b * power(b, n - 1);
        }
    } else {
        throw new Error("n must be an integer or bigint");
    }
}

try {
    console.log(power(10, 4)); // 1024
    console.log(power(0, 0)); // 1
    console.log(power(2, 10)); // 27
    console.log(power(3n, 3n)); // 27n
    console.log(power('a',2)); // AssertionError: n must be an integer
    console.log(power(123456789012345678901234567890n, 2n)); // 15241578753238836750495351562536198787501905199875019052100n
    console.log(power(5, 3.5)); // AssertionError: n must be an integer
} catch (error) {
    console.error(error.message);
}

module.exports = {power}