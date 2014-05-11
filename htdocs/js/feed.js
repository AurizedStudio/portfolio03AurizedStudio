google.load("feeds", "1");

function initialize() {
var feed = new google.feeds.Feed("http://gplusrss.com/rss/feed/39c61e6195a3817f963a5d1f38b4e4d4508cecbe24123"); // feed URL
feed.setNumEntries(5); // エントリー数
feed.load(function(result) {
	if (!result.error) { // 正常にRSSを取得
		var container = document.getElementById("googleplus-feed"); // feed表示要素
		var htmlstr = "";
		for (var i = 0; i < result.feed.entries.length; i++) { // エントリー数分回す
			var entry = result.feed.entries[i];
			htmlstr += '<div class="inspiration-entry">';

			htmlstr += '<h4><a href="' + entry.link + '">' + entry.title + '</a></h4>';

			var pdate = new Date(entry.publishedDate); // 日付を分解して表示
			var strdate = pdate.getFullYear() + '.' + (pdate.getMonth() + 1) + '.' + pdate.getDate();
			htmlstr += '<p>' + strdate + '</p>';

			htmlstr += entry.content;

			htmlstr += '</div>';
		}
		container.innerHTML = htmlstr;
	}
	else { // 正常にRSSを取得できない場合
		htmlstr = '<div>' + result.error.code + ':' + result.error.message + '</div>';
	}
});
}
google.setOnLoadCallback(initialize); // htmlを読み終えた後にfeedを読み込みにいく
