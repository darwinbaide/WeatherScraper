async function loadWeather() {
    version = 'current';
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
        document.getElementById('current-tmp').innerHTML = data.current;
        document.getElementById('forecast').innerHTML = data.forecast;
        document.getElementById('chance').innerHTML = data.chance;
        document.getElementById('forecast-img').innerHTML = data.img;
        document.getElementById('high-tmp').innerHTML = data.high;
        document.getElementById('low-tmp').innerHTML = data.low;
        document.getElementById('sunrise').innerHTML = data.sunrise;
        document.getElementById('sunset').innerHTML = data.sunset;
        document.getElementById('humidity').innerHTML = data.humidity;

    } else {
        document.getElementById("current-tmp").innerHTML = "Could not reach the server to retrieve data. " + total;


    }

}