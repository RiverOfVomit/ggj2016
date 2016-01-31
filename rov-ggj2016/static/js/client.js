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

$('.daemon-login').modal('show')
$('.daemon-login').on('hidden.bs.modal', function (e) {
    if(!socket) {
        $('.daemon-login').modal('show');
    }
});

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
        topBar.animate({top: "-140px"}, 500);

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
        $(".mini-game-btn").click(function() {
          socket.emit('button pushed', {data: 'Button pushed!'});
        });
    });

    socket.on('logoff', function() {
        console.log('logoff was send!');
        socket.emit('disconnect');
        socket = null;
        // Reset Client UI State
        $('.daemon-login').modal('show');
        $('body').removeClass('player-1 player-2 player-3');
        gameOut();
        topBarIn();
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
        createAudio(soundBottle);
        console.log(value);
        socket.emit('choose tile', { "tile": value });
        spinnerIn();

        // counter();
      }else{
        createAudio(soundNegative);
        $('#choose-tile-form p').hide().fadeIn("300");
        alert('Bitte Zahl eingeben');
      }
      $(this).find('input').blur();
      return false;
    });

    // choose tile response
    socket.on('choose tile result', function(msg) {
        //player object || false
      var tileResult = jQuery.parseJSON(msg)
      if (tileResult === false || tileResult.state === 'solved') {
        spinnerOut();
        alert('tile belegt/gelöst. Bitte andere Zahl wählen');
        // $('#choose-tile-form p').hide().text('Choose another ritual (1-9)').fadeIn('300', function(){
        //     $('#choose-tile-form p').hide().fadeIn('300');
        // });

      }else{
        spinnerOut();
        topBarOut();
        gameIn();
        // $('#choose-tile-form p').show().text('Choose a number between 1-9')
      };
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
        alert("Tile was resolved");
      };
    });
};
