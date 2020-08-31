from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.sparta

# 시작 페이지
@app.route('/')
def main():
    return render_template('index.html')

# 기념일 등
@app.route('/write', methods=['POST'])
def save_db():
    print ("svae_db")
    date = request.form['date']
    content = request.form['content']
    print (date, content)
    doc = {
        'date': date,
        'content': content,
    }
    db.chatbot.insert_one(doc)

    return jsonify({'result': 'success'})


# 주문 목록보기(Read) API
@app.route('/order', methods=['GET'])
def view_orders():
    # 여길 채워나가세요!
    orders = list(db.orders.find({}, {'_id': False}))
    return jsonify({'result': 'success', 'orders': orders})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
