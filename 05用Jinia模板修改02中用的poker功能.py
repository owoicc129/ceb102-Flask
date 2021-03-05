from flask import Flask, request, render_template
import poker as p

app = Flask(__name__)

@app.route('/poker', methods=['GET', 'POST'])
def poker():
    request_method = request.method
    players = 0
    cards = dict()
    if request_method == 'POST':
        players = int(request.form.get('players'))
        cards = p.poker(players) #poker檔裡poker功能
    return render_template('poker.html', request_method=request_method,
                                         cards=cards)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)