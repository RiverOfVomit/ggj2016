/* -------------------------------------------
	CLIENT
-----------------------------------------------*/
var loadingSpinner = $('.loading'),
    topBar = $('.top-bar'),
    game = $('.mini-game-inner'),
    gameBtn = $('.mini-game-btn'),
    socket = io.connect('http://' + document.domain + ':' + location.port + '/client');

var spinnerIn = function() {
    loadingSpinner.fadeIn();    
};

var spinnerOut = function() {
    loadingSpinner.fadeOut();
};

var topBarIn = function() {
    topBar.animate({top: "0"}, 500);    
};

var topBarOut = function() {
    topBar.animate({top: "-160px"}, 500);

  };

var gameIn = function() {
    game.fadeIn('300');
};

var gameOut = function() {
    game.fadeOut('300');
};


spinnerIn(); // during initial load until player create event is returned

socket.on('connect', function() {
    $(".mini-game-btn").click(function() {
      socket.emit('button pushed', {data: 'Button pushed!'});
    });
});

// create player
socket.on('player create result', function(msg) {
  console.log(msg); //player object || false
  if (msg === false) {
    alert('maximale Spieleranzahl erreicht');
  }else{
    var msgOb = jQuery.parseJSON(msg);
    $('body').addClass('player-' + msgOb.type);
    spinnerOut();
  };  
});

// choose tile
$('#choose-tile-form').submit(function(){
  var value = $(this).find('input').val();
  console.log(value);

  if (!value == '') {
    socket.emit('choose tile', { "tile": value });
    spinnerIn();

    // counter();
  }else{
    alert('Bitte Zahl eingeben');
  }
  return false;
});

// choose tile response
socket.on('choose tile result', function(msg) {
	//player object || false
	spinnerOut();
  topBarOut();
  gameIn();
});

// resolve tile
gameBtn.click(function(){
  socket.emit('resolve tile', { "gameResolved": true });
  gameOut();
  topBarIn();
  $('#choose-tile-form input').val('');
});


// create counter
// function counter(){
// 	var num = Math.floor(Math.random()*5+1), // number between 1 and 5
//       numEl = $('.counter-num');
//       numEl.text(num);

// for (i = num; i < cars.length; i--) {
//     text += cars[i] + "<br>";
// }

//   setTimeout(function(){
//     alert("countdown läuft"); }, 1000
//     );
// };
