#!/usr/local/bin/perl
#--- ↑ ◎Perlのパスが異なる場合は変更する。このパスはプロバイダに確認する。
#
#   アクセス解析用CGIスクリプト [アクセス・トラッカー] ver.1.0 (フリーソフト)
#   Copyright(C)1997-1999 Iwao Wada. All rights reserved.
#
#----------------------------------------------------------------------------------#
#  ここからが初期設定です（サーバーへの設置方法は同梱の'readme.txt'をご覧下さい）  #
#----------------------------------------------------------------------------------#
#
#   ●印の項目は必ず変更してください。
#　 ○印の項目は主にレイアウト関連です。基本的に変更不要です。
#　 ◎印の項目はサーバー環境によって変更する必要があります。（1行目も含みます）
#
#　''内に記述しますが、'を入れたい場合は '' を "" に変更してください。
#　なお、その場合は文字化けが生じることがあります。
#　詳しくは本サイトの解説等を参照してください。
#
#
#--------▼ 特定機能の使用に関する設定 ▼-------------------------------------------
#
#  ◎印はサーバー環境によっては正常に動作しない場合があります。
#  その場合は、その機能を無効にしてください。

$pass = 'kkiill';			# <--- ●管理者用パスワード（10文字以内の半角英数字）
$open = 0;				# <--- ○統計ページ（0：非公開／1：公開）
$lock = 1;				# <--- ◎ファイルロック機能（0：使わない／1：使う）
$jcode = 'sjis';			# <--- ○文字変換コード（sjis,jis,euc）
$max = 500;				# <--- ○1ログの最大保持件数（あまり大きくしない）

# ↓ ○ソート処理（0：しない／1：データ量が3000件以内ならばする／2：する）
$dosort = 1;
#  ソート(並び替え)処理を行いますか？ただしソート処理は処理するデータ量が多いほど、処理時間
#  を要し、サーバーに負荷をかけます。データ量が極端に多いと、タイムアウトになる場合もありま
#  す。そのことを考慮し、最大データ量($maxの値)が3000件を超えるような場合は、ソートしないよ
#  うにすること('$dosort=1'にする)を推奨します。なお、全ページについて解析する場合は、その分
#  データ量が多くなります。


#　送信ボタンを押して 'Method not implemented..' 等のエラーが出る場合は'GET'で試す。
#　なお'GET'の場合は文字制限がありますので長い文章等は途中で切れる場合があります。また、
#  フォームの入力内容がURLの後に表示されるため、セキュリティーが侵される危険性があります。
$method = 'POST';			# <--- ◎入力形式（'POST'／'GET'）


#--------▼ クッキーの設定 ▼-------------------------------------------------------
#
#  クッキーとはブラウザに保存される小さな情報です。再訪問者数のカウントに使用します。
#  全てのブラウザやサーバーで使用できるわけではありませんが、大抵の場合は大丈夫です。

$cookie = 1;				# <--- ○クッキー機能（0：使う／1：使わない）
$days = 30;				# <--- ○クッキーの有効日数（再訪問として扱う日数）

# ↓ ○この時間内の再訪問はカウントしない（単位：分／この機能を使わない場合は'0'にする）
$nocnt = 0;


#--------▼ パス/アドレス/ファイル名に関する設定 ▼---------------------------------
#
#  スクリプトと同じディレクトリの場合は、'./'です。1つ上のディレクトリは、'../'です。
#  ここでの「パス」とはサーバー内での場所 '../xxxxx' や '/home/hogehoge/public_html/' を
#	 　「アドレス」とはインターネット全体から見た場所 'http://～' を指しています。

require './template.pl';		# <--- ○Perl汎用ライブラリ"template.pl"のパス
require './jcode.pl';			# <--- ○日本語変換ライブラリ"jcode.pl"のパス
$bar = './width.gif';			# <--- ○グラフ用画像のパス/アドレス
$image = './dummy.gif';			# <--- ●ダミー画像のパス
$datadir = './data/';			# <--- ○ログファイル格納用のディレクトリのパス

# ↓ ○あなたのサイトのトップディレクトリのアドレス（サイト内からのリンクをひとまとめにする場合）
$surl = 'https://aurized-studio.jp/';

# ↓ ○あなたのサイトのトップディレクトリのアドレス（外部からの不正利用を防止する場合）
$turl = 'https://aurized-studio.jp/';
#
#  上記二項目はあなたのサイトのトップディレクトリのアドレスを指定して下さい。これは
#  本スクリプトや解析ページの上位ディレクトリを含む必要があります。多くの場合は、
#  'http://www.プロバイダ.ne.jp/~あなたのID/'です。なお、別のサーバーからも本スクリ
#  プトを利用する場合は指定しないでください。


#--------▼ デザイン等に関する設定(基本的に変更不要) ▼-----------------------------
#
#   基本的に変更の必要はありませんが、背景色やメッセージ等をサンプルとは変更したい場
#  合は変更してください。(一部の項目ではHTMLに関する基礎的な知識が必要です)

$title = 'https://aurized-studio.jp Access Analytics';		# <--- ○タイトル（<title>などで表示）
$hclr = '#FFFF80';			# <--- ○項目名の背景色
$mclr = '#CEFFCE';			# <--- ○主項目の背景色
$aclr = '#D2FFFF';			# <--- ○項目の背景色A
$bclr = '#FFFFD2';			# <--- ○項目の背景色B
$rclr = '#A0B8C8';			# <--- ○ログインページの右側背景色
$wdth = 2;				# <--- ○グラフの幅の倍率（$wdth×割合）

# ↓ ○<body>タグの設定（<>や'body'は不要です）
$body = 'text="#000000" link="#0000FF" bgcolor="#F0F0F0"';

$head=<<'HTML';
<!------ ↓ ○ヘッダー部に表示する文字列（HTML使用可能）-->

<h1 align="center">https://aurized-studio.jp Access Analytics</h1>

<!------ ↑ ここまで -->
HTML
$foot=<<'HTML';
<!------ ↓ ○フッター部に表示する文字列（HTML使用可能）-->


<!------ ↑ ここまで -->
HTML

####################################################################################
#                                                                                  #
# ・本スクリプトで初期設定が必要なのはここまでです。                               #
# ・スクリプトを改造する場合は、perlやCGIなどのそれなりの知識が必要です。          #
#                                                                                  #
####################################################################################



%FORM = &template'decode(0,0,0);
$lockfile = "$datadir" . "lock.tmp";
if (!$$) { $ps = $ENV{'REMOTE_ADDR'}; } else { $ps = $$; }
$tempfile = "$datadir$ps.tmp";
$times = &template'date('yyyy/mm/dd hh:nn');

if ($jcode eq 'euc') { $fcode = 'euc-jp'; }
elsif ($jcode eq 'sjis') { $fcode = 'Shift-jis'; }
elsif ($jcode eq 'jis') { $fcode = 'iso-2022-jp'; }
else { $fcode = $jcode; }
if ($FORM{'file'}) { &input; }
$script = "Access Tracker/1.0";
if (!$FORM{'max'}) { $end = '50'; }
else { $end = $FORM{'max'}; }

if (opendir(DIR,"$datadir")) {
	@DIR = readdir(DIR);
	closedir(DIR);
} else { &error('ディレクトリのオープンができません。'); }

$i = 0;
foreach $dir (@DIR) {
	if ($dir =~ /(.*).log/) {
		$LOGS[$i] = $1;
		$i ++;
	}
}
$i = 0;



#-------------------- 基本処理 -----------------------------------------------------

if ($FORM{'mode'} eq '' || $FORM{'mode'} eq ' 終了 ') { &start; }
elsif ($FORM{'pass'} ne $pass && $open == 0) { &error('パスワードが不正です。'); }

if (!$FORM{'type'}) { &error('解析項目を選択して下さい。'); }
elsif ($FORM{'page'} eq 'all' && $FORM{'type'} eq 'csv') { &error('解析ページを選択して下さい。'); }
elsif ($FORM{'page'} eq 'all' && $FORM{'type'} eq 'log') { &error('解析ページを選択して下さい。'); }
elsif ($FORM{'type'} eq 'reset') { &delete; }


if ($FORM{'page'} eq 'all') {
	foreach $logs (@LOGS) {
		$datafile = $datadir . $logs . ".log";
		@FILES = &template'read_file($datafile);
		if (!@FILES) { &error('ファイルのオープンができません。'); }
		shift(@FILES);
		push(@FILE,@FILES);
		
	}
	$total = $#FILE + 1;
} else {
	$datafile = $datadir . $FORM{'page'} . ".log";
	@FILE = &template'read_file($datafile);
	if (!@FILE) { &error('ファイルのオープンができません。'); }
	$total = $#FILE;
}

if ($FORM{'type'} eq 'csv') { &csv; }
if ($FORM{'page'} eq 'all') { $alls = ' selected'; }

#-------------------- 共通ヘッダー部 -----------------------------------------------

print <<"HTML";
Content-type: text/html

<html>
<head>
<title>$title</title>
<meta http-equiv="Content-Type" content="text/html; charset=$fcode">
</head>
<body $body>
$head
<form method="$method" action="log.cgi">
<input type="hidden" name="mode" value="view">
<input type="hidden" name="pass" value="$FORM{'pass'}">
  <div align="center"><center><table border="1" cellpadding="4" cellspacing="0">
    <tr>
      <td>アクセス解析 ： <select name="page" size="1">
        <option value="all"$alls>全てのページ</option>
HTML
foreach (@LOGS) {
	if ($FORM{'page'} eq $_) {
		print "        <option selected>$_</option>\n";
	} else {
		print "        <option>$_</option>\n";
	}
}
$selected{"$FORM{'type'}"} = ' selected';
$selected{"p$FORM{'max'}"} = ' selected';
print <<"HTML";
      </select><select name="type" size="1">
        <option value="date"$selected{'date'}>日付別</option>
        <option value="time"$selected{'time'}>時間別</option>
        <option value="week"$selected{'week'}>曜日別</option>
        <option value="host"$selected{'host'}>ホスト別</option>
        <option value="link"$selected{'link'}>リンク元別</option>
        <option value="page"$selected{'page'}>ページ別</option>
        <option value="agent"$selected{'agent'}>エージェント別</option>
        <option value="keyword"$selected{'keyword'}>キーワード別</option>
        <option value="log"$selected{'log'}>アクセス個別</option>
        <option value="csv">CSV形式</option>
      </select><select name="max" size="1">
        <option value="10"$selected{'p10'}>10件</option>
        <option value="20"$selected{'p20'}>20件</option>
        <option value="50"$selected{'p50'}>50件</option>
        <option value="100"$selected{'p100'}>100件</option>
        <option value="200"$selected{'p200'}>200件</option>
        <option value="300"$selected{'p300'}>300件</option>
        <option value="400"$selected{'p400'}>400件</option>
        <option value="500"$selected{'p500'}>500件</option>
      </select> <input type="submit" value="　 \OK 　"></td>
      <td> <input type="submit" name="mode" value=" 終了 "></td>
    </tr>
  </table>
  </center></div>
</form>
HTML

#-------------------- 各種ログの集計 -----------------------------------------------

if ($FORM{'type'} eq 'page') { &page_view; }
if ($FORM{'page'} ne 'all') { $logdata = shift(@FILE); }
if ($FORM{'type'} eq 'log') { &log_view; }
foreach $file (@FILE) {
	($date,$week,$time,$host,$link,$agent,$keyword,$again) = split(/,/, $file);
	if ($FORM{'type'} eq 'date') {
		($date,$time) = split(/ /, $date);
		$VST{"$date"} ++;
		if ($again != 0) { $REP{"$date"} ++; }
	} elsif ($FORM{'type'} eq 'week') {
		$VST{"$week"} ++;
		if ($again != 0) { $REP{"$week"} ++; }
	} elsif ($FORM{'type'} eq 'time') {
		$VST{"$time"} ++;
		if ($again != 0) { $REP{"$time"} ++; }
	} elsif ($FORM{'type'} eq 'host') {
		$VST{"$host"} ++;
		if ($again != 0) { $REP{"$host"} ++; }
	} elsif ($FORM{'type'} eq 'link') {
		if ($link =~ /$surl/ && $surl ne '') { $VST{'(local)'} ++; }
		else { $VST{"$link"} ++; }
		if ($again != 0) { $REP{"$link"} ++; }
	} elsif ($FORM{'type'} eq 'agent') {
		$VST{"$agent"} ++;
		if ($again != 0) { $REP{"$agent"} ++; }
	} elsif ($FORM{'type'} eq 'keyword') {
		$VST{"$keyword"} ++;
		if ($again != 0) { $REP{"$keyword"} ++; }
	}
}
while (($name,$value) = each(%VST)) {
	$DATA[$i] = "$name,$value,$REP{\"$name\"}";
	$i ++;
}

if ($dosort == 2) { $sortok = 1; }
elsif ($dosort == 1 && $#DATA < 3000) { $sortok = 1; }

if ($sortok) {
	if ($FORM{'type'} eq 'host' || $FORM{'type'} eq 'agent' || $FORM{'type'} eq 'link' || $FORM{'type'} eq 'keyword') {
		foreach $sorts (@DATA) {
			($name,$visit,$report) = split(/,/, $sorts);
			$visits = sprintf("%03d",$visit);
			push(@TMP ,"$visits,$sorts");
		} foreach $sorts (sort @TMP) {
			($visits,@NOW) = split(/\,/, $sorts);
			push(@NEW, join(',', @NOW));
		}
		@DATA = reverse(@NEW);
	} elsif ($FORM{'type'} eq 'date') {
		foreach $sorts (@DATA) {
			($name,$visit,$report) = split(/,/, $sorts);
			$name =~ s/\///g;
			$names = sprintf("%03d",$name);
			push(@TMP ,"$visits,$sorts");
		} foreach $sorts (sort @TMP) {
			($names,@NOW) = split(/\,/, $sorts);
			push(@NEW, join(',', @NOW));
		}
		@DATA = @NEW;
	}
}

#-------------------- 条件分岐 -----------------------------------------------------

if ($FORM{'type'} eq 'date') { &date_view; }
elsif ($FORM{'type'} eq 'week') { &week_view; }
elsif ($FORM{'type'} eq 'time') { &time_view; }
elsif ($FORM{'type'} eq 'host') { &host_view; }
elsif ($FORM{'type'} eq 'link') { &link_view; }
elsif ($FORM{'type'} eq 'agent') { &agent_view; }
elsif ($FORM{'type'} eq 'keyword') { &keyword_view; }
else { &error; }


#==================== 日付別統計 ===================================================

sub date_view {
	
	($logpage,$startday) = split(/,/, $logdata);
	if ($FORM{'page'} eq 'all') { $logpage = '&lt;全ページ&gt;'; }
	else { $logpage = "<a href=\"$logpage\">$logpage</a>"; }
	($sday,$a,$b,$c,$d,$e,$f,$g) = split(/,/, $DATA[$#DATA]);
	
	print "<h2 align=\"center\">日付別アクセス統計</h2>\n";
	print "<p align=\"center\">$logpage</p>\n";
	print "<p align=\"center\"><small><i>統計期間 $sday ～ $times　（累計 $total回）</i></small></p>\n";
	print "<div align=\"center\"><center>\n";
	print "<table border=\"3\" cellpadding=\"3\" cellspacing=\"3\" width=\"80%\">\n";
	print "  <tr>\n";
	print "    <td width=\"30%\" align=\"center\" bgcolor=\"$hclr\"><b>日付</b></td>\n";
	print "    <td width=\"20%\" align=\"center\" bgcolor=\"$hclr\"><b>ヒット数</b></td>\n";
	print "    <td width=\"50%\" align=\"center\" bgcolor=\"$hclr\"><b>グラフ</b></td>\n";
	print "  </tr>\n";
	
	@DATA = reverse(@DATA);
	for ($j = 0; $j < $end; $j ++) {
		($name,$count,$repert) = split(/,/, $DATA[$j]);
		if (!$repert) { $repert = 0; }
		if (!$DATA[$j]) { last; }
		$crate = $count * 100 / $total;
		$crate = sprintf("%.2f",$crate);
		if ($crate == 0 ) { $grate = 1; }
		elsif ($crate < 1) { $grate = 2; }
		else { $grate = $crate * $wdth; }
		
		$rrate = $repert * 100 / $total;
		$rrate = sprintf("%.2f",$rrate);
		if ($rrate == 0 ) { $grrat = 1; }
		elsif ($rrate < 1) { $grrat = 2; }
		else { $grrat = $rrate * $wdth; }
		$grrat = sprintf("%d",$grrat);
		($date,$time) = split(/ /, $name);
		
		print "  <tr>\n";
		print "    <td rowspan=\"2\" width=\"30%\" align=\"center\" bgcolor=\"$mclr\">$date</td>\n";
		print "    <td width=\"20%\" align=\"center\" bgcolor=\"$aclr\">$count <small>($crate%)</small></td>\n";
		print "    <td width=\"50%\" bgcolor=\"$aclr\"><img src=\"$bar\" width=\"$grate\" height=\"15\"></td>\n";
		print "  </tr>\n";
		print "  <tr>\n";
		print "    <td width=\"20%\" align=\"center\" bgcolor=\"$bclr\">$repert <small>($rrate%)</small></td>\n";
		print "    <td width=\"50%\" bgcolor=\"$bclr\"><img src=\"$bar\" width=\"$grrat\" height=\"15\"></td>\n";
		print "  </tr>\n";
	}
	print "</table>\n";
	print "</center></div>\n";
	print "<p align=\"center\">統計は最近<b>$end</b>日以内を表\示しています。下段は$days日以内の再訪問者数です。</p>\n";
	print "<hr noshade>\n";
	print "$foot";
	print "</body>\n";
	print "</html>\n";
	exit;
}

#==================== 曜日別統計 ===================================================

sub week_view {
	
	($logpage,$startday) = split(/,/, $logdata);
	if ($FORM{'page'} eq 'all') { $logpage = '&lt;全ページ&gt;'; }
	else { $logpage = "<a href=\"$logpage\">$logpage</a>"; }
	($sday,$a,$b,$c,$d,$e,$f,$g) = split(/,/, $FILE[$#FILE]);
	
	@LOG = ('日,0,0','月,0,0','火,0,0','水,0,0','木,0,0','金,0,0','土,0,0');
	foreach (@DATA) {
		($name,$count,$repert) = split(/,/, $_);
		if ($name eq '日') { $LOG[0] = "$name,$count,$repert"; }
		elsif ($name eq '月') { $LOG[1] = "$name,$count,$repert"; }
		elsif ($name eq '火') { $LOG[2] = "$name,$count,$repert"; }
		elsif ($name eq '水') { $LOG[3] = "$name,$count,$repert"; }
		elsif ($name eq '木') { $LOG[4] = "$name,$count,$repert"; }
		elsif ($name eq '金') { $LOG[5] = "$name,$count,$repert"; }
		elsif ($name eq '土') { $LOG[6] = "$name,$count,$repert"; }
	}
	
	print "<h2 align=\"center\">曜日別アクセス統計</h2>\n";
	print "<p align=\"center\">$logpage</p>\n";
	print "<p align=\"center\"><small><i>統計期間 $sday ～ $times　（累計 $total回）</i></small></p>\n";
	print "<div align=\"center\"><center>\n";
	print "<table border=\"3\" cellpadding=\"3\" cellspacing=\"3\" width=\"80%\">\n";
	print "  <tr>\n";
	print "    <td width=\"30%\" align=\"center\" bgcolor=\"$hclr\"><b>ページ</b></td>\n";
	print "    <td width=\"20%\" align=\"center\" bgcolor=\"$hclr\"><b>ヒット数</b></td>\n";
	print "    <td width=\"50%\" align=\"center\" bgcolor=\"$hclr\"><b>グラフ</b></td>\n";
	print "  </tr>\n";
	
	foreach (@LOG) {
		($name,$count,$repert) = split(/,/, $_);
		if (!$repert) { $repert = 0; }
		$crate = $count * 100 / $total;
		$crate = sprintf("%.2f",$crate);
		if ($crate == 0 ) { $grate = 1; }
		elsif ($crate < 1) { $grate = 2; }
		else { $grate = $crate * $wdth; }
		
		$rrate = $repert * 100 / $total;
		$rrate = sprintf("%.2f",$rrate);
		if ($rrate == 0 ) { $grrat = 1; }
		elsif ($rrate < 1) { $grrat = 2; }
		else { $grrat = $rrate * $wdth; }
		$grrat = sprintf("%d",$grrat);
		
		print "  <tr>\n";
		print "    <td rowspan=\"2\" width=\"30%\" align=\"center\" bgcolor=\"$mclr\">$name曜日</td>\n";
		print "    <td width=\"20%\" align=\"center\" bgcolor=\"$aclr\">$count <small>($crate%)</small></td>\n";
		print "    <td width=\"50%\" bgcolor=\"$aclr\"><img src=\"$bar\" width=\"$grate\" height=\"15\"></td>\n";
		print "  </tr>\n";
		print "  <tr>\n";
		print "    <td width=\"20%\" align=\"center\" bgcolor=\"$bclr\">$repert <small>($rrate%)</small></td>\n";
		print "    <td width=\"50%\" bgcolor=\"$bclr\"><img src=\"$bar\" width=\"$grrat\" height=\"15\"></td>\n";
		print "  </tr>\n";
	}
	print "</table>\n";
	print "</center></div>\n";
	print "<p align=\"center\">下段は$days日以内の再訪問者数です。</p>\n";
	print "<hr noshade>\n";
	print "$foot";
	print "</body>\n";
	print "</html>\n";
	exit;
}

#==================== 時間別統計 ===================================================

sub time_view {
	
	($logpage,$startday) = split(/,/, $logdata);
	if ($FORM{'page'} eq 'all') { $logpage = '&lt;全ページ&gt;'; }
	else { $logpage = "<a href=\"$logpage\">$logpage</a>"; }
	($sday,$a,$b,$c,$d,$e,$f,$g) = split(/,/, $FILE[$#FILE]);
	
	for ($i = 0; $i < 24; $i ++) { $LOG[$i] = "$i,0,0"; }
	foreach (@DATA) {
		($name,$count,$repert) = split(/,/, $_);
		$LOG[$name] = "$name,$count,$repert";
	}
	
	print "<h2 align=\"center\">時間別アクセス統計</h2>\n";
	print "<p align=\"center\">$logpage</p>\n";
	print "<p align=\"center\"><small><i>統計期間 $sday ～ $times　（累計 $total回）</i></small></p>\n";
	print "<div align=\"center\"><center>\n";
	print "<table border=\"3\" cellpadding=\"3\" cellspacing=\"3\" width=\"80%\">\n";
	print "  <tr>\n";
	print "    <td width=\"30%\" align=\"center\" bgcolor=\"$hclr\"><b>時間</b></td>\n";
	print "    <td width=\"20%\" align=\"center\" bgcolor=\"$hclr\"><b>ヒット数</b></td>\n";
	print "    <td width=\"50%\" align=\"center\" bgcolor=\"$hclr\"><b>グラフ</b></td>\n";
	print "  </tr>\n";
	
	$i = 0;
	foreach (@LOG) {
		($name,$count,$repert) = split(/,/, $_);
		if (!$repert) { $repert = 0; }
		$crate = $count * 100 / $total;
		$crate = sprintf("%.2f",$crate);
		if ($crate == 0 ) { $grate = 1; }
		elsif ($crate < 1) { $grate = 2; }
		else { $grate = $crate * $wdth; }
		
		$rrate = $repert * 100 / $total;
		$rrate = sprintf("%.2f",$rrate);
		if ($rrate == 0 ) { $grrat = 1; }
		elsif ($rrate < 1) { $grrat = 2; }
		else { $grrat = $rrate * $wdth; }
		$grrat = sprintf("%d",$grrat);
		
		if (!$count) { $count = 0; }
		
		print "  <tr>\n";
		print "    <td rowspan=\"2\" width=\"25%\" align=\"center\" bgcolor=\"$mclr\">$i時</td>\n";
		print "    <td width=\"20%\" align=\"center\" bgcolor=\"$aclr\">$count <small>($crate%)</small></td>\n";
		print "    <td width=\"55%\" bgcolor=\"$aclr\"><img src=\"$bar\" width=\"$grate\" height=\"15\"></td>\n";
		print "  </tr>\n";
		print "  <tr>\n";
		print "    <td width=\"20%\" align=\"center\" bgcolor=\"$bclr\">$repert <small>($rrate%)</small></td>\n";
		print "    <td width=\"55%\" bgcolor=\"$bclr\"><img src=\"$bar\" width=\"$grrat\" height=\"15\"></td>\n";
		print "  </tr>\n";
		$i ++;
	}
	print "</table>\n";
	print "</center></div>\n";
	print "<p align=\"center\">下段は$days日以内の再訪問者数です。</p>\n";
	print "<hr noshade>\n";
	print "$foot";
	print "</body>\n";
	print "</html>\n";
	exit;
}

#==================== ホスト別統計 =================================================

sub host_view {
	
	($logpage,$startday) = split(/,/, $logdata);
	if ($FORM{'page'} eq 'all') { $logpage = '&lt;全ページ&gt;'; }
	else { $logpage = "<a href=\"$logpage\">$logpage</a>"; }
	($sday,$a,$b,$c,$d,$e,$f,$g) = split(/,/, $FILE[$#FILE]);
	
	print "<h2 align=\"center\">ホスト別アクセス統計</h2>\n";
	print "<p align=\"center\">$logpage</p>\n";
	print "<p align=\"center\"><small><i>統計期間 $sday ～ $times　（累計 $total回）</i></small></p>\n";
	print "<div align=\"center\"><center>\n";
	print "<table border=\"3\" cellpadding=\"3\" cellspacing=\"3\" width=\"80%\">\n";
	print "  <tr>\n";
	print "    <td width=\"30%\" align=\"center\" bgcolor=\"$hclr\"><b>ホスト</b></td>\n";
	print "    <td width=\"20%\" align=\"center\" bgcolor=\"$hclr\"><b>ヒット数</b></td>\n";
	print "    <td width=\"50%\" align=\"center\" bgcolor=\"$hclr\"><b>グラフ</b></td>\n";
	print "  </tr>\n";
	
	for ($j = 0; $j < $end; $j ++) {
		($name,$count,$repert) = split(/,/, $DATA[$j]);
		if (!$repert) { $repert = 0; }
		if (!$DATA[$j]) { last; }
		$crate = $count * 100 / $total;
		$crate = sprintf("%.2f",$crate);
		if ($crate == 0 ) { $grate = 1; }
		elsif ($crate < 1) { $grate = 2; }
		else { $grate = $crate * $wdth; }
		
		$rrate = $repert * 100 / $total;
		$rrate = sprintf("%.2f",$rrate);
		if ($rrate == 0 ) { $grrat = 1; }
		elsif ($rrate < 1) { $grrat = 2; }
		else { $grrat = $rrate * $wdth; }
		$grrat = sprintf("%d",$grrat);
		
		print "  <tr>\n";
		print "    <td rowspan=\"2\" width=\"30%\" align=\"center\" bgcolor=\"$mclr\">$name</td>\n";
		print "    <td width=\"20%\" align=\"center\" bgcolor=\"$aclr\">$count <small>($crate%)</small></td>\n";
		print "    <td width=\"50%\" bgcolor=\"$aclr\"><img src=\"$bar\" width=\"$grate\" height=\"15\"></td>\n";
		print "  </tr>\n";
		print "  <tr>\n";
		print "    <td width=\"20%\" align=\"center\" bgcolor=\"$bclr\">$repert <small>($rrate%)</small></td>\n";
		print "    <td width=\"50%\" bgcolor=\"$bclr\"><img src=\"$bar\" width=\"$grrat\" height=\"15\"></td></td>\n";
		print "  </tr>\n";
	}
	print "</table>\n";
	print "</center></div>\n";
	print "<p align=\"center\">統計は上位<b>$end</b>件を表\示しています。下段は$days日以内の再訪問者数です。</p>\n";
	print "<hr noshade>\n";
	print "$foot";
	print "</body>\n";
	print "</html>\n";
	exit;
}

#==================== エージェント別統計 ===========================================

sub agent_view {
	
	($logpage,$startday) = split(/,/, $logdata);
	if ($FORM{'page'} eq 'all') { $logpage = '&lt;全ページ&gt;'; }
	else { $logpage = "<a href=\"$logpage\">$logpage</a>"; }
	($sday,$a,$b,$c,$d,$e,$f,$g) = split(/,/, $FILE[$#FILE]);
	
	print "<h2 align=\"center\">エージェント別アクセス統計</h2>\n";
	print "<p align=\"center\">$logpage</p>\n";
	print "<p align=\"center\"><small><i>統計期間 $sday ～ $times　（累計 $total回）</i></small></p>\n";
	print "<div align=\"center\"><center>\n";
	print "<table border=\"3\" cellpadding=\"3\" cellspacing=\"3\" width=\"80%\">\n";
	print "  <tr>\n";
	print "    <td width=\"30%\" align=\"center\" bgcolor=\"$hclr\"><b>エージェント</b></td>\n";
	print "    <td width=\"20%\" align=\"center\" bgcolor=\"$hclr\"><b>ヒット数</b></td>\n";
	print "    <td width=\"50%\" align=\"center\" bgcolor=\"$hclr\"><b>グラフ</b></td>\n";
	print "  </tr>\n";
	
	for ($j = 0; $j < $end; $j ++) {
		($name,$count,$repert) = split(/,/, $DATA[$j]);
		if (!$repert) { $repert = 0; }
		if (!$DATA[$j]) { last; }
		$crate = $count * 100 / $total;
		$crate = sprintf("%.2f",$crate);
		if ($crate == 0 ) { $grate = 1; }
		elsif ($crate < 1) { $grate = 2; }
		else { $grate = $crate * $wdth; }
		
		$rrate = $repert * 100 / $total;
		$rrate = sprintf("%.2f",$rrate);
		if ($rrate == 0 ) { $grrat = 1; }
		elsif ($rrate < 1) { $grrat = 2; }
		else { $grrat = $rrate * $wdth; }
		
		$grrat = sprintf("%d",$grrat);
		
		print "  <tr>\n";
		print "    <td rowspan=\"2\" width=\"30%\" align=\"center\" bgcolor=\"$mclr\">$name</td>\n";
		print "    <td width=\"20%\" align=\"center\" bgcolor=\"$aclr\">$count <small>($crate%)</small></td>\n";
		print "    <td width=\"50%\" bgcolor=\"$aclr\"><img src=\"$bar\" width=\"$grate\" height=\"15\"></td>\n";
		print "  </tr>\n";
		print "  <tr>\n";
		print "    <td width=\"20%\" align=\"center\" bgcolor=\"$bclr\">$repert <small>($rrate%)</small></td>\n";
		print "    <td width=\"50%\" bgcolor=\"$bclr\"><img src=\"$bar\" width=\"$grrat\" height=\"15\"></td></td>\n";
		print "  </tr>\n";
	}
	print "</table>\n";
	print "</center></div>\n";
	print "<p align=\"center\">統計は上位<b>$end</b>件を表\示しています。下段は$days日以内の再訪問者数です。</p>\n";
	print "<hr noshade>\n";
	print "$foot";
	print "</body>\n";
	print "</html>\n";
	exit;
}

#==================== リンク元別統計 ===============================================

sub link_view {
	
	($logpage,$startday) = split(/,/, $logdata);
	if ($FORM{'page'} eq 'all') { $logpage = '&lt;全ページ&gt;'; }
	else { $logpage = "<a href=\"$logpage\">$logpage</a>"; }
	($sday,$a,$b,$c,$d,$e,$f,$g) = split(/,/, $FILE[$#FILE]);
	
	print "<h2 align=\"center\">リンク元別アクセス統計</h2>\n";
	print "<p align=\"center\">$logpage</p>\n";
	print "<p align=\"center\"><small><i>統計期間 $sday ～ $times　（累計 $total回）</i></small></p>\n";
	print "<div align=\"center\"><center>\n";
	print "<table border=\"3\" cellpadding=\"3\" cellspacing=\"3\" width=\"80%\">\n";
	print "  <tr>\n";
	print "    <td width=\"30%\" align=\"center\" bgcolor=\"$hclr\"><b>リンク元</b></td>\n";
	print "    <td width=\"20%\" align=\"center\" bgcolor=\"$hclr\"><b>ヒット数</b></td>\n";
	print "    <td width=\"50%\" align=\"center\" bgcolor=\"$hclr\"><b>グラフ</b></td>\n";
	print "  </tr>\n";
	
	for ($j = 0; $j < $end; $j ++) {
		($name,$count,$repert) = split(/,/, $DATA[$j]);
		if (!$DATA[$j]) { last; }
		if (!$repert) { $repert = 0; }
		$crate = $count * 100 / $total;
		$crate = sprintf("%.2f",$crate);
		if ($crate == 0 ) { $grate = 1; }
		elsif ($crate < 1) { $grate = 2; }
		else { $grate = $crate * $wdth; }
		
		$rrate = $repert * 100 / $total;
		$rrate = sprintf("%.2f",$rrate);
		if ($rrate == 0 ) { $grrat = 1; }
		elsif ($rrate < 1) { $grrat = 2; }
		else { $grrat = $rrate * $wdth; }
		$grrat = sprintf("%d",$grrat);
		
		print "  <tr>\n";
		print "    <td rowspan=\"2\" width=\"30%\" align=\"center\" bgcolor=\"$mclr\">\n";
		if (!$name) {
			print "    <small>(other)</small></td>\n";
		} elsif ($name =~ /^http/i && $method eq 'POST') {
			print "    <small><a href=\"$name\" target=\"_blank\">$name</a></small></td>\n";
		} else {
			print "    <small>$name</small></td>\n";
		}
		print "    <td width=\"20%\" align=\"center\" bgcolor=\"$aclr\">$count <small>($crate%)</small></td>\n";
		print "    <td width=\"50%\" bgcolor=\"$aclr\"><img src=\"$bar\" width=\"$grate\" height=\"15\"></td>\n";
		print "  </tr>\n";
		print "  <tr>\n";
		print "    <td width=\"20%\" align=\"center\" bgcolor=\"$bclr\">$repert <small>($rrate%)</small></td>\n";
		print "    <td width=\"50%\" bgcolor=\"$bclr\"><img src=\"$bar\" width=\"$grrat\" height=\"15\"></td></td>\n";
		print "  </tr>\n";
	}
	print "</table>\n";
	print "</center></div>\n";
	print "<p align=\"center\">統計は上位<b>$end</b>件を表\示しています。下段は$days日以内の再訪問者数です。</p>\n";
	print "<hr noshade>\n";
	print "$foot";
	print "</body>\n";
	print "</html>\n";
	exit;
}

#==================== キーワード別統計 =============================================

sub keyword_view {
	
	($logpage,$startday) = split(/,/, $logdata);
	if ($FORM{'page'} eq 'all') { $logpage = '&lt;全ページ&gt;'; }
	else { $logpage = "<a href=\"$logpage\">$logpage</a>"; }
	($sday,$a,$b,$c,$d,$e,$f,$g) = split(/,/, $FILE[$#FILE]);
	
	print "<h2 align=\"center\">キーワード別アクセス統計</h2>\n";
	print "<p align=\"center\">$logpage</p>\n";
	print "<p align=\"center\"><small><i>統計期間 $sday ～ $times　（累計 $total回）</i></small></p>\n";
	print "<div align=\"center\"><center>\n";
	print "<table border=\"3\" cellpadding=\"3\" cellspacing=\"3\" width=\"80%\">\n";
	print "  <tr>\n";
	print "    <td width=\"30%\" align=\"center\" bgcolor=\"$hclr\"><b>キーワード</b></td>\n";
	print "    <td width=\"20%\" align=\"center\" bgcolor=\"$hclr\"><b>ヒット数</b></td>\n";
	print "    <td width=\"50%\" align=\"center\" bgcolor=\"$hclr\"><b>グラフ</b></td>\n";
	print "  </tr>\n";
	
	for ($j = 0; $j < $end; $j ++) {
		($name,$count,$repert) = split(/,/, $DATA[$j]);
		if (!$DATA[$j]) { last; }
		if (!$repert) { $repert = 0; }
		$crate = $count * 100 / $total;
		$crate = sprintf("%.2f",$crate);
		if ($crate == 0 ) { $grate = 1; }
		elsif ($crate < 1) { $grate = 2; }
		else { $grate = $crate * $wdth; }
		
		$rrate = $repert * 100 / $total;
		$rrate = sprintf("%.2f",$rrate);
		if ($rrate == 0 ) { $grrat = 1; }
		elsif ($rrate < 1) { $grrat = 2; }
		else { $grrat = $rrate * $wdth; }
		
		$grrat = sprintf("%d",$grrat);
		
		if (!$name) { $name = '<small>(other)</small>'; }
		
		print "  <tr>\n";
		print "    <td rowspan=\"2\" width=\"30%\" align=\"center\" bgcolor=\"$mclr\">$name</td>\n";
		print "    <td width=\"20%\" align=\"center\" bgcolor=\"$aclr\">$count <small>($crate%)</small></td>\n";
		print "    <td width=\"50%\" bgcolor=\"$aclr\"><img src=\"$bar\" width=\"$grate\" height=\"15\"></td>\n";
		print "  </tr>\n";
		print "  <tr>\n";
		print "    <td width=\"20%\" align=\"center\" bgcolor=\"$bclr\">$repert <small>($rrate%)</small></td>\n";
		print "    <td width=\"50%\" bgcolor=\"$bclr\"><img src=\"$bar\" width=\"$grrat\" height=\"15\"></td></td>\n";
		print "  </tr>\n";
	}
	print "</table>\n";
	print "</center></div>\n";
	print "<p align=\"center\">統計は上位<b>$end</b>件を表\示しています。下段は$days日以内の再訪問者数です。</p>\n";
	print "<hr noshade>\n";
	print "$foot";
	print "</body>\n";
	print "</html>\n";
	exit;
}

#==================== アクセス個別統計 =============================================

sub log_view {
	
	($logpage,$startday) = split(/,/, $logdata);
	$logpage = "<a href=\"$logpage\">$logpage</a>";
	($sday,$a,$b,$c,$d,$e,$f,$g) = split(/,/, $FILE[$#FILE]);
	
	print "<h2 align=\"center\">個別アクセス統計</h2>\n";
	print "<p align=\"center\">$logpage</p>\n";
	print "<p align=\"center\"><small><i>統計期間 $sday ～ $times　（累計 $total回）</i></small></p>\n";
	print "<div align=\"center\"><center>\n";
	print "<table border=\"3\" cellpadding=\"3\" cellspacing=\"3\" width=\"100%\">\n";
	print "  <tr>\n";
	print "    <td align=\"center\" bgcolor=\"$hclr\"><b>訪問日</b></td>\n";
	print "    <td align=\"center\" bgcolor=\"$hclr\"><b>前回訪問日</b></td>\n";
	print "    <td align=\"center\" bgcolor=\"$hclr\"><b>ホスト</b></td>\n";
	print "    <td align=\"center\" bgcolor=\"$hclr\"><b>エージェント</b></td>\n";
	print "    <td align=\"center\" bgcolor=\"$hclr\"><b>リンク元</b></td>\n";
	print "  </tr>\n";
	
	$i = 0;
	for ($j = 0; $j < $end; $j ++) {
		($date,$a,$b,$host,$link,$agent,$keyword,$befo) = split(/,/, $FILE[$j]);
		if (!$FILE[$j]) { last; }
		if ($aclr eq $bgclr) { $bgclr = $bclr; }
		else { $bgclr = $aclr; }
		if ($befo == 0) { $befo = '-'; }
		print "  <tr>\n";
		print "    <td align=\"center\" bgcolor=\"$bgclr\"><small>$date</small></td>\n";
		print "    <td align=\"center\" bgcolor=\"$bgclr\"><small>$befo</small></td>\n";
		print "    <td align=\"center\" bgcolor=\"$bgclr\"><small>$host</small></td>\n";
		print "    <td bgcolor=\"$bgclr\"><small>$agent</small></td>\n";
		if (!$link) {
			print "    <td bgcolor=\"$bgclr\" align=\"center\"><small>(other)</small></td>\n";
		} elsif ($link =~ /^http/i && $method eq 'POST') {
			print "    <td bgcolor=\"$bgclr\"><small><a href=\"$link\" target=\"_blank\">$link</a></small></td>\n";
		} else {
			print "    <td bgcolor=\"$bgclr\"><small>$link</small></td>\n";
		}
		print "  </tr>\n";
	}
	print "</table>\n";
	print "</center></div>\n";
	print "<p align=\"center\">統計は最近のアクセス<b>$end</b>件を表\示しています。</p>\n";
	print "<hr noshade>\n";
	print "$foot";
	print "</body>\n";
	print "</html>\n";
	exit;
}

#==================== ページ別統計 =================================================

sub page_view {
	
	$i = 0;
	$total = 0;
	$repert = 0;
	foreach $dir (@DIR) {
		if ($dir =~ /(.*).log/) {
			@FILE = &template'read_file("$datadir$dir");
			($logpage,$startday) = split(/,/, $FILE[0]);
			shift(@FILE);
			foreach (@FILE) {
				($s,$a,$b,$c,$d,$e,$f,$rep) = split(/,/, $_);
				if ($rep != 0) { $repert ++; }
			}
			$totalhit = $#FILE + 1;
			$DATA[$i] = "$logpage,$totalhit,$repert";
			$total = $total + $totalhit;
			$i ++;
		}
	}
	
	foreach $sorts (@DATA) {
		($name,$visit,$report) = split(/,/, $sorts);
		$visits = sprintf("%03d",$visit);
		push(@TMP ,"$visits,$sorts");
	} foreach $sorts (sort @TMP) {
		($visits,@NOW) = split(/\,/, $sorts);
		push(@NEW, join(',', @NOW));
	}
	@DATA = reverse(@NEW);
	
	print "<h2 align=\"center\">ページ別アクセス統計</h2>\n";
	print "<p align=\"center\"><small><i>統計期間 $sday ～ $times　（累計 $total回）</i></small></p>\n";
	print "<div align=\"center\"><center>\n";
	print "<table border=\"3\" cellpadding=\"3\" cellspacing=\"3\" width=\"80%\">\n";
	print "  <tr>\n";
	print "    <td width=\"30%\" align=\"center\" bgcolor=\"$hclr\"><b>ページ</b></td>\n";
	print "    <td width=\"20%\" align=\"center\" bgcolor=\"$hclr\"><b>ヒット数</b></td>\n";
	print "    <td width=\"50%\" align=\"center\" bgcolor=\"$hclr\"><b>グラフ</b></td>\n";
	print "  </tr>\n";
	
	$i = 0;
	for ($j = 0; $j < $end; $j ++) {
		($name,$count,$repert) = split(/,/, $DATA[$j]);
		if (!$DATA[$j]) { last; }
		if (!$repert) { $repert = 0; }
		$crate = $count * 100 / $total;
		$crate = sprintf("%.2f",$crate);
		if ($crate == 0 ) { $grate = 1; }
		elsif ($crate < 1) { $grate = 2; }
		else { $grate = $crate * $wdth; }
		
		$rrate = $repert * 100 / $total;
		$rrate = sprintf("%.2f",$rrate);
		if ($rrate == 0 ) { $grrat = 1; }
		elsif ($rrate < 1) { $grrat = 2; }
		else { $grrat = $rrate * $wdth; }
		$grrat = sprintf("%d",$grrat);
		
		if (!$name) { $name = '(other)'; }
		print "  <tr>\n";
		print "    <td rowspan=\"2\" width=\"30%\" align=\"center\" bgcolor=\"$mclr\"><small><a \n";
		print "    href=\"$name\" target=\"_blank\">$name</small></td>\n";
		print "    <td width=\"20%\" align=\"center\" bgcolor=\"$aclr\">$count <small>($crate%)</small></td>\n";
		print "    <td width=\"50%\" bgcolor=\"$aclr\"><img src=\"$bar\" width=\"$grate\" height=\"15\"></td>\n";
		print "  </tr>\n";
		print "  <tr>\n";
		print "    <td width=\"20%\" align=\"center\" bgcolor=\"$bclr\">$repert <small>($rrate%)</small></td>\n";
		print "    <td width=\"50%\" bgcolor=\"$bclr\"><img src=\"$bar\" width=\"$grrat\" height=\"15\"></td></td>\n";
		print "  </tr>\n";
	}
	print "</table>\n";
	print "</center></div>\n";
	print "<p align=\"center\">統計は上位<b>$end</b>件を表\示しています。下段は$days日以内の再訪問者数です。</p>\n";
	print "<hr noshade>\n";
	print "$foot";
	print "</body>\n";
	print "</html>\n";
	exit;
}

#==================== CSV形式で出力 ================================================

sub csv {
	shift(@FILE);
	unshift(@FILE,"日付,曜日,時間,ホスト,リンク元,エージェント,キーワード,前回訪問日\n");
	$j = 0;
	print "Content-type: text/plain\n\n";
	foreach (@FILE) {
		if ($j > $end) { last; }
		print $_;
		$j ++;
	}
	exit;
}

#==================== スタートページ ===============================================

sub start {

print <<"HTML";
Content-type: text/html

<html>
<head>
<title>$title</title>
<meta http-equiv="Content-Type" content="text/html; charset=$fcode">
</head>
<body $body>
$head
<hr noshade size="1" width="65%">
<form method="POST" action="./log.cgi" name="loginForm">
<input type="hidden" name="mode" value="view">
  <div align="center"><center><table border="0" cellpadding="2" width="60%" cellspacing="0">
    <tr>
      <td align="right" width="40%"><h2>解析対象を</h2>
      <p>　</td>
      <td bgcolor="$rclr" width="60%"><h2>選択してください</h2>
      <p>　</td>
    </tr>
    <tr>
      <td align="right" width="40%"><small>解析ページ ：</small></td>
      <td bgcolor="$rclr" width="60%"><select name="page" size="1">
        <option value="all">全てのページ</option>
HTML
	foreach (@LOGS) {
		print "        <option>$_</option>\n";
	}
	if ($open) { $psmsg = '      <tr><td align="right" width="40%"><small>パスワードは</small></td>' .
	                      "      <td bgcolor=\"$rclr\" width=\"60%\"><small>ログをリセットする場合のみ入力</small></td></tr>" }
print <<"HTML";
      </select></td>
    </tr>
    <tr>
      <td align="right" width="40%"><small>解析項目 ：</small></td>
      <td bgcolor="$rclr" width="60%"><select name="type" size="1">
        <option value="date">日付別</option>
        <option value="time">時間別</option>
        <option value="week">曜日別</option>
        <option value="host">ホスト別</option>
        <option value="link">リンク元別</option>
        <option value="page">ページ別</option>
        <option value="agent">エージェント別</option>
        <option value="keyword">キーワード別</option>
        <option value="log">アクセス個別</option>
        <option value="csv">CSV形式</option>
        <option value="0">------------</option>
        <option value="reset">ログのリセット</option>
      </select></td>
    </tr>
    <tr>
      <td align="right" width="40%"><small>表\示件数 ：</small></td>
      <td bgcolor="$rclr" width="60%"><select name="max" size="1">
        <option value="10">10件</option>
        <option value="20">20件</option>
        <option value="50" selected>50件</option>
        <option value="100">100件</option>
        <option value="200">200件</option>
        <option value="300">300件</option>
        <option value="400">400件</option>
        <option value="500">500件</option>
      </select></td>
    </tr>
    <tr>
      <td align="right" width="40%"><small>パスワード ：</small></td>
      <td bgcolor="$rclr" width="60%"><input type="password" name="pass" size="20" maxlength="10"></td>
    </tr>
    <tr>
      <td align="right" width="40%"><br>
      </td>
      <td bgcolor="$rclr" width="60%">　　<br>
      <input type="submit" value="　 \OK 　"><input type="reset" value="×"><br>
      　　</td>
    </tr>
    $psmsg
  </table>
  </center></div>
</form>
<hr noshade size="1" width="65%">
<script language="JavaScript">
<!--
    document.loginForm.pass.value = "";
// -->
</script>
<h5 align="right">Free Script [ <a href="http://www2.117.ne.jp/~come-on/Homepage/" target="_top">$script</a> ]</h5>
</body>
</html>
HTML
	exit;
}

#==================== ログのリセット ===============================================

sub delete {
	if ($FORM{'pass'} ne $pass) { &error('パスワードが不正です。'); }
	if ($FORM{'page'} eq 'all') {
		foreach $dir (@DIR) {
			if ($dir =~ /(.*).log/) {
				unlink("$datadir$dir");
			}
		}
	} else {
		unlink("$datadir$FORM{'page'}.log");
	}
	&start;
}

#==================== ログの記録 ===================================================

sub input {
	
	#----- 基本情報の設定 -----------------------
	@TIME = gmtime(time + 9 * 3600);
	$cdate = &template'cookie_date($days);
	$week = &template'date('ww');
	$hour = $TIME[2];
	$mint = $TIME[1];
	$today = sprintf("%d/%02d/%02d",$TIME[5]+1900,$TIME[4],$TIME[3]);
	$ctime = sprintf("%d/%02d/%02d %02d-%02d",$TIME[5]+1900,$TIME[4],$TIME[3],$TIME[2],$TIME[1]);
	%COOKIE = &template'cookie($FORM{'file'});
	$link = $FORM{'link'};
	$datafile = $datadir . $FORM{'file'} . ".log";
	
	#----- 環境変数の設定 -----------------------
	$agent = $ENV{'HTTP_USER_AGENT'};
	$href = $ENV{'HTTP_REFERER'};
	$host = $ENV{'REMOTE_HOST'};
	$addr = $ENV{'REMOTE_ADDR'};
	if ($host eq $addr) { $host = gethostbyaddr(pack('C4',split(/\./,$host)),2) || $addr; }
	if ($host =~ /(.*)\.(.*)\.(.*)\.(.*)$/) { $host = "\*\.$2\.$3\.$4"; }
	elsif ($host =~ /(.*)\.(.*)\.(.*)$/) { $host = "\*\.$2\.$3"; }
	
	$key = $link;
	$link =~ s/(.*)\?.*/$1?/i;
	
	#----- サーチエンジンの判別 -----------------
	if ($link eq 'http://search.yahoo.co.jp/bin/search?' || $link eq 'http://search.yahoo.com/bin/search?') { $sname = 'p'; }
	elsif ($link eq 'http://www.infoseek.co.jp/Titles?' || $link eq 'http://japan.infoseek.com/Titles?') { $sname = 'qt'; }
	elsif ($link eq 'http://www.goo.ne.jp/default.asp?') { $sname = 'MT'; }
	elsif ($link eq 'http://www.excite.co.jp/search.gw?' || $link eq 'http://jp.excite.com/search.gw?') { $sname = 's'; }
	elsif ($link eq 'http://www.lycos.co.jp/cgi-bin/pursuit?') { $sname = 'query'; }
	elsif ($link eq 'http://search.netplaza.biglobe.ne.jp/cgi-bin/search-renew3.cgi?') { $sname = 'key'; }
	elsif ($link eq 'http://search.fresheye.com/?') { $sname = 'kw'; }
	elsif ($link eq 'http://para.cab.infoweb.ne.jp/cgi-bin/para?') { $sname = 'Querystring'; }
	elsif ($link eq 'http://kaze.csj.co.jp/search/lookup-main.cgi?') { $sname = 'key'; }
	elsif ($link eq 'http://www.altavista.com/cgi-bin/query?') { $sname = 'q'; }
	else { $cantkey = 1; }
	
	
	#----- キーワードの取得 ---------------------
	if (!$cantkey) {
		$key = $ENV{'QUERY_STRING'};
		($gomi,$key) = split(/\?/, $key);
		@KEY = split(/&/, $key);
		foreach (@KEY) {
			($name,$value) = split(/=/, $_);
			if ($name eq $sname) {
				$keyword = $value;
				last;
			}
		}
		$keyword =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;
		$keyword =~ tr/+/ /;
		$keyword =~ s/&/&amp;/g;
		$keyword =~ s/"/&quot;/g;
		$keyword =~ s/</&lt;/g;
		$keyword =~ s/>/&gt;/g;
		$keyword =~ s/,/&#44;/g;
		if ($jcode) { &jcode'convert(*keyword,"$jcode"); }
	}
	
	#----- 前回訪問日の取得 ---------------------
	if (!$COOKIE{'repert'}) { $repert = 0; }
	else {
		$repert = $COOKIE{'repert'};
		$repert =~ s/-/:/;
		($dates,$timer) = split(/ /, $repert);
		if ($dates eq $today && $nocnt != 0) {
			($hours,$mints) = split(/:/, $timer);
			$before = $hours * 60 + $mints;
			$nowtme = $hour * 60 + $mint;
			if ($nowtme - $before <= $nocnt) {
				$no_count = 1;
			}
		}
	}
	
	#----- 不正利用防止 -------------------------
	if ($href !~ /$turl/ && $turl ne '') { $no_count = 1; }
	
	#----- 指定時間内の再訪問はカウントしない ---
	if (!$no_count) {
		
		#----- ファイルの読み込み -------------------
		@FILE = &template'read_file($datafile);
		if ($max < $#FILE) { splice(@FILE, $max); }
		
		$agent =~ s/,/&#44;/g;
		shift(@FILE);
		$data = "$times,$week,$hour,$host,$link,$agent,$keyword,$repert\n";
		unshift(@FILE, $data);
		unshift(@FILE, "$href,\n");
		
		#----- ファイルへ書き込み/ロック ------------
		&template'lock_check($lockfile,$lock);
		&template'file_lock($tempfile,$datafile,$lockfile,$lock,@FILE,"");
		
	}
	
	#----- ダミー画像を返す ---------------------
	print "Content-type: image/gif\n";
	if ($cookie) { print "Set-Cookie: $FORM{'file'}=repert:$ctime; expires=$cdate\n"; }
	print "\n";
	&template'include($image);
	exit;

}

#==================== エラー処理 ===================================================

sub error {
	local($msg) = @_;
	if (!$msg) { $msg = '原因不明のエラーにより，処理を強制終了します。'; }
	print "Content-type: text/html\n\n";
print <<"HTML";
<html>
<head>
<title>$title [システムエラー]</title>
<meta http-equiv="Content-Type" content="text/html; charset=$fcode">
</head>
<body>
<p>　</p>
<div align="center"><center>
<table border="1" width="80%" cellpadding="5" cellspacing="0">
  <tr>
    <td width="100%" bgcolor="#0000FF" align="center"><b><font color="#FFFFFF">システムエラー</font></b></td>
  </tr>
  <tr>
    <td width="100%"><p align="center">　　<br>
    <font color="#FF0000">このプログラムは不正な処理を行ったので強制終了されます。</font></p>
    <hr noshade size="1">
    <div align="center"><center><table border="0">
      <tr>
        <td><b>$msg</b></td>
      </tr>
    </table>
    </center></div>
    <hr noshade size="1">
    <blockquote>
      <p>　リクエスト処理中に不正な命令が実行されたため，この処理を強制終了します。エラーの発生原因としてリクエストが不正確，管理者よりアクセス権が与えられていない，誤った設定がなされている等の可能\性があります。エラーが解決しない場合はこのサイトの管理者に連絡してください。</p>
    </blockquote>
    </td>
  </tr>
</table>
</center></div>
</body>
</html>
HTML
	exit;
}

