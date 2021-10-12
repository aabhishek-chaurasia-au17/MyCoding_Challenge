var pushbtn = document.getElementById("pushbtn");
var ans = document.getElementById("answer");
var popbtn = document.getElementById("popbtn");
var deletebtn = document.getElementById("deletebtn");
var arr = []

pushbtn.addEventListener("click", function(){
    var input = document.getElementById("enter").value;
    arr.push(input)
    ans.innerText=arr
    console.log(arr)
    // input.focus()
    // input=""
    var input = document.getElementById("enter").value="";
    var input = document.getElementById("enter").focus();
})

popbtn.addEventListener("click", function(){
    arr.shift()
    ans.innerText=arr  
    var input = document.getElementById("enter").value="";
    var input = document.getElementById("enter").focus();
})

deletebtn.addEventListener("click", function(){
    var input = document.getElementById("enter").value="";
    var input = document.getElementById("enter").focus();
    arr=[]
    ans.innerText=arr
})



