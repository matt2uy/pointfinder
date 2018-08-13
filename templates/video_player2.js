var vid = $('#v0')[0];

vid.onplay = vid.onclick = function() {
    vid.onplay = vid.onclick = null;

    setTimeout(function() {
        vid.pause();
        setInterval(function() {
            if($.browser.opera) {
                var oldHandler = vid.onplay;
                vid.onplay = function() {
                    vid.pause();
                    vid.onplay = oldHandler;
                };
                vid.play();
            } else {
                vid.currentTime += (1 / 29.97);
            }
        }, 2000);
    }, 12000);

    setInterval(function() {
        $('#time').html((vid.currentTime * 29.97).toPrecision(5));
    }, 100);
};