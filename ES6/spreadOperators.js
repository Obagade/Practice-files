function addNumbers(a,b,c){
    console.log(a+ b+ c);
}

var nums = [3,4,7];
addNumbers(...nums); //the ... is the spread operator that allows you to add the nums

//Another example

var meats = ['bacon', 'ham'];
var food = ['apples', ...meats, 'kiwi', 'rice']; //the ...meat here allows you to add the meat array to food array from index 1
console.log(food);