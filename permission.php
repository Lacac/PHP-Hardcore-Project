<?php

class permission
{
	public $username;
	public $password;

	function __construct($u, $p) {
		$this->username = $u;
		$this->password = $p;
	}

	function __toString() {
		return $u.$p;
	}
/*
	function is_teacher() {
		$teacher = false;
        
        $con1 = new mysqli("localhost","kali","kali","class");
		if ($con1->connect_error) {
			die("Connection failed: " . $con1->connect_error);
		}
		$user = $this->username;
		$pass = $this->password;
		$stmt = $con1->prepare("SELECT * FROM teacher WHERE username = ? AND password = ?");
        $stmt->bind_param("ss", $user, $pass);
        $stmt->execute();
        if($stmt->fetch() == 1){
            $teacher = true;
        }
        return $teacher;
	}

    function is_student() {
        $student = false;

        $con2 = new mysqli("localhost","kali","kali","class");
		if ($con2->connect_error) {
			die("Connection failed: " . $con2->connect_error);
		}
		$user = $this->username;
		$pass = $this->password;
		$stmt = $con2->prepare("SELECT * FROM student WHERE username = ? AND password = ?");
        $stmt->bind_param("ss", $user, $pass);
        $stmt->execute();
        if($stmt->fetch() == 1){
            $student = true;
        }
        return $student;
    }
*/
	function connect_to_mssql() {
		$serverName = "LAPTOP-3GJTBRSD\DBS401NHOM2";
		$database = "DBS_IA1601_GROUP2";
		$uid = "sa";
		$pass = "24062001";
		$connectionOptions = [
			"Database" => $database,
			"Uid" => $uid,
			"PWD" => $pass
		];
		$conn = sqlsrv_connect($serverName, $connectionOptions);
		if ($conn === false) {
			die(print_r(sqlsrv_errors(), true));
		}
		return $conn;
	}

	function is_teacher() {
		 $teacher = false;

		// $serverName = "LAPTOP-3GJTBRSD\DBS401NHOM2";
		// $database ="DBS_IA1601_GROUP2";
		// $uid = "sa";
		// $pass ="24062001";

		// $connection =[
		// "Database" => $database,
		// "Uid" => $uid,
		// "PWD" => $pass
		// ];

		// $conn =sqlsrv_connect($serverName,$connection);
		$conn= $this->connect_to_mssql();
		$user = $this->username;
		$pass = $this->password;
		$tsql = "SELECT * FROM teacher WHERE username = ? AND password = ?";
		$params = array($user, $pass);
		$stmt = sqlsrv_query($conn, $tsql, $params);
		if ($stmt === false) {
			die(print_r(sqlsrv_errors(), true));
		}
		if (sqlsrv_fetch($stmt) === true) {
			$teacher = true;
		}
		sqlsrv_free_stmt($stmt);
		sqlsrv_close($conn);
		return $teacher;
	}

	function is_student() {
		 $student = false;
		// $serverName = "LAPTOP-3GJTBRSD\DBS401NHOM2";
		// $database ="DBS_IA1601_GROUP2";
		// $uid = "sa";
		// $pass ="24062001";

		// $connection =[
		// "Database" => $database,
		// "Uid" => $uid,
		// "PWD" => $pass
		// ];

		// $conn =sqlsrv_connect($serverName,$connection);
		$conn= $this->connect_to_mssql();
		$user = $this->username;
		$pass = $this->password;
		$tsql = "SELECT * FROM student WHERE username = ? AND password = ?";
		$params = array($user, $pass);
		$stmt = sqlsrv_query($conn, $tsql, $params);
		if ($stmt === false) {
			die(print_r(sqlsrv_errors(), true));
		}
		if (sqlsrv_fetch($stmt) === true) {
			$student = true;
		}
		sqlsrv_free_stmt($stmt);
		sqlsrv_close($conn);
		return $student;
	}

}

?>
