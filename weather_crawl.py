# what I have installed using pip
# beautifulsoup4
# lxml
# numpy
# suntime

import datetime
from bs4 import BeautifulSoup, SoupStrainer
from urllib.request import urlopen
import json
from suntime import Sun
import random
import threading

#start_time = datetime.datetime.now()

#Getting the position of yesterday's date on the calender
dt = datetime.datetime.now()- datetime.timedelta(days=1)

#print(str(datetime.datetime.now()))

year = dt.year
month = dt.month
day = dt.day
hour = dt.hour

#Checking if it is day or night
latitude = 36.3504
longitude = 127.3845
sun = Sun(latitude, longitude)
sr_time = (sun.get_sunrise_time()+datetime.timedelta(hours=9)).time()
ss_time = (sun.get_sunset_time()+datetime.timedelta(hours=9)).time()
sr_hour = int(sr_time.hour)
ss_hour = int(ss_time.hour)
curr_time = datetime.datetime.now().time()
isDay = 0
if (sr_time < curr_time < ss_time):
    isDay = 1

#retrieving data
dict_param = {
    'yy': year,
    'mm': month,
    'dd': day,
    'hh': hour,
    'obs': 0
}

def set_dict_param(dict,dtime,disp):
    tmpDT = dtime-datetime.timedelta(hours=disp)
    dict['yy'] = tmpDT.year
    dict['mm'] = tmpDT.month
    dict['dd'] = tmpDT.day
    dict['hh'] = tmpDT.hour
    return tmpDT

#data = [avg,min,max,precip,snow,wind,humid,sun,cloud,weather]
obs_list = [7,10,8,21,28,6,12,35,59,90]
time_list = [int(hour)]
weather_url = []
chart_url = ["http://www.weather.go.kr/weather/observation/currentweather.jsp?type=t99&mode=0&stn=0&reg=133&auto_man=m&tm={yy}.{mm}.{dd}.{hh}:00".format(**dict_param)]
res = []
cres = []

for i in range(len(obs_list)):
    dict_param['obs'] = obs_list[i]
    weather_url.append("http://www.weather.go.kr/weather/climate/past_table.jsp?stn=133&yy={yy}&obs={obs}".format(**dict_param))

for i in range(7):
    if (time_list[-1]%3 == 0):
        dt = set_dict_param(dict_param,dt,3)
    else:
        dt = set_dict_param(dict_param,dt,1)
    time_list.append(int(dict_param['hh']))
    chart_url.append("http://www.weather.go.kr/weather/observation/currentweather.jsp?type=t99&mode=0&stn=0&reg=133&auto_man=m&tm={yy}.{mm}.{dd}.{hh}:00".format(**dict_param))


#processing data
row = int(day)
col = int(month)

source = [None]*len(obs_list)
chart_source = [None]*8

def crawlThread(i):
    #print("thread "+str(i)+" started")
    html = urlopen(weather_url[i])
    source[i] = html.read()
    html.close()
    #print("thread "+str(i)+" finished")

def chartThread(i):
    #print("thread "+str(i)+" started")
    html = urlopen(chart_url[i])
    chart_source[i] = html.read()
    html.close()
    #print("thread "+str(i)+" finished")

threads = list()
for i in range(len(obs_list)):
    x = threading.Thread(target=crawlThread, args=(i,))
    threads.append(x)
    x.start()

for i in range(8):
    x = threading.Thread(target=chartThread, args=(i,))
    threads.append(x)
    x.start()

for t in threads:
    t.join()

only_tables = SoupStrainer("table")

for i in range(len(obs_list)):
    soup = BeautifulSoup(source[i], "lxml",parse_only=only_tables)
    #table_div = soup.find(id="content_weather")
    tables = soup.find_all("table")
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

for i in range(8):
    soup = BeautifulSoup(chart_source[i], "lxml",parse_only=only_tables)
    tables = soup.find_all("table")
    wt_table = tables[0]
    trs = wt_table.find_all('tr')
    currTr = trs[3]
    tds = currTr.find_all('td')
    #(weather,currtemp)
    tmp = tds[1].text
    if ("구름" in tmp):
        csky = "little_grey"
    elif ("비" in tmp):
        csky = "rainy"
    elif ("소나기" in tmp):
        csky = "rainy"
    elif ("눈" in tmp):
        csky = "snowy"
    elif ("무" in tmp):
        csky = "foggy"
    elif ("흐림" in tmp):
        csky = "grey"
    else:
        csky = "sunny"
    tmpIsDay = "0"
    if (sr_hour <= time_list[i] < ss_hour):
        tmpIsDay = "1"
    tmptuple = (time_list[i],csky,tds[5].text,tmpIsDay)
    cres.append(tmptuple)

#Setting sky(yesterday's weather)
sky = ""
if (float(res[8]) >= 9):
    sky = "grey"
elif (float(res[8]) >= 6):
    sky = "little_grey"
elif (float(res[8]) >= 3):
    sky = "little_sunny"
else:
    sky = "sunny"

if (float(res[5]) > 17):
    sky = "windy"

if (res[3]!="0"):
    sky = "rainy"

if (res[4]!="0"):
    sky = "snowy"

#Comment farm
comment_rainy = ["어제는 비가 왔네요. 우산은 잘 챙겨 나가셨겠죠?",
                 "저런! 어제 비가 왔네요. 혹시 감기에 걸리시지는 않으셨나요?"]
comment_snowy = ["어제는 눈이 왔어요! 친구들과 즐거운 하루 보내셨나요?",
               "어제는 눈이 내렸네요. 소복히 쌓이는 눈을 보며 힐링하셨기를 바라요."]
comment_sunny = ["어제는 맑은 날이었어요. 화창한 날씨에 기분도 한껏 들뜨셨겠죠?",
                 "어제 이렇게 맑을 줄 알았으면 소풍이라도 갈 걸 그랬어요."]
comment_cloudy = ["어제는 흐린 날이었어요. 오늘은 어떨까요?"]
comment_hot = ["어제는 아주 더운 날이었네요! 시원하게 입고 나가셨나요?",
               "어제는 엄청 더웠네요. 오늘은 좀 시원할까요?"]
comment_cold = ["어제는 엄청 추웠어요! 혹시 감기에 걸리시지는 않으셨나요?",
               "어제는 엄청 추웠네요. 더 따뜻하게 입고 나갈 걸 그랬어요"]
comment_windy = ["어제는 바람이 많이 불었네요. 따뜻하게 입고 나가셨죠?"]
comment_foggy = ["어제는 안개가 많이 꼈어요. 앞은 조심히 보고 다니셨나요?"]

#Choosing a random comment
comments = []
if (sky=="rainy"):
    comments = comment_rainy
elif (sky=="snowy"):
    comments = comment_snowy
elif (sky=="foggy"):
    comments = comment_foggy
elif (float(res[0]) < 5):
    comments = comment_cold
elif (float(res[0]) > 30):
    comments = comment_hot
elif (float(res[5]) > 17):
    comments = comment_windy
elif (sky=="grey" or sky=="little_grey"):
    comments = comment_cloudy
else:
    comments = comment_sunny

comment = comments[random.randint(0,len(comments)-1)]

#[avg,min,max,precip,snow,wind,humid,sun,cloud,weather]
ret = {
    "avg_temp": res[0],
    "min_temp":res[1],
    "max_temp":res[2],
    "precip":res[3],
    "snow":res[4],
    "wind":res[5],
    "humid":res[6],
    "sun":res[7],
    "cloud":res[8],
    "sky":sky,
    "comment":comment,
    "isDay":str(isDay),
    "t0_time":str(cres[0][0]),
    "t0_weather": cres[0][1],
    "t0_temp":cres[0][2],#+"℃",
    "t0_isDay":cres[0][3],
    "t1_time":str(cres[1][0]),
    "t1_weather": cres[1][1],
    "t1_temp":cres[1][2],#+"℃",
    "t1_isDay":cres[1][3],
    "t2_time":str(cres[2][0]),
    "t2_weather": cres[2][1],
    "t2_temp":cres[2][2],#+"℃",
    "t2_isDay":cres[2][3],
    "t3_time":str(cres[3][0]),
    "t3_weather": cres[3][1],
    "t3_temp":cres[3][2],#+"℃",
    "t3_isDay":cres[3][3],
    "t4_time":str(cres[4][0]),
    "t4_weather": cres[4][1],
    "t4_temp":cres[4][2],#+"℃",
    "t4_isDay":cres[4][3],
    "t5_time":str(cres[5][0]),
    "t5_weather": cres[5][1],
    "t5_temp":cres[5][2],#+"℃",
    "t5_isDay":cres[5][3],
    "t6_time":str(cres[6][0]),
    "t6_weather": cres[6][1],
    "t6_temp":cres[6][2],#+"℃",
    "t6_isDay":cres[6][3],
    "t7_time":str(cres[7][0]),
    "t7_weather": cres[7][1],
    "t7_temp":cres[7][2],#+"℃",
    "t7_isDay":cres[7][3]
}
print(json.dumps(ret))

#end_time = datetime.datetime.now()
#print("required time = "+str((end_time-start_time).total_seconds()))
