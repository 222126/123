from flask import Flask, render_template

# 創建 Flask 應用
app = Flask(__name__)

# 路由定義：首頁
@app.route('/')
def home():
    return '1234'

# 啟動應用
if __name__ == '__main__':
    app.run(debug=True)