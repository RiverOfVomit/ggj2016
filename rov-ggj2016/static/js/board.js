/* -------------------------------------------
	BOARD
-----------------------------------------------*/

var socket = io.connect('http://' + document.domain + ':' + location.port + '/board');

socket.on('connect', function() {
    //socket.emit('board connected', {data: 'Board connected!'});
});

socket.on('button pushed', function(msg) {
    console.log(msg);
    $('#messages').append($('<li>').text(msg.data));
});

socket.on('tile update', function(msg) {
    result = jQuery.parseJSON(msg)
    if (result.player) {
        console.log(result);
    } else {
        console.log("no player found");
    };
});

socket.on('update players', function(msg) {
    result = jQuery.parseJSON(msg)
    jQuery.each(result, function(i, players) {
          addPlayersToPlayerOverview(players);
    });
});

$('.reset-btn').click(function(){
  socket.emit('board reset');
  return false;
});

var addPlayersToPlayerOverview = function(players) {
    $('.players').html('');
    jQuery.each(players, function(i, player) {
        $('.players').append('<li>' + player.name + '</li>');
    });
};
