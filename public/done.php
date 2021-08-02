<!doctype html>
<html lang="en">

<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
  
    <!-- Bootstrap -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" crossorigin="anonymous">  
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.5.4/dist/umd/popper.min.js"
        integrity="sha384-q2kxQ16AaE6UbzuKqyBE9/u/KzioAlnx2maXQHiDX9d4/zp8Ok3f+M7DPm+Ib6IU"
        crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/js/bootstrap.min.js"
        integrity="sha384-pQQkAEnwaBkjpqZ8RU1fF1AKtTcHJwFl3pblpTlHXybJjHpMYo79HY3hIi4NKxyj"
        crossorigin="anonymous"></script>

        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=Concert+One&family=Orbitron&display=swap" rel="stylesheet">

    <style>
        .rounded {
            border-radius: 2rem !important;         
        }
        .box {
            width: 300px;
        }
        p, h1, .btn {
            font-family: 'Orbitron', sans-serif;
        }
        .btn {
            font-family: 'Press Start 2P', cursive;
            width: 200px;
        }
        .warm{
            background-color: lightsalmon;
        }
        .hot{
            background-color: red;  
        }
        .cool{
            background-color: lavender;  
        }
        .cold{
            background-color: lightblue;  
        }




    </style>

    <title>Pi Home</title>
</head>

<body>
    
    <div class="border rounded mx-auto my-3 box ">
        <h1 class="text-center my-3">Pi Home</h1>
    </div>

    <div class="border rounded mx-auto my-3 box ">
        <h1 class="text-center my-3"> Your wish is my command</h1>
    </div>

    <div class="col text-center">
        <form action="index.php" method="POST">
            <input type="submit" name="WaterNow"  class="btn btn-primary btn-lg my-3" value="Home"> <br>
        </form>
    </div>

</body>

</html>