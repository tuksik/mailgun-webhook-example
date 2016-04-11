from flask import Flask, request
app = Flask(__name__)

@app.route('/email/inbox',methods=['POST'])
def inbox():
    f = open('inbox.txt','a+')
    f.write("=============================================\n")
    f.write("to : " + request.form['recipient'] + "\n")
    f.write("from : " + request.form['sender'] + "\n")
    f.write("subject : " + request.form['subject'] + "\n")
    f.write("message : \n" + request.form['body-plain'] + "\n")
    f.write("=============================================\n")
    return '', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=80)
