function printReversedTriangle(num) {
  var result = '';
  for (var i = 0 ; i < num ; i++)
  {
  	for (var j = num-i ; j > 0 ; j--)
      result = result + '*';
    result = result + '\n';
  }
  return result;
}

console.log("결과 : " +'\n'+ printReversedTriangle(3));