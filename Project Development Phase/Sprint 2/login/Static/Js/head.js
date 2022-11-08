var text = ["Welcome to job Recommender","Find a Startup Jobs", "Find a carrer you'll love", "Find Great places to work","Find your dream job now","Free Job Alerts","Search by skill","Search by company","Search by job title"];
var counter = 0;
var elem = document.getElementById("changeText");
var inst = setInterval(change, 4000);

function change() {
  elem.innerHTML = text[counter];
  counter++;
  if (counter >= text.length) {
    counter = 0;

  }
}


