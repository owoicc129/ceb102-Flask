from flask import Flask , render_template , request
import model #這個檔

app = Flask(__name__)

@app.route('/hello')
def hello():
    user = request.args.get('username')  #指定一定要打username才會帶入你的參數
    return render_template('hello.html',username=user) #帶入模板名稱+要放的變數

@app.route('/hello_post', methods=['GET', 'POST']) #可接受用這兩種方法連進來
def hello_post():
    request_method = request.method
    username =''
    if request.method == 'POST':    #如果是用post的方式連近來 就把表單username填入的參數帶入
        username = request.form.get('username')
    return render_template('hello_post.html', request_method=request_method,username=username )



#MVC =Model View Controller  資料庫 網頁 控制器
@app.route('/show_staff')
def hello_google():
    staff_data = model.getStaff()   #使用model檔案裡getStaff()功能 連線mySQL
    column = ['ID', 'Name', 'DeptId', 'Age', 'Gender', 'Salary']
    return render_template('show_staff.html', staff_data=staff_data,
                                              column=column)


if __name__ =='__main__':
    app.run(host='0.0.0.0',port=5000)