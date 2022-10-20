import datetime
from pathlib import Path

import numpy  as np
import pandas as pd
from matplotlib.ticker import FuncFormatter
from matplotlib.ticker import FormatStrFormatter

from CreateChart import CreateChart

# Set file path for data set
file_name = 'BlockData.csv'
file_path = Path(f'data/{file_name}')

# Read data set
df = pd.read_csv(file_path, low_memory=False)

# Define formatting functions
def FormatMinutes (x, pos):
    '''Format values such that 60->1.'''
    return '%1.0f' % (x / 60)

def FormatThousands (x, pos):
    '''Format values such that 1000->1.'''
    return '%1.0f' % (x * 1e-3)

def FormatMillions (x, pos):
    '''Format values such that 1000000->1.'''
    return '%1.0f' % (x * 1e-6)

# Define chart functions
def ChartBlockTimeToMine():
    '''
    Create a chart to show the time to mine each Bitcoin block.
    
    Call function CreateChart() with desired variables such that a chart will
    be shown in the desired format and using the desired data set.
    '''

    CreateChart(
                chart_type='scatter', 
                x=df['Block Height'], 
                y=df['Time'].diff(), 
                average=df['Time'].diff().rolling(2016).mean(), 
                title='Time To Mine Each Bitcoin Block', 
                xlabel='Block Height (thousands)', 
                xformat=FuncFormatter(FormatThousands), 
                xticks=np.arange(0, len(df['Block Height']), step=21*10**4), 
                xlim=[0, len(df['Block Height'])], 
                ylabel='Time to Mine (minutes)', 
                yformat=FuncFormatter(FormatMinutes), 
                yticks=np.arange(0, 7201, step=600), 
                ylim=[1,7200],
                hline=600,
                )

def ChartBlockSize():
    '''
    Create a chart to show the size of each Bitcoin block.
    
    Call function CreateChart() with desired variables such that a chart will
    be shown in the desired format and using the desired data set.
    '''

    # Print info
    print(f'Smallest Block Size: {str(round(df["Size"].min() / (10**6), 6))} MB')
    print(f'Largest Block Size: {str(round(df["Size"].max() / (10**6), 6))} MB')
    print(f'Total Block Size: {str(round(df["Size"].cumsum().iloc[-1] / (10**9), 2))} GB')

    CreateChart(
                chart_type='scatter', 
                x=df['Block Height'], 
                y=df['Size'] / 10**6,
                average=df['Size'].rolling(2016).mean() / 10**6,
                title='Size of Each Bitcoin Block', 
                xlabel='Block Height (thousands)', 
                xformat=FuncFormatter(FormatThousands), 
                xticks=np.arange(0, len(df['Block Height']), step=21*10**4), 
                xlim=[0, len(df['Block Height'])], 
                ylabel='Block Size (MB)',  
                yformat=FormatStrFormatter('%.2f'), 
                yticks=np.arange(0, 3.01, step=0.5), 
                ylim=[0, 3.01],
                )

def ChartBlockWeight():
    '''
    Create a chart to show the weight of each Bitcoin block.
    
    Call function CreateChart() with desired variables such that a chart will
    be shown in the desired format and using the desired data set.
    '''

    # Print info
    print(f'Smallest Block Weight: {str(df["Weight"].min())}')
    print(f'Largest Block Weight: {str(df["Weight"].max())}')
    print(f'Max Block Weight: {4*10**6}')

    CreateChart(
                chart_type='scatter', 
                x=df['Block Height'], 
                y=df['Weight'],
                average=df['Weight'].rolling(2016).mean(), 
                title='Weight of Each Bitcoin Block', 
                xlabel='Block Height (thousands)', 
                xformat=FuncFormatter(FormatThousands), 
                xticks=np.arange(0, len(df['Block Height']), step=21*10**4), 
                xlim=[0, len(df['Block Height'])], 
                ylabel='Block Weight (millions)', 
                yformat=FuncFormatter(FormatMillions), 
                yticks=np.arange(0, (4*10**6) + 1, step=10**6), 
                ylim=[1, (4*10**6) + 1],
                )

def ChartBlockDifficulty(): 
    '''
    Create a chart to show the difficulty of each Bitcoin block.
    
    Call function CreateChart() with desired variables such that a chart will
    be shown in the desired format and using the desired data set.
    '''

    # Print info
    print(f'Current Block Difficulty: {str(df["Difficulty"].iloc[-1])}') 

    CreateChart(
                chart_type='line', 
                x=df['Block Height'], 
                y=df['Difficulty'], 
                title='Difficulty of Each Bitcoin Block', 
                xlabel='Block Height (thousands)', 
                xformat=FuncFormatter(FormatThousands), 
                xticks=np.arange(0, len(df['Block Height']), step=21*10**4), 
                xlim=[0, len(df['Block Height'])], 
                ylabel='Difficulty', 
                ylim=[1, 10**14],
                yscale='log',
                )

def ChartTxPerBlock():
    '''
    Create a chart to show the number of transactions in each Bitcoin block.
    
    Call function CreateChart() with desired variables such that a chart will
    be shown in the desired format and using the desired data set.
    '''

    # Print info
    print(f'Lowest Number of Transactions in a Block: {str(df["nTx"].min())}')
    print(f'Highest Number of Transactions in a Block: {str(df["nTx"].max())}')

    CreateChart(
                chart_type='scatter', 
                x=df['Block Height'], 
                y=df['nTx'], 
                average=df['nTx'].rolling(2016).mean(), 
                title='Number of Transactions in Each Bitcoin Block', 
                xlabel='Block Height (thousands)', 
                xformat=FuncFormatter(FormatThousands), 
                xticks=np.arange(0, len(df['Block Height']), step=21*10**4), 
                xlim=[0, len(df['Block Height'])], 
                ylabel='Number of Transactions', 
                ylim=[1, 6*10**3],
                )

def ChartTxTotal():
    '''
    Create a chart to show the total number of transactions in Bitcoin blockchain.
    
    Call function CreateChart() with desired variables such that a chart will
    be shown in the desired format and using the desired data set.
    '''

    # Print info
    print(f'Total Number of Transactions: {str(df["nTx"].cumsum().iloc[-1])}')

    CreateChart(
                chart_type='line', 
                x=df['Block Height'], 
                y=df['nTx'].cumsum(), 
                title='Total Number of Transactions on the Bitcoin Blockchain', 
                xlabel='Block Height (thousands)', 
                xformat=FuncFormatter(FormatThousands), 
                xticks=np.arange(0, len(df['Block Height']), step=21*10**4), 
                xlim=[0, len(df['Block Height'])], 
                ylabel='Number of Transactions',  
                yticks=np.arange(0, (10**9) + 1, step=10**8), 
                ylim=[1, 10**9],
                )

def ChartIssuanceSchedule():
    '''
    Create a chart to show the targetted issuance schedule of the Bitcoin network
    compared to the actual issuance.

    The targetted issuance schedule is based on a desired 10 minute / 600 second
    gap between the creation of blocks.
    
    Call function CreateChart() with desired variables such that a chart will
    be shown in the desired format and using the desired data set.
    '''

    genesis_time = df['Time'].iloc[0]
    actual_block_date = []
    target_block_date = []

    # Get block timestamps for actual issuance schedule
    for i in df['Time']:
        actual_block_date.append(datetime.datetime.fromtimestamp(i))

    # Get block timestamps for targetted issuance schedule where a block is created
    # on average every 10 minutes or 600 seconds from the genesis (initial) block.
    for i in df['Block Height']:
        target_block_date.append(datetime.datetime.fromtimestamp(genesis_time + (i * 600)))

    CreateChart(
                chart_type='line', 
                x=actual_block_date, 
                y=df['Block Reward'].cumsum(), 
                x2=target_block_date,
                title='Bitcoin Issuance Schedule', 
                xlabel='Year', 
                ylabel='Existing Coins (millions)',
                yformat=FuncFormatter(FormatMillions),  
                yticks=np.arange(0, (21*10**6)+1, step=(21*10**6)/7),
                ylim=[0, 21*10**6],
                )

def ChartSupplyInflation(): 
    '''
    Create a chart to show the targetted supply inflation of the Bitcoin network and
    the associated number of coins in circulation.
    
    Call function CreateChart() with desired variables such that a chart will
    be shown in the desired format and using the desired data set.
    '''

    print('Chart Supply Inflation is not currently working.')
    return # BROKEN

    charted_halvings = 14 # max 33
    blocks_per_year = 52560

    # Call GetBlockRewards(block_height) to return a list of all block reward values
    # up to the specified block height
    block_rewards = GetBlockRewards(charted_halvings * blocks_per_halving)

    # Get the cumulative sum of block rewards to show the number of coins in circulation
    coin_supply = pd.Series(data=block_rewards).cumsum()

    inflation_rate = []

    # Get the annualized supply inflation rate at each block
    for i in range(len(coin_supply)):
        inflation_rate.append((block_rewards[i] * blocks_per_year) / coin_supply[i])

    CreateChart(
                chart_type='line', 
                x=np.arange(0, (charted_halvings * 21*10**6)), 
                y=coin_supply, 
                y2=inflation_rate,
                title='Bitcoin Supply Inflation', 
                xlabel='Block Height (thousands)', 
                xformat=FuncFormatter(FormatThousands), 
                xticks=np.arange(0, (charted_halvings * 21*10**6), step=21*10**4), 
                xlim=[0, (charted_halvings * 21*10**6)], 
                ylabel='Existing Coins (millions)',
                yformat=FuncFormatter(FormatMillions),  
                yticks=np.arange(0, (21*10**6)+1, step=(21*10**6)/7),
                ylim=[0, 21*10**6],
                y2label='% Inflation Rate',
                vline=len(df['Block Height']),  
                )

def ChartBlockAvgTxFee():
    '''
    Create a chart to show the average transaction fee in each Bitcoin block.
    
    Call function CreateChart() with desired variables such that a chart will
    be shown in the desired format and using the desired data set.
    '''
    
    CreateChart(
                chart_type='scatter', 
                x=df['Block Height'], 
                y=(df['Coinbase'] - df['Block Reward']) / df['nTx'], 
                average=((df['Coinbase'] - df['Block Reward']) / df['nTx']).rolling(2016).mean(),
                title='Average Transaction Fee in Each Bitcoin Block', 
                xlabel='Block Height (thousands)', 
                xformat=FuncFormatter(FormatThousands), 
                xticks=np.arange(0, len(df['Block Height']), step=21*10**4), 
                xlim=[0, len(df['Block Height'])], 
                ylabel='Transaction Fee (BTC)',  
                ylim=[0, 0.01401],
                )

def ChartBlockSumTxFees():
    '''
    Create a chart to show the sum of transaction fees in each Bitcoin block.
    
    Call function CreateChart() with desired variables such that a chart will
    be shown in the desired format and using the desired data set.
    '''

    CreateChart(
                chart_type='scatter', 
                x=df['Block Height'], 
                y=(df['Coinbase'] - df['Block Reward']), 
                average=(df['Coinbase'] - df['Block Reward']).rolling(2016).mean(),
                title='Sum of Transaction Fees in Each Bitcoin Block', 
                xlabel='Block Height (thousands)', 
                xformat=FuncFormatter(FormatThousands), 
                xticks=np.arange(0, len(df['Block Height']), step=21*10**4), 
                xlim=[0, len(df['Block Height'])], 
                ylabel='Transaction Fees (BTC)',  
                ylim=[0, 16],
                )

def ChartBlockSumTxFeesPctCoinbase():
    '''
    Create a chart to show the sum of transaction fees in each Bitcoin block as a % of that block's coinbase amount.
    
    Call function CreateChart() with desired variables such that a chart will
    be shown in the desired format and using the desired data set.
    '''
    
    CreateChart(
                chart_type='scatter', 
                x=df['Block Height'], 
                y=(1 - (df['Block Reward'] / df['Coinbase'])) * 100, 
                average=(1 - (df['Block Reward'] / df['Coinbase'])).rolling(2016).mean() * 100,
                title='Sum of Transaction Fees in Each Bitcoin Block as a % of the Coinbase Amount', 
                xlabel='Block Height (thousands)', 
                xformat=FuncFormatter(FormatThousands), 
                xticks=np.arange(0, len(df['Block Height']), step=21*10**4), 
                xlim=[0, len(df['Block Height'])], 
                ylabel='% of Coinbase',  
                ylim=[0, 100.1],
                )

def ChartBlockCoinbase(): 
    '''
    Create a chart to show the coinbase amount in each Bitcoin block.
    
    Call function CreateChart() with desired variables such that a chart will
    be shown in the desired format and using the desired data set.
    '''

    CreateChart(
                chart_type='scatter', 
                x=df['Block Height'], 
                y=df['Coinbase'], 
                average=df['Coinbase'].rolling(2016).mean(),
                title='Coinbase Amount in Each Bitcoin Block', 
                xlabel='Block Height (thousands)', 
                xformat=FuncFormatter(FormatThousands), 
                xticks=np.arange(0, len(df['Block Height']), step=21*10**4), 
                xlim=[0, len(df['Block Height'])], 
                ylabel='Coinbase Amount (BTC)',  
                ylim=[0, 60.1],
                )