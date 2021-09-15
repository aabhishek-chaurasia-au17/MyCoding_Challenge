//assign elements to variables
let str= document.getElementById('str');
let submit= document.getElementById('submit');
let answerBox= document.getElementById('answer-box');

submit.addEventListener("click", function(e){
  //convert value inputed into an array and assign it a variable
  string= str.value.split(',');
  
  //check if the input field contains two comma-delimited strings
    if(string.length !== 2){

      alert("Please input two strings of equal length seperated by a comma");

      return;
    }

//remove white spaces between the strings if any
  let str1= string[0].trim();

  let str2= string[1].trim();


//check if the length of the strings are equal
  if(str1.length !== str2.length){

    alert("Error: The strings aren't of equal length");

    return;
  }

  let count= 0;

 //loop over the two strings
  for(i= 0; i < str1.length; i++){

//Anytime the characters at index 'i' of the strings are different, increase count by 1 //
    if(str1[i] !== str2[i]) count++;

  }

  //display the result in the answer box
  answerBox.innerHTML= count;
})

//clear the answer box if the input field is empty
str.oninput= function(e){
  
  if(this.value== ""){
    
    answerBox.innerHTML="";
    
  }
}