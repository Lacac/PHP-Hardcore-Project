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
        hr {
            border: 10px solid green;
            border-radius: 5px;
        }
    </style>
</head>
<body>
<br/>
<hr>
<br/><h2>Details of clicked student</h2>
</br>
<table>
           <tr>
               <th>Fullname</th>
               <th>Email</th>
               <th>Phone number</th>
           </tr>
           <?php
            session_start();
            // Nhập giá trị number bằng phương thức post
            $data = isset($_POST['td_data']) ? $_POST['td_data'] : '';
            $_SESSION['id'] = $data;
            // echo $data;
            require 'permission.php';
            $u = "your_username";
            $p = "your_password";   
            $permission = new permission($u,$p);
            $conn = $permission->connect_to_mssql();
            // $data = mysqli_real_escape_string($conn, $data); // Sử dụng hàm mysqli_real_escape_string() để bảo vệ chống lại các cuộc tấn công SQL injection
            $sql = "SELECT fullname, email, phonenum FROM student WHERE id=?";
            $stmt = sqlsrv_prepare($conn, $sql, array(&$data));
            if (sqlsrv_execute($stmt)) {
                $result = sqlsrv_fetch_array($stmt, SQLSRV_FETCH_ASSOC);
                if (!empty($result)) {
                    echo "<tr><td>".$result["fullname"]."</td><td>".$result["email"]."</td><td>".$result["phonenum"]."</td></tr>";
                } else {
                    $msg = "This profile is empty now!";
                }
            } else {
                $msg = "Query execution failed!";
            }
            ?>
</table>
<br/>
<button type="button" class="btn btn-primary btn-lg" onclick='window.location.href="sendmess.php"'>Chat with this student</button>
<?php if(isset($_SESSION['teacher']) && $_SESSION['teacher']) echo '<a href="tec_update.php"><button type="button" class="btn btn-primary btn-lg">Update information</button></a>';?>
<?php if(isset($_SESSION['teacher']) && $_SESSION['teacher']) echo '<br/><br/><form action="delete.php" method="post"><button type="submit" name="delete" class="btn btn-primary btn-lg">Delete this student</button></form>';?>
</body>
</html>
