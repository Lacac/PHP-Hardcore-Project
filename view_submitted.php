<?php
session_start();
if (!isset($_SESSION['teacher']) && !isset($_SESSION['student'])) {
    // Redirect them to the login page
    header("Location: login.php");
    exit; // Terminate the script after redirection
}

if (!isset($_GET['assignment'])) {
    echo "No assignment selected.";
    exit; // Terminate the script if no assignment parameter is provided
}

$assignment = $_GET['assignment']; // Get the assignment name from the URL parameter

// Update the path to the assignment directory based on the provided assignment parameter
$mypath = "baitap/" . $assignment;

$fileList = glob("$mypath/*");

if (count($fileList) > 0) {
    foreach ($fileList as $filename) {
        if (is_file($filename)) {
            $target = basename("$filename", ".pdf");
            $target1 = basename("$filename");
            $downloadLink = '/baitap/' . $assignment . '/' . $target . '/' . $target1; // Update the download link with the assignment parameter
            $safeFileName = htmlspecialchars($target); // Sanitize the file name

            echo $safeFileName . ' <a href="' . $downloadLink . '">Download</a><br>';
        }
    }
} else {
    echo 'No files found.';
}
?>
