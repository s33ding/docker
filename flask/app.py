from flask import Flask, render_template
from redis import Redis

app = Flask(__name__, template_folder='template')
redis = Redis(host='redis', port=6379)

@app.route('/')
def hello():
    redis.incr('hits')
    counter = str(redis.get('hits'),'utf-8')
    return render_template('home.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
