import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('NADAC_as_of_2017-09-06.csv', thousands=',')  # thousands argument tells pandas that these are floats

print(df.shape)
df = df.drop_duplicates(['NDC Description'], keep='first')
print(df.shape)

prices = df['NADAC_Per_Unit'].tolist()
print(prices)

sns.set_style('whitegrid')
sns.kdeplot(np.array(prices), bw=1, shade=True)
plt.title('Drug Price (NADAC) Probability Density')
plt.ylabel('Density')
plt.xlabel('Price')
sns.plt.show()


sns.set_style('whitegrid')
sns.kdeplot(np.array(prices), bw=1, shade=True)
plt.title('Drug Price (NADAC) Natural Log Probability Density')
plt.ylabel('Density')
plt.xlabel('Natural Log Price')
plt.xscale('log')
sns.plt.show()


