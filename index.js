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

function ns_button(task, id){
    if (task == "in"){
        document.getElementById(id).style.height = '10%';
    }
    else if (task == "out"){
        document.getElementById(id).style.height = '0%';
    }
}

// functies voor feedback ----------------------------------------------------------------------------------------------
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

// functies voor moderatie ----------------------------------------------------------------------------------------------

var curren_bericht = "";
var naam_mod = "";

function get_bericht(){
    new QWebChannel(qt.webChannelTransport, function(channel) {
        var backend = channel.objects.backend;
            backend.get_bericht_between(function(pyval) {
                curren_bericht = pyval;
                document.getElementById('berichtbubbel').innerHTML = curren_bericht;
            });
        });
}

function give_feedback(keuring){
    new QWebChannel(qt.webChannelTransport, function(channel) {
        var backend = channel.objects.backend;
            backend.give_feedback(keuring, naam_mod, curren_bericht);
            get_bericht();
        });

}

function login(){
    var email = document.getElementById('login_email').value;
    var wachtwoord = document.getElementById('login_ww').value;

    new QWebChannel(qt.webChannelTransport, function(channel) {
        var backend = channel.objects.backend;
            backend.login_between(email, wachtwoord, function(pyval) {
                if (pyval == 'False'){
                    alert("foute gegevens");
                } else {
                    naam_mod = pyval;
                    document.getElementById('login_email').value = '';
                    document.getElementById('login_ww').value = '';
                    document.getElementById('div_mod_overlay').style.height = '0%';
                }
            });
        });

}

function maak_acc(){
    var email = document.getElementById('new_login_email').value;
    var wachtwoord = document.getElementById('new_login_ww').value;
    var naam = document.getElementById('new_login_naam').value;

    new QWebChannel(qt.webChannelTransport, function(channel) {
        var backend = channel.objects.backend;
            backend.login_new_between(naam, wachtwoord, email, function(pyval) {
                if (pyval == false){
                    alert("error");
                } else {
                    alert("aangemaakt");
                    email = document.getElementById('new_login_email').value = "";
                    wachtwoord = document.getElementById('new_login_ww').value = "";
                    naam = document.getElementById('new_login_naam').value = "";

                    document.getElementById('div_mod_overlay').style.height = '0%';
                    document.getElementById('log_in_new_id').style.display = 'display';
                }
            });
        });
}

function make_new(){
    document.getElementById('div_mod_overlay').style.height = '100%';
    document.getElementById('log_in_new_id').style.display = 'block';
}

function log_out(){
    location.reload();
}

function close_new_mod(){
    email = document.getElementById('new_login_email').value = "";
    wachtwoord = document.getElementById('new_login_ww').value = "";
    naam = document.getElementById('new_login_naam').value = "";

    document.getElementById('div_mod_overlay').style.height = '0%';
    document.getElementById('log_in_new_id').style.display = 'display';
}

function all_messges(){

}

// functies voor scherm ----------------------------------------------------------------------------------------------
var locatie_scherm = '';
var berichten_fresh = '';

function scherm_locatie(locatie){
    locatie_scherm = locatie;
    document.getElementById('locatie_div').innerHTML = locatie;
    get_faciliteiten();
    setInterval(get_current_wheater, 60000);
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

                get_current_wheater();
            
            });
        });
}

function get_current_trains(){
    document.getElementById("trein_info_id").innerHTML = '';

    new QWebChannel(qt.webChannelTransport, function(channel) {
        var backend = channel.objects.backend;
            backend.get_current_trains(locatie_scherm, function(pyval) {
                antwoord = pyval;

                for (let i = 0; i < pyval.length; i++) {
                    //pyval[i];

                    base = "<div class='singel_train_div'><button class='soort'>";

                    if (pyval[i][1] == 'IC'){
                        base = base + "IC</button><button class='orig'>";
                    } else {
                        base = base + "SPR</button><button class='orig'>";
                    }

                    base = base + "Vanaf: " + pyval[i][0];

                    if (pyval[i][2] == 'ON_STATION'){
                        base = base + "</button><button class='loc'><i class='fa-solid fa-location-dot'></i></button></div>";
                    } else {
                        base = base + "</button><button class='loc'><i class='fa-solid fa-train-tram'></i></button></div>";
                    }

                    document.getElementById("trein_info_id").innerHTML = document.getElementById("trein_info_id").innerHTML + base;
                }

                get_berichten();
            });
        });
}


function get_current_wheater(){
    new QWebChannel(qt.webChannelTransport, function(channel) {
        var backend = channel.objects.backend;
            backend.get_current_wheater(locatie_scherm, function(pyval) {
                antwoord = pyval;

                antwoord = antwoord.split(";");
                weer = antwoord[0].split(".")

                document.getElementById('weer_graden_id').innerHTML = weer[0] + "\u00B0C " + antwoord[1];
                get_current_trains();
            });
        });
}

function get_berichten(){

    new QWebChannel(qt.webChannelTransport, function(channel) {
        var backend = channel.objects.backend;
            backend.get_berichten(locatie_scherm, function(pyval) {

                if (pyval != berichten_fresh){

                    document.getElementById('bericht_text_id').innerHTML = '';
                
                    for (let i = 0; i < pyval.length; i++) {
                        base = "<button class='textvak'>" + pyval[i][0] + "<div class='naamvak'> ~" + pyval[i][1] + "</div></button>";

                        document.getElementById('bericht_text_id').innerHTML = document.getElementById('bericht_text_id').innerHTML + base;
                    }

                    berichten_fresh = pyval;
                };

                document.getElementById('scherm_overlay').style.height = "0%";
            });
        });
}
