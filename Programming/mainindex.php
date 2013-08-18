<?php
#Runs piano bar if ON button is pressed
if ($_GET['on']) {
	exec("pianobar")
}
?>

<html>
<head>
<style>

body
{
background-color:rgb(24,24,24);
color:white;
font-family:"Arial Black", Gadget, sans-serif;
min-width:300px;
}

h1
{
text-align:center;
font-size:60px;
}

h4
{
text-align:left;
font-size:10px;
color:rgb(90,90,90);
position:absolute;
bottom:5px;
}

.volbutton {
	display: block;
	height: 27.5%;
	width: 25%;
	background: rgb(65,65,65);
	font-size:40px;
	font-family:"Arial Black", Gadget, sans-serif;
	text-align: center;
	border: 2px solid rgb(55,55,55);
	color: white;
	border-radius: 15px;
	text-shadow: 0 2px 2px rgba(255,255,255,0.2);
	-webkit-box-shadow: 0 3px 0 rgb(50,50,50);
	box-shadow: 0 3px 0 rgb(50,50,50);
}
a.volbutton {
	text-decoration: none;
}

.skipbutton {
	display: block;
	height: 12.5%;
	width: 25%;
	background: rgb(65,65,65);
	font-size:40px;
	font-family:"Arial Black", Gadget, sans-serif;
	text-align: center;
	border: 2px solid rgb(55,55,55);
	color: white;
	border-radius: 15px;
	text-shadow: 0 2px 2px rgba(255,255,255,0.2);
	-webkit-box-shadow: 0 3px 0 rgb(50,50,50);
	box-shadow: 0 3px 0 rgb(50,50,50);
}
a.skipbutton {
	text-decoration: none;
}

.chbutton {
	display: block;
	height: 12.5%;
	width: 60%;
	background: rgb(65,65,65);
	font-size:40px;
	font-family:"Arial Black", Gadget, sans-serif;
	text-align: center;
	border: 2px solid rgb(55,55,55);
	color: white;
	border-radius: 15px;
	text-shadow: 0 2px 2px rgba(255,255,255,0.2);
	-webkit-box-shadow: 0 3px 0 rgb(50,50,50);
	box-shadow: 0 3px 0 rgb(50,50,50);
	}
a.chbutton {
	text-decoration: none;
}


</style>
<title>Raspi Radio Remote</title>
</head>

<body>
<h1>Raspi Radio Remote</h1>

<a href="http://google.com/" style="position:absolute; right:5%; top:20%;" class="volbutton">+</a> 

<a href="http://google.com/" style="position:absolute; right:5%; top:50%;" class="volbutton">-</a>

<a href="?on" type="submit" style="position:absolute; right:5%; top:80%;" class="skipbutton">ON(temp)</a>

<a href="http://google.com/" style="position:absolute; top:20%; left:5%" class="chbutton">1 - Classic Rock</a> 

<a href="http://google.com/" class="chbutton" style="position:absolute; top:35%; left:5%;">2 - Classical</a>

<a href="http://google.com/" class="chbutton" style="position:absolute; top:50%;left:5%;">3 - Club/Dance</a> 

<a href="http://google.com/" class="chbutton" style="position:absolute; top:65%; left:5%;">4 - Rap</a>

<a href="http://google.com/" style="position:absolute; top:80%; left:5%" class="chbutton">5 - Today's Hits</a> 


<h4>
More info at github.com/mkukar/RaspiRadio <br>
Michael Kukar 2013
</h4>

</body>

</html>
