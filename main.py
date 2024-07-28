import joblib
import warnings
from flask import Flask
from flask import request
from flask import jsonify


model = joblib.load("classifier.pkl")
warnings.filterwarnings('ignore')

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict ():

# body = request.json() REEMPLAZAZR POR DATA
# http://localhost:8000/predict
    
    data = {
        "Age": 27,0,
        "C":  0,
        "Fare": 71.2833,
        "Parch": 2,
        "Pclass": 3,
        "Q":  0,
        "S": 1,
        "SibSp": 3,
        "female":  1,
        "male":  0
    }
     data_values = [
        data["Age"],
        data["C"],
        data["Fare"],
        data["Parch"],
        data["Pclass"],
        data["Q"],
        data["SibSp"],
        data["female"],
        data["male"],


     ]
    prediction = model.predict([data_values])[0]
    prediction = int(prediction)
    if prediction==1:
       msg = "Pasajero sobreviviria"
    else 
       msg = "Pasajero no sobreviviria"

    return jsonify({
       "msg": msg,
       "prediction": prediction
    })

if __name__ == "_main_":
    app.run(port=8000, debug=True)


# body = request.json
 
# data = request.json
 