from flask import Flask
app=Flask(__name__)

# @app.route("/test")

app.route('/test')
def haai():
    return "wd"
# app.add_url_rule('/','test', hello_world)
if __name__=="__main__":
    app.run()