from flask import Flask,request,jsonify
import series as s  #套用其他檔案的def
import poker as p


app = Flask(__name__)

@app.route('/series') #沒寫methods 預設GET方式進入網頁 所以要打 ? 接參數
def getSeries():
    n= int(request.args.get('n'))
    output = s.Func(n) #用series 的def
    return str(output) #回傳html的字串

@app.route('/poker') #沒寫methods 預設GET方式進入網頁 所以要打 ? 接參數
def poker():
    n= int(request.args.get('n'))
    outputDict = p.poker(n)
    return jsonify(outputDict) #用jsonify才會有純粹的json字串 不然回傳是html




if __name__ =='__main__':
    app.run(debug=True,host='0.0.0.0',port=5000)