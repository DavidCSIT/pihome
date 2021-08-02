<?php
    require 'dbconfig.php';
    $mysqli = new mysqli($servername,$username,$password,$dbname);
    if (mysqli_connect_errno( )) die("Failed to connect to database");

    if (!empty($_POST["waternow"])){
        exec("/home/pi/PiRainMaker/rainmaker.py 2");
        header('Location: http:/done.php');
    }
    elseif (!empty($_POST["skip1"]))
        $sql = "UPDATE config set value='1' where id='skip'";
    elseif (!empty($_POST["skip2"]))
        $sql = "UPDATE config set value='F' where id='heating'";
    elseif (!empty($_POST["heat1"]))
        $sql = "UPDATE config set value='1' where id='override'";
    elseif (!empty($_POST["heat2"]))
        $sql = "UPDATE config set value='2' where id='override'";
    else {
        print("what?");
        exit();
     }
   
    if ($mysqli -> query( $sql)) {
        printf("workred");        
    }
     else{
        printf("failed");
        exit();     
     }

     if (!empty($_POST["heat1"]) || !empty($_POST["heat2"])){
        $sql = "UPDATE config set value='T' where id='heating'";
        if ($mysqli -> query( $sql)) {
            printf("workred");        
        }
         else{
            printf("failed");
            exit();
         }
     }
    $mysqli -> close();
    header('Location: http:/index.php');
?>