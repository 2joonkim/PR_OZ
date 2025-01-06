from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api/v1/feeds', methods=['GET'])
def show_all_feeds():
    data = {'result': 'success', 'data': {'feed1': 'data1', 'feed2': 'data2'}}
    return jsonify(data)

@app.route('/api/v1/feeds/<int:feed_id>', methods=['GET'])
def show_one_feed(feed_id):
    print(feed_id)
    data = {'result': 'success', 'data': {'feed1': 'data1', 'feed2': 'data2'}}
    return jsonify(data)

#게시글 전달 api
@app.route('/api/v1/feeds', methods=['POST'])
def create_one_feed():
    name = request.form['name']
    age = request.form['age']
    print(name, age)
    return jsonify({'result':'success'})

#데이터 추가 api
datas = [{'itmes': [{"name": "item1", "price": 10}]}]

@app.route("/api/v1/datas", methods=['GET'])
def get_datas():
    return {'datas':datas}

@app.route("/api/v1/datas", methods=['POST'])
def create_data():
    request_data = request.get_json()

    new_data = {'items':request_data.get('itmes', [])}
    datas.append(new_data)
    return new_data, 201

if __name__ == '__main__':
    app.run(debug=True)
