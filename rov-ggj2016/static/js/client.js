/* -------------------------------------------
	CLIENT
-----------------------------------------------*/
var loadingSpinner = $('.loading'),
    topBar = $('.top-bar'),
    game = $('.mini-game-inner'),
    gameBtn = $('.mini-game-btn'),
    soundBottle = 'static/assets/sound/open-bottle.mp3',
    soundSend = 'static/assets/sound/send.mp3',
    soundNegative = 'static/assets/sound/negative1.mp3',
    socket = null


$('.daemon-login').modal('toggle')
$('.daemon-login').on('hidden.bs.modal', function (e) {
    if(!socket) {
        $('.daemon-login').modal('show');
    }
})

$('.daemon-login-game').click(function(){
    console.log("Starting game login");
    socket = io.connect('http://' + document.domain + ':' + location.port + '/client');
    if(socket) {
        console.log(socket);
        $('.daemon-login').modal('hide');
        initializeClientStuff();
        return false;
    }
});

var initializeClientStuff = function() {

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

    var createAudio = function(src) {
        $('audio').remove();
        $('body').append('<audio src="'+ src +'" autoplay></audio>');
    };

    spinnerIn(); // during initial load until player create event is returned

    socket.on('connect', function() {
    /*
        uuid = localStorage.getItem('gameUniqueId');
        if(uuid) {
            console.log("uuid was found: ", uuid);
        } else {
            var randomlyGeneratedUID = Math.random().toString(36).substring(3,16) + +new Date;
            localStorage.setItem('gameUniqueId', randomlyGeneratedUID);
            uuid = localStorage.getItem('gameUniqueId')
            console.debug("uuid was created: ", uuid);
        }
        socket.emit('register player', {'uuid': uuid});
    */

        $(".mini-game-btn").click(function() {
          socket.emit('button pushed', {data: 'Button pushed!'});
        });
    });

    // create player
    socket.on('player create result', function(msg) {

      console.log("Player create result:",msg); //player object || false
      if (msg == "false") {
        alert('maximale Spieleranzahl erreicht');
      }else{
        var player = jQuery.parseJSON(msg);
        $('body').addClass('player-' + player.type);
        $('.player-name').html(player.name);
        spinnerOut();
      };

    });



    // choose tile
    $('#choose-tile-form').submit(function(){
      var value = $(this).find('input').val();


      if (!value == '') {
        // sound test
        createAudio(soundBottle);
        console.log(value);
        socket.emit('choose tile', { "tile": value });
        spinnerIn();

        // counter();
      }else{
        createAudio(soundNegative);
        $('#choose-tile-form p').hide().fadeIn("300");
        console.log('Bitte Zahl eingeben');
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
      createAudio(soundSend);
      socket.emit('resolve tile');
      gameOut();
      topBarIn();
      $('#choose-tile-form input').val('');
      return false;
    });

    // resolve tile response
    socket.on('resolve tile result', function(msg) {
      if (msg == "false") {
        alert('Fehler: Tile konnte nicht resolved werden');
      }else{
        tile = jQuery.parseJSON(msg);
        console.log("Tile was resolved", tile)
      };
    });
};
