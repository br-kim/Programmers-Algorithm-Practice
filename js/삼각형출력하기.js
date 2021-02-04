function printTriangle(num) {
  var result = '';
  for(var j = 0; j < num; j++)
  {
 	 for(var i = 0; i <= j; i++)
    	result = result + '*';
    result = result + '\n';
  }
    return result;
}
console.log( printTriangle(3) );