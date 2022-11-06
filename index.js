function start(){
    pyval = document.getElementById("id").innerHTML;
    if (pyval == "F"){
        tijd();
    } else if (pyval == "M"){
        get_bericht();
    } else if (pyval == "S"){
        tijd();
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

// functies voor moderatie ----------------------------------------------------------------------------------------------

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
    new QWebChannel(qt.webChannelTransport, function(channel) {
        var backend = channel.objects.backend;
            backend.give_feedback(keuring, naam_mod, curren_bericht);
            get_bericht();
        });

}

// functies voor scherm ----------------------------------------------------------------------------------------------
var locatie_scherm = ''

function scherm_locatie(locatie){
    locatie_scherm = locatie;
    document.getElementById('locatie_div').innerHTML = locatie;
    get_faciliteiten();
}

function get_faciliteiten(){
    var antwoord = '';

    new QWebChannel(qt.webChannelTransport, function(channel) {
        var backend = channel.objects.backend;
            backend.get_faciliteiten(locatie_scherm, function(pyval) {
                antwoord = pyval;
                antwoord = antwoord.split(",");

                if (antwoord[0] == 'True'){
                    document.getElementById('faciliteit_id').innerHTML = document.getElementById('faciliteit_id').innerHTML + "<button><img src='./icons/img_ovfiets.png'></button>";
                } if (antwoord[1] == 'True'){
                    document.getElementById('faciliteit_id').innerHTML = document.getElementById('faciliteit_id').innerHTML + "<button><img src='./icons/img_lift.png'></button>";
                } if (antwoord[2] == 'True'){
                    document.getElementById('faciliteit_id').innerHTML = document.getElementById('faciliteit_id').innerHTML + "<button><img src='./icons/img_toilet.png'></button>";
                } if (antwoord[3] == 'True'){
                    document.getElementById('faciliteit_id').innerHTML = document.getElementById('faciliteit_id').innerHTML + "<button><img src='./icons/img_pr.png'></button>";
                }

                get_current_trains();
            
            });
        });
}

function get_current_trains(){
    new QWebChannel(qt.webChannelTransport, function(channel) {
        var backend = channel.objects.backend;
            backend.get_current_trains(locatie_scherm, function(pyval) {
                antwoord = pyval;

                for (let i = 0; i < pyval.length; i++) {
                    pyval[i]

                    base = "<div class='singel_train_div'><button class='soort'>";

                    if (pyval[i][1] == 'IC'){
                        base = base + "IC</button><button class='orig'>";
                    } else {
                        base = base + "SPR</button><button class='orig'>";
                    }

                    base = base + pyval[i][0]

                    if (pyval[i][2] == 'ON_STATION'){
                        base = base + "</button><button class='loc'><i class='fa-solid fa-location-dot'></i></button></div>";
                    } else {
                        base = base + "</button><button class='loc'><i class='fa-solid fa-train-tram'></i></button></div>";
                    }

                    document.getElementById("trein_info_id").innerHTML = document.getElementById("trein_info_id").innerHTML + base;
                }

                get_current_wheater();
            });
        });
}


function get_current_wheater(){
    new QWebChannel(qt.webChannelTransport, function(channel) {
        var backend = channel.objects.backend;
            backend.get_current_wheater(locatie_scherm, function(pyval) {
                antwoord = pyval;

                antwoord = antwoord.split(";");

                document.getElementById('weer_graden_id').innerHTML = antwoord[0] + "\u00B0C " + antwoord[1];
                get_berichten();
            });
        });
}


function get_berichten(){
    new QWebChannel(qt.webChannelTransport, function(channel) {
        var backend = channel.objects.backend;
            backend.get_berichten(locatie_scherm, function(pyval) {
                
                for (let i = 0; i < pyval.length; i++) {
                    base = "<button class='textvak'>" + pyval[i][0] + "<div class='naamvak'> ~" + pyval[i][1] + "</div></button>";

                    document.getElementById('bericht_text_id').innerHTML = document.getElementById('bericht_text_id').innerHTML + base;
                }

                document.getElementById('scherm_overlay').style.height = "0%";
            });
        });
}