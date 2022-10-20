from pathlib import Path

import numpy  as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

from ExtractData import GetBlockRewards
from ChartSettings import FormatThousands, FormatMillions

def ChartSupplyInflation():
    file_name = 'BlockData.csv'
    file_path = Path(f'data/{file_name}')

    df = pd.read_csv(file_path, low_memory=False)

    charted_halvings = 14 # max 33
    blocks_per_year = 52560

    block_rewards = GetBlockRewards(charted_halvings * 21*10**4)
    coin_supply = pd.Series(data=block_rewards).cumsum()

    inflation = []
    
    for i in range(len(coin_supply)):
        inflation.append(round((block_rewards[i] * blocks_per_year) / coin_supply[i], 6))

    inflation_rate = pd.Series(data=inflation) * 100

    x = np.arange(0, (charted_halvings * 21*10**4))
    y1 = coin_supply
    y2 = inflation_rate

    ax1col = 'black'
    ax2col = 'orange'

    fig, ax1 = plt.subplots()

    plt.title("Bitcoin Supply Inflation", pad=30)

    plt.axvline(x = len(df['Block Height']), color = ax1col, linestyle='--')

    ax1.plot(x, y1, color = ax1col)
    ax1.spines['top'].set_visible(False)
    ax1.spines['right'].set_visible(False)
    ax1.tick_params(axis = 'y', labelcolor = ax1col, color = 'white')
    plt.grid(True, which='major', axis='both', alpha=0.4)

    ax1.set_xlabel("Block Height (thousands)", labelpad=20)
    ax1.xaxis.set_major_formatter(FuncFormatter(FormatThousands))
    plt.xticks(np.arange(0, (charted_halvings * 21*10**4), step=21*10**4))
    plt.xlim([0, (charted_halvings * 21*10**4)])
    ax1.set_ylabel('Existing Coins (millions)', color=ax1col, labelpad=20)
    ax1.yaxis.set_major_formatter(FuncFormatter(FormatMillions))
    plt.yticks(np.arange(0, 21*10**6 + 1, step=21*10**6 / 7))
    plt.ylim([0, 21*10**6])

    ax2 = ax1.twinx()
    ax2.plot(x, y2, color = ax2col)
    ax2.spines['top'].set_visible(False)
    ax2.spines['right'].set_visible(False)
    ax2.tick_params(axis = 'y', labelcolor = ax2col, color = 'white')


    ax2.set_ylabel('% Inflation Rate', color=ax2col, labelpad=20)
    plt.ylim([0.0001, 1000])
    plt.yscale('log')
    plt.minorticks_off()

    plt.show()  

ChartSupplyInflation()