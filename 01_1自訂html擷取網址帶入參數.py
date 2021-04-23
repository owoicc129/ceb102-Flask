from flask import Flask, request

app = Flask(__name__)

@app.route('/hello_get', methods=['GET'])
def hello_get():
    username = request.args.get('username')   #GET方式連網就要把參數打在網址上 /hello_get?username=11
    userage = request.args.get('userage')

    #以下整串是HTML 內文寫在Body裡 ，head-title是網頁標籤會顯示的
    outStr = """
    <html>
        <head>
            <title>Hello</title>   
        </head>
        <body>
    """

    if username == None:
        outStr += """
        Who are you?
        """
    else:
        outStr += f"""
        Hello {username} !
        """
        if userage != None:        #年紀有給就顯示
            outStr += f"""
            You are {userage} years old.
            """

    outStr += """
        </body>
    </html>
    """
    return outStr

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)