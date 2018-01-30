from flask import Flask, render_template

app = Flask(__name__)
app.secret_key = "My Secret Key"


@app.route('/')
def main():
    return render_template('view.html')
