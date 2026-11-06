
// var getConcatenation = function(nums) {
//     let ansArray = [];

//     for (let i = 0; i < nums.length; i++) {
//         ansArray.push(nums[i]);
//     }

//     for (let i = 0; i < nums.length; i++) {
//         ansArray.push(nums[i]);
//     }

//     return ansArray;
// };

// const numsx = [1, 2, 3];
// console.log(getConcatenation(numsx)); 


// 7ms



// var getConcatenation = function(nums) {
//     let ansArray = [...nums];

//     for (let i = 0; i < nums.length; i++) {
//         ansArray.push(nums[i]);
//     }


//     return ansArray;
// };

// const numsx = [1, 2, 3];
// console.log(getConcatenation(numsx));

//4ms

var getConcatenation = function(nums) {
    return ansArray = nums.concat(nums);

};


const numsx = [1, 2, 3];
console.log(getConcatenation(numsx));

//1ms





