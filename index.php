<HEAD>
<STYLE TYPE="text/css">
a:link, a:visited {

    font-weight: bold;
    color: #ffffff;
    background-color: #98bf21;
    width: 120px;
    text-align: center;
    padding: 4px;
    text-decoration: none;
}

a:hover, a:active {
    background-color: #7A991A;
}
</STYLE>
<meta name="viewport" content="width=device-width">
</HEAD>
<form method='post'>
<center><img width="80%" src='youthgarden.svg'><br><br>
<a href="http://www.psdr3.org/garden">Garden Home</a> | <a href="http://www.psdr3.org/garden/history">Photos</a> | <a href="http://www.psdr3.org/garden_timelapse_2015.mp4">Timelapse Movie</a></center><br><br>

<table width="100%"><tr ><td align=center><input type=submit name=zone1 value="Zone1"></td><td align=center></td><td align=center><input type=submit name=zone2 value="Zone 2"></td></tr>
<tr><td align=center>
<select name="zone1time">
  <option value="">-Water-Timer-</option>
  <option value="5">5</option>
  <option value="10">10</option>
  <option value="15">15</option>
  <option value="20">20</option>
  <option value="25">25</option>
  <option value="30">30</option>
  <option value="45">45</option>
  <option value="60">60</option>
  <option value="90">90</option>
  <option value="120">120</option>
</select>	
</td><td align=center>North</td><td align=center>
<select name="zone2time">
  <option value="">-Water-Timer-</option>
  <option value="5">5</option>
  <option value="10">10</option>
  <option value="15">15</option>
  <option value="20">20</option>
  <option value="25">25</option>
  <option value="30">30</option>
  <option value="45">45</option>
  <option value="60">60</option>
  <option value="90">90</option>
  <option value="120">120</option>
</select>	
</td></tr></table>
<center><img src='/garden.jpg' width="80%"><center>
<!--<center><img src='http://plans.garden-planner.net/uploads/plan-previews/581347.jpg' width="400" height="400"></center>-->
<table width="100%"><tr><td align=center><input type=submit name=zone4 value="Zone 4"></td><td align=center>South</td><td align=center><input type=submit name=zone3 value="Zone 3"></td></tr>
<tr><td align=center>
<select name="zone4time">
  <option value="">-Water-Timer-</option>
  <option value="5">5</option>
  <option value="10">10</option>
  <option value="15">15</option>
  <option value="20">20</option>
  <option value="25">25</option>
  <option value="30">30</option>
  <option value="45">45</option>
  <option value="60">60</option>
  <option value="90">90</option>
  <option value="120">120</option>
</select>	
</td><td align=center></td><td align=center>
<select name="zone3time">
  <option value="">-Water-Timer-</option>
  <option value="5">5</option>
  <option value="10">10</option>
  <option value="15">15</option>
  <option value="20">20</option>
  <option value="25">25</option>
  <option value="30">30</option>
  <option value="45">45</option>
  <option value="60">60</option>
  <option value="90">90</option>
  <option value="120">120</option>
</select>	
</td></tr></table>
<br>
<center>West<br><img width="80%" src='http://www.psdr3.org/images/youthgarden.jpg'><br>East</center>
<?php
if ($_REQUEST['zone1']) {echo 'triggered';
	exec('sudo python /home/pi/TSA-Garden/Garden.py 0 '.($_REQUEST['zone1time'])*60).' > /dev/null 2>&1 &';
} else if ($_REQUEST['zone2']){
	exec('sudo python /home/pi/TSA-Garden/Garden.py 1 '.($_REQUEST['zone2time'])*60).' > /dev/null 2>&1 &';
} else if ($_REQUEST['zone3']){
	exec('sudo python /home/pi/TSA-Garden/Garden.py 2 '.($_REQUEST['zone3time'])*60).' > /dev/null 2>&1 &';
} else if ($_REQUEST['zone4']){
	exec('sudo python /home/pi/TSA-Garden/Garden.py 3 '.($_REQUEST['zone4time'])*60).' > /dev/null 2>&1 &';
}
$home = "/var/www/garden.psdr3.org/";
//$home = "/Users/ladmin/Sites/Web/garden.psdr3.org/";
$options = array(
  'http'=>array(
    'method'=>"GET",
    'header'=>"Accept-language: en\r\n" .
              "Cookie: foo=bar\r\n" .  // check function.stream-context-create on php.net
              "User-Agent: Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B334b Safari/531.21.102011-10-16 20:23:10\r\n" // i.e. An iPad 
  )
);

$context = stream_context_create($options);

$past = $home."past.txt";
$garden = $home."garden.jpg";
if (file_exists($past) && ((time() - filemtime($past)) < 1800)) {
	$file  = file_get_contents($past);
	
} else { 
//	$pict =  file_get_contents("http://plans.garden-planner.net/uploads/plans/581347.jpg");
	$file = file_get_contents("http://w1.weather.gov/xml/current_obs/KSTL.xml", false, $context);
	$cached = fopen_recursive($past, "w");
	fwrite($cached, $file);
	fclose($cached);
//	$cached = fopen_recursive($garden, "w");
//	fwrite($cached, $pict);
//	fclose($cached);
}
	
$xml=simplexml_load_string($file);
echo "\n<br><b><a href='http://w1.weather.gov/xml/current_obs/KSTL.xml'>Currently</a></b><br><br>\n";
echo "Temperature ".preg_replace( "/ \(.*\)/","" , $xml->temperature_string)."<br>\n";
echo $xml->weather."<br>\n";
echo "Wind ".preg_replace( "/ \(.*\)/","" , $xml->wind_string)."<br>\n";


$obsv = $home."obsv.txt";
if (file_exists($obsv) && ((time() - filemtime($obsv)) < 1800)) {
	$file  = file_get_contents($obsv);
} else { 
	$file = file_get_contents("http://w1.weather.gov/obhistory/KSTL.html", false, $context);
	$cached = fopen_recursive($obsv, "w");
	fwrite($cached, $file);
	fclose($cached);
}

	
preg_match_all('/\<tr align\=\"center\" valign\=\"top\" bgcolor\=\"\#\w\w\w\w\w\w\"\>\<td\>(\d+)\<\/td\>\<td align\=\"right\"\>(\d\d\:\d\d)\<\/td\>\<td\>([^<]+)\<\/td\>\<td\>([^<]+)\<\/td\>\<td align\=\"left\"\>([^<]+)\<\/td\>\<td\>([^<]+)\<\/td\>\<td\>([^<]+)\<\/td\>\<td\>([^<]+)\<\/td\>\s+\n?\s?\<td\>([^<]+|)\<\/td\>\<td\>([^<]+|)\<\/td\>\<td\>(\d+)\%\<\/td\>\<td\>([^<]+)\<\/td\>\<td\>([^<]+)\<\/td\>\<td\>(\d\d\.?\d?\d?)\<\/td\>\<td\>(\d+\.?\d?)\<\/td\>\<td\>([^<]+|)\<\/td\>\<td\>([^<]+|)\<\/td\>\<td\>([^<]+|)\<\/td\>\<\/tr\>/',$file,$matches);
//print_r($matches);
echo "\n<br><b><a href='http://w1.weather.gov/obhistory/KSTL.html'>Past 3 Days</a></b><br><br>\n";
$temp = round((array_sum($matches[7])/count($matches[7]))); echo $temp." F Average Temperature<br>\n"; 
$humid = round((array_sum($matches[11])/count($matches[11]))); echo $humid."% Average Humidty<br>\n";
$osun=0;
foreach ($matches[6] as $sky) {
	if ($sky=="CLR") { $osun+=1;}
	else if ($sky=="OVC") { $osun+=1;}
	else {
	preg_match('/(\w\w\w)\d\d\d$/',$sky,$cc);
	//if (!$cc[1])  {echo $sky;}
	$cc=$cc[1];
	if ($cc=="CLR")	{ $osun+=1;}
	else if ($cc=="FEW")	{ $osun+=.75;}
	else if ($cc=="SCT")	{ $osun+=.5;}
	else if ($cc=="BKN")	{ $osun+=.25;}
	//else {echo $cc;}
	}
}
// Calculate Season Month Modifier
date_default_timezone_set('UTC');
$month = date("n");
if ($month > 5 ) { $month -= 6;}
else if ($month < 6 ) { $month = 6 - $month; }
$month =+ 1; $season = 1.5 / $month;

$sun = round((($osun/count($matches[6]))*100)); echo $sun."% Sunlight Strength<br>\n";

$owind=0;$ocout=0;
foreach ($matches[3] as $winds) {
	if ($winds != "Calm") {
		preg_match('/^\w+ (\d+)/',$winds,$cc);
		$owind+=$cc[1];
	}
	$ocout++;
}
$wind = round(($owind/$ocout)*1.15078); echo $wind." MPH Average Windspeed<br>\n";
$rain = array_sum($matches[16]); echo $rain." IN of Rain Recorded<br>\n";
$evap = round((((( $temp + $sun + ($wind * 4) )/3) + (100 - $humid))/2)-($rain*25)); 
if ($evap < 0 ) {$evap = 0;}
echo $evap."% Evaporation Rate<br>\n";

$soon = $home."soon.txt";
if (file_exists($soon) && ((time() - filemtime($soon)) < 1800)) {
	$lines = file($soon);
} else { 
	$file = file_get_contents("http://www.nws.noaa.gov/cgi-bin/mos/getmav.pl?sta=KSTL", false, $context);
	$cached = fopen_recursive($soon, "w");
	fwrite($cached, $file);
	fclose($cached);
	$lines = file($soon);
}


echo "\n<br><b><a href='http://www.nws.noaa.gov/cgi-bin/mos/getmav.pl?sta=KSTL'>Next 3 Days</a></b><br><br>\n";
$sunl=0;$rm=0;$rx=0;$prh=0;
foreach ($lines as $line_num => $line) {
//	if ($line_num > 4 && $line_num < 27) {echo "Line #{$line_num} : " . htmlspecialchars($line) . "\n";}
	if ($line_num == 6) {
		preg_match_all('/\/([A-Z]+)\s+(\d+)/',$line,$dates);
		//print_r($dates);
	} else if ($line_num == 7) {
		preg_match_all('/(\d+)/',$line,$time);
		$days[$dates[1][0].$dates[2][0]] = 0;
		$d = 1;
		for ($i = 0; $i < count($time[1]); $i++) {
			if ($i > 0 && $time[1][$i] == "00") {
				$days[$dates[1][$d].$dates[2][$d]] = $i;$d++; 	
			}
		}
		//print_r($days);
	} else if ($line_num == 9) {
		preg_match_all('/(\d+)/',$line,$temp);
		$ptemp = round((array_sum($temp[1])/count($temp[1])));
		echo "High ".max($temp[1])." F Low ".min($temp[1])." F<br>\n"; 
		echo $ptemp." F Average Temperature<br>\n";
	} else if ($line_num == 10) {
		preg_match_all('/(\d+)/',$line,$dew);
		for ($i = 0; $i < count($dew[1]); $i++) {
			$ct = ($temp[1][$i] - 32) * (5/9);
			$cd = ($dew[1][$i] - 32) * (5/9);
			$rh= round(100*(EXP((17.625*$cd)/(243.04+$cd))/EXP((17.625*$ct)/(243.04+$ct))));
			$prh+=$rh;
		}
		$phumid = round($prh/count($temp[1]));echo $phumid."% Average Humidty<br>\n";	
		//print_r($times);
	} else if ($line_num == 11) {
		$sunl = 0;
		preg_match_all('/ (\w\w)/',$line,$cloud);
		foreach ($cloud[1] as $cc) {
			if ($cc=="CL")	{ $sunl+=1;}
			else if ($cc=="FW")	{ $sunl+=.75;}
			else if ($cc=="SC")	{ $sunl+=.5;}
			else if ($cc=="BK")	{ $sunl+=.25;}
		}
		
		$psun = round((($sunl/count($cloud[1]))*100));echo $psun."% Sunlight Strength<br>\n";
	} else if ($line_num == 13) {
		preg_match_all('/ (\d+)/',$line,$wind);
		$pwind =  round((array_sum($wind[1])/count($wind[1]))*1.15078);
		echo $pwind." MPH Average Windspeed<br>\n";
	} else if ($line_num == 15) {
		preg_match_all('/ (\d+)/',$line,$chance);
		$pchance = max($chance[1]); echo $pchance."% Chance of Rain<br>\n";
	} else if ($line_num == 17) {
		preg_match_all('/ (\d+)/',$line,$rain);
		foreach ($rain[1] as $rp) {
			if ($rp == 1) { $rm+=.01; $rx+=.09;}
			else if ($rp == 2) { $rm+=.1; $rx+=.24;}
			else if ($rp == 3) { $rm+=.25; $rx+=.49;}
			else if ($rp == 4) { $rm+=.5; $rx+=.99;}
			else if ($rp == 5) { $rm+=1; $rx+=1.99;}
			else if ($rp == 6) { $rm+=2; $rx+=2.5;}
		}
		if ($rm) {
			$prain = ($rm+$rx)/2;
			echo $rm."-".$rx." IN of Rain Predicted<br>\n";
		}
	} else if ($line_num == 20) {
		$pevap = round((((( $ptemp + $psun + ($pwind * 4) )/3) + (100 - $phumid))/2)-($prain*25)); 
		if ($pevap < 0 ) {$pevap = 0;}
		echo $pevap."% Evaporation Rate<br>\n";
		
	}
}

function fopen_recursive($path, $mode, $chmod=0755){
  preg_match('`^(.+)/([a-zA-Z0-9.]+)$`i', $path, $matches);
  $directory = $matches[1];
  $file = $matches[2];

  if (!is_dir($directory)){
    if (!mkdir($directory, $chmod, 1)){
    return FALSE;
    }
  }
 return fopen ($path, $mode);
}

?>
