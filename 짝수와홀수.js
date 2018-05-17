function evenOrOdd(num) {
  var result = '';
  while((num != 1) && (num != 0))
    num = num % 2;
  if (num == 1)
    result = "Odd";
  else
    result = "Even";
  return result;
}
console.log("결과 : " + evenOrOdd(2));
console.log("결과 : " + evenOrOdd(3));