<?php
   session_start();
   $randinfo = $_REQUEST['randinfo'];
   if ($_SESSION['faultranking'] != $randinfo) exit("No same");
   echo '<?xml version="1.0" encoding="UTF-8" ?>';
   echo "\n";
?>

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<title></title>

<style type='text/css'>
@import url(./cssjs/style.css);
a:link,a:visited{
 color:#000000;  
 text-decoration: none;
}
a:hover{text-decoration: underline;}
p
{
 line-height : 15px;
font-size:150%;
}
#result
{
  float : right;
  z-index : 1;
}

</style>
<script src="./cssjs/jquery-2.0.3.js"></script>
<script src="./cssjs/utility.js"></script>  <!--- for Dstar Lcov function --->
</head>
<body >

<?php
  $color=array("#b420b3","#ff01fd","#c40300","#fa0203","#ff8a8a","#fb7802",
               "#ffc48a","#feff8a","#029500","#a5c8a4"); 
  $ranking = array();
  $content = array();
  $pd = $_GET["pid"];
  $file = $_SESSION["faultrankingfilename"]; // code.cpp
  //$file = $_GET["file"]; // code.cpp
  $test_dir = "/home/coding/FL/problemIO/".$pd."/";
  $path_parts = pathinfo($file);
  $code_dir = $path_parts['filename'];
  $path = "/home/coding/FL/ufiles/";
  $faultpath = $path.$code_dir."/";
?>

<!--- this is left div Dstar--->
<div style="width:600px;height:575px;position:absolute;top:5px;left:5px">
<!--<div style="width:600px;height:60px;">-->
<ul class="ul_menu">
  <li id="D1" onclick="Ds(this)"><img src="./cssjs/gif/D1.jpg" /></li>
  <li id="D2" onclick="Ds(this)"><img src="./cssjs/gif/D2.jpg" /></li>
  <li id="D3" onclick="Ds(this)"><img src="./cssjs/gif/D3.jpg" /></li>
</ul>
<!--</div>-->
<?php
 
  $line = 0;
  $txt = fopen($faultpath."fault.txt","r");
  $line1 = fgets($txt);
  while ( !feof($txt))
  {
      $n = fgets($txt);
      $x = explode(":",$n);
      //echo $_POST['Dstar'];
      if(isset($_SESSION['Dstar']) && $x[0] == $_SESSION['Dstar']) 
      {
		for ($i=0;$i<=9;$i++)
        {
	  		$n = fgets($txt);
            $result = explode(":",$n);
            $r = str_replace("\n","",$result[1]);
            if(!array_key_exists($r,$ranking))
            {
      	         $ranking[$r] = $color[$i];
            }
        }
        break;
     }	
  } //end while
//  var_dump($ranking);
  $line = 1;
  $cpp = fopen($faultpath.$file,"r");
  while ( !feof($cpp))
  {	  
	$f=fgets($cpp); 
	$f = str_replace("<","&lt;",$f); 
	$f = str_replace(">","&gt;",$f); 
	if(!array_key_exists($line,$content))
    {
    	$content[$line] = $f;
    }
	$line++;  
  }
  $totalline = $line;
//  echo $line;
//  var_dump($content);
//  var_dump($ranking);
?>
<!--this is line number -->
<div style="width:360px;height:60px;">
</div>
<pre class="fl_line" >
<span class="header">  #</span>
<?php
	for($L = 1;$L<=$totalline-1;$L++){
		if($L<=9)   echo "<span class=\"fl_l\">&nbsp;&nbsp&nbsp;".$L.".</span>";
		else	echo "<span class=\"fl_l\">&nbsp;&nbsp;".$L.".</span>";
        echo "<br>";
	}
?>
</pre>
<!--this is passed line -->
<pre class="fl_pass" >
<span class="header">   Pass Line</span>
<?php
	if(isset($_SESSION["lcov"])){
		$pass = fopen($faultpath."g".$_SESSION["lcov"].".txt","r");
		for($p=1;$p<=5;$p++) $f=fgets($pass);
		for($L = 1;$L<=$totalline-1;$L++){
			$f=fgets($pass);
			$ps = explode(":",$f);
			echo "<span class=\"fl_p\">".$ps[0].":&nbsp;&nbsp;</span>";
		    echo "<br>";
		}
		fclose($pass);
	}
	else{
		for($L = 1;$L<=$totalline-1;$L++){
			echo "<span class=\"fl_p\">:&nbsp;&nbsp;</span>";
		    echo "<br>";
		}
	}
?>
</pre>
<!--this is code content -->
<pre class="fl_code" >
<span style="font-weight:bold;">Source code</span>
<?php
	for($L = 1;$L<=$totalline-1;$L++){
		if(array_key_exists($L,$ranking))
			  echo "<span class=\"fl_c\"STYLE=\"background-color:".$ranking[$L]."\" >".$content[$L]."</span>";
		else	echo "<span class=\"fl_c\">".$content[$L]."</span>";
        echo "<br>";
	}
?>
</pre>

</div>

<!--- this is center div ranking line color--->
<div style="width:700px;height:60px;position:absolute;top:0%;left:900px">
	<p style="position:absolute;left:250px;">#<?php if(isset($_SESSION['Dstar'])) echo $_SESSION['Dstar'];?> Ranking Color#</p>
	<div id="web_status">
	<img style="position:absolute;top:53px;left:148px;" src="./cssjs/gif/sysStatus.jpg"></img>
	<?php
		$x = 1;
		foreach ($ranking as $k => $v) {
		    echo "<div id=\"sys_lvl_".$x."\" class=\"sys_lvl\">".$k."</div>";
		    $x++;
		}
	?>
	</div>
</div>

<!--- this is right div wrong test color--->
<div style="width:700px;position:absolute;top:102px;left:900px">
	<p align= "center">#Wrong Test#</p>
	<form method="post" action="dstar.php" >
	<p align="center">
	<?php
	$line1 = str_replace(" ",";",$line1);
	$line1 = str_replace("\n","",$line1);  
	if($line1 !="correct"){
		$result = explode(";",$line1);
		if(!empty($result)){
			foreach( $result as $i){
			    if($i!=NULL){
                                $sp = preg_split('/[a-zA-Z]/',$i); //spilt text and digit
				echo "<input  type=\"radio\" name=\"wrong\"  onclick=\"javascript: submit()\" value=\"".$sp[1]."\">".$i."</input>";
			    }
			}
		}
	}
        else{
           echo "<p align=\"center\">You Pass the Test this time.<br><br>Welcome to try again! </p>";
           unset($_SESSION['wrong']);
        } 
	?>
	</p>
	</form>

	<?php 
	if(isset($_SESSION['wrong']))
	{  //echo "The Wrong test you have selected ".$_POST['wrong'];
	?>
	<table class="inputoutput" align="center">
	    <tbody>
		<tr>
		<td colspan=5 align="center">
		<?php
			echo "No.".$_SESSION['wrong']."  Test";
		?>
		</td>
		</tr>
		<tr>
		<td class="SampleCaption">
		<h3 style="text-align:left">
		      Input Data
		</h3>
		</td>
		<td width="10%">
		</td>
		<td class="SampleCaption">
		<h3 style="text-align:left">
		      Correct Output Data
		</h3>
		</td>
		<td width="10%">
		</td>
		<td class="SampleCaption">
		<h3 style="text-align:left">
		      User Output Data
		</h3>
		</td>
		</tr>
		<tr>
		</tr>
		<tr class="inputoutput">
		<td class="inputoutput" valign="top">
		<pre><?php 
			$filename= $test_dir.$pd."_input".$_SESSION['wrong'].".txt";
			$file = fopen($filename,"r");
			$str = fread($file,filesize($filename));
			echo $str;   
			fclose($file);
		?>
		</pre>
		</td>
		<td width="10%">
		</td>
		<td class="inputoutput" valign="top">
		<pre><?php 
			$filename= $test_dir.$pd."_output".$_SESSION['wrong'].".txt";
			$file = fopen($filename,"r");
			$str = fread($file,filesize($filename));
			echo $str;   
			fclose($file);
		?>
		</pre>
		</td>
		<td width="10%">
		</td>
		<td class="inputoutput" valign="top">
		<pre><?php 
			$filename= $faultpath.$pd."_useroutput".$_SESSION['wrong'].".txt";
			$file = fopen($filename,"r");
			$str = fread($file,filesize($filename));
			echo $str;   
			fclose($file);
		?>
		</pre>
		</td>
		</tr>
		<tr>
		<td align="center" colspan=5 title="You can look program that test data  passed line">
		<a id="<?php echo $_SESSION['wrong'];?>" onclick="Ps(this)">pass line</a>
		</td>
		</tr>
	    </tbody>
	</table>
	<?php
	}
	?>
</div>

</body>
</html>
