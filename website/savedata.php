<?php
function savedata($j){
    require_once('db.php');  // +
//    $j = $_GET["pid"];
    $dbtable = "id".$j;
    $save_location = "/home/coding/FL/problemIO/".$j."/";
    
    if (!file_exists($save_location)) { mkdir($save_location); }
    $link = db_open();  // +
    $max = db_count($dbtable,$link);  // +
    $dircount = scan($save_location);
    $dircount -= 2;
//    echo $max;
    if($dircount/2 > 100) deleting($save_location);
    if($max >= 10){
        if( ($max-$dircount/2)>0 )
        {
           save($dbtable,$link,$dircount/2+1,$max,$save_location,$j); 
        }
        else if(($max-$dircount/2)==0)
        {
            if($max == 100 )  // 24 --> 100
            {   
	        if((int)date('d')%3 == 0){
	            save($dbtable,$link,1,$max,$save_location,$j);
	        }
            }
        }
        return 1;
    }
    else{
        return 0;	
    }
    db_close($link);
}
?>



<?php
function save($dbtable,$link,$min,$max,$save_location,$j){
for($IDX = $min;$IDX <= $max; ++$IDX){
	$result = db_IDX($dbtable,$link,$IDX);
	if(mysql_num_rows($result) > 0){  // have data
//        echo $IDX."ddd"."";
		$row = mysql_fetch_row($result);  // +
		$f = fopen($save_location.$j."_input".$IDX.".txt","w");
		fwrite($f,$row[1]);  /*  input column */  // +
		fclose($f);
		$f = fopen($save_location.$j."_output".$IDX.".txt","w");
		fwrite($f,$row[2]);  /*  input column */  // +
		fclose($f);
	}
}
}
function deleting($save_location){
    foreach(scandir($save_location) as $file) {
        if ('.' === $file || '..' === $file) continue;
        if (is_dir("$save_location/$file")) deleting("$save_location/$file");
        else unlink("$save_location/$file");
    }
    rmdir($save_location);
    mkdir($save_location);
}
?>
