from flask import Flask, render_template

app = Flask(__name__)

with open("articleTitles.txt", 'r') as f:
    content1 = f.readline()
    content2 = f.readline()
    content3 = f.readline()
    content4 = f.readline()
    content5 = f.readline()


    f.close()

@app.route('/')
def index():
    #SHIFT+f5 to hard-refresh
    return render_template('index.html', content1=content1, content2=content2, content3=content3, content4=content4, content5=content5)

if __name__ == '__main__':
    app.run(debug=True)
