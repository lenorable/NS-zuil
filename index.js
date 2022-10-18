function stuur(){
    var feedback = document.getElementById("feedback").value;
    var naam = document.getElementById("naam").value;

    new QWebChannel(qt.webChannelTransport, function(channel) {
    var backend = channel.objects.backend;
        backend.sendfeedback(feedback, naam);
    });
}