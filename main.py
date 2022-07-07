
import time
from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home_page():
  return time.time()

if __name__ == '__main__':
  app.run()
