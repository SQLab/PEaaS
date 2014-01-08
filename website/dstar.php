<?php 
    session_start();
    if(isset($_GET["Dstar"]))
		$_SESSION["Dstar"]=$_GET["Dstar"];
    else if(isset($_POST["wrong"]))
		$_SESSION["wrong"]=$_POST["wrong"];
    else if(isset($_GET["lcov"]))
		$_SESSION["lcov"]=$_GET["lcov"];
    echo "<script type='text/javascript'>";
    echo "history.go(-1)";
    echo "</script>"; 
?>
