from  flask import Flask,request,render_template
import config
from Model.utils import MedicalInsurance
from query import insert_query

app = Flask(__name__)

@app.route("/")
def get_homeapi():
    return render_template("index.html")

@app.route("/predicted_charges",methods = ["POST"])
def get_medicalInsurance():
    
    data = request.form 
    age = eval(data["age"])
    gender = data["gender"]
    bmi = eval(data["bmi"])
    children = int(data["children"])
    smoker = data["smoker"]
    region = data["region"]

    medical = MedicalInsurance(age,gender,bmi,smoker,children,region)
    
    charges = medical.get_predicted_charges()
    charges = float(charges)
    args = (age,gender,bmi,children,smoker,region,charges)
    print(args)
    print("Db Started")
    insert_query(args)
    print("DB Operation finish")

    return render_template("index.html",charges=charges)


if __name__ == "__main__":
    app.run(debug=False, host ='0.0.0.0', port = 8080)

