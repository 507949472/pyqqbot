from flask import Flask, request
import json
from indao.getchuli import getcl


app = Flask(__name__)

@app.route('/', methods=['POST','GET'])
def receive():
    a=request.get_data(as_text="utf-8")
    a=json.loads(a)
    getcl(a)
    return ""


if __name__ == '__main__':
    app.run(debug=True,port=5701)