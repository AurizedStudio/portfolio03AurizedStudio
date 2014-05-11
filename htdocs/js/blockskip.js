$(function(){
	$(".blockskip a").focus(function(){
		$(this).addClass("show");
	});
	$(".blockskip a").blur(function(){
		var scrHeight = $(this).outerHeight({margin: true});
		$(this).removeClass("show");
		window.scrollBy(0,-scrHeight);
	});
});
