from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient
import requests
from bs4 import BeautifulSoup


client = MongoClient('localhost', 27017)
db = client.sparta

app = Flask(__name__)

headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}

# 시작 페이지
@app.route('/')
def main():
    return render_template('index.html')

# 기념일 등록
@app.route('/write', methods=['POST'])
def save_db():
    date = request.form['date']
    content = request.form['content']
    doc = {
        'date': date,
        'content': content,
    }
    db.chatbot.insert_one(doc)
    return jsonify({'result': 'success', 'msg':'등록 완료'})

# 기념일 읽기
@app.route('/read', methods=['GET'])
def load_db():
    result = list(db.chatbot.find({}, {'_id': False}))
    return jsonify({'result': 'success', 'db': result})

# 기념일 읽기 (for chatbot)
@app.route('/readStr', methods=['GET'])
def load_db():
    import datetime
    now = datetime.datetime.now()
    results = list(db.chatbot.find({}, {'_id': False}))
    count = 0
    result_string = "오늘의 기념일은 \n"
    # print
    # now.year, ,
    for result in results:
        if "%04d-%02d-%02d"%(now.year, now.month, now.day) == result['date']:
            count += 1
            result_string += "- %s\n"%result['content']
    if count == 0:
        result_string = "오늘은 기념일이 없습니다."
    else:
        result_string = "오늘은 기념일이 2건 있습니다.\n%s"%result_string
    print (result_string)
    return jsonify({'result': 'success', 'db': result_string})

# 코스피 지수
@app.route('/kospi', methods=['GET'])
def kospi():
    data = requests.get('https://finance.naver.com/sise/sise_index.nhn?code=KOSPI', headers=headers)
    soup = BeautifulSoup(data.text, 'html.parser')
    value = soup.select_one('#now_value').text
    diff = soup.select_one('#change_value_and_rate').text.strip().split(" ")
    diff_value = float(diff[0])
    diff_percent = float(diff[1][:diff[1].rfind("%")])
    if diff_percent < 0:
        diff_value = -diff_value
    result_string = "코스피는 %s원으로 전일 대비 %0.2f원(%0.2f%%)입니다." % (value, diff_value, diff_percent)
    return jsonify({'result': 'success', 'kospi': result_string})

# 날씨
@app.route('/weather', methods=['GET'])
def weather():
    data = requests.get(
        'https://weather.com/weather/today/l/142d25167924cf52b9f5ac8c7fcae8d23b95524ab51af1f534a1e8efc246914c',
        headers=headers)
    soup = BeautifulSoup(data.text, 'html.parser')
    temp = soup.select_one(
        '#WxuCurrentConditions-main-b3094163-ef75-4558-8d9a-e35e6b9b1034 > div > section > div > div._-_-node_modules--wxu-components-src-organism-CurrentConditions-CurrentConditions--dataWrapperInner--2h2vG > div._-_-node_modules--wxu-components-src-organism-CurrentConditions-CurrentConditions--primary--3xWnK > span').text.strip()
    temp = float((int(temp.replace("°", "")) - 32) * 5. / 9.)

    desc = soup.select_one(
        '#WxuCurrentConditions-main-b3094163-ef75-4558-8d9a-e35e6b9b1034 > div > section > div > div._-_-node_modules--wxu-components-src-organism-CurrentConditions-CurrentConditions--dataWrapperInner--2h2vG > div._-_-node_modules--wxu-components-src-organism-CurrentConditions-CurrentConditions--primary--3xWnK > div').text.strip()
    result_string = "서울:%0.1f°(%s)" % (temp, desc)

    return jsonify({'result': 'success', 'weather': result_string})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
