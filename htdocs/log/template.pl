package template;
;########################################################################################
;#
;#    <template.pl>  Perl Script Library  ver 2.02
;#
;#    Copyright (C) 1997-1999 Iwao Wada.  <iwao@drive.co.jp>
;#
;#  - 利用規程
;#     ・このライブラリの配布・転載・改造は自由ですが、著作権は放棄していません。
;#     ・改造版を再配布する場合は、必ずオリジナルも添付して配布してください。
;#     ・このライブラリを起因とするいかなる不利益についても一切の責任は負いません。
;#
;#  - 機能一覧
;#    ／クッキー処理／日付設定処理／フォームデコード／ファイル読込み
;#    ／データ読込み／メール送信／検索／文字列暗号化／暗号照合／
;#    ／ファイルロック／クリッカブルリンク
;#
;#  - 制限事項
;#     このライブラリは、すべてのサーバーで実行できるわけではありません。サーバーに
;#      よっては、一部の処理が使えない場合がありますが、ご了承下さい。
;#
;#  - 改訂履歴
;#     09 Mar,1999 日付変換処理を改良
;#     06 Mar,1999 メール送信処理に関するバグフィックス
;#     22 Feb,1999 ライブラリをパッケージ化
;#     18 Feb,1999 ロック処理に関するバグフィックス
;#     06 Feb,1999 メール送信とエラー処理に関する機能強化
;#     18 Jan,1999 ファイル挿入処理を追加
;#     15 Jan,1999 検索結果を戻り値として返すようにした
;#     12 Jan,1999 検索処理に関するバグフィックス
;#     08 Jan,1999 HTMLメールに対応。メールの送信結果(1/0)を戻り値とした
;#     05 Jan,1999 数字画像変換処理のサブルーチンを追加
;#     03 Jan,1999 日付の表記方法を引数で自由に指定できるようにした
;#     31 Dec,1998 フォームデコード処理に関するバグフィックス
;#     30 Dec,1998 暗号処理で戻り値を返すようにした
;#     08 Dec,1998 初バージョン(1.00)公開
;#
;#---------------------------------------------------------------------------------------
;#
;#   ■ クッキーの有効日数処理 <&template'cookie_date>
;#
;#	引数:(クッキーの有効日数)
;#	戻り値:GMT式に変換された日付
;#
;#---------------------------------------------------------------------------------------
;#
;#   ■ クッキー処理 <&template'cookie>
;#	 ブラウザからクッキーの取得を行います。各クッキーはカンマ","で区切られてお
;#	り、変数名と変数はコロン":"で区切りられているものとします。
;#
;#	引数:(クッキーの名前)
;#	戻り値:各クッキーが代入された連想配列
;#
;#---------------------------------------------------------------------------------------
;#
;#   ■ 日付設定処理 <&template'date>
;#	 ローカル時刻を設定します。日時の表記方法は引数によって設定できます。戻り値
;#	は設定された日時になります。
;#
;#	引数:(日時の表記方法)
;#	戻り値:現在日時
;#
;#	[日時表記の指定方法(例)]
;#
;#	  $date = &template'date('yyyy/mm/dd [ww] hh:mm ss');
;#
;#	   上記のように指定すると、戻り値は 1999/09/12 [日] 14:04 24 のような形に
;#	  なります。(1999年9月12日日曜日14時4分24秒を例にしています。)
;#
;#	    yyyy = 年-西暦4桁表記  	(ex.1999)
;#	      yy = 年-西暦2桁表記  	(ex.99)
;#	     yyy = 年-和暦表記  	(ex.11)
;#	       m = 月-数字1桁表記	(ex.5)
;#	      mm = 月-数字2桁表記	(ex.09) > 1桁の場合は2桁目には0が付きます
;#	     mm2 = 月-英語略表記 	(ex.Sep)
;#	     mm3 = 月-英語完全表記	(ex.September)
;#	       d = 日-数字1桁表記	(ex.12)
;#	      dd = 日-数字2桁表記	(ex.12) > 1桁の場合は2桁目には0が付きます
;#	      ww = 曜日-漢字表記 	(ex.日)
;#	     ww2 = 曜日-英語略表記	(ex.Sun)
;#	     ww3 = 曜日-英語完全表記	(ex.Sunday)
;#	       h = 時-数字1桁24時間表記	(ex.14)
;#	      h2 = 時-数字1桁12時間表記	(ex.2)
;#	      hh = 時-数字2桁24時間表記	(ex.14) > 1桁の場合は2桁目には0が付きます
;#	     hh2 = 時-数字2桁12時間表記	(ex.02) > 1桁の場合は2桁目には0が付きます
;#	       n = 分-数字1桁表記	(ex.4)
;#	      nn = 分-数字2桁表記	(ex.04) > 1桁の場合は2桁目には0が付きます
;#	       s = 秒-数字1桁表記	(ex.24)
;#	      ss = 秒-数字2桁表記  	(ex.24) > 1桁の場合は2桁目には0が付きます
;#	      ap = 時-AM/PM表記
;#
;#	   日付は上記のように設定されます。いくつかの例をあげます。
;#
;#	    ・ yyyy/mm/dd/ [ww] hh:nn ss	⇒ 1999/09/12 [日] 14:04 24
;#	    ・ yyyy年mm月dd日 (ww) hh時nn分	⇒ 1999年09月12日 (日) 14時04分
;#	    ・ 平成yyy年mm月dd日 午後h2時n分	⇒ 平成11年09月12日 午後2時4分
;#	    ・ yyyy年mm月dd日 ww曜日 午後h時n分	⇒ 1999年09月12日 日曜日 午後2時4分
;#	    ・ yy-m-d [ww2] hh:nn ss		⇒ 99-9-12 [Sun] 14:04 24
;#	    ・ ww3,mm3 dd,yyyy h2:nn pm		⇒ Sunday,September 3,1999 2:04 pm
;#	    ・ ww2,d mm2,yyyy PM hh2:nn		⇒ Sun,3 Sep,1999 PM 02:04
;#
;#---------------------------------------------------------------------------------------
;#
;#   ■ デコード処理 <&template'decode>
;#	 フォームから入力(リクエスト)された内容をデコードします。GETとPOSTの両方に
;#	対応しています。日本語コードの変換には日本語コード変換ライブラリ"jcode.pl"が
;#	必要です。デコードされたものは、連想配列に代入され、それが戻り値となります。
;#	戻り値を取得して、$FORM{'変数名'}で呼び出せます。
;#
;#	引数:(HTMLタグの可否,改行の可否,文字コード);
;#	戻り値:各要素が代入された連想配列
;#
;#---------------------------------------------------------------------------------------
;#
;#   ■ ファイル読み込み <&template'read_file>
;#	 ファイルをオープンし、それをファイルハンドラ"FILE"に関連づけ、配列"@FILE"に
;#	代入します。@FILEが戻り値となります。
;#
;#	引数:(オープンするファイルのパス);
;#	戻り値:ファイルハンドラから取得した配列
;#
;#---------------------------------------------------------------------------------------
;#
;#   ■ データ読み込み <&template'read_data>
;#	 データが各行にあり、データ1つをカンマ","で区切っているような形式の場合は、
;#	「データ読み込み 」が使えます。ただし、カンマで区切られた各配列要素が
;#	「変数名=値」(例:"name=Hogehoge")のような場合のみ使えます。なお、配列要
;#	素が複数行の場合はループ処理("foreach"文等)の中で使って下さい。
;#
;#	引数:(読み込むデータ配列);
;#	戻り値:各要素が代入された連想配列
;#
;#---------------------------------------------------------------------------------------
;#
;#   ■ メール送信 <&template'send_mail>
;#	 "sendmail"を使ってメールを送信します。"sendmail"のパスはサーバー管理者に問
;#	い合わせてください。多くの場合は"/usr/lib/sendmail"だと思われます。
;#
;#	引数:(sendmailのパス,TO,CC,BCC,FROM,件名,本文,HTMLメール);
;#	戻り値:正常に処理できたならば真
;#
;#---------------------------------------------------------------------------------------
;#
;#   ■ 検索 <&template'search>
;#
;#	引数:(検索文字列,検索モード,大小文字判別,検索対象配列);
;#	戻り値:抽出されたデータ
;#
;#---------------------------------------------------------------------------------------
;#
;#   ■ 暗号化処理 <&template'coding>
;#	 crypt関数を使って、暗号化します。引数として暗号化する文字列(パスワード)と
;#	暗号化の種を渡します。
;#
;#	引数:(暗号化する文字列,暗号化に使う種);
;#	戻り値:暗号化された文字列;
;#
;#---------------------------------------------------------------------------------------
;#
;#   ■ 暗号照合 <&template'decoding>
;#	 前項によって暗号化された文字列が、入力された文字列かどうかを照合します。
;#
;#	引数:(照合する文字列,暗号化されている文字列,暗号化に使った種);
;#	戻り値:照合する文字列と暗号化されている文字列が一致した場合は真
;#
;#---------------------------------------------------------------------------------------
;#
;#   ■ クリッカブルリンク <&template'link>
;#	 文字列に含まれるURLやメールアドレスを、リンクに変換します。
;#
;#	引数:(リンクに変換する文字列);
;#	戻り値:(リンクに変換された文字列);
;#
;#---------------------------------------------------------------------------------------
;#
;#   ■ ファイル出力 <&template'include>
;#
;#	引数:(ファイルのパス);
;#	戻り値:正常に処理できたならば真
;#
;#---------------------------------------------------------------------------------------
;#
;#   ■ ロックチェック <&template'lock_check>
;#	 オープンしようとしているファイルがロックされているかチェックします。
;#
;#	引数:(ロックファイルのパス,1);
;#	戻り値:ロックされていないならば真
;#
;#---------------------------------------------------------------------------------------
;#
;#   ■ ファイルロック <&template'file_lock>
;#	 ファイルをロック、書き込みを行います。テンポラリーファイルはプロセスIDなど
;#	を使用してください。テンポラリーファイル、ロックファイル、データファイルのデ
;#	ィレクトリの属性は777である必要があります。
;#
;#	引数:(テンポラリファイル,データファイル,ロックファイル,1,書込む配列,書込む変数);
;#	戻り値:正常に処理できたならば真
;#
;########################################################################################


;# ==========================
;# Set Cookie date.
;# ==========================

sub cookie_date{
	local($days) = @_;
	@CDATE = localtime(time + $days * 24 * 60 * 60);
	@cweek = ('Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday');
	@cmon  = ('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec');
	$cweek = $cweek[$CDATE[6]];
	$cmon  = $cmon[$CDATE[4]];
	$CDATE[5] += 1900;
	$cyear = $CDATE[5];
	$cday  = sprintf ("%02d",$CDATE[3]);
	$chour = sprintf ("%02d",$CDATE[2]);
	$cmin  = sprintf ("%02d",$CDATE[1]);
	$csec  = sprintf ("%02d",$CDATE[0]);
	$cdate = "$cweek, $cday\-$cmon\-$cyear $chour:$cmin:$csec GMT";
	return $cdate;
}

;# ==========================
;# Cookie Processing.
;# ==========================

sub cookie {
	local($cookie_name) = @_;
	$cookies = $ENV{'HTTP_COOKIE'};
	@pair = split(/;/,$cookies);
	foreach $group (@pair) {
		($name, $value) = split(/=/, $group);
		$name =~ s/ //g;
		$COOK{$name} = $value;
	}
	@pair = split(/\,/,$COOK{$cookie_name});
	foreach $group (@pair) {
		($name, $value) = split(/:/, $group);
		$COOKIE{$name} = $value;
	}
	return %COOKIE;
}

;# ==========================
;# Set day and time.
;# ==========================

sub date {
	local($time) = @_;
	@DATE = localtime(time);
	if ($time =~ /yyyy/ ) {
		$DATE[5] += 1900;
		$time =~ s/yyyy/$DATE[5]/;
	} elsif ($time =~ /yyy/ ) {
		$DATE[5] += 1900;
		$year = $DATE[5] - 1988;
		$time =~ s/yyy/$year/;
	} else {
		$time =~ s/yy/$DATE[5]/;
	}
	
	if ($time =~ /dd/ ) {
		$day  = sprintf ("%02d",$DATE[3]);
		$time =~ s/dd/$day/;
	} else {
		$time =~ s/d/$DATE[3]/;
	}
	
	if ($time =~ /hh2/ ) {
		if ($DATE[2] - 12 == 0) { $DATE[2] = 12; }
		else { $DATE[2] -= 12; }
		$hour = sprintf ("%02d",$DATE[2]);
		$time =~ s/hh2/$hour/;
	} elsif ($time =~ /hh/ ) {
		$hour = sprintf ("%02d",$DATE[2]);
		$time =~ s/hh/$hour/;
	} elsif ($time =~ /h2/ ) {
		if ($DATE[2] - 12 == 0) { $DATE[2] = 12; }
		else { $DATE[2] -= 12; }
		$time =~ s/h2/$DATE[2]/;
	} else {
		$time =~ s/h/$DATE[2]/;
	}
	
	if ($time =~ /nn/ ) {
		$min  = sprintf ("%02d",$DATE[1]);
		$time =~ s/nn/$min/;
	} else {
		$time =~ s/n/$DATE[1]/;
	}
	
	if ($time =~ /ss/ ) {
		$sec = sprintf ("%02d",$DATE[0]);
		$time =~ s/ss/$sec/;
	} else {
		$time =~ s/s/$DATE[0]/;
	}
	
	if ($time =~ /ww2/ ) {
		@week = ('Sun','Mon','Tues','Wed','Thu','Fri','Sat');
		$time =~ s/ww2/$week[$DATE[6]]/;
	} elsif ($time =~ /ww3/ ) {
		@week = ('Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday');
		$time =~ s/ww3/$week[$DATE[6]]/;
	} else {
		@week = ('日','月','火','水','木','金','土');
		$time =~ s/ww/$week[$DATE[6]]/;
	}
	
	if ($time =~ /mm2/ ) {
		@mont  = ('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec');
		$time =~ s/mm2/$mont[$DATE[4]]/;
	} elsif ($time =~ /mm3/ ) {
		@mont  = ('January','Februay','March','April','May','June','July','August','September','October','November','December');
		$time =~ s/mm3/$mont[$DATE[4]]/;
	} elsif ($time =~ /mm/ ) {
		$mon  = sprintf ("%02d",$DATE[4] + 1);
		$time =~ s/mm/$mon/;
	} else {
		$mon  = $DATE[4] + 1;
		$time =~ s/m/$mon/;
	}
	return $time;
}

;# ==========================
;# Decode font-codes.
;# ==========================

sub decode {
	local($tag,$return,$jcode) = @_;
	if ($ENV{'REQUEST_METHOD'} eq 'POST') {
		read(STDIN, $FORM_DATA, $ENV{'CONTENT_LENGTH'});
	} else { $FORM_DATA = $ENV{'QUERY_STRING'}; }
	@pair = split(/&/,$FORM_DATA);
	foreach $group (@pair) {
		($name, $value) = split(/=/, $group);
		$value =~ tr/+/ /;
		$value =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;
		if ($jcode) { &jcode'convert(*value,"$jcode"); }
		if (!$tag) {
			$value =~ s/&/&amp;/g;
			$value =~ s/"/&quot;/g;
			$value =~ s/</&lt;/g;
			$value =~ s/>/&gt;/g;
		}
		$value =~ s/,/&#44;/g;
		$value =~ s/\r\n/\n/g;
		$value =~ s/\r/\n/g;
		if ($return) { $value =~ s/\n/<br>/g; }
		else { $value =~ s/\n//g; }
		$FORM{$name} = $value;
	}
	return %FORM;
}

;# ==========================
;# File Read.
;# ==========================

sub read_file {
	local($datafile) = @_;
	if (open(FILE,"$datafile")) {
		@FILE = <FILE>;
		close(FILE);
	}
	return @FILE;
}

;# ==========================
;# Data Read.
;# ==========================

sub read_data {
	local(@DATAS) = @_;
	foreach $data (@DATAS) {
		($name, $value) = split (/=/, $data);
		$DATA{$name} = $value;
	}
	return %DATA;
}

;# ==========================
;# Send Email.
;# ==========================

sub send_mail {
	local($sendmail,$mailto,$mailcc,$mailbc,$from,$subject,$message,$html) = @_;
	if (open(ML,"| $sendmail -t")) {
		print ML "X-HTTP_REFERER: $link\n";
		print ML "X-HTTP_USER_AGENT: $agent\n";
		print ML "X-REMOTE_HOST: $host\n";
		print ML "X-REMOTE_ADDR: $addr\n";
		if ($mailto)	{ $mailto = &template'jis($mailto); print ML "TO: $mailto\n"; }
		if ($mailcc)	{ $mailcc = &template'jis($mailcc); print ML "CC: $mailcc\n"; }
		if ($mailbc)	{ $mailbc = &template'jis($mailbc); print ML "BCC: $mailbc\n"; }
		if ($from)	{ $from = &template'jis($from);	    print ML "From: $from\n"; }
		print ML "Content-Transfer-Encoding: 7bit\n";
		if ($html) {
			print ML "Content-Type: text/html\; charset=\"ISO-2022-JP\"\n";
		} else {
			print ML "Content-Type: text/plain\; charset=\"ISO-2022-JP\"\n";
		}
		$subject = &template'jis($subject); print ML "Subject: $subject\n";
		$message = &template'jis($message); print ML "$message\n";
		close(ML);
		return 1;
	} else {
		return 0;
	}
}

sub jis {
	$msg = $_[0];
	&jcode'convert(*msg, 'jis');
	return $msg;
}

;# ==========================
;# Keyword Search.
;# ==========================

sub search {
	local($keyword,$mchmode,$bigsmall,@DATAS) = @_;
	if (!$bigsmall) { $keyword =~ tr/[A-Z]/[a-z]/; }
	$keyword =~ s/　/ /g;
	@KEY = split(/ /, $keyword);
	foreach $datas (@DATAS) {
		$line = $datas;
		if (!$bigsmall) {
			$line =~ tr/[A-Z]/[a-z]/;
		}
		if ($mhmode eq 'or') {
			$result = 0;
			foreach $key (@KEY) {
				if (index($line,$key) >= 0) {
					$result = 1;
					last;
				}
			}
		} else {
			$result = 1;
			foreach $key (@KEY) {
				if (!(index($line,$key) >= 0)) {
					$result = 0;
					last;
				}
			}
		}
		if ($result) {
			push(@RESULT,$datas);
		}
	}
	return @RESULT;
}

;# ==========================
;# Coding.
;# ==========================

sub coding {
	local($pass,$salt) = @_;
	return crypt($pass,$salt);
}

;# ==========================
;# Decoding.
;# ==========================

sub decoding {
	local($pass,$pwd,$salt) = @_;
	if (crypt($pass,$salt) eq $pwd) {
		return 1;
	} else {
		return 0;
	}
}

;# ==========================
;# Inline Link.
;# ==========================

sub link { 
	local($_) = $_[0]; 
	$_ =~ s/([^=^\"]|^)((http|https|telnet|ftp|gopher|news):[!#-9A-~]+)/$1<a href=\"$2\" target=\"_blank\">$2<\/a>/g; 
	$_ =~ s/([!#-9A-~\-\_]+\@[!#-9A-~\-\_\.]+)/<a href=\"mailto:$1\">$1<\/a>/g;
	$_;
}

;# ==========================
;# Include File.
;# ==========================

sub include {
	local($include_file) = @_;
	if (open(FILE,"$include_file")) {
		print $_ while (<FILE>);
		close(FILE);
		return 1;
	} else {
		return 0;
	}
}

;# ==========================
;# Lock check.
;# ==========================

sub lock_check {
	local($lockfile,$lock) = @_;
	$locked = 0;
	if (!$lock) { return 1; }
	foreach (1 .. 3) {
		if (-e "$lockfile") {
			sleep(1);
		} else {
			return 1;
		}
	}
	return 0;
}

;# ==========================
;# File Lock.
;# ==========================

sub file_lock {
	local($tempfile,$datafile,$lockfile,$lock,@DATA,$data) = @_;
	$locked = 0;
	if (!$lock) {
		if (open(FILE,">$datafile")) {
			if ($data) {
				print FILE $data;
			} elsif (@DATA) {
				print FILE @DATA;
			}
			close(FILE);
		} else {
			return 0;
		}
		return 1;
	}
	if (open(FILE,">$tempfile")) {
		if ($data) { print FILE $data; }
		elsif (@DATA) {
			print FILE @DATA;
		}
		close(FILE);
	} else {
		return 0;
	}
	foreach (1 .. 3) {
		if (-e "$lockfile") {
			sleep(1);
		} else {
			if (open(FILE,">$lockfile")) {
				close(FILE);
				rename($tempfile,$datafile);
				unlink($lockfile);
				$locked = 1;
				last;
			} else {
				sleep(1);
			}
		}
	}
	
	if (-e $tempfile) {
		unlink($tempfile);
	}
	if ($locked) {
		return 1;
	} else {
		return 0;
	}
}
1;
