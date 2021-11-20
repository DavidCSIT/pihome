<?php
    ini_set('display_errors', 1);
    ini_set('display_startup_errors', 1);
    error_reporting(E_ALL);

    //connect to db
    require 'dbconfig.php';
    $mysqli = new mysqli($servername,$username,$password,$dbname);    
    if (mysqli_connect_errno( )) die("Failed to connect to database");


    //update DB based on button pushed
    if (!empty($_POST["waterVegs"]))
        $sql = "UPDATE config set value='-1' where id='skip'";
    elseif (!empty($_POST["waterBerries"]))
        $sql = "UPDATE config set value='-2' where id='skip'";
    elseif (!empty($_POST["skip1"]))
        $sql = "UPDATE config set value='1' where id='skip'";
    elseif (!empty($_POST["skip2"]))
        $sql = "UPDATE config set value='2' where id='skip'";
    elseif (!empty($_POST["heat1"]))
        $sql = "UPDATE config set value='1' where id='override'";
    elseif (!empty($_POST["heat2"]))
        $sql = "UPDATE config set value='2' where id='override'";
    else {
        print("what?");
        exit();
    }
    
    //check sql worked    
    if ($mysqli -> query( $sql)) {
        printf("worked");        
    }
     else{
        printf("failed");
        exit();     
    }
    
    //change heating status if required
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
     
    //change watering status if required
    if (!empty($_POST["waterVegs"]) || !empty($_POST["waterBerries"])){
       $sql = "UPDATE config set value='T' where id='watering'";
       if ($mysqli -> query( $sql)) {
            printf("workred");        
       }
       else{
           printf("failed");
           exit();
         }
     }
     
     
    $mysqli -> close();
    header('Location: http:/done.php');
?>