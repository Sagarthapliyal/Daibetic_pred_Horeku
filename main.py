# importing the flask lib##
from flask import Flask, render_template, request
import joblib
app= Flask(__name__)
# load the model
model=joblib.load('model/diabatic_80.pkl')

@app.route('/')  ## decorator
def home():
    return render_template('home.html')

@app.route('/data', methods=['post'])  ## decorator
def data():                                             # function for getting form data to be print
    preg=request.form.get('preg')
    plas=request.form.get('plas')
    pres=request.form.get('pres')
    skin=request.form.get('skin')
    test=request.form.get('test')
    mass=request.form.get('mass')
    pedi=request.form.get('pedi')
    age=request.form.get('age')

    result=model.predict([[preg,plas,pres,skin,test,mass,pedi,age]])

    if result[0]==1:
        data='Patient is Diabetic'
    else:
        data='Patient is not Diabetic'
    
    print(data)

    return render_template('predict.html', data=data)


app.run(debug=True)  ####run command will be at the last

#http: hyper text transfer protocol
#//127.0.0.1-- local machine address
# :5000- port- gateway server
# / route