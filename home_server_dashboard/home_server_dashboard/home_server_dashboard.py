from flask import Flask, render_template

app = Flask(__name__)

@app.route("/dashboard")
def dashboard():
    """
        This function is used to render
        the dashboard.html
    """
    return render_template("dashboard.html")

def main():
    """
        This function is used as an entry point
        for our package. We start the flask application.
    """
    app.run(host='0.0.0.0', port=5000, debug=True)
