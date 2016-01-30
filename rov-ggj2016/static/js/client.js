/* -------------------------------------------
	CLIENT
-----------------------------------------------*/
var socket = io.connect('http://' + document.domain + ':' + location.port);

	socket.on('connect', function() {
        socket.emit('client connected', {data: 'Client connected!'});
        $("#mini-game-btn").click(function() {
          socket.emit('echo', {data: 'Echo-String-on-click'});
          socket.emit('button pushed', {data: 'Button pushed!'});
        });
    });

	// var socket = io.connect('http://' + document.domain + ':' + location.port);
    // socket.on('connect', function() {
    //     socket.emit('echo', {data: 'Echo-String-on-connect'});
    // });

// create counter
function counter(){
	var multiplier //1 5
};