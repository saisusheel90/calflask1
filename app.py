from flask import Flask,request,render_template
app=Flask(__name__)

@app.route('/')

def welcome():
    return "welcome to the flask"

@app.route('/cal',methods=["GET"])
def math_operator():
    operation=request.json["operation"]
    number1=request.json["operation"]
    number2=request.json["operation"]
    
    if operation=="add":
        result=number1+number2
    elif operation=="sub":
        result=number1-number2
    elif operation=="mulutiply":
        result=number1*number2
    else: 
        result=number1/number2
    return result


print(__name__)

if __name__=='__main__':
    app.run()