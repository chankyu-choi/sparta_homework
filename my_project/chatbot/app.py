from flask import Flask, render_template, jsonify, request

from apscheduler.schedulers.background import BackgroundScheduler

app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbchatbot

def crawling():
    date = "2020-08-12"
    content = "crawled"
    weather = "sunny"
    stock = "2300"
    keyword = "keyword1, keyword2, keyword3"
    doc = {
        'date': date,
        'content': content,
        'weather': weather,
        'stock': stock,
        'keyword': keyword,
    }
    db.data.insert_one(doc)

@app.route('/')
def project_home():
    return render_template('index.html')

@app.route('/write', methods=['POST'])
def write():
    date = request.form['date']
    content = request.form['content']
    weather = request.form['weather']
    stock = request.form['stock']
    keyword = request.form['keyword']
    doc = {
        'date': date,
        'content': content,
        'weather': weather,
        'stock': stock,
        'keyword    ': keyword,
    }
    db.data.insert_one(doc)
    return jsonify({'result': 'success'})

@app.route('/load', methods=['GET'])
def load():
    # 여길 채워나가세요!
    data = list(db.data.find({}, {'_id': False}))
    return jsonify({'result': 'success', 'data': data})

if __name__ == '__main__':
    # scheduler = BackgroundScheduler()
    # # https://apscheduler.readthedocs.io/en/stable/modules/triggers/cron.html#module-apscheduler.triggers.cron
    # scheduler.add_job(func=crawling, trigger="cron", second=10)
    # scheduler.start()
    crawling()
    app.run('0.0.0.0', port=5000, debug=True)