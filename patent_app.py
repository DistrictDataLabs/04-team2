from flask import Flask
from sim import similarity 

app = Flask(__name__)

@app.route("/hello")
@app.route("/hello/<name>")
def hello(name=None):
    return "Hello World! Your name is %s." % name

@app.route("/test")
def test():
    array = ['quick brown fox','the quick brown fox']
    sim = similarity.text_similarity(array)
    return "Similarity of %s is %s" % (array,sim)



if __name__ == "__main__":
    app.debug = False
    #app.run(host='0.0.0.0.')
    app.run(debug=True)
