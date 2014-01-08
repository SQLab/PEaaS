<?php
   require('db.php');	
   $j = $_GET['pid'];
   $codepath = "/home/coding/OG/problist/code_file/".$j."/";
   $ACpath = "/home/coding/OG/problist/DB/".$j."/";
   if (!file_exists($ACpath)) {  mkdir($ACpath); }
   if(scan($ACpath)==2 && scan($codepath)!=2 && scan($ACpath) < scan($codepath)){
        $ACcmd = "python3.3 /home/coding/OG/autocompiler.py ".$j." ".$codepath." ".$ACpath;
        //echo $ACcmd;
        $o = shell_exec($ACcmd);
   }
//   echo $o;
//   echo "?pid=".$id["probid"];
?>

