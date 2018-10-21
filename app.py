from flask import Flask, render_template
import time

app = Flask(__name__)

with open("articleTitles.txt", 'r') as c:
    content1 = c.readline()
    content2 = c.readline()
    content3 = c.readline()
    content4 = c.readline()
    content5 = c.readline()
with open("articleURLS.txt", 'r') as u:
    link1 = u.readline()
    link2 = u.readline()
    link3 = u.readline()
    link4 = u.readline()
    link5 = u.readline()
with open("publication.txt", 'r') as p:
    pub1 = p.readline()
    pub2 = p.readline()
    pub3 = p.readline()
    pub4 = p.readline()
    pub5 = p.readline()

c.close()
u.close()
p.close()


@app.route('/')
def index():
    #SHIFT+f5 to hard-refresh
    return render_template('index.html', content1=content1, content2=content2, content3=content3, content4=content4, content5=content5, link1=link1, link2=link2, link3=link3, link4=link4, link5=link5, pub1=pub1, pub2=pub2, pub3=pub3, pub4=pub4, pub5=pub5)

while True:
    print ("Updating...")
    if __name__ == '__main__':
        app.run(debug=True)
        time.sleep(5) #sleep for 60 seconds


