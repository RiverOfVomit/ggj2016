/* -------------------------------------------
	BOARD
-----------------------------------------------*/

var socket = io.connect('http://' + document.domain + ':' + location.port + '/board'),
	board = $('.board-tbl');

socket.on('connect', function() {
    //socket.emit('board connected', {data: 'Board connected!'});
    $('.daemon-won').modal('show')
});

socket.on('button pushed', function(msg) {
    console.log('button pushed' + msg);
    $('#messages').append($('<li>').text(msg.data));
});

// update board
socket.on('tiles update', function(msg) {
    tiles_and_players = jQuery.parseJSON(msg)
    tiles = jQuery.parseJSON(tiles_and_players.tiles)
    players = jQuery.parseJSON(tiles_and_players.players)
    console.log("received tiles", tiles);
    //reset board
    board.find('td').removeClass('open reserved resolved solved')
    $.each(tiles, function(i,key, value){
    	var obj = tiles[i],
    		tileId = obj.id,
    		state = obj.state;
            debugger;
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
  $('.daemon-won').modal('hide')
  return false;
});

var addPlayersToPlayerOverview = function(players) {
    $('.players').html('');
    jQuery.each(players, function(i, player) {
        $('.players').append('<li>' + player.name + '<span class="score">' + player.score +'</span></li>');
    });
};
