<?php
session_start();
if (!isset($_SESSION['teacher']) && !isset($_SESSION['student'])) {
    // Redirect them to the login page
    header("Location: login.php");
    exit(); // Terminate script execution after redirection
}

$fileList = glob('baitap/*');
foreach ($fileList as $filename) {
    if (is_dir($filename)) {
        $assignment = basename($filename);
        $submitLink = "submit.php?assignment=" . urlencode($assignment);
        $viewSubmittedLink = "view_submitted.php?assignment=" . urlencode($assignment);
        echo $filename . '<a href="' . $filename . '"> Download </a>' . '<a href="' . $submitLink . '"> Nop bai </a>' . '<a href="' . $viewSubmittedLink . '"> Bai da nop </a>', '<br>';
    }
}
?>
