# Import modules

import time

from btcrpc import rpc
from blockchainInfo import getBlockHeight

import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

import numpy  as np
import pandas as pd

from pathlib import Path
# --------------------------------------------------------------------------------------
# Start timer

startTime           = time.time()
# --------------------------------------------------------------------------------------
# Variables

# set max block height
maxHeight           = getBlockHeight()
# --------------------------------------------------------------------------------------
# Main
print('nTx                  :')

fileName = 'blockInfo.csv'
filePath = Path('data/' + fileName)

# load data frame
df = pd.read_csv(filePath)

# print stats
print('min tx               : ' + str(df['nTx'].min()))
print('max tx               : ' + str(df['nTx'].max()))

# show data frame
print(df)
# --------------------------------------------------------------------------------------
# Save data
dfData = df[['Block Height', 'nTx']]
dfData.to_csv('data/blockInfo Split/Block Transactions.csv', mode='w', index=False, header=True)

print(dfData)
# --------------------------------------------------------------------------------------
# Create chart

# variables
x = df['Block Height']
y = df['nTx']

axcol = 'orange'

# functions
# replace 1000 with 1
def thousands (x, pos):
    return '%1.0f' % (x * 1e-3)

# general
fig, ax = plt.subplots()
plt.scatter(x,y, color = axcol, s = 1, alpha = 0.2)
plt.plot(df['nTx'].rolling(2016).mean(), color = 'k', alpha = 0.6, linewidth = 1)

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.grid(True, which = 'major', axis = 'both', alpha = 0.4)
plt.title("Transactions Per Block",pad = 30)

# x
ax.set_xlabel("Block Height (thousands)", labelpad = 20)
ax.xaxis.set_major_formatter(FuncFormatter(thousands))
plt.xticks(np.arange(0,maxHeight,step = 210000))
plt.xlim([0, maxHeight])

# # y
ax.set_ylabel('Number of Transactions', labelpad = 20)
plt.ylim([1,6000])
# --------------------------------------------------------------------------------------
# Stop timer

executionTime = (time.time() - startTime)
print()
print('Execution time: ' + str(round(executionTime,3)) + 's')
# --------------------------------------------------------------------------------------
# Show chart

plt.show()