// portfolio slider
$(function(){
	$(".owl-carousel").owlCarousel({
		items: 1,
		nav: true,
		navText: ['前へ','次へ']
//v1		singleItem: true,
//v1		navigation: true
	});
});

// グロナビ開閉ボタン
$(function(){
	$('p.menubtn a').on('click',function(){
		$('nav.gnav').slideToggle('fast');
		return false;
	});
});
