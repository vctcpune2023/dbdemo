import numpy as np
import config
import pickle
import json
class MedicalInsurance():
    def __init__(self,age,gender,bmi,smoker,children,region):
        self.age = age
        self.gender = gender.lower()
        self.bmi = bmi
        self.smoker = smoker.lower()
        self.children = children
        self.region = "region_" + region.lower()

    def get_model(self):
        #### loading model
        with open(config.model_path,"rb") as file:
            self.model = pickle.load(file)
        ### load scaling model
        with open(config.scaler_path,"rb") as file:
            self.stdscale = pickle.load(file)
        ### load json
        with open(config.json_path,"r") as file:
            self.json_data = json.load(file)

    def get_predicted_charges(self):
        self.get_model()

        test_array = np.zeros(len(self.json_data["columns"]))
        #  ["gender", "bmi", "children", "smoker", "region_northeast",
        #    "region_northwest", "region_southeast", 
        #   "region_southwest", 
        # "age_buckets", "weight", "risky"]
        test_array[0] = self.json_data["gender"][self.gender]
        test_array[1] = self.bmi
        test_array[2] = self.children
        test_array[3] = self.json_data["smoker"][self.smoker]
        region_index =  self.json_data["columns"].index(self.region)
        test_array[region_index] = 1
        self.age_buckets = 0 if self.age <18 else 1 if self.age <30 else 2 if self.age <45 else 3 if self.age<60 else 4
        test_array[8] = self.age_buckets
        self.weight = 0 if self.bmi <25 else 1
        test_array[9] = self.weight
        self.risky = 1 if self.age_buckets == 4  else 0
        test_array[10] = self.risky

        ### we to pass to scaling object
        std_array = self.stdscale.transform([test_array])## 2D Array

        predicted_charges = np.around(self.model.predict(std_array)[0],2)

        return predicted_charges
         





    
        