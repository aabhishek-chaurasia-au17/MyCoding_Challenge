// Q2. Display a multiplication table of a number like so in the browser console. (7.5 Marks)


const input = parseInt(prompt("Enter Number"));


for(let i = 1; i <= 10; i++){

    const resulte = i * input;
    console.log(`${input} * ${i} = ${resulte}`);
}