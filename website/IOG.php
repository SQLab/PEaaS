<?php
    session_start();
    require_once('db.php');   //  +++++++ 
    $j = $_GET['pid'];
    $dbtable = "id".$j;
    $link = db_open();  //  +++++++ 
    $max = db_count($dbtable,$link);  // +
    $IDX = rand(1,$max);
    $data = db_IDX($dbtable,$link,$IDX);
    if(mysql_num_rows($data) > 0){
        $row = mysql_fetch_row($data);
        $_SESSION['inDBi'] = $row[1];  
        $_SESSION['inDBo'] = $row[2];
    }
    else{
        echo "<script type='text/javascript'>";
        echo 'alert("Sorry! No Data!! Please Click the other button to Generate Data.");';
        echo "</script>"; 
        goto Nodata;
    }
Nodata:
    db_close($link);  //  +++++++ 
//    $response = "?pid=".$j."&input=".$_GET["input"]."&output=".$_GET["output"]."&fault=".$_GET["fault"];
//    echo $response;
?>
