from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html', title="grapheneX [Web]")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)