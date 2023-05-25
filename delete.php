<?php
session_start();
if(!isset($_SESSION['teacher']) || !$_SESSION['teacher']){
    header('Location: login.php');
}
?>
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
</head>
<body>
    <?php
        if(isset($_POST['delete'])){
            require 'permission.php';
            $u = "your_username";
            $p = "your_password";
            $permission = new permission($u, $p);
            $con14 = $permission->connect_to_mssql();
            $x = 0;
            $arr = array();
            $sql = "SELECT * FROM student WHERE id='" . $_SESSION['id'] . "'";
            $result = sqlsrv_query($con14, $sql);
            if ($result !== false) {
                while ($row = sqlsrv_fetch_array($result, SQLSRV_FETCH_ASSOC)) {
                    foreach ($row as $r) {
                        $arr[$x] = $r;
                        $x++;
                    }
                }
            } else {
                $msg = "This profile is empty now!";
            }

            // $permission1 = new permission($u, $p);
            $con15 = $permission->connect_to_mssql();
            $id = $_SESSION['id'];
            $sql = "DELETE FROM student WHERE id='$id'";
            $result = sqlsrv_query($con15, $sql);
            if ($result !== false) {
                echo'delete successful';
            } else {
                echo'delete successful';
            }
            // $permission2 = new permission($u, $p);
            $con16 = $permission->connect_to_mssql(); 
            $sql = "DROP TABLE [$arr[1]]";
            if($stmt1->execute() && $con16->query($sql)){    
                $msg = "This student has been deleted!";
            }
        
        }
    ?>
    <br/>
    <h1 style="color: green;"><?php if(isset($msg)) echo $msg; ?></h1>
    <?php if(isset($msg))  echo '<a href="index.php"><button type="button" class="btn btn-secondary">Come back to home page</button></a>'; ?>
</body>
</html>
