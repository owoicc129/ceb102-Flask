from flask import Flask   #import flask套件裡的兩個模組

app = Flask(__name__) #建立Flask物件，指自己這隻程式


@app.route('/')  #建立接口 打 / 就可以連到，並執行helloFlask功能
def helloFlask():
    return 'hello Flask!'

@app.route('/hello/<username>')  #可帶參數
def hello(username):
    return 'hello{}'.format(username)

@app.route('/add/<x>/<y>')    #輸入數字做相加
def add(x,y):
    return str(int(x)+int(y))  #return一定只能回傳字串


#建議要寫這(如果有很多controller，不寫的話每個分支都會app.run)
if __name__ =='__main__':
    app.run(host='0.0.0.0',port=5000) #可進入127.0.0.1:5000看