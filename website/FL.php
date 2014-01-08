<style type='text/css'>
@import url(cssjs/style.css);
</style>
<?php
	require_once("savedata.php");
        session_start();
        $randinfo = rand();
        $_SESSION['faultranking'] = $randinfo;
        $bl = savedata($_GET['pid']);
//        echo $bl;
        if(!$bl){
             echo "<h2>Submit - upload status</h2>";
             echo "<fieldset class=\"error\"><legend>Warning</legend> Warning: Data less 10. Please click the other button to Get Data.</fieldset>";
          exit();

        }
	if($_FILES['file']['error']>0){
      echo "<h2>Submit - upload status</h2>";
      echo "<fieldset class=\"error\"><legend>ERROR</legend> Error: No file was uploaded.</fieldset>";
	  exit();
	}
    $ftype = pathinfo($_FILES['file']['name']);
    if($ftype['extension']!="c" &&  $ftype['extension']!="cpp")
    {  
       echo "<h2>Submit - upload status</h2>";
       echo "<fieldset class=\"error\"><legend>ERROR</legend> Error: The Type was NOT supported.</fieldset>";
       exit();
    }
    $j = $_GET['pid'];
    $file_name = $randinfo . $_FILES['file']['name'] ;
    $_SESSION['faultrankingfilename'] = $file_name;
	$copypath = '/home/coding/FL/ucodes/'.$file_name;
	#$copypath = '/home/coding/FL/ucodes/'.$_FILES['file']['name'];
	move_uploaded_file($_FILES['file']['tmp_name'],$copypath);
	chmod($copypath,0777);
    	

	$cmd = "python3.3 /home/coding/FL/faultloc_abpath.py ".$file_name." ".$j;
	$output = shell_exec($cmd);
    // when fault loc end

    sleep(10);
    $returnpage = "fault_homepage.php?randinfo=" . $randinfo . "&pid=".$_GET['pid'];//"&file=".$file_name;
    //$returnpage = "fault_homepage.php?randinfo=" . $randinfo . "&pid=".$_GET['pid']."&file=".$file_name;
    echo "<script type='text/javascript'>";
    echo "window.location.href='".$returnpage."';";
    echo "</script>";

//	header($returnpage);
?>
