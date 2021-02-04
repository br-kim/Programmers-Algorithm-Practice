function alpha_string46(s){
  var result = true;

  if((s.length == 4) || (s.length == 6))
    result = true;
  else
    result = false;
  
  for(var i = 0; i < s.length ; i++)
    if(isNaN(s[i]) == true)
      result = false;
  return result;
}
console.log( alpha_string46("a234") );