import numpy as np
import pandas as pd
import sklearn.linear_model as lm
import sklearn.cross_validation as cv
import matplotlib.pyplot as plt

train = pd.read_csv('/Users/MacBook/Downloads/Book_Code/Chapter6/titanic_train.csv')
test = pd.read_csv('/Users/MacBook/Downloads/Book_Code/Chapter6/titanic_test.csv')
train[train.columns[[2,4,5,1]]].head()

data = train[['Sex', 'Age', 'Pclass', 'Survived']].copy()
data['Sex'] = data['Sex'] == 'female'
data = data.dropna()

data_np = data.astype(np.int32).values
X = data_np[:,:-1]
y = data_np[:,-1]

female = X[:,0] == 1
survived = y == 1

# This vector contains the age of the passengers.
age = X[:,1]
# We compute a few histograms.
bins_ = np.arange(0, 121, 5)
S = {'male': np.histogram(age[survived & ~female], 
                          bins=bins_)[0],
     'female': np.histogram(age[survived & female], 
                            bins=bins_)[0]}
D = {'male': np.histogram(age[~survived & ~female], 
                          bins=bins_)[0],
     'female': np.histogram(age[~survived & female], 
                            bins=bins_)[0]}
bins = bins_[:-1]
plt.figure(figsize=(15,8))
for i, sex, color in zip((0, 1),('male', 'female'), ('#3345d0', '#cc3dc0')):
    plt.subplot(121 + i)
    plt.bar(bins, S[sex], bottom=D[sex], color=color,
            width=5, label='Survived')
    plt.bar(bins, D[sex], color='#aaaaff', width=5, label='Died', alpha=0.4)
    plt.xlim(0, 80)
    plt.grid(None)
    
    plt.title(sex + " Survived")
    plt.xlabel("Age (years)")
    plt.legend()
    
(X_train, X_test, y_train, y_test) = cv.train_test_split(X, y, test_size=.05)
print X_train, y_train

# Logistic Regression from linear_model
logreg = lm.LogisticRegression();
logreg.fit(X_train, y_train)
y_predicted = logreg.predict(X_test)

plt.figure(figsize=(15,8));
plt.imshow(np.vstack((y_test, y_predicted)),
           interpolation='none', cmap='bone');
plt.xticks([]); plt.yticks([]);
plt.title(("Actual and predicted survival outcomes on the test set"))

