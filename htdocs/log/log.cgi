#!/usr/local/bin/perl
#--- �� ��Perl�̃p�X���قȂ�ꍇ�͕ύX����B���̃p�X�̓v���o�C�_�Ɋm�F����B
#
#   �A�N�Z�X��͗pCGI�X�N���v�g [�A�N�Z�X�E�g���b�J�[] ver.1.0 (�t���[�\�t�g)
#   Copyright(C)1997-1999 Iwao Wada. All rights reserved.
#
#----------------------------------------------------------------------------------#
#  �������炪�����ݒ�ł��i�T�[�o�[�ւ̐ݒu���@�͓�����'readme.txt'�������������j  #
#----------------------------------------------------------------------------------#
#
#   ����̍��ڂ͕K���ύX���Ă��������B
#�@ ����̍��ڂ͎�Ƀ��C�A�E�g�֘A�ł��B��{�I�ɕύX�s�v�ł��B
#�@ ����̍��ڂ̓T�[�o�[���ɂ���ĕύX����K�v������܂��B�i1�s�ڂ��܂݂܂��j
#
#�@''���ɋL�q���܂����A'����ꂽ���ꍇ�� '' �� "" �ɕύX���Ă��������B
#�@�Ȃ��A���̏ꍇ�͕��������������邱�Ƃ�����܂��B
#�@�ڂ����͖{�T�C�g�̉�������Q�Ƃ��Ă��������B
#
#
#--------�� ����@�\�̎g�p�Ɋւ���ݒ� ��-------------------------------------------
#
#  ����̓T�[�o�[���ɂ���Ă͐���ɓ��삵�Ȃ��ꍇ������܂��B
#  ���̏ꍇ�́A���̋@�\�𖳌��ɂ��Ă��������B

$pass = 'kkiill';			# <--- ���Ǘ��җp�p�X���[�h�i10�����ȓ��̔��p�p�����j
$open = 0;				# <--- �����v�y�[�W�i0�F����J�^1�F���J�j
$lock = 1;				# <--- ���t�@�C�����b�N�@�\�i0�F�g��Ȃ��^1�F�g���j
$jcode = 'sjis';			# <--- �������ϊ��R�[�h�isjis,jis,euc�j
$max = 500;				# <--- ��1���O�̍ő�ێ������i���܂�傫�����Ȃ��j

# �� ���\�[�g�����i0�F���Ȃ��^1�F�f�[�^�ʂ�3000���ȓ��Ȃ�΂���^2�F����j
$dosort = 1;
#  �\�[�g(���ёւ�)�������s���܂����H�������\�[�g�����͏�������f�[�^�ʂ������قǁA��������
#  ��v���A�T�[�o�[�ɕ��ׂ������܂��B�f�[�^�ʂ��ɒ[�ɑ����ƁA�^�C���A�E�g�ɂȂ�ꍇ�������
#  ���B���̂��Ƃ��l�����A�ő�f�[�^��($max�̒l)��3000���𒴂���悤�ȏꍇ�́A�\�[�g���Ȃ���
#  ���ɂ��邱��('$dosort=1'�ɂ���)�𐄏����܂��B�Ȃ��A�S�y�[�W�ɂ��ĉ�͂���ꍇ�́A���̕�
#  �f�[�^�ʂ������Ȃ�܂��B


#�@���M�{�^���������� 'Method not implemented..' ���̃G���[���o��ꍇ��'GET'�Ŏ����B
#�@�Ȃ�'GET'�̏ꍇ�͕�������������܂��̂Œ������͓��͓r���Ő؂��ꍇ������܂��B�܂��A
#  �t�H�[���̓��͓��e��URL�̌�ɕ\������邽�߁A�Z�L�����e�B�[���N�����댯��������܂��B
$method = 'POST';			# <--- �����͌`���i'POST'�^'GET'�j


#--------�� �N�b�L�[�̐ݒ� ��-------------------------------------------------------
#
#  �N�b�L�[�Ƃ̓u���E�U�ɕۑ�����鏬���ȏ��ł��B�ĖK��Ґ��̃J�E���g�Ɏg�p���܂��B
#  �S�Ẵu���E�U��T�[�o�[�Ŏg�p�ł���킯�ł͂���܂��񂪁A���̏ꍇ�͑��v�ł��B

$cookie = 1;				# <--- ���N�b�L�[�@�\�i0�F�g���^1�F�g��Ȃ��j
$days = 30;				# <--- ���N�b�L�[�̗L�������i�ĖK��Ƃ��Ĉ��������j

# �� �����̎��ԓ��̍ĖK��̓J�E���g���Ȃ��i�P�ʁF���^���̋@�\���g��Ȃ��ꍇ��'0'�ɂ���j
$nocnt = 0;


#--------�� �p�X/�A�h���X/�t�@�C�����Ɋւ���ݒ� ��---------------------------------
#
#  �X�N���v�g�Ɠ����f�B���N�g���̏ꍇ�́A'./'�ł��B1��̃f�B���N�g���́A'../'�ł��B
#  �����ł́u�p�X�v�Ƃ̓T�[�o�[���ł̏ꏊ '../xxxxx' �� '/home/hogehoge/public_html/' ��
#	 �@�u�A�h���X�v�Ƃ̓C���^�[�l�b�g�S�̂��猩���ꏊ 'http://�`' ���w���Ă��܂��B

require './template.pl';		# <--- ��Perl�ėp���C�u����"template.pl"�̃p�X
require './jcode.pl';			# <--- �����{��ϊ����C�u����"jcode.pl"�̃p�X
$bar = './width.gif';			# <--- ���O���t�p�摜�̃p�X/�A�h���X
$image = './dummy.gif';			# <--- ���_�~�[�摜�̃p�X
$datadir = './data/';			# <--- �����O�t�@�C���i�[�p�̃f�B���N�g���̃p�X

# �� �����Ȃ��̃T�C�g�̃g�b�v�f�B���N�g���̃A�h���X�i�T�C�g������̃����N���ЂƂ܂Ƃ߂ɂ���ꍇ�j
$surl = 'https://aurized-studio.jp/';

# �� �����Ȃ��̃T�C�g�̃g�b�v�f�B���N�g���̃A�h���X�i�O������̕s�����p��h�~����ꍇ�j
$turl = 'https://aurized-studio.jp/';
#
#  ��L�񍀖ڂ͂��Ȃ��̃T�C�g�̃g�b�v�f�B���N�g���̃A�h���X���w�肵�ĉ������B�����
#  �{�X�N���v�g���̓y�[�W�̏�ʃf�B���N�g�����܂ޕK�v������܂��B�����̏ꍇ�́A
#  'http://www.�v���o�C�_.ne.jp/~���Ȃ���ID/'�ł��B�Ȃ��A�ʂ̃T�[�o�[������{�X�N��
#  �v�g�𗘗p����ꍇ�͎w�肵�Ȃ��ł��������B


#--------�� �f�U�C�����Ɋւ���ݒ�(��{�I�ɕύX�s�v) ��-----------------------------
#
#   ��{�I�ɕύX�̕K�v�͂���܂��񂪁A�w�i�F�⃁�b�Z�[�W�����T���v���Ƃ͕ύX��������
#  ���͕ύX���Ă��������B(�ꕔ�̍��ڂł�HTML�Ɋւ����b�I�Ȓm�����K�v�ł�)

$title = 'https://aurized-studio.jp Access Analytics';		# <--- ���^�C�g���i<title>�Ȃǂŕ\���j
$hclr = '#FFFF80';			# <--- �����ږ��̔w�i�F
$mclr = '#CEFFCE';			# <--- ���區�ڂ̔w�i�F
$aclr = '#D2FFFF';			# <--- �����ڂ̔w�i�FA
$bclr = '#FFFFD2';			# <--- �����ڂ̔w�i�FB
$rclr = '#A0B8C8';			# <--- �����O�C���y�[�W�̉E���w�i�F
$wdth = 2;				# <--- ���O���t�̕��̔{���i$wdth�~�����j

# �� ��<body>�^�O�̐ݒ�i<>��'body'�͕s�v�ł��j
$body = 'text="#000000" link="#0000FF" bgcolor="#F0F0F0"';

$head=<<'HTML';
<!------ �� ���w�b�_�[���ɕ\�����镶����iHTML�g�p�\�j-->

<h1 align="center">https://aurized-studio.jp Access Analytics</h1>

<!------ �� �����܂� -->
HTML
$foot=<<'HTML';
<!------ �� ���t�b�^�[���ɕ\�����镶����iHTML�g�p�\�j-->


<!------ �� �����܂� -->
HTML

####################################################################################
#                                                                                  #
# �E�{�X�N���v�g�ŏ����ݒ肪�K�v�Ȃ̂͂����܂łł��B                               #
# �E�X�N���v�g����������ꍇ�́Aperl��CGI�Ȃǂ̂���Ȃ�̒m�����K�v�ł��B          #
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
} else { &error('�f�B���N�g���̃I�[�v�����ł��܂���B'); }

$i = 0;
foreach $dir (@DIR) {
	if ($dir =~ /(.*).log/) {
		$LOGS[$i] = $1;
		$i ++;
	}
}
$i = 0;



#-------------------- ��{���� -----------------------------------------------------

if ($FORM{'mode'} eq '' || $FORM{'mode'} eq ' �I�� ') { &start; }
elsif ($FORM{'pass'} ne $pass && $open == 0) { &error('�p�X���[�h���s���ł��B'); }

if (!$FORM{'type'}) { &error('��͍��ڂ�I�����ĉ������B'); }
elsif ($FORM{'page'} eq 'all' && $FORM{'type'} eq 'csv') { &error('��̓y�[�W��I�����ĉ������B'); }
elsif ($FORM{'page'} eq 'all' && $FORM{'type'} eq 'log') { &error('��̓y�[�W��I�����ĉ������B'); }
elsif ($FORM{'type'} eq 'reset') { &delete; }


if ($FORM{'page'} eq 'all') {
	foreach $logs (@LOGS) {
		$datafile = $datadir . $logs . ".log";
		@FILES = &template'read_file($datafile);
		if (!@FILES) { &error('�t�@�C���̃I�[�v�����ł��܂���B'); }
		shift(@FILES);
		push(@FILE,@FILES);
		
	}
	$total = $#FILE + 1;
} else {
	$datafile = $datadir . $FORM{'page'} . ".log";
	@FILE = &template'read_file($datafile);
	if (!@FILE) { &error('�t�@�C���̃I�[�v�����ł��܂���B'); }
	$total = $#FILE;
}

if ($FORM{'type'} eq 'csv') { &csv; }
if ($FORM{'page'} eq 'all') { $alls = ' selected'; }

#-------------------- ���ʃw�b�_�[�� -----------------------------------------------

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
      <td>�A�N�Z�X��� �F <select name="page" size="1">
        <option value="all"$alls>�S�Ẵy�[�W</option>
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
        <option value="date"$selected{'date'}>���t��</option>
        <option value="time"$selected{'time'}>���ԕ�</option>
        <option value="week"$selected{'week'}>�j����</option>
        <option value="host"$selected{'host'}>�z�X�g��</option>
        <option value="link"$selected{'link'}>�����N����</option>
        <option value="page"$selected{'page'}>�y�[�W��</option>
        <option value="agent"$selected{'agent'}>�G�[�W�F���g��</option>
        <option value="keyword"$selected{'keyword'}>�L�[���[�h��</option>
        <option value="log"$selected{'log'}>�A�N�Z�X��</option>
        <option value="csv">CSV�`��</option>
      </select><select name="max" size="1">
        <option value="10"$selected{'p10'}>10��</option>
        <option value="20"$selected{'p20'}>20��</option>
        <option value="50"$selected{'p50'}>50��</option>
        <option value="100"$selected{'p100'}>100��</option>
        <option value="200"$selected{'p200'}>200��</option>
        <option value="300"$selected{'p300'}>300��</option>
        <option value="400"$selected{'p400'}>400��</option>
        <option value="500"$selected{'p500'}>500��</option>
      </select> <input type="submit" value="�@ \OK �@"></td>
      <td> <input type="submit" name="mode" value=" �I�� "></td>
    </tr>
  </table>
  </center></div>
</form>
HTML

#-------------------- �e�탍�O�̏W�v -----------------------------------------------

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

#-------------------- �������� -----------------------------------------------------

if ($FORM{'type'} eq 'date') { &date_view; }
elsif ($FORM{'type'} eq 'week') { &week_view; }
elsif ($FORM{'type'} eq 'time') { &time_view; }
elsif ($FORM{'type'} eq 'host') { &host_view; }
elsif ($FORM{'type'} eq 'link') { &link_view; }
elsif ($FORM{'type'} eq 'agent') { &agent_view; }
elsif ($FORM{'type'} eq 'keyword') { &keyword_view; }
else { &error; }


#==================== ���t�ʓ��v ===================================================

sub date_view {
	
	($logpage,$startday) = split(/,/, $logdata);
	if ($FORM{'page'} eq 'all') { $logpage = '&lt;�S�y�[�W&gt;'; }
	else { $logpage = "<a href=\"$logpage\">$logpage</a>"; }
	($sday,$a,$b,$c,$d,$e,$f,$g) = split(/,/, $DATA[$#DATA]);
	
	print "<h2 align=\"center\">���t�ʃA�N�Z�X���v</h2>\n";
	print "<p align=\"center\">$logpage</p>\n";
	print "<p align=\"center\"><small><i>���v���� $sday �` $times�@�i�݌v $total��j</i></small></p>\n";
	print "<div align=\"center\"><center>\n";
	print "<table border=\"3\" cellpadding=\"3\" cellspacing=\"3\" width=\"80%\">\n";
	print "  <tr>\n";
	print "    <td width=\"30%\" align=\"center\" bgcolor=\"$hclr\"><b>���t</b></td>\n";
	print "    <td width=\"20%\" align=\"center\" bgcolor=\"$hclr\"><b>�q�b�g��</b></td>\n";
	print "    <td width=\"50%\" align=\"center\" bgcolor=\"$hclr\"><b>�O���t</b></td>\n";
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
	print "<p align=\"center\">���v�͍ŋ�<b>$end</b>���ȓ���\\�����Ă��܂��B���i��$days���ȓ��̍ĖK��Ґ��ł��B</p>\n";
	print "<hr noshade>\n";
	print "$foot";
	print "</body>\n";
	print "</html>\n";
	exit;
}

#==================== �j���ʓ��v ===================================================

sub week_view {
	
	($logpage,$startday) = split(/,/, $logdata);
	if ($FORM{'page'} eq 'all') { $logpage = '&lt;�S�y�[�W&gt;'; }
	else { $logpage = "<a href=\"$logpage\">$logpage</a>"; }
	($sday,$a,$b,$c,$d,$e,$f,$g) = split(/,/, $FILE[$#FILE]);
	
	@LOG = ('��,0,0','��,0,0','��,0,0','��,0,0','��,0,0','��,0,0','�y,0,0');
	foreach (@DATA) {
		($name,$count,$repert) = split(/,/, $_);
		if ($name eq '��') { $LOG[0] = "$name,$count,$repert"; }
		elsif ($name eq '��') { $LOG[1] = "$name,$count,$repert"; }
		elsif ($name eq '��') { $LOG[2] = "$name,$count,$repert"; }
		elsif ($name eq '��') { $LOG[3] = "$name,$count,$repert"; }
		elsif ($name eq '��') { $LOG[4] = "$name,$count,$repert"; }
		elsif ($name eq '��') { $LOG[5] = "$name,$count,$repert"; }
		elsif ($name eq '�y') { $LOG[6] = "$name,$count,$repert"; }
	}
	
	print "<h2 align=\"center\">�j���ʃA�N�Z�X���v</h2>\n";
	print "<p align=\"center\">$logpage</p>\n";
	print "<p align=\"center\"><small><i>���v���� $sday �` $times�@�i�݌v $total��j</i></small></p>\n";
	print "<div align=\"center\"><center>\n";
	print "<table border=\"3\" cellpadding=\"3\" cellspacing=\"3\" width=\"80%\">\n";
	print "  <tr>\n";
	print "    <td width=\"30%\" align=\"center\" bgcolor=\"$hclr\"><b>�y�[�W</b></td>\n";
	print "    <td width=\"20%\" align=\"center\" bgcolor=\"$hclr\"><b>�q�b�g��</b></td>\n";
	print "    <td width=\"50%\" align=\"center\" bgcolor=\"$hclr\"><b>�O���t</b></td>\n";
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
		print "    <td rowspan=\"2\" width=\"30%\" align=\"center\" bgcolor=\"$mclr\">$name�j��</td>\n";
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
	print "<p align=\"center\">���i��$days���ȓ��̍ĖK��Ґ��ł��B</p>\n";
	print "<hr noshade>\n";
	print "$foot";
	print "</body>\n";
	print "</html>\n";
	exit;
}

#==================== ���ԕʓ��v ===================================================

sub time_view {
	
	($logpage,$startday) = split(/,/, $logdata);
	if ($FORM{'page'} eq 'all') { $logpage = '&lt;�S�y�[�W&gt;'; }
	else { $logpage = "<a href=\"$logpage\">$logpage</a>"; }
	($sday,$a,$b,$c,$d,$e,$f,$g) = split(/,/, $FILE[$#FILE]);
	
	for ($i = 0; $i < 24; $i ++) { $LOG[$i] = "$i,0,0"; }
	foreach (@DATA) {
		($name,$count,$repert) = split(/,/, $_);
		$LOG[$name] = "$name,$count,$repert";
	}
	
	print "<h2 align=\"center\">���ԕʃA�N�Z�X���v</h2>\n";
	print "<p align=\"center\">$logpage</p>\n";
	print "<p align=\"center\"><small><i>���v���� $sday �` $times�@�i�݌v $total��j</i></small></p>\n";
	print "<div align=\"center\"><center>\n";
	print "<table border=\"3\" cellpadding=\"3\" cellspacing=\"3\" width=\"80%\">\n";
	print "  <tr>\n";
	print "    <td width=\"30%\" align=\"center\" bgcolor=\"$hclr\"><b>����</b></td>\n";
	print "    <td width=\"20%\" align=\"center\" bgcolor=\"$hclr\"><b>�q�b�g��</b></td>\n";
	print "    <td width=\"50%\" align=\"center\" bgcolor=\"$hclr\"><b>�O���t</b></td>\n";
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
		print "    <td rowspan=\"2\" width=\"25%\" align=\"center\" bgcolor=\"$mclr\">$i��</td>\n";
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
	print "<p align=\"center\">���i��$days���ȓ��̍ĖK��Ґ��ł��B</p>\n";
	print "<hr noshade>\n";
	print "$foot";
	print "</body>\n";
	print "</html>\n";
	exit;
}

#==================== �z�X�g�ʓ��v =================================================

sub host_view {
	
	($logpage,$startday) = split(/,/, $logdata);
	if ($FORM{'page'} eq 'all') { $logpage = '&lt;�S�y�[�W&gt;'; }
	else { $logpage = "<a href=\"$logpage\">$logpage</a>"; }
	($sday,$a,$b,$c,$d,$e,$f,$g) = split(/,/, $FILE[$#FILE]);
	
	print "<h2 align=\"center\">�z�X�g�ʃA�N�Z�X���v</h2>\n";
	print "<p align=\"center\">$logpage</p>\n";
	print "<p align=\"center\"><small><i>���v���� $sday �` $times�@�i�݌v $total��j</i></small></p>\n";
	print "<div align=\"center\"><center>\n";
	print "<table border=\"3\" cellpadding=\"3\" cellspacing=\"3\" width=\"80%\">\n";
	print "  <tr>\n";
	print "    <td width=\"30%\" align=\"center\" bgcolor=\"$hclr\"><b>�z�X�g</b></td>\n";
	print "    <td width=\"20%\" align=\"center\" bgcolor=\"$hclr\"><b>�q�b�g��</b></td>\n";
	print "    <td width=\"50%\" align=\"center\" bgcolor=\"$hclr\"><b>�O���t</b></td>\n";
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
	print "<p align=\"center\">���v�͏��<b>$end</b>����\\�����Ă��܂��B���i��$days���ȓ��̍ĖK��Ґ��ł��B</p>\n";
	print "<hr noshade>\n";
	print "$foot";
	print "</body>\n";
	print "</html>\n";
	exit;
}

#==================== �G�[�W�F���g�ʓ��v ===========================================

sub agent_view {
	
	($logpage,$startday) = split(/,/, $logdata);
	if ($FORM{'page'} eq 'all') { $logpage = '&lt;�S�y�[�W&gt;'; }
	else { $logpage = "<a href=\"$logpage\">$logpage</a>"; }
	($sday,$a,$b,$c,$d,$e,$f,$g) = split(/,/, $FILE[$#FILE]);
	
	print "<h2 align=\"center\">�G�[�W�F���g�ʃA�N�Z�X���v</h2>\n";
	print "<p align=\"center\">$logpage</p>\n";
	print "<p align=\"center\"><small><i>���v���� $sday �` $times�@�i�݌v $total��j</i></small></p>\n";
	print "<div align=\"center\"><center>\n";
	print "<table border=\"3\" cellpadding=\"3\" cellspacing=\"3\" width=\"80%\">\n";
	print "  <tr>\n";
	print "    <td width=\"30%\" align=\"center\" bgcolor=\"$hclr\"><b>�G�[�W�F���g</b></td>\n";
	print "    <td width=\"20%\" align=\"center\" bgcolor=\"$hclr\"><b>�q�b�g��</b></td>\n";
	print "    <td width=\"50%\" align=\"center\" bgcolor=\"$hclr\"><b>�O���t</b></td>\n";
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
	print "<p align=\"center\">���v�͏��<b>$end</b>����\\�����Ă��܂��B���i��$days���ȓ��̍ĖK��Ґ��ł��B</p>\n";
	print "<hr noshade>\n";
	print "$foot";
	print "</body>\n";
	print "</html>\n";
	exit;
}

#==================== �����N���ʓ��v ===============================================

sub link_view {
	
	($logpage,$startday) = split(/,/, $logdata);
	if ($FORM{'page'} eq 'all') { $logpage = '&lt;�S�y�[�W&gt;'; }
	else { $logpage = "<a href=\"$logpage\">$logpage</a>"; }
	($sday,$a,$b,$c,$d,$e,$f,$g) = split(/,/, $FILE[$#FILE]);
	
	print "<h2 align=\"center\">�����N���ʃA�N�Z�X���v</h2>\n";
	print "<p align=\"center\">$logpage</p>\n";
	print "<p align=\"center\"><small><i>���v���� $sday �` $times�@�i�݌v $total��j</i></small></p>\n";
	print "<div align=\"center\"><center>\n";
	print "<table border=\"3\" cellpadding=\"3\" cellspacing=\"3\" width=\"80%\">\n";
	print "  <tr>\n";
	print "    <td width=\"30%\" align=\"center\" bgcolor=\"$hclr\"><b>�����N��</b></td>\n";
	print "    <td width=\"20%\" align=\"center\" bgcolor=\"$hclr\"><b>�q�b�g��</b></td>\n";
	print "    <td width=\"50%\" align=\"center\" bgcolor=\"$hclr\"><b>�O���t</b></td>\n";
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
	print "<p align=\"center\">���v�͏��<b>$end</b>����\\�����Ă��܂��B���i��$days���ȓ��̍ĖK��Ґ��ł��B</p>\n";
	print "<hr noshade>\n";
	print "$foot";
	print "</body>\n";
	print "</html>\n";
	exit;
}

#==================== �L�[���[�h�ʓ��v =============================================

sub keyword_view {
	
	($logpage,$startday) = split(/,/, $logdata);
	if ($FORM{'page'} eq 'all') { $logpage = '&lt;�S�y�[�W&gt;'; }
	else { $logpage = "<a href=\"$logpage\">$logpage</a>"; }
	($sday,$a,$b,$c,$d,$e,$f,$g) = split(/,/, $FILE[$#FILE]);
	
	print "<h2 align=\"center\">�L�[���[�h�ʃA�N�Z�X���v</h2>\n";
	print "<p align=\"center\">$logpage</p>\n";
	print "<p align=\"center\"><small><i>���v���� $sday �` $times�@�i�݌v $total��j</i></small></p>\n";
	print "<div align=\"center\"><center>\n";
	print "<table border=\"3\" cellpadding=\"3\" cellspacing=\"3\" width=\"80%\">\n";
	print "  <tr>\n";
	print "    <td width=\"30%\" align=\"center\" bgcolor=\"$hclr\"><b>�L�[���[�h</b></td>\n";
	print "    <td width=\"20%\" align=\"center\" bgcolor=\"$hclr\"><b>�q�b�g��</b></td>\n";
	print "    <td width=\"50%\" align=\"center\" bgcolor=\"$hclr\"><b>�O���t</b></td>\n";
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
	print "<p align=\"center\">���v�͏��<b>$end</b>����\\�����Ă��܂��B���i��$days���ȓ��̍ĖK��Ґ��ł��B</p>\n";
	print "<hr noshade>\n";
	print "$foot";
	print "</body>\n";
	print "</html>\n";
	exit;
}

#==================== �A�N�Z�X�ʓ��v =============================================

sub log_view {
	
	($logpage,$startday) = split(/,/, $logdata);
	$logpage = "<a href=\"$logpage\">$logpage</a>";
	($sday,$a,$b,$c,$d,$e,$f,$g) = split(/,/, $FILE[$#FILE]);
	
	print "<h2 align=\"center\">�ʃA�N�Z�X���v</h2>\n";
	print "<p align=\"center\">$logpage</p>\n";
	print "<p align=\"center\"><small><i>���v���� $sday �` $times�@�i�݌v $total��j</i></small></p>\n";
	print "<div align=\"center\"><center>\n";
	print "<table border=\"3\" cellpadding=\"3\" cellspacing=\"3\" width=\"100%\">\n";
	print "  <tr>\n";
	print "    <td align=\"center\" bgcolor=\"$hclr\"><b>�K���</b></td>\n";
	print "    <td align=\"center\" bgcolor=\"$hclr\"><b>�O��K���</b></td>\n";
	print "    <td align=\"center\" bgcolor=\"$hclr\"><b>�z�X�g</b></td>\n";
	print "    <td align=\"center\" bgcolor=\"$hclr\"><b>�G�[�W�F���g</b></td>\n";
	print "    <td align=\"center\" bgcolor=\"$hclr\"><b>�����N��</b></td>\n";
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
	print "<p align=\"center\">���v�͍ŋ߂̃A�N�Z�X<b>$end</b>����\\�����Ă��܂��B</p>\n";
	print "<hr noshade>\n";
	print "$foot";
	print "</body>\n";
	print "</html>\n";
	exit;
}

#==================== �y�[�W�ʓ��v =================================================

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
	
	print "<h2 align=\"center\">�y�[�W�ʃA�N�Z�X���v</h2>\n";
	print "<p align=\"center\"><small><i>���v���� $sday �` $times�@�i�݌v $total��j</i></small></p>\n";
	print "<div align=\"center\"><center>\n";
	print "<table border=\"3\" cellpadding=\"3\" cellspacing=\"3\" width=\"80%\">\n";
	print "  <tr>\n";
	print "    <td width=\"30%\" align=\"center\" bgcolor=\"$hclr\"><b>�y�[�W</b></td>\n";
	print "    <td width=\"20%\" align=\"center\" bgcolor=\"$hclr\"><b>�q�b�g��</b></td>\n";
	print "    <td width=\"50%\" align=\"center\" bgcolor=\"$hclr\"><b>�O���t</b></td>\n";
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
	print "<p align=\"center\">���v�͏��<b>$end</b>����\\�����Ă��܂��B���i��$days���ȓ��̍ĖK��Ґ��ł��B</p>\n";
	print "<hr noshade>\n";
	print "$foot";
	print "</body>\n";
	print "</html>\n";
	exit;
}

#==================== CSV�`���ŏo�� ================================================

sub csv {
	shift(@FILE);
	unshift(@FILE,"���t,�j��,����,�z�X�g,�����N��,�G�[�W�F���g,�L�[���[�h,�O��K���\n");
	$j = 0;
	print "Content-type: text/plain\n\n";
	foreach (@FILE) {
		if ($j > $end) { last; }
		print $_;
		$j ++;
	}
	exit;
}

#==================== �X�^�[�g�y�[�W ===============================================

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
      <td align="right" width="40%"><h2>��͑Ώۂ�</h2>
      <p>�@</td>
      <td bgcolor="$rclr" width="60%"><h2>�I�����Ă�������</h2>
      <p>�@</td>
    </tr>
    <tr>
      <td align="right" width="40%"><small>��̓y�[�W �F</small></td>
      <td bgcolor="$rclr" width="60%"><select name="page" size="1">
        <option value="all">�S�Ẵy�[�W</option>
HTML
	foreach (@LOGS) {
		print "        <option>$_</option>\n";
	}
	if ($open) { $psmsg = '      <tr><td align="right" width="40%"><small>�p�X���[�h��</small></td>' .
	                      "      <td bgcolor=\"$rclr\" width=\"60%\"><small>���O�����Z�b�g����ꍇ�̂ݓ���</small></td></tr>" }
print <<"HTML";
      </select></td>
    </tr>
    <tr>
      <td align="right" width="40%"><small>��͍��� �F</small></td>
      <td bgcolor="$rclr" width="60%"><select name="type" size="1">
        <option value="date">���t��</option>
        <option value="time">���ԕ�</option>
        <option value="week">�j����</option>
        <option value="host">�z�X�g��</option>
        <option value="link">�����N����</option>
        <option value="page">�y�[�W��</option>
        <option value="agent">�G�[�W�F���g��</option>
        <option value="keyword">�L�[���[�h��</option>
        <option value="log">�A�N�Z�X��</option>
        <option value="csv">CSV�`��</option>
        <option value="0">------------</option>
        <option value="reset">���O�̃��Z�b�g</option>
      </select></td>
    </tr>
    <tr>
      <td align="right" width="40%"><small>�\\������ �F</small></td>
      <td bgcolor="$rclr" width="60%"><select name="max" size="1">
        <option value="10">10��</option>
        <option value="20">20��</option>
        <option value="50" selected>50��</option>
        <option value="100">100��</option>
        <option value="200">200��</option>
        <option value="300">300��</option>
        <option value="400">400��</option>
        <option value="500">500��</option>
      </select></td>
    </tr>
    <tr>
      <td align="right" width="40%"><small>�p�X���[�h �F</small></td>
      <td bgcolor="$rclr" width="60%"><input type="password" name="pass" size="20" maxlength="10"></td>
    </tr>
    <tr>
      <td align="right" width="40%"><br>
      </td>
      <td bgcolor="$rclr" width="60%">�@�@<br>
      <input type="submit" value="�@ \OK �@"><input type="reset" value="�~"><br>
      �@�@</td>
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

#==================== ���O�̃��Z�b�g ===============================================

sub delete {
	if ($FORM{'pass'} ne $pass) { &error('�p�X���[�h���s���ł��B'); }
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

#==================== ���O�̋L�^ ===================================================

sub input {
	
	#----- ��{���̐ݒ� -----------------------
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
	
	#----- ���ϐ��̐ݒ� -----------------------
	$agent = $ENV{'HTTP_USER_AGENT'};
	$href = $ENV{'HTTP_REFERER'};
	$host = $ENV{'REMOTE_HOST'};
	$addr = $ENV{'REMOTE_ADDR'};
	if ($host eq $addr) { $host = gethostbyaddr(pack('C4',split(/\./,$host)),2) || $addr; }
	if ($host =~ /(.*)\.(.*)\.(.*)\.(.*)$/) { $host = "\*\.$2\.$3\.$4"; }
	elsif ($host =~ /(.*)\.(.*)\.(.*)$/) { $host = "\*\.$2\.$3"; }
	
	$key = $link;
	$link =~ s/(.*)\?.*/$1?/i;
	
	#----- �T�[�`�G���W���̔��� -----------------
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
	
	
	#----- �L�[���[�h�̎擾 ---------------------
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
	
	#----- �O��K����̎擾 ---------------------
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
	
	#----- �s�����p�h�~ -------------------------
	if ($href !~ /$turl/ && $turl ne '') { $no_count = 1; }
	
	#----- �w�莞�ԓ��̍ĖK��̓J�E���g���Ȃ� ---
	if (!$no_count) {
		
		#----- �t�@�C���̓ǂݍ��� -------------------
		@FILE = &template'read_file($datafile);
		if ($max < $#FILE) { splice(@FILE, $max); }
		
		$agent =~ s/,/&#44;/g;
		shift(@FILE);
		$data = "$times,$week,$hour,$host,$link,$agent,$keyword,$repert\n";
		unshift(@FILE, $data);
		unshift(@FILE, "$href,\n");
		
		#----- �t�@�C���֏�������/���b�N ------------
		&template'lock_check($lockfile,$lock);
		&template'file_lock($tempfile,$datafile,$lockfile,$lock,@FILE,"");
		
	}
	
	#----- �_�~�[�摜��Ԃ� ---------------------
	print "Content-type: image/gif\n";
	if ($cookie) { print "Set-Cookie: $FORM{'file'}=repert:$ctime; expires=$cdate\n"; }
	print "\n";
	&template'include($image);
	exit;

}

#==================== �G���[���� ===================================================

sub error {
	local($msg) = @_;
	if (!$msg) { $msg = '�����s���̃G���[�ɂ��C�����������I�����܂��B'; }
	print "Content-type: text/html\n\n";
print <<"HTML";
<html>
<head>
<title>$title [�V�X�e���G���[]</title>
<meta http-equiv="Content-Type" content="text/html; charset=$fcode">
</head>
<body>
<p>�@</p>
<div align="center"><center>
<table border="1" width="80%" cellpadding="5" cellspacing="0">
  <tr>
    <td width="100%" bgcolor="#0000FF" align="center"><b><font color="#FFFFFF">�V�X�e���G���[</font></b></td>
  </tr>
  <tr>
    <td width="100%"><p align="center">�@�@<br>
    <font color="#FF0000">���̃v���O�����͕s���ȏ������s�����̂ŋ����I������܂��B</font></p>
    <hr noshade size="1">
    <div align="center"><center><table border="0">
      <tr>
        <td><b>$msg</b></td>
      </tr>
    </table>
    </center></div>
    <hr noshade size="1">
    <blockquote>
      <p>�@���N�G�X�g�������ɕs���Ȗ��߂����s���ꂽ���߁C���̏����������I�����܂��B�G���[�̔��������Ƃ��ă��N�G�X�g���s���m�C�Ǘ��҂��A�N�Z�X�����^�����Ă��Ȃ��C������ݒ肪�Ȃ���Ă��铙�̉\\��������܂��B�G���[���������Ȃ��ꍇ�͂��̃T�C�g�̊Ǘ��҂ɘA�����Ă��������B</p>
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

