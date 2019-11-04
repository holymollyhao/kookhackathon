# kookhackathon
This project was a made in a 30-h hackathon to create the most useless thing(any) for users.
So, our team made this website "어제의 날씨" that lets the users know yesterday's weather.

## Structure
```
어제의 날씨
├── weather_crawl.py
├── yesweather_server.js
└── scripts,views, etc.
```
* `weather_crawl.py` crawls data from the KMA using python's library, beautiful soup. When the program runs,
it spits out the following information in JSON format: avg_temp, min_temp, max_temp, precip, snow, wind, humid, etc.

* `yesweeather_server.js` is the server for the website. It runs the python program upon basic get request, and using
the JSON output given, renders the ejs file.

## Features

* Using the information of when the sun sets, the website supports darkmode. When the sun is down, the background of the website
and the image of the website changes from sky blue to dark blue, from sun to moon.

<img width="400" height="230" alt="스크린샷 2019-11-03 오후 3 48 48" src="https://user-images.githubusercontent.com/50355670/68081467-cad0d300-fe51-11e9-9d0e-99ec11d36305.png">    <img width="400" alt="스크린샷 2019-11-03 오후 3 01 03" src="https://user-images.githubusercontent.com/50355670/68081251-4e88c080-fe4e-11e9-9cbc-0a034de892d0.png">

* On clicking the "down" button, we get a TMI information. When mouse hovers over the images, the textbox changes to show information.(Also, the page automatically scrolls down)

<img width="400" alt="스크린샷 2019-11-03 오후 3 00 01" src="https://user-images.githubusercontent.com/50355670/68081255-4fb9ed80-fe4e-11e9-9ee4-9173f3dd0176.png">     <img width="400" alt="스크린샷 2019-11-03 오후 3 01 19" src="https://user-images.githubusercontent.com/50355670/68081250-4e88c080-fe4e-11e9-8c20-de54ce1664fe.png">

