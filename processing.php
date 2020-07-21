<?php
# Start of Data aquisition


$version = $_POST['version'];// grabs the version to see what function to go into
//$version="current";



if($version == "current"){
    
    $result = SQLSend('SELECT * FROM weather.today;');
    while($row = mysqli_fetch_array($result)){
        //var_dump($row);
        $forecast =$row["forecast"];
        $chance =$row["rainChance"];
        $humidity =$row["humidity"];
        $sunrise =$row["sunrise"];
        $sunset =$row["sunset"];
        $high ="High:".str_replace("°","",strval($row["high"]))."°";
        $low ="Low".str_replace("°","",strval($row["low"]))."°";
        $current =str_replace("°","",strval($row["current"]))."°";
    }
    $img='<img src="svg/wi-hail.svg" style="width:100%" class="img-responsive" />';
    $arr = array('Done' => 'yes', 'forecast' =>$forecast, 'chance' =>$chance, 'humidity' =>$humidity, 'sunrise' =>$sunrise, 'sunset' =>$sunset, 'high' =>$high, 'img' =>$img, 'low' =>$low, 'current' =>$current);// sends back data to display 
    echo json_encode($arr);// sends the response with correct json
}


if($version == "forecast"){
    $htmlText='<div class="row font-weight-bold"><div class="col">Date</div><div class="col ">Temp</div><div class="col ">Forecast</div><div class="col ">Rain Chance</div></div><hr>';
    $result = SQLSend('SELECT * FROM weather.forecast;');
    while($row = mysqli_fetch_array($result)){
        //var_dump($row);
        $htmlText.='<div class="row font-weight-bold text-white"><div class="col">'.$row[1].'</div><div class="col ">'.$row[2].'</div><div class="col ">'.$row[3].'</div><div class="col ">'.$row[4].'</div></div>';
        $htmlText.='<hr><div class="row font-weight-bold text-white"><div class="col">'.$row[5].'</div><div class="col ">'.$row[6].'</div><div class="col ">'.$row[7].'</div><div class="col ">'.$row[8].'</div></div>';
        $htmlText.='<hr><div class="row font-weight-bold text-white"><div class="col">'.$row[9].'</div><div class="col ">'.$row[10].'</div><div class="col ">'.$row[11].'</div><div class="col ">'.$row[12].'</div></div>';
        $htmlText.='<hr><div class="row font-weight-bold text-white"><div class="col">'.$row[13].'</div><div class="col ">'.$row[14].'</div><div class="col ">'.$row[15].'</div><div class="col ">'.$row[16].'</div></div>';
        $htmlText.='<hr><div class="row font-weight-bold text-white"><div class="col">'.$row[17].'</div><div class="col ">'.$row[18].'</div><div class="col ">'.$row[19].'</div><div class="col ">'.$row[20].'</div></div>';
        $htmlText.='<hr><div class="row font-weight-bold text-white"><div class="col">'.$row[21].'</div><div class="col ">'.$row[22].'</div><div class="col ">'.$row[23].'</div><div class="col ">'.$row[24].'</div></div>';
    }
   
    $arr = array('Done' => 'yes', 'Data' =>$htmlText);// sends back data to display 
    echo json_encode($arr);// sends the response with correct json
}



function SQLSend($query){
    
    $dbhost = "127.0.0.1:3306";
    $dbuser = "darwin";
    $dbpass = "Db12345678";
    $dbname = "weather";
    $mysqli = new mysqli($dbhost, $dbuser, $dbpass, $dbname);
    /* check connection */
    if ($mysqli->connect_errno) {
        printf("Connect failed: %s\n", $mysqli->connect_error);
        exit();
    }
    /* Select queries return a resultset */
    $result = $mysqli->query($query);
    $mysqli->close();
    return $result;
    }

?>


