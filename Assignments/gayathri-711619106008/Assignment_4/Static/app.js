var text = [" Find a Startup Jobs", "Find a carrer you'll love", "Find Great places to work","Find your dream job now"];
var counter = 0;
var elem = document.getElementById("changeText");
var inst = setInterval(change, 2000);

function change() {
  elem.innerHTML = text[counter];
  counter++;
  if (counter >= text.length) {
    counter = 0;

  }
}