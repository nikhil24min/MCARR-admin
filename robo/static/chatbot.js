function talk(){
    var know = {
    "Who are you" : "Hello, Codewith_random here ",
    "How are you" : "Good :)",
    "What can i do for you" : "Please Give us A Follow & Like.",
    "Your followers" : "I have my family of 5000 members, i don't have follower ,have supportive Famiy ",
    "ok" : "Thank You So Much ",
    "Bye" : "Okay! Will meet soon.."
    };
    var user = document.getElementById('userBox').value;
    document.getElementById('chatLog').innerHTML = user + "<br>";
    if (user in know) {
    document.getElementById('chatLog').innerHTML = know[user] + "<br>";
    }else{
    document.getElementById('chatLog').innerHTML = "Sorry,I didn't understand <br>";
    }
    }

const api_url = "http://ec2-54-234-230-205.compute-1.amazonaws.com/reply/";

// Defining async function
async function getapi(url,mca) {
  
  // Storing response
  const response = await fetch(url+mca);
  
  // Storing data in form of JSON
  var data = await response.json();
  console.log(data);
  if (response) {
      hideloader();
  }
  show(data);
}
// Calling that async function
getapi(api_url,"mca");

