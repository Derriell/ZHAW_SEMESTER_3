function equal(a, b) {
    if (a === b) return true;

    if (typeof a === 'object' && a !== null && typeof b === 'object' && b !== null) {
        const aKeys = Object.keys(a);
        const bKeys = Object.keys(b);

        if (aKeys.length !== bKeys.length) return false;

        for (let key of aKeys) {
            if (!bKeys.includes(key) || a[key] !== b[key]) return false;
        }

        return true;
    }

    return false;
}

module.exports = { equal };