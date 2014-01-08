<?php
   session_start();
   if(!isset($_GET["pid"]) || empty($_GET["pid"])) exit("Sorry No this problem!!");
   if(!isset($_GET["input"]) && !isset($_GET["output"]) && !isset($_GET["fault"]) && !isset($_GET["timelimit"])) 
	exit("Fewer parameter!");
   require('compile.php');
   echo '<?xml version="1.0" encoding="UTF-8" ?>';
   echo "\n";
?>

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<title>Test Case Generator</title>
<script type="text/javascript" src="cssjs/jquery-2.0.3.js"></script>
<script type="text/javascript" src="cssjs/IO.js"></script>
<style type='text/css'>
@import url(cssjs/style.css);
</style>
<?php
    $para = array('pid'=>$_GET["pid"],'input'=>$_GET["input"],'output'=>$_GET["output"],'fault'=>$_GET["fault"],'timelimit'=>$_GET["timelimit"]);
//    var_dump($para);
?>
</head>
<body onload="enableornot(t)">

<div id ="presubmit"></div>
    <h1 align="center" >No.<?php print($_GET["pid"]);?> Test Case Generator</h1>
    <div id="problem" class="content">
        <table width="100%">
        <tbody>
        <tr class="generator">
            <td style="padding: 0px; margin: 0px;" >
                                
                <table class="generator_table" >
                <tbody>
                <tr>
                <td width="45%" align = "center">
                    <b>Input:</b>
                </td>
                <td width="10%" align = "center">
                </td >
                <td align = "center">
                    <b>Output:</b>
                </td>
                </tr>
                <tr>
                <td>
                    <textarea class ="abb"  id="input" tabindex="1" cols=50 rows=10 name="input" ><?php
                        if ( isset( $_SESSION['gi'])){ echo $_SESSION['gi']; }
			else if(isset( $_SESSION['inDBi'])){ echo $_SESSION['inDBi']; }
                    ?></textarea>
                </td>
                <td>
                </td>
                <td style="vertical-align: top">
                    <textarea class ="abb" id="output" tabindex="3" readonly="readonly" cols=50 rows=10><?php
                        if(isset( $_SESSION['go']))   echo $_SESSION['go'];
			else if(isset( $_SESSION['inDBo']))   echo $_SESSION['inDBo'];
                    ?></textarea>
                </td>
                </tr>
                <tr>
                <td align="center">
                    <select id = "level">
                        <option value = "0">Choose Level</option>
                        <option value = "1">Easy</option>
                        <option value = "2">Medium</option>
                        <option value = "3">Hard</option>
                    </select>
                    <button id = "submiti"  onclick="InputGen(t);">Generate Input</button>
                </td>
                <td align="center">
                    <button id = "submitio" onclick="IOtGen(t);" >Generate IO</button>
                </td>
                <td align="center">
                    <button id = "submito" onclick="OutputGen(t);">Generate Output</button>
                </td>
                </tr>
		</tbody>
                </table>

            </td>
        </tr>
        <tr>
			<td style="padding: 0px; margin: 0px;" >
			</td>
		</tr>
		</tbody>
        
		</table>
	
    </div>
    <form action=<? echo "FL.php?pid=".$_GET["pid"]; ?> enctype="multipart/form-data" method="post">
			Debug Code Upload : <input id="file" name="file" type="file">
			<input id="submitcode" name="submitcode" type="submit" value="Start Debug">
			</form>
<script type="text/javascript">
var t = <?php echo json_encode($para ); ?>;
//alert("DD");
//history.go(-1);
</script>
<?php
    unset( $_SESSION['gi']);
    unset( $_SESSION['go']);
    unset( $_SESSION['inDBi']);
    unset( $_SESSION['inDBo']);
?>
</body>
</html>
