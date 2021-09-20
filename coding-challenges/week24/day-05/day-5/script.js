const category = document.getElementById("category");
const cate_URL = "https://opentdb.com/api_category.php";
let html = "";
const submit_btn = document.getElementById("submit_btn");
const difficulty = document.getElementById("difficulty");
const type = document.getElementById("type");
const filter = document.getElementById("filter");
const questions_section = document.getElementById("questions_section");
const amt = document.getElementById("amount");
const question_text = document.getElementById("question_text");
const question_actual = document.getElementById("question_actual");
let count = 0;

async function quiz() {
  const res = await fetch(cate_URL);
  const cate_data = await res.json();

  cate_data.trivia_categories.map((item) => {
    return (html += `<option value=${item.id}>${item.name}</option>`);
  });

  category.innerHTML = html;

  submit_btn.addEventListener("click", async () => {
    count += 1;
    filter.classList.add("d-none");
    questions_section.classList.remove("d-none");
    const question_url = await fetch(
      `https://opentdb.com/api.php?amount=1&category=${
        category.value
      }&difficulty=${difficulty.value.toLowerCase()}&type=${type.value.toLowerCase()}`
    );
    const question_array = await question_url.json();
    const arr = [];

    question_text.innerText = `Question 1:`;
    question_actual.innerText = `${question_array.results[0].question}`;

    console.log(question_array.results[0]);
    for (
      let i = 0;
      i < question_array.results[0].incorrect_answers.length;
      i++
    ) {
      arr.push(question_array.results[0].incorrect_answers[i]);
    }
    arr.push(question_array.results[0].correct_answer);
    console.log(arr);
  });
}

quiz();
