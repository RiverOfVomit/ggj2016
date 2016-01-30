/* -------------------------------------------
	GAME LOGIC
-----------------------------------------------*/

$("#mini-game-btn").click(function() {
	var socket = io.connect('http://' + document.domain + ':' + location.port);
	socket.emit('echo', {data: 'Echo-String-on-click'});
	return false;
});

	// var socket = io.connect('http://' + document.domain + ':' + location.port);
    // socket.on('connect', function() {
    //     socket.emit('echo', {data: 'Echo-String-on-connect'});
    // });