import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.neighbors import KNeighborsClassifier as KNN
from sklearn.metrics import precision_score, recall_score, f1_score, accuracy_score


  
data = pd.read_csv("data (2).csv")



data.dropna(inplace=True)



attributes = ['Speed', 'Agility', 'Intelligence', 'Luck']


for attr in attributes:
    
    plt.figure()
    
    sns.scatterplot(data=data, x=attr, y='Can Defeat Dragon', alpha=0.7)
    
    plt.title(f"{attr} vs Can Defeat Dragon")
    
    plt.xlabel(attr)
    plt.ylabel("Can Defeat Dragon")
    

x = data[['Speed', 'Agility', 'Intelligence', 'Luck']].values
y = data['Can Defeat Dragon'].values


point = int(0.8 * len(x))

X_train, X_test = x[:point], x[point:]
y_train, y_test = y[:point], y[point:]


model = KNN(5)


model.fit(X_train, y_train)


y_pred = model.predict(X_test)


accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)

recall = recall_score(y_test, y_pred)

f1 = f1_score(y_test, y_pred)


print(f"Accuracy: {accuracy:.2f}")
print(f"Precision: {precision:.2f}")
print(f"Recall: {recall:.2f}")
print(f"F1 Score: {f1:.2f}")


new_heroes = np.array([[0, 8, 7, 8, 9], [0, 8, 6, 8, 8]])
predictions = model.predict(new_heroes[:, 1:])



i = 0
for hero in (new_heroes):
    print(f"Hero {i+1} with attributes {hero} {'CAN' if predictions[i] == 1 else 'CANNOT'} defeat the DRAGON.")
    i += 1

