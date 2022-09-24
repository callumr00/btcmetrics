# Import modules

import time

from btcrpc import rpc
from blockchainInfo import getBlockHeight

import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

import numpy  as np
import pandas as pd

from pathlib import Path

import os
# --------------------------------------------------------------------------------------
# Start timer

startTime           = time.time()
# --------------------------------------------------------------------------------------
# Variables

# set max block height
maxHeight           = getBlockHeight()
# --------------------------------------------------------------------------------------
# Main
print('nTXpS                :')

fileName = 'blockInfo.csv'
filePath = Path('data/' + fileName)

# load data frame
df = pd.read_csv(filePath)
print(df)

blockHeight = df['Block Height']
time = df['Time']
medianTime = df['Median Time']
nTx = df['nTx']

# print(df.iloc[1,2])
# print(df.iloc[2,2])
# print(df.iloc[3,2])
# print(df.iloc[2,2]-df.iloc[1,2])

# timeDiff = []
# for i in time:
#     difference = df.iloc[i,2]-df.iloc[i-1,2]
#     timeDiff.append(difference)
# print(timeDiff)

# Total cumulative tx
df['ntxtotal'] = df['nTx'].cumsum()
# Time per block
df['timediff'] = df['Time'].diff()
# Median time per block
df['medtimediff'] = df['Median Time'].diff()
# tx per second
df['txps'] = df['nTx']/df['Time'].diff()

print(df)
df = df.drop(['Difficulty','Chainwork','Stripped Size','Size','Weight'], axis=1)
print(df)


fileName = 'txData.csv'
filePath = Path('data/' + fileName)
open(filePath, 'x')
# export data frame to csv
if os.path.getsize(filePath) == 0:
    df.to_csv(filePath, mode='w', index=False, header=True)
else:
    df.to_csv(filePath, mode='a', index=False, header=False)

    # df2 = pd.DataFrame(
    #     {
    #         'Block Height' : blockHeight
    #         'Time Diff' : timeDiff
    #     }
    # )

# while blockHeight > 1 & blockHeight <= 10:
#     timeDiff = print(df.iloc[blockHeight])

# --------------------------------------------------------------------------------------
# Create chart

# variables
x = df['Block Height']
y = df['txps']

axcol = 'orange'

# functions
# replace 1000 with 1
def thousands (x, pos):
    return '%1.0f' % (x * 1e-3)

# general
fig, ax = plt.subplots()
ax.plot(x,y, color = axcol)

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.grid(True, which = 'major', axis = 'both', alpha = 0.4)
plt.title("nTxpS",pad = 30)

# x
ax.set_xlabel("Block Height (thousands)", labelpad = 20)
ax.xaxis.set_major_formatter(FuncFormatter(thousands))
plt.xlim([0, maxHeight])

# y
ax.set_ylabel('Difficulty', labelpad = 20)
# plt.yscale('log')
# plt.ylim([1,20000])
# --------------------------------------------------------------------------------------
# Stop timer

# executionTime = (time.time() - startTime)
# print()
# print('Execution time: ' + str(round(executionTime,3)) + 's')
# # --------------------------------------------------------------------------------------
# Show chart

plt.show()