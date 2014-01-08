<?php
 session_start();
 $j = $_GET['pid'];
 $currentpath = "/home/coding/IG/";
 $descriptionpath = $currentpath . "/cDDB/";
 $descriptionfile = $descriptionpath.$j.".txt";

 $cmd = "python3.3 /home/coding/IG/numeric_input_generator1.1.py ".$descriptionfile." ".$_GET['level'];
 $output = shell_exec($cmd);

 $filename = $descriptionpath.$j."_input.txt";
 $file = fopen($filename,"r");
 $str = fread($file,filesize($filename));
 $_SESSION['gi'] = $str;

// $response = "?pid=".$j."&input=".$_GET['input']."&output=".$_GET['output']."&fault=".$_GET['fault'];
// echo $response;

?>
