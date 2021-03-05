from flask import Flask
#第一步先創建一個叫static的資料夾
# 127.0.0.1:5000/test/sally.jpg


app = Flask(__name__,static_folder='./static',static_url_path='/test')
#                     資料夾位置-當前的static資料夾        網頁接口


if __name__ =='__main__':
    app.run(debug=True,host='0.0.0.0',port=5000)