import pandas as pd
import statsmodels.formula.api as smf
from matplotlib import pyplot as plt

df = pd.read_csv('/Users/MacBook/Downloads/Book_Code/Chapter6/sports.csv', index_col=0)
fig, axs = plt.subplots(1, 3, sharey=True)
df.plot(kind='scatter', x='sports', y='acceptance', ax=axs[0], figsize=(16, 8))
df.plot(kind='scatter', x='music', y='acceptance', ax=axs[1])
df.plot(kind='scatter', x='academic', y='acceptance', ax=axs[2])

# create a fitted model in one line
lm = smf.ols(formula='acceptance ~ music', data=df).fit()

X_new = pd.DataFrame({'music': [df.music.min(), df.music.max()]})
preds = lm.predict(X_new)

df.plot(kind='scatter', x='music', y='acceptance', figsize=(12,12), s=50)

plt.title("Linear Regression - Fitting Music vs Acceptance Rate", fontsize=20)
plt.xlabel("Music", fontsize=16)
plt.ylabel("Acceptance", fontsize=16)

# then, plot the least squares line
plt.plot(X_new, preds, c='red', linewidth=2)

