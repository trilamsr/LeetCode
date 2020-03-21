// Tobo

function betterCompression(S) {
    let sortArr = [];
    sortArr = S.match(/(\w[0-9]+)/g).sort((a, b) => a > b ? 1 : -1)
    let resultMap = sortArr.reduce((a, b) => {
        const split = [b.charAt(0), b.substring(1, b.length)];
        a[split[0]] ? a[split[0]] += parseInt(split[1]) : a[split[0]] = parseInt(split[1]);
        return a;
    }, {});
    let result = "";
    for (let k of Object.keys(resultMap)) {
        result += `${k}${resultMap[k]}`;
    }
    return result;
}