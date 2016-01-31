/* -------------------------------------------
	BOARD
-----------------------------------------------*/

var socket = io.connect('http://' + document.domain + ':' + location.port + '/board'),
	board = $('.board-tbl');

socket.on('connect', function() {
    //socket.emit('board connected', {data: 'Board connected!'});
});

socket.on('button pushed', function(msg) {
    console.log('button pushed' + msg);
    $('#messages').append($('<li>').text(msg.data));
});

// update board
socket.on('tile update', function(msg) {
    result = jQuery.parseJSON(msg)
    if (result.player) {
        console.log('tile update ' + result.id);
        if (result.state == 'reserved') {
        	board.find('.tile-' + (result.id +1)).addClass('reserved');
        };

    } else {
        console.log("no player found");
    };
});

// update board
socket.on('tiles update', function(msg) {
    tiles = jQuery.parseJSON(msg)
    console.log(tiles);
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
