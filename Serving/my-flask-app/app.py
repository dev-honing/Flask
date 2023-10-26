from flask import Flask, render_template

app = Flask(__name)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get-request', methods=['GET'])
def get_request():
    print('GET 요청을 처리했습니다')
    return 'GET 요청 처리를 완료했습니다'

@app.route('/post-request', methods=['POST'])
def post_request():
    print('POST 요청을 처리했습니다')
    return 'POST 요청 처리를 완료했습니다'

if __name__ == '__main__':
    app.run(debug=True)
