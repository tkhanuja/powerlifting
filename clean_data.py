import pandas as pd
#create data frame
data = pd.read_csv("openpowerlifting.csv")

###################
#Data Cleaning


#convert kg data to lbs
data["BodyweightLbs"] = [x * 2.2046 for x in data["BodyweightKg"] ]
data = data.drop("BodyweightKg", axis = 1)

#convert weight class ranges to floats
convert = []
for x in data["WeightClassKg"]:
    y = str(x)
    if '+' in y:
        y = y.replace('+', '')
    convert.append(float(y))  
data["WeightClassKg"] = convert

data['WeightClassKg'] = data['WeightClassKg'].astype(float)


data["WeightClassLbs"] = [x * 2.2046 for x in data["WeightClassKg"] ]
data = data.drop("WeightClassKg", axis = 1)

# data["Squat4Lbs"] = [x * 2.2046 for x in data["Squat4Kg"] ]


data["BestSquatLbs"] = [x * 2.2046 for x in data["BestSquatKg"] ]
data = data.drop("BestSquatKg", axis = 1)

# data["Bench4Lbs"] = [x * 2.2046 for x in data["Bench4Kg"] ]

data["BestBenchLbs"] = [x * 2.2046 for x in data["BestBenchKg"] ]
data = data.drop("BestBenchKg", axis = 1)

# data["Deadlift4Lbs"] = [x * 2.2046 for x in data["Deadlift4Kg"] ]


data["BestDeadliftLbs"] = [x * 2.2046 for x in data["BestDeadliftKg"] ]
data = data.drop("BestDeadliftKg", axis = 1)

data["TotalLbs"] = [x * 2.2046 for x in data["TotalKg"] ]
data = data.drop("TotalKg", axis = 1)
#end conversion

#drop unnecessary columns
data = data.drop("Deadlift4Kg", axis = 1)
data = data.drop("Bench4Kg", axis = 1)
data = data.drop("Squat4Kg", axis = 1)



print(data.describe())
for i in range(386414):
    d = data.loc[i]
    if d["BestBenchLbs"] and d["BestBenchLbs"] <= 45 or d["BestBenchLbs"] >= 500:
        data = data.drop(i, axis = 0)
    
    elif d["BestSquatLbs"] and d["BestSquatLbs"] <= 100 or d["BestSquatLbs"]>= 700:
           data = data.drop(i, axis = 0) 
    elif d["BestDeadliftLbs"] and d["BestDeadliftLbs"] <= 225 or d["BestDeadliftLbs"]>= 800:
           data = data.drop(i, axis = 0) 
    elif d["BodyweightLbs"] and d["BodyweightLbs"] <= 100 or d["BodyweightLbs"]>= 300:
           data = data.drop(i, axis = 0)
    elif d["Age"] and d["Age"] <= 14 or d["Age"]>= 85:
           data = data.drop(i, axis = 0)
    else:
        continue
       
print(data.describe())
data.to_csv("cleaned_openpowerlifting.csv")

