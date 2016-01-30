/* -------------------------------------------
	CLIENT
-----------------------------------------------*/
var loadingSpinner = $('.loading'),
    topBbar = $('.top-bar'),
    socket = io.connect('http://' + document.domain + ':' + location.port);

	socket.on('connect', function() {
        socket.emit('client connected', {data: 'Client connected!'});
        $(".mini-game-btn").click(function() {
          socket.emit('echo', {data: 'Echo-String-on-click'});
          socket.emit('button pushed', {data: 'Button pushed!'});
        });
    });

		socket.on('choose tile result', function(msg) {
			console.log(msg);
			loadingSpinner.fadeOut();
		});

	// var socket = io.connect('http://' + document.domain + ':' + location.port);
    // socket.on('connect', function() {
    //     socket.emit('echo', {data: 'Echo-String-on-connect'});
    // });

// choose tile
$('#choose-tile-form').submit(function(){
  var value = $(this).find('input').val();
  console.log(value);

  if (!value == '') {
    socket.emit('choose tile', { "tile": value });

    loadingSpinner.fadeIn();
    topBbar.animate({top: "-190px"}, 500);
    $('.mini-game-inner ').delay('200').fadeIn('300');
    // counter();
  }else{
    alert('Bitte Zahl eingeben');
  }
  return false;
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
