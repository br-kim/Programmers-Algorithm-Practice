function findKim(seoul){
  var idx = 0;
  for(var index = 0 ; index < seoul.length ; index++)
    if (seoul[index]  == "Kim")
      idx = index;
  return "김서방은 " + idx + "에 있다";
}
console.log( findKim(["Queen", "Tod", "Kim"]));