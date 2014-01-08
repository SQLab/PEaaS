$(function() {
	$('.ul_menu li img')
	.hover(
		function(){
			$(this).stop().animate({'marginTop':'-60px'},'fast');
		},
		function () {
			$(this).stop().animate({'marginTop':'0px'},'normal');
		}
	);
});
function Ds(obj){
	$.ajax({ 
		url: 'dstar.php',
		data     : {'Dstar' : obj.id },
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
function Ps(obj){
	$.ajax({ 
		url: 'dstar.php',
		data     : {'lcov' : obj.id },
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
