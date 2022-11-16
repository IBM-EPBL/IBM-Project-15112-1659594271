var text1 = ["On Registering,you can", "Build your profile", "Let recruiters find you","Get job postings delivered to your email","Find a job and grow your career"];
var counter1 = 0;
var elem1 = document.getElementById("changeText1");
var inst1 = setInterval(change1, 4000);

function change1() {
  elem1.innerHTML = text1[counter1];
  counter1++;
  if (counter1 >= text1.length) {
    counter1 = 0;

  }
}
