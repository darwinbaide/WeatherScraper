function start() {
    user = getCookie("uer");
    if (user == "") {
        alert("Please Log in first.");
        location.replace("http://172.18.76.150/darwin/BidSource/beta3/dashboard/login.html");
    } // if not logged in then go back

    if (sessionStorage.getItem("websiteID") === null) {
        alert("Key from Home was not present. Please select a website from home page first.");
        location.replace("directory.html");
    } else {
        if (sessionStorage.getItem("type") === null) {
            sessionStorage.setItem('type', '1');
        }
    }

}

function load() {
    version = 'work';
    type = sessionStorage.getItem("type");
    inputText = sessionStorage.getItem("websiteID");
    total = "version=".concat(version, "& websiteID=", inputText, "& type=", type); // This will hold the data to send
    makeCalls(total);





}

async function makeCalls(total) {

    let responsive = await fetch("processing.php", {
        method: 'post',
        headers: {
            "Content-type": "application/x-www-form-urlencoded; charset=UTF-8"
        },
        body: total
    });
    let data = await responsive.json();
    //console.log(data);

    if (responsive.ok == false || responsive.status !== 200) {
        alert("Request Failed ");
        console.log('Network response was not ok.');
        return;
    }
    if (data.Done == "yes") {
        sessionStorage.setItem('firstline', data.firstLine);
        sessionStorage.setItem('pending', data.pending);
        sessionStorage.setItem('timestamp', Date.now());
        sessionStorage.setItem('status', data.status);

        document.getElementById('mySidenav').innerHTML = data.Data;
        dataT = data.Content;
        if (data.status == "1") {
            document.getElementById("alertOutput").innerHTML = ' <div class="alert alert-danger m-3" id="alertStatus">Pending Status - ' + data.firstLine + '</div>';
        } else if (data.status == "2") {
            document.getElementById("alertOutput").innerHTML = ' <div class="alert alert-warning m-3" id="alertStatus">Working Status - ' + data.firstLine + '</div>';
        } else {
            document.getElementById("alertOutput").innerHTML = ' <div class="alert alert-success m-3" id="alertStatus">Approved Status - ' + data.firstLine + '</div>';
        }
        if (data.frame == "yes") {


            sessionStorage.setItem('pending', data.pending);
            document.getElementById('output').innerHTML = '<div class="embed-responsive embed-responsive-16by9">  ' + "<iframe src='http://172.18.76.150/" + dataT + "'></iframe> </div>";
        } else {

            document.getElementById('output').innerHTML = dataT;
        }
        searchIT(data.filename);
        logIt("Change " + data.pending + " to working on", 0, 0, getCookie("unu"), "working on");
    } else {
        document.getElementById("output").innerHTML = "Could not reach the server to retrieve data. " + total;
        console.log("Date Failed: " + total);
        m //akeCalls(total); // this shouldnt get reached if the response came in, but just incase the message came in but the response wasnt the correct json format
    }
    if (sessionStorage.getItem("type") == "1") {
        var box1 = document.getElementById("requestType").checked = false;
    } else {
        var box1 = document.getElementById("requestType").checked = true;
    }
    return ("Yes");
}



async function makeSQL(total) {
    let responsive = await fetch("processing.php", {
        method: 'post',
        headers: {
            "Content-type": "application/x-www-form-urlencoded; charset=UTF-8"
        },
        body: total
    });
    let data = await responsive;
    if (responsive.ok == false || responsive.status !== 200) {
        alert("Request Failed ");
        console.log('Network response was not ok.');
        return;
    }

    return ("Yes");
}

function searchIT(input) {


    var a = document.getElementById('mySidenav').getElementsByTagName('a');
    index = 0;
    for (var i = 0; i < a.length; i++) {
        if (a[i].getAttribute("name") == input) {
            index = i;
        }
    }

    if (index == 1) {
        sessionStorage.setItem("prev", "");
        sessionStorage.setItem("current", a[index].getAttribute("name"));
        if (a.length > 1) {
            sessionStorage.setItem("next", a[index + 1].getAttribute("name"));
        } else {
            sessionStorage.setItem("next", "");
        }
    } else if (index == a.length - 1) {
        sessionStorage.setItem("next", "");
        sessionStorage.setItem("current", a[index].getAttribute("name"));
        if (a.length > 1) {
            sessionStorage.setItem("prev", a[index - 1].getAttribute("name"));
        } else {
            sessionStorage.setItem("prev", "");
        }
    } else {
        sessionStorage.setItem("prev", a[index - 1].getAttribute("name"));
        sessionStorage.setItem("current", a[index].getAttribute("name"));
        sessionStorage.setItem("next", a[index + 1].getAttribute("name"));

    }

}

async function linkClick(inputText) {
    sleep(150);
    inputStatus = sessionStorage.getItem("status");
    /* if (inputStatus == "1") { // this will tell me what the status was coming in. 
        unload(); // release to pending if it was being work on
    } */

    type = sessionStorage.getItem("type");
    websiteid = sessionStorage.getItem("websiteID");
    version = 'specific';
    total = "version=".concat(version, "& name=", inputText, "& websiteID=", websiteid, "& type=", type); // This will hold the data to send

    let responsive = await fetch("processing.php", {
        method: 'post',
        headers: {
            "Content-type": "application/x-www-form-urlencoded; charset=UTF-8"
        },
        body: total
    });
    let data = await responsive.json();
    console.log(responsive.ok);
    if (responsive.ok == false || responsive.status !== 200) {
        alert("Request Failed ");
        console.log('Network response was not ok.');
        return;
    }
    if (data.Done == "yes") {
        sessionStorage.setItem('firstline', data.firstLine);
        sessionStorage.setItem('pending', data.pending);
        sessionStorage.setItem('timestamp', Date.now());
        sessionStorage.setItem('status', data.status);

        document.getElementById('mySidenav').innerHTML = data.Data;
        dataT = data.Content;

        if (data.status == "1") {
            document.getElementById("alertOutput").innerHTML = ' <div class="alert alert-danger m-3" id="alertStatus">Pending Status - ' + data.firstLine + '</div>';
        } else if (data.status == "2") {
            document.getElementById("alertOutput").innerHTML = ' <div class="alert alert-warning m-3" id="alertStatus">Working Status - ' + data.firstLine + '</div>';
        } else {
            document.getElementById("alertOutput").innerHTML = ' <div class="alert alert-success m-3" id="alertStatus">Approved Status - ' + data.firstLine + '</div>';
        }



        if (data.frame == "yes") {


            document.getElementById('output').innerHTML = '<div class="embed-responsive embed-responsive-16by9">  ' + "<iframe src='http://172.18.76.150/" + dataT + "'></iframe> </div>";
        } else {
            document.getElementById('output').innerHTML = dataT;
        }
        searchIT(data.filename);
    } else {
        document.getElementById("output").innerHTML = "Could not reach the server to retrieve data. " + total;
        console.log("Date Failed: " + total);
        //makeCalls(total); // this shouldnt get reached if the response came in, but just incase the message came in but the response wasnt the correct json format
    }
    if (sessionStorage.getItem("type") == "1") {
        var box1 = document.getElementById("requestType").checked = false;
    } else {
        var box1 = document.getElementById("requestType").checked = true;
    }
    return ("Yes");
}



function previousBTN() {
    if (sessionStorage.getItem("prev") == "" || sessionStorage.getItem(null)) {
        alert("Cannot go to a previous.");
    } else {
        inputStatus = sessionStorage.getItem("status");
        if (inputStatus == "1") { // this will tell me what the status was coming in. 
            unload(); // release to pending if it was being work on
        }
        target = sessionStorage.getItem("prev");
        linkClick(target);
    }
}


function nextBTN() {
    if (sessionStorage.getItem("next") == "" || sessionStorage.getItem("next") == null) {
        alert("Cannot go to next.");
    } else {
        inputStatus = sessionStorage.getItem("status");
        if (inputStatus == "1") { // this will tell me what the status was coming in. 
            unload();
        }
        target = sessionStorage.getItem("next");
        linkClick(target);
    }
}


function changeRequest() {
    var x = document.getElementById("requestType").checked;
    if (x == true) {
        sessionStorage.setItem('type', '2');
    } else {
        sessionStorage.setItem('type', '1');
    }

    unload();
    load();
}

function directoryBTN() {
    userID = getCookie("unu");
    logIt("User " + userID + " Left Directory# " + sessionStorage.getItem("websiteID"), 0, 0, userID, "close directory");
    sessionStorage.clear();
    location.replace("directory.html");
}

function loadBTN() {
    firstURL = sessionStorage.getItem('firstline');
    document.getElementById('output').innerHTML = '<div class="embed-responsive embed-responsive-16by9">  ' + "<iframe src='" + firstURL + "'></iframe> </div>";
}

function approveBTN() {

    status = "3"
    version = 'approve';
    timeStart = sessionStorage.getItem('timestamp');
    timeNow = Date.now();
    elapsedTime = (parseInt(timeNow) - parseInt(timeStart)) / 1000;
    pendingID = sessionStorage.getItem("pending");
    total = "version=".concat(version, "& pending=", pendingID, "& status=", status, "& elapsed=", elapsedTime); // This will hold the data to send
    makeSQL(total);
    userID = getCookie("unu");
    logIt("User " + userID + " approved ID#  " + pendingID, elapsedTime, pendingID, userID, "approve");
    sessionStorage.setItem('button', 'true');
    location.reload();
}

function rejectBTN() {
    status = "4"
    timeStart = sessionStorage.getItem('timestamp');
    timeNow = Date.now();
    elapsedTime = (parseInt(timeNow) - parseInt(timeStart)) / 1000;
    pendingID = sessionStorage.getItem("pending");
    version = "reject";
    total = "version=".concat(version, "& pending=", pendingID, "& status=", status, "& elapsed=", elapsedTime); // This will hold the data to send
    makeSQL(total);
    userID = getCookie("unu");
    logIt("User " + userID + " rejected ID#  " + pendingID, elapsedTime, pendingID, userID, "reject");
    sessionStorage.setItem('button', 'true');
    location.reload();
}

function junkBTN() {
    confirming = confirm("Are you sure you want to Junk this?");
    if (confirming == false) {
        return; // confirmation on te button press
    }
    status = "5"
    version = 'junk';
    timeStart = sessionStorage.getItem('timestamp');
    timeNow = Date.now();
    elapsedTime = (parseInt(timeNow) - parseInt(timeStart)) / 1000;
    pendingID = sessionStorage.getItem("pending");
    total = "version=".concat(version, "& pending=", pendingID, "& status=", status, "& elapsed=", elapsedTime); // This will hold the data to send
    makeSQL(total);
    userID = getCookie("unu");
    logIt("User " + userID + " junked ID#  " + pendingID, elapsedTime, pendingID, userID, "junk");
    sessionStorage.setItem('button', 'true');
    location.reload();
}

function pendingBTN() {
    status = "1"
    version = 'newPending';
    timeStart = sessionStorage.getItem('timestamp');
    timeNow = Date.now();
    elapsedTime = (parseInt(timeNow) - parseInt(timeStart)) / 1000;
    pendingID = sessionStorage.getItem("pending");
    total = "version=".concat(version, "& pending=", pendingID, "& status=", status, "& elapsed=", elapsedTime); // This will hold the data to send
    makeSQL(total);
    userID = getCookie("unu");
    logIt("User " + userID + " changed  to pending ID#  " + pendingID, elapsedTime, pendingID, userID, "pending");
    location.reload();
}

function unload() {
    if (sessionStorage.getItem('status') != "1") {
        return;

    } else {
        status = "1";
        version = 'newPending';
        timeStart = sessionStorage.getItem('timestamp');
        timeNow = Date.now();
        elapsedTime = (parseInt(timeNow) - parseInt(timeStart)) / 1000;
        pendingID = sessionStorage.getItem("pending");
        total = "version=".concat(version, "& pending=", pendingID, "& status=", status, "& elapsed=", elapsedTime); // This will hold the data to send
        makeSQL(total);

    }

}

function unloadPage() {
    // this ujust clears the previous things saved onto the browser except for the website id to work on. 
    temp = sessionStorage.getItem('websiteID');
    temp2 = sessionStorage.getItem('type');
    sessionStorage.clear();
    sessionStorage.setItem('websiteID', temp);
    sessionStorage.setItem('type', temp2);
}

window.addEventListener("beforeunload", function(event) {
    //event.returnValue = "File will be released to queue as it was not Finished.";
    inputStatus = sessionStorage.getItem("status");
    buttonStatus = sessionStorage.getItem("button");

    if (inputStatus == "1" && buttonStatus != "true") { // this will tell me what the status was coming in. 
        // the status is changed to staus 2 working on after the creation of the html
        // this means that if it was status 1 then we know that we are the ones that changed it to staus 2 and not somebody else working no it 
        // this also stops us from accidentally changing the approved to pending if theres a regresh while on an approved.
        unload();
    }



});

function logIt(workString, elapsed, pending, userid, type) {
    command = 'INSERT INTO `BidSource`.`worklog`(`workstring`,`elapsedtime`,`pendingid`,`userid`,`type`, `date`) VALUES("' + workString + '",' + elapsed.toString() + ',' + pending.toString() + ',' + userid.toString() + ',"' + type + '" , now());';
    total = "version=".concat("sql", "& data=", command); // This will hold the data to send
    makeSQL(total); // this just sends the sql command and doesnt wait for anything
    console.log("Updated Log.");
}



function sleep(millisecondsToWait) {
    var now = new Date().getTime();
    while (new Date().getTime() < now + millisecondsToWait) {
        /* do nothing; this will exit once it reaches the time limit */
        /* if you want you could do something and exit */
    }
}

function getCookie(c_name) {
    if (document.cookie.length > 0) {
        c_start = document.cookie.indexOf(c_name + "=");
        if (c_start != -1) {
            c_start = c_start + c_name.length + 1;
            c_end = document.cookie.indexOf(";", c_start);
            if (c_end == -1) {
                c_end = document.cookie.length;
            }
            return unescape(document.cookie.substring(c_start, c_end));
        }
    }
    return "";
}