
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Welcome to Cloud Computing</title>
    </head>
    <body style="text-align:center; font-family:Arial; margin-top:100px;">
        <h1 style="color:blue;">Welcome to Cloud Computing!</h1>
        <h2>My First Flask Application on Azure</h2>
        <p>Successfully deployed using Azure App Service.</p>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
