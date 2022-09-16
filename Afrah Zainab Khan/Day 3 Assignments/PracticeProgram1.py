from flask import Flask
app=Flask(__name__)
@app.route('/hello')
def hello_world():
    return "Welcome to python class"
@app.route('/user')
def user_login():
    return "User logged in"
if __name__=='__main__':
    app.run(debug = True)
