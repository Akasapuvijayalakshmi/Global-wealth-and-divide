from flask import Flask,render_template,request

sales=Flask(__name__) #intializing the flask app



@sales.route('/')
def helloworld():
    return render_template("index.html")

if __name__=='__main__':
    sales.run(debug=False, port=7000)