const express = require('express');
const http = require('http');
const app = express();
const bodyParser= require("body-parser");
app.use(express.static('public/views'));
app.use(express.static('public/scripts'));
app.set('views', __dirname+'/public/views');
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({extended: false}));

const server = app.listen(8000, () => {
    console.log('server is running at port 8000');	
});



app.get('/', (req, res) => {
	var myPythonScriptPath = 'weather_crawl.py';

	// Use python shell
	var {PythonShell} = require('python-shell');
	var pyshell = new PythonShell(myPythonScriptPath);
	var data;
	pyshell.on('message', function (message) {
		console.log(message);
		res.render('yesweather.ejs' , JSON.parse(message));
	});
    
})
app.get('/rainy', (req, res) => {
   const data={"avg_temp": "17.8", "min_temp": "15.9", "max_temp": "20.1", "precip": "38.3", "snow": "0", "wind": "1.4", "humid": "86.9", "sun": "0.0", "cloud": "9.8", "sky": "rainy", "comment": "\uc800\ub7f0! \uc5b4\uc81c \ube44\uac00 \uc654\ub124\uc694. \ud639\uc2dc \uac10\uae30\uc5d0 \uac78\ub9ac\uc2dc\uc9c0\ub294 \uc54a\uc73c\uc168\ub098\uc694?", "isDay": "1", "t0_time": "21", "t0_weather": "rainy", "t0_temp": "16.0", "t0_isDay": "0", "t1_time": "18", "t1_weather": "little_grey", "t1_temp": "16.6", "t1_isDay": "0", "t2_time": "15", "t2_weather": "sunny", "t2_temp": "21.8", "t2_isDay": "1", "t3_time": "12", "t3_weather": "foggy", "t3_temp": "19.3", "t3_isDay": "1", "t4_time": "9", "t4_weather": "foggy", "t4_temp": "12.9", "t4_isDay": "1", "t5_time": "6", "t5_weather": "foggy", "t5_temp": "11.2", "t5_isDay": "1", "t6_time": "3", "t6_weather": "foggy", "t6_temp": "11.5", "t6_isDay": "0", "t7_time": "0", "t7_weather": "foggy", "t7_temp": "12.3", "t7_isDay": "0"};

   console.log(data);
   res.render('yesweather.ejs', data);
   /*resolve(res);*/
})

app.get('/hot', (req, res) => {
   const data={"avg_temp": "29.0", "min_temp": "26.2", "max_temp": "33.1", "precip": "0", "snow": "0", "wind": "1.2", "humid": "78.3", "sun": "7.6", "cloud": "7.5", "sky": "little_grey", "comment": "\uc5b4\uc81c\ub294 \ud750\ub9b0 \ub0a0\uc774\uc5c8\uc5b4\uc694. \uc624\ub298\uc740 \uc5b4\ub5a8\uae4c\uc694?", "isDay": "0", "t0_time": "12", "t0_weather": "little_grey", "t0_temp": "30.7", "t0_isDay": "1", "t1_time": "18", "t1_weather": "little_grey", "t1_temp": "16.6", "t1_isDay": "0", "t2_time": "15", "t2_weather": "sunny", "t2_temp": "21.8", "t2_isDay": "1", "t3_time": "12", "t3_weather": "foggy", "t3_temp": "19.3", "t3_isDay": "1", "t4_time": "9", "t4_weather": "foggy", "t4_temp": "12.9", "t4_isDay": "1", "t5_time": "6", "t5_weather": "foggy", "t5_temp": "11.2", "t5_isDay": "1", "t6_time": "3", "t6_weather": "foggy", "t6_temp": "11.5", "t6_isDay": "0", "t7_time": "0", "t7_weather": "foggy", "t7_temp": "12.3", "t7_isDay": "0"};

   console.log(data);
   res.render('yesweather.ejs', data);
   /*resolve(res);*/
})

app.get('/snowy', (req, res) => {
   const data={"avg_temp": "-0.8", "min_temp": "-2.8", "max_temp": "0.4", "precip": "3.0", "snow": "4.6", "wind": "0.5", "humid": "76.6", "sun": "0.0", "cloud": "9.0", "sky": "snowy", "comment": "\uc5b4\uc81c\ub294 \ub208\uc774 \uc654\uc5b4\uc694! \uce5c\uad6c\ub4e4\uacfc \uc990\uac70\uc6b4 \ud558\ub8e8 \ubcf4\ub0b4\uc168\ub098\uc694?", "isDay": "0", "t0_time": "21", "t0_weather": "foggy", "t0_temp": "0.1", "t0_isDay": "0", "t1_time": "18", "t1_weather": "little_grey", "t1_temp": "16.6", "t1_isDay": "0", "t2_time": "15", "t2_weather": "sunny", "t2_temp": "21.8", "t2_isDay": "1", "t3_time": "12", "t3_weather": "foggy", "t3_temp": "19.3", "t3_isDay": "1", "t4_time": "9", "t4_weather": "foggy", "t4_temp": "12.9", "t4_isDay": "1", "t5_time": "6", "t5_weather": "foggy", "t5_temp": "11.2", "t5_isDay": "1", "t6_time": "3", "t6_weather": "foggy", "t6_temp": "11.5", "t6_isDay": "0", "t7_time": "0", "t7_weather": "foggy", "t7_temp": "12.3", "t7_isDay": "0"};

   console.log(data);
   res.render('yesweather.ejs', data);
   /*resolve(res);*/
})

app.get('/windy', (req, res) => {
   const data={"avg_temp": "26.2", "min_temp": "23.9", "max_temp": "29.9", "precip": "1.5", "snow": "0", "wind": "5.5", "humid": "81.4", "sun": "0.6", "cloud": "9.3", "sky": "rainy", "comment": "\uc800\ub7f0! \uc5b4\uc81c \ube44\uac00 \uc654\ub124\uc694. \ud639\uc2dc \uac10\uae30\uc5d0 \uac78\ub9ac\uc2dc\uc9c0\ub294 \uc54a\uc73c\uc168\ub098\uc694?", "isDay": "0", "t0_time": "21", "t0_weather": "rainy", "t0_temp": "24.1", "t0_isDay": "0", "t1_time": "18", "t1_weather": "little_grey", "t1_temp": "16.6", "t1_isDay": "0", "t2_time": "15", "t2_weather": "sunny", "t2_temp": "21.8", "t2_isDay": "1", "t3_time": "12", "t3_weather": "foggy", "t3_temp": "19.3", "t3_isDay": "1", "t4_time": "9", "t4_weather": "foggy", "t4_temp": "12.9", "t4_isDay": "1", "t5_time": "6", "t5_weather": "foggy", "t5_temp": "11.2", "t5_isDay": "1", "t6_time": "3", "t6_weather": "foggy", "t6_temp": "11.5", "t6_isDay": "0", "t7_time": "0", "t7_weather": "foggy", "t7_temp": "12.3", "t7_isDay": "0"};

   console.log(data);
   res.render('yesweather.ejs', data);
   /*resolve(res);*/
})
