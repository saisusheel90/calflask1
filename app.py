from flask import Flask,request,render_template
import json
app=Flask(__name__)

@app.route('/')

def welcome():
    return "welcome to the flask"

@app.route('/cal',methods=["GET"])
def math_operator():
    operation=request.json["operation"]
    number1=request.json["number1"]
    number2=request.json["number2"]
    
    if operation=="add":
        result=number1+number2
    elif operation=="sub":
        result=number1-number2
    elif operation=="multiply":
        result=number1*number2
    else: 
        result=number1/number2
    #return jsonify(result)
    return "The operation is {} and the result is: {}".format(operation,result)

print(__name__) 

if __name__=='__main__':
    app.run()