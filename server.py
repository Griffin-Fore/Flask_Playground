from flask import Flask, render_template

app = Flask(__name__)

# @app.route('/')
# def hello(times,color):
#     return render_template("index.html",times=3,color="blue")

#if passing through the URL, needed to pass through the def() function

@app.route('/play')
def play():
    return render_template("index.html")

@app.route('/play/<int:times>')
def playtimes(times):
    return render_template("index.html",times=times)

@app.route('/play/<int:times>/<string:color>')
def playtimescolor(times,color):
    return render_template("index.html",times=times,color=color)

if __name__=="__main__":
    app.run(debug=True)