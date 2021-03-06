exports.creditCheck = function (str) {
  let arr = [];
  str = str.toString().split("").reverse();
  for (let i in str) {
    if (i % 2 !== 0) {
      arr.push(+str[i] * 2);
    } else {
      arr.push(+str[i]);
    }
  }
  for (let j in arr) {
    if (arr[j] > 9) {
      let bigger = arr[j].toString().split("");
      arr[j] = +bigger[0] + +bigger[1];
    }
  }
  let res = arr.reduce((curr, pre) => curr + pre, 0);
  if (res % 10 === 0) {
    return "The number is valid!";
  } else return "The number is invalid!";
};

// console.log(this.creditCheck("5541808923795240"));
