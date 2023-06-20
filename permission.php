<?php

class permission {
    public $username;
    public $password;

    function __construct($u, $p) {
        $this->username = $u;
        $this->password = $p;
    }

    // function is_teacher() {
    //     $teacher = false;
    //     $conn = $this->connect_to_mssql("LAPTOP-3GJTBRSD\DBS401NHOM2", "DBS_IA1601_GROUP2", "", "");
    //     $user = $this->username;
    //     $pass = $this->password;
    //     $tsql = "SELECT * FROM teacher WHERE username = ? AND password = ?";
    //     $params = array($user, $pass);
    //     $stmt = sqlsrv_query($conn, $tsql, $params);
    //     if ($stmt === false) {
    //         die(print_r(sqlsrv_errors(), true));
    //     }
    //     if (sqlsrv_fetch($stmt) === true) {
    //         $teacher = true;
    //     }
    //     sqlsrv_free_stmt($stmt);
    //     sqlsrv_close($conn);
    //     return $teacher;
    // }
    function is_teacher() {
        $teacher = false;
        $conn = $this->connect_to_mssql("LAPTOP-3GJTBRSD\DBS401NHOM2", "DBS_IA1601_GROUP2", "sa", "24062001");
        $user = $this->username;
        $pass = $this->password;
       
        if(preg_match('/[\'"]/', $user) ){
            exit('Failed logon');
        }
        // Lỗ hổng SQL Injection: Không sử dụng tham số an toàn
        $tsql = "SELECT * FROM teacher WHERE username = '$user' AND password = '$pass'";

        $stmt = sqlsrv_query($conn, $tsql);
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
        $conn = $this->connect_to_mssql("LAPTOP-3GJTBRSD\DBS401NHOM2", "DBS_IA1601_GROUP2", "sa", "24062001");
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
}
//  DBS{IA1601_GROUP2_FLAG3}
?>
