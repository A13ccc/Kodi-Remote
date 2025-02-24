function vibrateOnPress() {
    if ('vibrate' in navigator) {
        navigator.vibrate(50);
    }
}

document.getElementById('up').addEventListener('click', function() {
    vibrateOnPress();
    fetch('/input/up')
        .then(response => response.json())
        .then(data => console.log(data));
    
        console.log("up")
});

document.getElementById('down').addEventListener('click', function() {
    vibrateOnPress();
    fetch('/input/down')
        .then(response => response.json())
        .then(data => console.log(data));

    console.log("down")
});

document.getElementById('left').addEventListener('click', function() {
    vibrateOnPress();
    fetch('/input/left')
        .then(response => response.json())
        .then(data => console.log(data));

    console.log("left")
});

document.getElementById('right').addEventListener('click', function() {
    vibrateOnPress();
    fetch('/input/right')
        .then(response => response.json())
        .then(data => console.log(data));

    console.log("right")
});

document.getElementById('select').addEventListener('click', function() {
    vibrateOnPress();
    fetch('/input/select')
        .then(response => response.json())
        .then(data => console.log(data));

    console.log("select")
});

document.getElementById('rewind').addEventListener('click', function() {
    vibrateOnPress();
    fetch('/seek/backward')
        .then(response => response.json())
        .then(data => console.log(data));
});

document.getElementById('fast-forward').addEventListener('click', function() {
    vibrateOnPress();
    fetch('/seek/forward')
        .then(response => response.json())
        .then(data => console.log(data));
});

document.getElementById('play-pause').addEventListener('click', function() {
    vibrateOnPress();
    fetch('/play_pause')
        .then(response => response.json())
        .then(data => console.log(data));
});

document.getElementById('back').addEventListener('click', function() {
    vibrateOnPress();
    fetch('/input/back')
        .then(response => response.json())
        .then(data => console.log(data));
});

document.getElementById('volume-up').addEventListener('click', function() {
    vibrateOnPress();
    fetch('/input/volume_up')
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                console.log("Volume up command sent successfully.");
            } else {
                console.error("Failed to send volume up command:", data.error);
            }
        });
});

document.getElementById('volume-down').addEventListener('click', function() {
    vibrateOnPress();
    fetch('/input/volume_down')
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                console.log("Volume down command sent successfully.");
            } else {
                console.error("Failed to send volume down command:", data.error);
            }
        });
});

document.getElementById('context-menu').addEventListener('click', function() {
    vibrateOnPress();
    fetch('/input/context_menu')
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                console.log("Context menu command sent successfully.");
            } else {
                console.error("Failed to send context menu command:", data.error);
            }
        });
});

document.getElementById('info-menu').addEventListener('click', function() {
    fetch('/input/info_menu')
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                console.log("Info menu command sent successfully.");
            } else {
                console.error("Failed to send info menu command:", data.error);
            }
        });
})

document.getElementById('keyboard-button').addEventListener('click', function() {
    var textInput = document.getElementById('text-input');
    if (textInput.style.display === 'none') {
        textInput.style.display = 'block';
    } else {
        textInput.style.display = 'none';
    }
});

document.getElementById('stop').addEventListener('click', function() {
    vibrateOnPress();
    fetch('/stop')
        .then(response => response.json())
        .then(data => console.log(data));
});