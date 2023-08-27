$(document).ready(function() {
    var cronometroElement = $('#cronometro');
    var startButton = $('#startButton');
    var pauseButton = $('#pauseButton');
  
    var isRunning = false;
    var seconds = 0;
    var intervalId;
  
    function formatTime(time) {
      var hours = Math.floor(time / 3600);
      var minutes = Math.floor((time % 3600) / 60);
      var seconds = time % 60;
  
      var formattedTime = padNumber(hours) + ':' + padNumber(minutes) + ':' + padNumber(seconds);
      return formattedTime;
    }
  
    function padNumber(number) {
      return number.toString().padStart(2, '0');
    }
  
    function startTimer() {
      isRunning = true;
      intervalId = setInterval(function() {
        seconds++;
        cronometroElement.text(formatTime(seconds));
      }, 1000);
    }
  
    function pauseTimer() {
      isRunning = false;
      clearInterval(intervalId);
    }
  
    startButton.on('click', function() {
      if (!isRunning) {
        startTimer();
      }
    });
  
    pauseButton.on('click', function() {
      if (isRunning) {
        pauseTimer();
      }
    });
  
    // Atualiza o cronômetro ao carregar a página
    $.ajax({
      url: getTimerStateURL,
      type: 'GET',
      success: function(response) {
        if (response.is_running) {
          seconds = response.seconds;
          startTimer();
        }
      }
    });
  });