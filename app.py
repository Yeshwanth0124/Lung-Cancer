from flask import *
import pandas as pd
import pickle
import numpy as np
import joblib
import warnings
import traceback
warnings.filterwarnings("ignore")
app = Flask(__name__)
@app.route("/")
def page():
    return render_template('webpage.html')
@app.route("/home")
def home():
    return render_template('webpage.html')
@app.route("/signin")
def signin():
    return render_template('signin.html')
@app.route("/fetchdata",methods=['GET','POST'])
def data():
    try:
        form_data = {
        "gender" : request.form.get('gender'),
        "smoking" : request.form.get('smoking'),
        "yellowfinger" : request.form.get('yellowfingers'),
        "anxiety" : request.form.get('anxiety'),
        "peerpressure" : request.form.get('peerpressure'),
        "chronic" : request.form.get('chronic'),
        "fatigue" : request.form.get('fatigue'),
        "allergy" : request.form.get('allergy'),
        "wheezing" : request.form.get('wheezing'),
        "alchohol" : request.form.get('alchohol'),
        "coughing" : request.form.get('coughing'),
        "shortnessofbreath" : request.form.get('shortnessofbreath'),
        "swallowingdifficulty" : request.form.get('swallowingdifficulty'),
        "chestpain" : request.form.get('chestpain'),
        "age" : request.form.get('age')
        }
        df = pd.DataFrame.from_dict(form_data,orient="index")
        df_rep = df.replace({"M":1,"m":1,"F":0,"f":0,"Yes":1,"yes":1,"no":0,"No":0,"YES":1,"NO":0})
        print(df_rep.columns)
        np_arr = np.array(df_rep)
        reshaped_arr = np_arr.reshape(1,-1)
        df = pd.DataFrame(reshaped_arr)
        print(df.shape)
        print(df)
        dict = df.to_dict()
        Model = joblib.load("Model")
        predict = Model.predict(df)
        if predict == 0:
            return jsonify("No Lung Cancer  ")
        elif predict==1:
            return jsonify("Lung Cancer")
    except Exception as e:
        return jsonify({"error":str(e)})
'''@app.route("/predict")
 def predict():
     try:
         data = pd.read_excel("Excel_test_sample.xlsx")
        arr_data = df.to_numpy()
         Model = joblib.load('Model')
         prediction = Model.predict(arr_data)
         result = {"prediction":"Lung Cancer" if prediction==1 else "No Lung Cancer"}
         return jsonify(result)
     except Exception as e:
         return jsonify({"error":str(e)})'''
if __name__=="__main__":
    app.run(debug=True,use_reloader=False)
