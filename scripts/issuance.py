# Import modules
import time

from btcrpc import rpc

import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

import numpy  as np
import pandas as pd

from pathlib import Path

import datetime
# --------------------------------------------------------------------------------------
# Start timer

startTime           = time.time()
# --------------------------------------------------------------------------------------
# Variables

# --------------------------------------------------------------------------------------
# Main

maxCoins            = 21000000

aDateList           = []
eDateList           = []
supplyList          = []

print('test                 :')

fileName = 'blockInfo.csv'
filePath = Path('data/' + fileName)

# load data frame
df = pd.read_csv(filePath)

for item in df['Time']:
    # get a(ctual) block dates
    aDateList.append(datetime.datetime.fromtimestamp(item))

aBlockDate = pd.Series(data = aDateList)
print('actual block dates   :')
print(aBlockDate)
print()

genesisTime         = df['Time'].iloc[0]

for item in df['Block Height']:
    # get t(arget) block dates
    eDateList.append(datetime.datetime.fromtimestamp(genesisTime + (item * 600)))
    # get circulating supply
    supplyList.append(50/2**(np.floor(item/210000)))

tBlockDate = pd.Series(data = eDateList)
print('target block dates   :')
print(tBlockDate)
print()

coinSupply = pd.Series(data = supplyList).cumsum()
print('coin supply          :')
print(coinSupply)
print()
# --------------------------------------------------------------------------------------
# Save data
dfData = pd.DataFrame({'Actual Block Date': aBlockDate, 'Target Block Date': tBlockDate, 'Coin Supply': coinSupply})
dfData.to_csv('data/blockInfo Split/Block Issuance.csv', mode='w', index=False, header=True)

print(dfData)
# --------------------------------------------------------------------------------------
# Create chart

# variables
x1 = aBlockDate
x2 = tBlockDate
y = coinSupply

axcol1 = 'orange'
axcol2 = 'black'

# functions
# replace 1000000 with 1
def millions (x, pos):
    return '%1.0f' % (x * 1e-6)

# general
fig, ax = plt.subplots()

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# x


# y
ax.set_ylabel('Existing Coins (millions)', labelpad = 20)
ax.plot(x1, y, color = axcol1)
ax.plot(x2, y, color = axcol2, alpha = 0.4)
ax.tick_params(axis = 'y', color = 'white')
ax.yaxis.set_major_formatter(FuncFormatter(millions))
plt.ylim([0, maxCoins])
plt.yticks(np.arange(0, maxCoins + 1,step = maxCoins / 7))
plt.grid(True, which = 'major', axis = 'both', alpha = 0.4)

# set title
plt.title("Bitcoin Issuance Schedule",pad = 30)

# --------------------------------------------------------------------------------------
# Stop timer

executionTime = (time.time() - startTime)
print()
print('Execution time: ' + str(round(executionTime,3)) + 's')
# --------------------------------------------------------------------------------------
# Show chart

plt.show()