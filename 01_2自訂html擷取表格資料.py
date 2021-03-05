from flask import Flask, request

app = Flask(__name__)

@app.route('/hello_post', methods=['GET', 'POST'])
def hello_post():
    outStr = """
    <html>
    <form action="/hello_post" method="POST">
        <label>What is your name?</label>
        <br>
        <input type="textbox" name="username">
        <button type="submit">Submit</button>
    </form>
    <div>
    %s
    </div>
    </html>
    """
    if request.method == 'GET':
        return outStr%('')   #  %s的地方顯示空白
    elif request.method == 'POST':
        username = request.form.get('username')
        return outStr%('Hello %s'%(username))


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)