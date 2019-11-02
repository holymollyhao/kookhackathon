import datetime
import numpy as np
from bs4 import BeautifulSoup
from urllib.request import urlopen
import calendar
import json

dt = datetime.date.today()- datetime.timedelta(days=1)
weekday = dt.weekday()
year = dt.year
month = dt.month
day = dt.day
cal = calendar.monthcalendar(year,month)
c = np.array(cal)
i,j = np.where(c==day)


dict_param = {
    'yy': year,
    'mm': month,
    'obs': 0
}

#tmi = [avg,min,max,precip,snow,wind,humid,sun,cloud,weather]
obs_list = [7,10,8,21,28,6,12,35,59,90]
weather_url = []
res = []

for i in range(len(obs_list)):
    dict_param['obs'] = obs_list[i]
    weather_url.append("http://www.weather.go.kr/weather/climate/past_table.jsp?stn=133&yy={yy}&obs={obs}".format(**dict_param))

row = int(day)
col = int(month)

for i in range(len(obs_list)):
    html = urlopen(weather_url[i])
    source = html.read()
    html.close()

    soup = BeautifulSoup(source, "lxml")
    table_div = soup.find(id="content_weather")
    tables = table_div.find_all("table")
    wt_table = tables[1]
    trs = wt_table.find_all('tr')
    currTr = trs[row]
    tds = currTr.find_all('td')
    if (i < len(obs_list)-1):
        tmp = tds[col].text
        if (tmp=="\xa0"):
            tmp = "0"
        res.append(tmp)
    else:
        tmp = [x for x in tds[col].contents if getattr(x, 'name', None) != 'br']
        res.append(tmp)



sky = ""
if (float(res[8]) >= 9):
    sky = "grey"
elif (float(res[8]) >= 6):
    sky = "little_grey"
elif (float(res[8]) >= 3):
    sky = "little_sunny"
else:
    sky = "sunny"

for x in res[9]:
    if(x=="박무" or x=="연무"):
        sky = "foggy"

if (res[3]!="0"):
    sky = "rainy"

if (res[4]!="0"):
    sky = "snowy"

comment = "기모찌"

#[avg,min,max,precip,snow,wind,humid,sun,cloud,weather]

ret = {
    "avg_temp": res[0],
    "min_temp": res[1],
    "max_temp":res[2],
    "precip":res[3],
    "snow":res[4],
    "wind":res[5],
    "humid":res[6],
    "sun":res[7],
    "cloud":res[8],
    "sky":sky}
print(ret)

