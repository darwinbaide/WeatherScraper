async function loadWeather() {
    version = 'forecast';
    total = "version=".concat(version); // This will hold the data to send
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
        document.getElementById('forecast1').innerHTML = data.Data;
    } else {
        document.getElementById("current-tmp").innerHTML = "Could not reach the server to retrieve data. " + total;


    }

}