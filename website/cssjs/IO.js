
function enableornot(json){
	if(json.input != "0") document.getElementById("submiti").disabled = false;
	else document.getElementById("submiti").disabled = true;
	if(json.output != "0"){ 
             document.getElementById("submito").disabled = false;
             document.getElementById("submitio").disabled = false;
        }
	else{ 
            document.getElementById("submito").disabled = true;
            document.getElementById("submitio").disabled = true;
        }
	if(json.fault != "0") document.getElementById("submitcode").disabled = false;
	else document.getElementById("submitcode").disabled = true;
}

function InputGen(json){
//alert(json);
// disable all tag
var level = document.getElementById("level").value;
//alert(level);
    if(level !== "0"){
	document.getElementById("input").disabled = true;
	document.getElementById("submiti").disabled = true;
	document.getElementById("submitio").disabled = true;
	document.getElementById("submito").disabled = true;
	document.getElementById("submitcode").disabled = true;
        $.ajax({ 
            url: 'IG.php',
            data     : {'pid' : json.pid, 'input' : json.input,'output':json.output , 'fault':json.fault ,'level':level},
            type     : 'GET',
            success: function(response){
                       //alert(response); // ------------ debug code 
                       history.go(0);
            },
            error:function(response){
               alert("error!!");
            }
        });
    }
    else{
	alert("Please Choose Level!!");
    }
}

function OutputGen(json){
// disable all tag
document.getElementById("input").disabled = true;
document.getElementById("submiti").disabled = true;
document.getElementById("submitio").disabled = true;
document.getElementById("submito").disabled = true;
document.getElementById("submitcode").disabled = true;
$("#presubmit").html('<img src="cssjs/gif/presubmit.gif" >');
	$.ajax({ 
		url: 'OG.php',
		data     : {'pid':json.pid,'input':json.input,'output':json.output,'fault':json.fault },
		type     : 'GET',
		success: function(response){
		//   alert(response); //-- debug code
		   history.go(0);
		},
		error: function(response){
		   alert("error!!");
		}
        });
}
function IOtGen(json){
// disable all tag
document.getElementById("input").disabled = true;
document.getElementById("submiti").disabled = true;
document.getElementById("submitio").disabled = true;
document.getElementById("submito").disabled = true;
document.getElementById("submitcode").disabled = true;
	$.ajax({ 
		url: 'IOG.php',
		data     : {'pid':json.pid,'input':json.input,'output':json.output,'fault':json.fault },
		type     : 'GET',
		success: function(response){
		//   alert(response); //-- debug code
		   history.go(0);
		},
		error: function(response){
		   alert("error!!");
		}
        });

}
