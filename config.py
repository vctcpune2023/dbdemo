import os

model_path=os.path.join("Model","KNN_model.pkl")
scaler_path=os.path.join("Model","scale.pkl")
json_path=os.path.join("Model","project_data.json")

DB_PASS = "admin"
DB_PARAM = {'host': 'dshealth.culi2vvhaxwm.ap-south-1.rds.amazonaws.com', 'database': 'health', 'user': 'admin', 'password': 'rootroot'}

DB_PARAM_LOCAL = {'host': 'localhost', 'database': 'health', 'user': 'root', 'password': 'admin'}
# db password
# root
# vctc1234