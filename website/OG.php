<?php
    session_start();
    require_once('db.php');   //  +++++++ 
 
    date_default_timezone_set("Asia/Taipei");
    $j = $_GET['pid'];
    $dbtable = "id".$j;
    $link = db_open();  //  +++++++ 

    $filename = "/home/coding/IG/cDDB/".$j."_input.txt";
    $file = fopen($filename,"r");
    $str = fread($file,filesize($filename));
    $tchk = table_check($dbtable,$link);
    if(!$tchk) table_create($dbtable,$link);
    $sql="select output from ".$dbtable." where input=".'"'.$str.'"';
    $result = mysql_query($sql, $link) or die(mysql_error());
	
    if(mysql_num_rows($result) > 0){  // have data
	    while($row = mysql_fetch_assoc($result))    $output = $row[output];
    }
    else{           
        $cmd = "python3.3 /home/coding/OG/outputgen.py ".$j;
        $output = shell_exec($cmd);
        $time =  date('Y-m-d H:i:s');  //  +++++++ 
        //  +++++++  24 --> 100
        if(db_count($dbtable,$link)>=100){
            $oldest = db_oldest($dbtable,$link);
//            var_dump($oldest);
            db_update($dbtable,$link,$str,$output,$time,$oldest);
        }
        else{
            $IDX = db_count($dbtable,$link) + 1;	
            db_insert($dbtable,$link,$IDX,$str,$output,$time);
        }
	//  +++++++
    }
    $_SESSION['gi'] = $str;  
    $_SESSION['go'] = $output;

    db_close($link);  //  +++++++ 
//    $response = "?pid=".$j."&input=".$_GET["input"]."&output=".$_GET["output"]."&fault=".$_GET["fault"];
//    echo $response;
?>
