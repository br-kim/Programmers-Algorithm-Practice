function average(array){
  var answer = 0;
	for(var i = 0 ; i < array.length ; i++)
     answer = answer + array[i];
  return answer / array.length;;
}
var testArray = [5,3,4] 
console.log("평균값 : " + average(testArray));