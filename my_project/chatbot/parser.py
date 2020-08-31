import requests
from bs4 import BeautifulSoup

# 주가 : 코스피
def stock_kospi():
    import requests
    from bs4 import BeautifulSoup
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}

    data = requests.get('https://finance.naver.com/sise/sise_index.nhn?code=KOSPI', headers=headers)
    soup = BeautifulSoup(data.text, 'html.parser')
    value = soup.select_one('#now_value').text
    diff = soup.select_one('#change_value_and_rate').text.strip().split(" ")
    diff_value = float(diff[0])
    diff_percent = float(diff[1][:diff[1].rfind("%")])
    if diff_percent < 0:
        diff_value = -diff_value
    result_string = "코스피는 %s원으로 전일 대비 %0.2f원(%0.2f%%)입니다."%(value, diff_value, diff_percent)

# 주가 : 네이버
def stock_naver():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get('https://finance.naver.com/item/main.nhn?code=035420', headers=headers)
    soup = BeautifulSoup(data.text, 'html.parser')
    value = soup.select_one('div > p.no_today > em').text.strip().split("\n")[0]
    diff_value = soup.select_one('div > p.no_exday > em:nth-child(2)').text.strip().split("\n")[1]
    return value, diff_value

# 날씨
def weather():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get('https://weather.com/weather/today/l/142d25167924cf52b9f5ac8c7fcae8d23b95524ab51af1f534a1e8efc246914c', headers=headers)
    soup = BeautifulSoup(data.text, 'html.parser')
    temp = soup.select_one('#WxuCurrentConditions-main-b3094163-ef75-4558-8d9a-e35e6b9b1034 > div > section > div > div._-_-node_modules--wxu-components-src-organism-CurrentConditions-CurrentConditions--dataWrapperInner--2h2vG > div._-_-node_modules--wxu-components-src-organism-CurrentConditions-CurrentConditions--primary--3xWnK > span').text.strip()
    temp = float((int(temp.replace("°", ""))-32)*5./9.)

    desc = soup.select_one('#WxuCurrentConditions-main-b3094163-ef75-4558-8d9a-e35e6b9b1034 > div > section > div > div._-_-node_modules--wxu-components-src-organism-CurrentConditions-CurrentConditions--dataWrapperInner--2h2vG > div._-_-node_modules--wxu-components-src-organism-CurrentConditions-CurrentConditions--primary--3xWnK > div').text.strip()
    result_string = "서울:%0.1f°(%s)"%(temp, desc)


weather()