function findTag(str) {
    let start = -1;
    for (let i = 0; i < str.length; i++) {
        if (str[i] === '<') {
            start = i;
        } else if (str[i] === '>' && start !== -1) {
            let tag = str.slice(start + 1, i);
            if (!tag.includes(' ')) {
                return tag;
            }
            start = -1; // Reset start if the tag is invalid
        }
    }
    return undefined;
}

module.exports = { findTag };