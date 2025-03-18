from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/get/sum')
def main():
    a=int(request.args.get('a'))
    b=int(request.args.get('b'))
    c=a+b
    return {"result":c}

if __name__ == '__main__':  
    app.run(debug=True)