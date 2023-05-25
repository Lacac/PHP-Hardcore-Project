<?php session_start(); ?>
<!DOCTYPE html>
<html>
<head>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
    <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>
    <style type="text/css">
        table {
            border-collapse: collapse;
            width: 100%;
            color: #d96459;
            font-family: monospace;
            font-size: 25px;
            text-align:left; 
        }
        th {
            background-color: #d96459;
            color: white; 
        }
        tr:nth-child(even) {background-color: #f2f2f2}
    </style>
</head>
<body>
    <nav class="navbar navbar-light bg-light">
         <span class="navbar-brand mb-0 h1">
            List of students 
         </span>
    </nav>
    <br/>
       <table>
           <tr>
               <th>ID</th>
               <th>Fullname</th>
               <th>Email</th>
               <th>Phone number</th>
           </tr>
           <?php    
                
                require 'permission.php';
                $u = "your_username";
                $p = "your_password";   
                $permission = new permission($u,$p);
                $conn = $permission->connect_to_mssql();
                $sql = "SELECT id, fullname, email, phonenum FROM student";
                $result = sqlsrv_query($conn, $sql);
                if ($result === false) {
                    die(print_r(sqlsrv_errors(), true));
                }
                if(sqlsrv_has_rows($result)){
                    while($row = sqlsrv_fetch_array($result, SQLSRV_FETCH_ASSOC)){
                        echo '<tr><td onclick="load_ajax(this)">'.$row["id"]."</td><td>".$row["fullname"]."</td><td>".$row["email"]."</td><td>".$row["phonenum"]."</td></tr>";
                    }
                } else{
                    $msg = "This class is empty now!";
                }
           ?>
    </table>
    <p><?php if(isset($msg)) echo $msg; ?></p>
    <script>
        function load_ajax(param){
                $.ajax({
                    url : "details.php",
                    type : "post",
                    dataType:"text",
                    data : {
                         td_data : param.innerHTML   // input with id = number
                    },
                    success : function (result){
                        $('#result').html(result);
                    }
                });
            }
    </script>
    <div id="result">
    </div>
</body>
</html>
 