from controller import connection, send_email
from flask import Flask, request, jsonify, render_template


app = Flask(__name__)


@app.route('/email')
def index():
    return render_template('send_email.html')


@app.route('/send_email', methods=['POST'])
def login():
    email = request.form["email"]
    senha = request.form["senha"]
    to = request.form["to"]
    subject = request.form["subject"]
    body = request.form["body"]
    response_connection = None

    try:
        response_connection = connection(email, senha)
    except Exception as ex:
        print(ex)

    try:
        send_email(email, senha, subject, body, to)
    except Exception as ex:
        print(ex)

    return jsonify({'response_connection': response_connection})


if __name__ == '__main__':
    app.run(debug=True)
