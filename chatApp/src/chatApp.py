from flask import Flask, render_template, session


app = Flask(__name__)

app.secret_key = 'thesuperultimatesecretkey'

app.config['dbconfig'] = {'host': '127.0.0.1',
                          'user': 'mainUser',
                          'password': 'mainUserPassword',
                          'database': 'chatApp'
                          }


# main login page
@app.route('/')
def home_page():
    return render_template('frontend/login.html')


@app.route('/chatrooms', methods=['GET', 'POST'])
def chatrooms():
    return "Loged In!"


if __name__ == '__main__':
    app.run(debug=True)
