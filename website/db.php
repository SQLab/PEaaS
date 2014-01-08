<?php
function db_open(){
    $DB_SET = array();
    $cfg = fopen("config.cfg","r");
    $SETTING = fgets($cfg);
    $SETTING = str_replace("\n","",$SETTING);
    if ( strcmp($SETTING,"[SETTING]") == 0 )
    {
        while(!feof($cfg)){
            $s = fgets($cfg);
            $s = str_replace("\n","",$s);
            $piece = explode("=",$s);
            $DB_SET[$piece[0]] = $piece[1];
        }
    }
    fclose($cfg);

    $link = mysql_connect( $DB_SET["server"], $DB_SET["account"], $DB_SET["password"]) or die(mysql_error());
    mysql_select_db($DB_SET["db"],$link);
    return $link;
}
function table_check($dbtable,$link){
    $sql = "SHOW TABLES LIKE '$dbtable'";
    $t = mysql_query($sql, $link);
    $row = mysql_fetch_row($t);
//    echo $row[0];
    if($row[0] === $dbtable) return 1;
    else return 0;
}
function table_create($dbtable,$link){
$sql = "CREATE TABLE ".$dbtable." 
(
idx BIGINT(20) NOT NULL, 
PRIMARY KEY(idx),
input TEXT,
output TEXT,
time DATETIME
)";
    $c = mysql_query($sql, $link) or die(mysql_error());
}
function db_close($link){
    mysql_close($link);
}
function db_count($dbtable,$link){
    $sqlcount = "SELECT COUNT(*) FROM ".$dbtable;
    $count = mysql_query($sqlcount, $link) or die(mysql_error());
    $row = mysql_fetch_row($count);
    return $row[0]; //	index count
}
function db_insert($dbtable,$link,$IDX,$input,$output,$time){
    $sqlinsert="INSERT INTO ".$dbtable." (idx,input,output,time)  VALUES ('$IDX','$input','$output','$time');";
    mysql_query($sqlinsert,$link) or die(mysql_error()) ;
}
function db_update($dbtable,$link,$input,$output,$time,$oldest){
    $sqlupdate ="UPDATE ".$dbtable." SET input = '$input', output = '$output' , time = '$time' WHERE time = '$oldest'";
    mysql_query($sqlupdate,$link) or die(mysql_error()) ;
}
function db_oldest($dbtable,$link){
    $sqloldest = "SELECT * FROM ".$dbtable." where time <= ( NOW()) ORDER BY time";
    $oldest = mysql_query($sqloldest, $link) or die(mysql_error());
    $row = mysql_fetch_row($oldest);
    
    return $row[3]; // return oldest time
}
function db_IDX($dbtable,$link,$IDX){
    $sql="select * from ".$dbtable." where idx=".$IDX;
    $result = mysql_query($sql, $link) or die(mysql_error());
    return $result;
}
function scan($dir){
    return count(scandir($dir));
}

?>
