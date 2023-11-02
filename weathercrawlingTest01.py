# beautifulsoup4, requests 설치
import requests
from bs4 import BeautifulSoup

#area = '한남동'
area= input("날씨를 알고 싶은 동명을 입력하세요 : ")
weather_html = requests.get(f'https://search.naver.com/search.naver?&query={area} 날씨')
print(weather_html.text)

weather_soup = BeautifulSoup(weather_html.text, 'html.parser')

area_text = weather_soup.find('h2', {'class':'title'}).text
print(f"입력하신 지역은 : {area_text}")

today_temperature = weather_soup.find('div', {'class':'temperature_text'}).text # 현재온도
today_temperature = today_temperature[6:11]
print(f" * 현재온도 : {today_temperature}")


today_temperature = weather_soup.find('span', {'class':'weather before_slash'}).text # 현재온도
print(f" * 닐씨는 : {today_temperature}")

yesterday_weathertext = weather_soup.find('p', {'class':'summary'}).text # 어제온도
yesterday_weathertext = yesterday_weathertext[:13].strip()
# 통 13글자를 가져온 후 strip으로 양쪽의 공백제거 후 저장
print(f"어제와 비교하면 : {yesterday_weathertext}")

sense_temperature = weather_soup.select('dl.summary_list>dd')
# <dl> 중에서 class 가 summary_list인 태그를 찾은 후 그 안의 <dd>태그들을 모두 리스트로 반환
sense_temperature_text = sense_temperature[0].text
print(f" * 습도는 : {sense_temperature_text}")

sense_temperature = weather_soup.select('dl.summary_list>dd')
# <dl> 중에서 class 가 summary_list인 태그를 찾은 후 그 안의 <dd>태그들을 모두 리스트로 반환
sense_temperature = weather_soup.find('div', {'class':'weather_info'}).find('dl',{classmethod


}sense_temperature[0].text
print(f" * 체감온도 : {sense_temperature}")
dust_info = weather_soup.select('ul.today_chart_list>li')
#print(dust_info)

dust1_info = dust_info[0].find('span', {'class':'txt'}).text # 미세먼지 정보
print(f" * 미세먼지 : {dust1_info}")
dust2_info = dust_info[1].find('span', {'class':'txt'}).text # 초미세먼지 정보
print(f" * 초미세먼지 : {dust2_info}")


