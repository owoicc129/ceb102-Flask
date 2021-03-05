from flask import Flask,request  #要多引入request才能接收參數

app = Flask(__name__)

@app.route('/hello_get') #沒寫methods 預設GET方式進入網頁
def hello_get():
    username = request.args.get('username')  #用username這個字+後面接參數才接收，其他都不接受
    userage = request.args.get('userage')    #而且get方法後面接參數要用 " ? "
    return 'Hello {} , you are {} years old.'.format(username,userage)
#request.args.get (此requset不是爬蟲的request,get也不是連網的get)
#  要求   參數  接收
#GET帶參數是打在網址 像這樣 127.0.0.1:5000/hello_get?username=Allen&userage=22






@app.route('/hello_post', methods=['GET', 'POST']) #可接受用這兩種方法連進來
#一開始/hello_post進來還沒輸入表單時是用GET進入網頁
#但按下按鈕提交後 就會用POST重新進入網頁

def hello_post():
    #用HTML設立表單 用/hello_post連到後會看到表框+按鈕
    #這邊給了form action-post，就是當你按下按鈕後會執行的動作
    outStr = """
    <form action="/hello_post" method="POST">  
        <input type="textbox" name="username">
        <button type="submit">SUBMIT</button>
    </form>
    """
    if request.method == 'POST':    #如果是用POST方式連網 就把表單username填入的參數帶入
        username = request.form.get('username')  #request.form.get (是要求 表格參數 接收)
        outStr += """<div>Hello {}</div>""".format(username) #加在原本內容下面
    return outStr



if __name__ =='__main__':
    app.run(debug=True,host='0.0.0.0',port=5000)
    # debug=True 是用來讓你不用把之前已開過的的網頁關掉重開

