function numPY(s){
  var result = true;
  var pcnt = 0;
  var ycnt = 0;
  for (var i = 0; i < s.length ; i++)
  {
    if ((s[i] == "p") ||(s[i] ==  "P"))
      pcnt++;
    else if ((s[i] == "y") ||(s[i] ==  "Y"))
      ycnt++;
  }
  if (pcnt != ycnt)
  	result = false;
  
  return result;
}
console.log( numPY("pPoooyY") )
console.log( numPY("Pyy") )