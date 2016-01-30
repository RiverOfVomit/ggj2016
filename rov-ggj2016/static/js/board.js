/* -------------------------------------------
	BOARD
-----------------------------------------------*/
var socket = io.connect('http://' + document.domain + ':' + location.port);

    socket.on('connect', function() {
        socket.emit('board connected', {data: 'Board connected!'});
    });

    socket.on('button pushed', function(msg) {
        console.log(msg);
        $('#messages').append($('<li>').text(msg.data));
    });

    $('.reset-btn').click(function(){
      socket.emit('board reset');
      return false;
    });
