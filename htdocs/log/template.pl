package template;
;########################################################################################
;#
;#    <template.pl>  Perl Script Library  ver 2.02
;#
;#    Copyright (C) 1997-1999 Iwao Wada.  <iwao@drive.co.jp>
;#
;#  - ���p�K��
;#     �E���̃��C�u�����̔z�z�E�]�ځE�����͎��R�ł����A���쌠�͕������Ă��܂���B
;#     �E�����ł��Ĕz�z����ꍇ�́A�K���I���W�i�����Y�t���Ĕz�z���Ă��������B
;#     �E���̃��C�u�������N���Ƃ��邢���Ȃ�s���v�ɂ��Ă���؂̐ӔC�͕����܂���B
;#
;#  - �@�\�ꗗ
;#    �^�N�b�L�[�����^���t�ݒ菈���^�t�H�[���f�R�[�h�^�t�@�C���Ǎ���
;#    �^�f�[�^�Ǎ��݁^���[�����M�^�����^������Í����^�Í��ƍ��^
;#    �^�t�@�C�����b�N�^�N���b�J�u�������N
;#
;#  - ��������
;#     ���̃��C�u�����́A���ׂẴT�[�o�[�Ŏ��s�ł���킯�ł͂���܂���B�T�[�o�[��
;#      ����ẮA�ꕔ�̏������g���Ȃ��ꍇ������܂����A�������������B
;#
;#  - ��������
;#     09 Mar,1999 ���t�ϊ�����������
;#     06 Mar,1999 ���[�����M�����Ɋւ���o�O�t�B�b�N�X
;#     22 Feb,1999 ���C�u�������p�b�P�[�W��
;#     18 Feb,1999 ���b�N�����Ɋւ���o�O�t�B�b�N�X
;#     06 Feb,1999 ���[�����M�ƃG���[�����Ɋւ���@�\����
;#     18 Jan,1999 �t�@�C���}��������ǉ�
;#     15 Jan,1999 �������ʂ�߂�l�Ƃ��ĕԂ��悤�ɂ���
;#     12 Jan,1999 ���������Ɋւ���o�O�t�B�b�N�X
;#     08 Jan,1999 HTML���[���ɑΉ��B���[���̑��M����(1/0)��߂�l�Ƃ���
;#     05 Jan,1999 �����摜�ϊ������̃T�u���[�`����ǉ�
;#     03 Jan,1999 ���t�̕\�L���@�������Ŏ��R�Ɏw��ł���悤�ɂ���
;#     31 Dec,1998 �t�H�[���f�R�[�h�����Ɋւ���o�O�t�B�b�N�X
;#     30 Dec,1998 �Í������Ŗ߂�l��Ԃ��悤�ɂ���
;#     08 Dec,1998 ���o�[�W����(1.00)���J
;#
;#---------------------------------------------------------------------------------------
;#
;#   �� �N�b�L�[�̗L���������� <&template'cookie_date>
;#
;#	����:(�N�b�L�[�̗L������)
;#	�߂�l:GMT���ɕϊ����ꂽ���t
;#
;#---------------------------------------------------------------------------------------
;#
;#   �� �N�b�L�[���� <&template'cookie>
;#	 �u���E�U����N�b�L�[�̎擾���s���܂��B�e�N�b�L�[�̓J���}","�ŋ�؂��Ă�
;#	��A�ϐ����ƕϐ��̓R����":"�ŋ�؂���Ă�����̂Ƃ��܂��B
;#
;#	����:(�N�b�L�[�̖��O)
;#	�߂�l:�e�N�b�L�[��������ꂽ�A�z�z��
;#
;#---------------------------------------------------------------------------------------
;#
;#   �� ���t�ݒ菈�� <&template'date>
;#	 ���[�J��������ݒ肵�܂��B�����̕\�L���@�͈����ɂ���Đݒ�ł��܂��B�߂�l
;#	�͐ݒ肳�ꂽ�����ɂȂ�܂��B
;#
;#	����:(�����̕\�L���@)
;#	�߂�l:���ݓ���
;#
;#	[�����\�L�̎w����@(��)]
;#
;#	  $date = &template'date('yyyy/mm/dd [ww] hh:mm ss');
;#
;#	   ��L�̂悤�Ɏw�肷��ƁA�߂�l�� 1999/09/12 [��] 14:04 24 �̂悤�Ȍ`��
;#	  �Ȃ�܂��B(1999�N9��12�����j��14��4��24�b���ɂ��Ă��܂��B)
;#
;#	    yyyy = �N-����4���\�L  	(ex.1999)
;#	      yy = �N-����2���\�L  	(ex.99)
;#	     yyy = �N-�a��\�L  	(ex.11)
;#	       m = ��-����1���\�L	(ex.5)
;#	      mm = ��-����2���\�L	(ex.09) > 1���̏ꍇ��2���ڂɂ�0���t���܂�
;#	     mm2 = ��-�p�ꗪ�\�L 	(ex.Sep)
;#	     mm3 = ��-�p�ꊮ�S�\�L	(ex.September)
;#	       d = ��-����1���\�L	(ex.12)
;#	      dd = ��-����2���\�L	(ex.12) > 1���̏ꍇ��2���ڂɂ�0���t���܂�
;#	      ww = �j��-�����\�L 	(ex.��)
;#	     ww2 = �j��-�p�ꗪ�\�L	(ex.Sun)
;#	     ww3 = �j��-�p�ꊮ�S�\�L	(ex.Sunday)
;#	       h = ��-����1��24���ԕ\�L	(ex.14)
;#	      h2 = ��-����1��12���ԕ\�L	(ex.2)
;#	      hh = ��-����2��24���ԕ\�L	(ex.14) > 1���̏ꍇ��2���ڂɂ�0���t���܂�
;#	     hh2 = ��-����2��12���ԕ\�L	(ex.02) > 1���̏ꍇ��2���ڂɂ�0���t���܂�
;#	       n = ��-����1���\�L	(ex.4)
;#	      nn = ��-����2���\�L	(ex.04) > 1���̏ꍇ��2���ڂɂ�0���t���܂�
;#	       s = �b-����1���\�L	(ex.24)
;#	      ss = �b-����2���\�L  	(ex.24) > 1���̏ꍇ��2���ڂɂ�0���t���܂�
;#	      ap = ��-AM/PM�\�L
;#
;#	   ���t�͏�L�̂悤�ɐݒ肳��܂��B�������̗�������܂��B
;#
;#	    �E yyyy/mm/dd/ [ww] hh:nn ss	�� 1999/09/12 [��] 14:04 24
;#	    �E yyyy�Nmm��dd�� (ww) hh��nn��	�� 1999�N09��12�� (��) 14��04��
;#	    �E ����yyy�Nmm��dd�� �ߌ�h2��n��	�� ����11�N09��12�� �ߌ�2��4��
;#	    �E yyyy�Nmm��dd�� ww�j�� �ߌ�h��n��	�� 1999�N09��12�� ���j�� �ߌ�2��4��
;#	    �E yy-m-d [ww2] hh:nn ss		�� 99-9-12 [Sun] 14:04 24
;#	    �E ww3,mm3 dd,yyyy h2:nn pm		�� Sunday,September 3,1999 2:04 pm
;#	    �E ww2,d mm2,yyyy PM hh2:nn		�� Sun,3 Sep,1999 PM 02:04
;#
;#---------------------------------------------------------------------------------------
;#
;#   �� �f�R�[�h���� <&template'decode>
;#	 �t�H�[���������(���N�G�X�g)���ꂽ���e���f�R�[�h���܂��BGET��POST�̗�����
;#	�Ή����Ă��܂��B���{��R�[�h�̕ϊ��ɂ͓��{��R�[�h�ϊ����C�u����"jcode.pl"��
;#	�K�v�ł��B�f�R�[�h���ꂽ���̂́A�A�z�z��ɑ������A���ꂪ�߂�l�ƂȂ�܂��B
;#	�߂�l���擾���āA$FORM{'�ϐ���'}�ŌĂяo���܂��B
;#
;#	����:(HTML�^�O�̉�,���s�̉�,�����R�[�h);
;#	�߂�l:�e�v�f��������ꂽ�A�z�z��
;#
;#---------------------------------------------------------------------------------------
;#
;#   �� �t�@�C���ǂݍ��� <&template'read_file>
;#	 �t�@�C�����I�[�v�����A������t�@�C���n���h��"FILE"�Ɋ֘A�Â��A�z��"@FILE"��
;#	������܂��B@FILE���߂�l�ƂȂ�܂��B
;#
;#	����:(�I�[�v������t�@�C���̃p�X);
;#	�߂�l:�t�@�C���n���h������擾�����z��
;#
;#---------------------------------------------------------------------------------------
;#
;#   �� �f�[�^�ǂݍ��� <&template'read_data>
;#	 �f�[�^���e�s�ɂ���A�f�[�^1���J���}","�ŋ�؂��Ă���悤�Ȍ`���̏ꍇ�́A
;#	�u�f�[�^�ǂݍ��� �v���g���܂��B�������A�J���}�ŋ�؂�ꂽ�e�z��v�f��
;#	�u�ϐ���=�l�v(��:"name=Hogehoge")�̂悤�ȏꍇ�̂ݎg���܂��B�Ȃ��A�z��v
;#	�f�������s�̏ꍇ�̓��[�v����("foreach"����)�̒��Ŏg���ĉ������B
;#
;#	����:(�ǂݍ��ރf�[�^�z��);
;#	�߂�l:�e�v�f��������ꂽ�A�z�z��
;#
;#---------------------------------------------------------------------------------------
;#
;#   �� ���[�����M <&template'send_mail>
;#	 "sendmail"���g���ă��[���𑗐M���܂��B"sendmail"�̃p�X�̓T�[�o�[�Ǘ��҂ɖ�
;#	�����킹�Ă��������B�����̏ꍇ��"/usr/lib/sendmail"���Ǝv���܂��B
;#
;#	����:(sendmail�̃p�X,TO,CC,BCC,FROM,����,�{��,HTML���[��);
;#	�߂�l:����ɏ����ł����Ȃ�ΐ^
;#
;#---------------------------------------------------------------------------------------
;#
;#   �� ���� <&template'search>
;#
;#	����:(����������,�������[�h,�召��������,�����Ώ۔z��);
;#	�߂�l:���o���ꂽ�f�[�^
;#
;#---------------------------------------------------------------------------------------
;#
;#   �� �Í������� <&template'coding>
;#	 crypt�֐����g���āA�Í������܂��B�����Ƃ��ĈÍ������镶����(�p�X���[�h)��
;#	�Í����̎��n���܂��B
;#
;#	����:(�Í������镶����,�Í����Ɏg����);
;#	�߂�l:�Í������ꂽ������;
;#
;#---------------------------------------------------------------------------------------
;#
;#   �� �Í��ƍ� <&template'decoding>
;#	 �O���ɂ���ĈÍ������ꂽ�����񂪁A���͂��ꂽ�����񂩂ǂ������ƍ����܂��B
;#
;#	����:(�ƍ����镶����,�Í�������Ă��镶����,�Í����Ɏg������);
;#	�߂�l:�ƍ����镶����ƈÍ�������Ă��镶���񂪈�v�����ꍇ�͐^
;#
;#---------------------------------------------------------------------------------------
;#
;#   �� �N���b�J�u�������N <&template'link>
;#	 ������Ɋ܂܂��URL�⃁�[���A�h���X���A�����N�ɕϊ����܂��B
;#
;#	����:(�����N�ɕϊ����镶����);
;#	�߂�l:(�����N�ɕϊ����ꂽ������);
;#
;#---------------------------------------------------------------------------------------
;#
;#   �� �t�@�C���o�� <&template'include>
;#
;#	����:(�t�@�C���̃p�X);
;#	�߂�l:����ɏ����ł����Ȃ�ΐ^
;#
;#---------------------------------------------------------------------------------------
;#
;#   �� ���b�N�`�F�b�N <&template'lock_check>
;#	 �I�[�v�����悤�Ƃ��Ă���t�@�C�������b�N����Ă��邩�`�F�b�N���܂��B
;#
;#	����:(���b�N�t�@�C���̃p�X,1);
;#	�߂�l:���b�N����Ă��Ȃ��Ȃ�ΐ^
;#
;#---------------------------------------------------------------------------------------
;#
;#   �� �t�@�C�����b�N <&template'file_lock>
;#	 �t�@�C�������b�N�A�������݂��s���܂��B�e���|�����[�t�@�C���̓v���Z�XID�Ȃ�
;#	���g�p���Ă��������B�e���|�����[�t�@�C���A���b�N�t�@�C���A�f�[�^�t�@�C���̃f
;#	�B���N�g���̑�����777�ł���K�v������܂��B
;#
;#	����:(�e���|�����t�@�C��,�f�[�^�t�@�C��,���b�N�t�@�C��,1,�����ޔz��,�����ޕϐ�);
;#	�߂�l:����ɏ����ł����Ȃ�ΐ^
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
		@week = ('��','��','��','��','��','��','�y');
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
	$keyword =~ s/�@/ /g;
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
