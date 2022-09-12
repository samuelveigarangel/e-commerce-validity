const countdown = document.getElementsByClassName('countdown')
const show_countdown = document.getElementsByClassName('show-countdown')
// Update the count down every 1 second

var x = setInterval(function() {

  // Get today's date and time
  // Find the distance between now and the count down date
for (i = 0; i < countdown.length; i++){
  // Set the date we're counting down to
  var now = new Date().getTime();
  var countDownDate = new Date(countdown[i].innerHTML).getTime();
  var distance = countDownDate - now;

  // Time calculations for days, hours, minutes and seconds
  var days = Math.floor(distance / (1000 * 60 * 60 * 24));
  var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
  var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
  var seconds = Math.floor((distance % (1000 * 60)) / 1000);

  // Display the result in the element with id="demo"
  show_countdown[i].innerHTML = days + "d " + hours + " : "
  + minutes + " : " + seconds + " ";
  if (distance < 0) {
    show_countdown[i].innerHTML = "EXPIRADO!";
    show_countdown[i].style.backgroundColor = '#c00';
    show_countdown[i].style.color = 'white';  
      }
    }
}, 1000);
  // If the count down is finished, write some text
