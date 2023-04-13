from flask import Flask, render_template, request
##import table
app = Flask(__name__)


@app.route("/")
def main():
##    print(table.rows)
    return render_template('index.html')
@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/api/signup',methods=['POST'])
def signUp():
    # create user code will be here !!

        # read the posted values from the UI
        _name = request.form['inputName']
        _email = request.form['inputEmail']
        _password = request.form['inputPassword']
if __name__ == "__main__":
    app.run()



