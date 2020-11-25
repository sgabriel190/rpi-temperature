from flask import Flask
app = Flask(__name__)

@app.route('/tempsens')
def tempsens_page():
    return render_template('')

if __name__ == "__main__":
    app.run(host="192.168.0.107", port="1111")
