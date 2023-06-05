<?php
session_start();
if(!isset($_SESSION['student']) || !$_SESSION['student']){
    // Redirect them to the login page
    header("Location: login.php");  
}

if (!isset($_GET['assignment']) || empty($_GET['assignment'])) {
    // Redirect them back to the assignment list page
    header("Location: assign_list.php");
    exit();
}

$assignment = $_GET['assignment'];
$mypath = "./baitap/$assignment";

?>

<!DOCTYPE html>
<html>
<head>
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
</head>
<body>
<form action="uploadanswer.php?assignment=<?php echo urlencode($assignment); ?>" method="post" enctype="multipart/form-data">
<div class="form-group">
  <label for="exampleFormControlFile1">Chon bai tap de nop:</label>
  <input type="file" class="form-control-file" name="fileToUpload" id="fileToUpload">
  <br/>
  <input type="submit" value="Upload File" name="submit">
</div>
</form>
</body>
</html>
