## url routing for flask



from flask import Flask, render_template, request,redirect,url_for,jsonify


## Create a flask Application

app = Flask(__name__)

@app.route("/",methods=["GET"])
def welcome():
    return "<h1>welcome to the flask web application page made by ansh verma</h1>"



@app.route("/index",methods=["GET"])
def index():
    return "<h2>welcome to the first index page</h2>"

## variable rule
@app.route('/success/<int:score>')
def success(score):
    return "The person has passed and the score is: "+ str(score)



@app.route('/failure/<int:score>')
def failure(score):
    return "The person has failed and the score is: "+ str(score)


@app.route('/form',methods=["GET","POST"])
def form():
    if request.method=="GET":
        return render_template('form.html')
    else:
        maths=float(request.form['maths'])
        Science=float(request.form['science'])
        history=float(request.form['history'])


        average_marks= (maths+Science+history)/3
        res=""
        if average_marks>=50:
            res="success"
        else:
            res="failure"

        return redirect(url_for(res,score=average_marks))


        #return render_template('form.html',score=average_marks)
    

@app.route('/api',methods=['POST'])
def calculate_sum():
    data=request.get_json()
    a_val=float(dict(data)['a'])
    b_val=float(dict(data)['b'])
    c_val=float(dict(data)['c'])
    return jsonify(a_val+b_val,c_val)
    



if __name__ == "__main__":
    app.run(debug=True)