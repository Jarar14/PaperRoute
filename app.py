from flask import Flask, render_template

app = Flask(__name__)

with open("day1.txt", 'r') as f:
    content = f.read()

@app.route('/')
def index():
    #SHIFT+f5 to hard-refresh
    return render_template('index.html', content=content)

if __name__ == '__main__':
    app.run(debug=True)
