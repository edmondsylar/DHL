from flask import Flask, render_template, request
from action import DHL

# flask app instance.
app = Flask(__name__)

@app.route('/', methods=['POST', 'GET', 'PUT'])
def onlyroute():
    status = ''
    if request.method == 'POST':
        if request.files['upload_file']:
            f=request.files['upload_file']
            name = f.filename
            usr = DHL(name)
            status = usr.res()
            # return status message
    return render_template('upload.html', msg = status)


if __name__ == '__main__':
    app.run(debug=True, port=7896, host='0.0.0.0')
