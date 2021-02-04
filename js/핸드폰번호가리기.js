function hide_numbers(s){
  var result = "";
  for(var i = 0; i < s.length-4; i++)
    result = result + "*";

  for(var j = s.length-4; j < s.length; j++)
    result = result + s[j];

  return result;
}
console.log("결과 : " + hide_numbers('01033334444'));