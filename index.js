function start(){
    pyval = document.getElementById("id").innerHTML;
    if (pyval == "F"){
        tijd();
    } else if (pyval == "M"){
        get_bericht();
    } else if (pyval == "S"){

    }
}

function tijd(){
    var tijd = new Date();
    var uurnormaal = tijd.getHours();
    var minuutnormaal = tijd.getMinutes();
    var uurnul = "";
    var minuutnul = "";

    if (uurnormaal < 10) {
        uurnul = "0";
    } else {
        uurnul = "";
    }

    if (minuutnormaal < 10) {
        minuutnul = "0";
    } else {
        minuutnul = "";
    }

    var showtime = uurnul + uurnormaal + ":" + minuutnul + minuutnormaal;
    document.getElementById("timedisplay").innerHTML = showtime;
    setTimeout(arguments.callee, 1000);
}

function stuur(){
    var feedback = document.getElementById("feedback").value;
    var naam = document.getElementById("naam").value;

    if (feedback != ""){
        new QWebChannel(qt.webChannelTransport, function(channel) {
        var backend = channel.objects.backend;
            backend.sendfeedback(feedback, naam);
        });
    }

    document.getElementById("feedback").value = "";
    document.getElementById("naam").value = "";
}

function ns_button(task, id){
    if (task == "in"){
        document.getElementById(id).style.height = '10%';
    }
    else if (task == "out"){
        document.getElementById(id).style.height = '0%';
    }
}

function info(){
    closemenu();
    document.getElementById("infodiv").style.height = "85%";
}

function privacy(){
    closemenu();
    document.getElementById("privacydiv").style.height = "85%";
}

function contact(){
    closemenu();
    document.getElementById("contactdiv").style.height = "85%";
}

function disclaimer(){
    closemenu();
    document.getElementById("disclaimerdiv").style.height = "85%";
}

function closemenu(){
    document.getElementById("infodiv").style.height = "0%";
    document.getElementById("privacydiv").style.height = "0%";
    document.getElementById("contactdiv").style.height = "0%";
    document.getElementById("disclaimerdiv").style.height = "0%";
}

var curren_bericht = ""

function get_bericht(){
    new QWebChannel(qt.webChannelTransport, function(channel) {
        var backend = channel.objects.backend;
            backend.get_bericht_between(function(pyval) {
                curren_bericht = pyval;
                document.getElementById('berichtbubbel').innerHTML = curren_bericht;
            });
        });
}

function give_feedback(keuring, naam_mod){

    //document.getElementById('berichtbubbel').innerHTML = keuring + naam_mod + curren_bericht;


    new QWebChannel(qt.webChannelTransport, function(channel) {
        var backend = channel.objects.backend;
            backend.give_feedback(keuring, naam_mod, curren_bericht);
            get_bericht();
        });

}