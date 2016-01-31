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
socket.on('tiles update', function(msg) {
    tiles = jQuery.parseJSON(msg)
    //reset board
    board.find('td').removeClass('open reserved resolved')
    $.each(tiles, function(i,key, value){
    	var obj = tiles[i],
    		tileId = obj.id,
    		state = obj.state;
    	board.find('.tile-' + tileId).addClass(state);
    });
});

socket.on('update players', function(msg) {
    result = jQuery.parseJSON(msg)
    jQuery.each(result, function(i, players) {
          addPlayersToPlayerOverview(players);
    });
});

socket.on('game won', function(msg) {
    console.log("Game won!");
    $('.daemon-won').modal('show')
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
