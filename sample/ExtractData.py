import os
from pathlib import Path
import time

import numpy  as np
import pandas as pd
from tqdm import tqdm
from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException

from ConnectRPC import rpc

# Start timer
startTime = time.time()

# Print project name and script name
project = os.path.basename(os.path.dirname(os.path.dirname(__file__)))
script, _ = os.path.splitext(os.path.basename(__file__))
print('\n', f'{project} | {script}'.center(os.get_terminal_size().columns, ' '))

# Set file path for data file
file_name = 'BlockData.csv'
file_path = Path(f'data/{file_name}')

def GetBlockHeight():
    '''Get the current block height of the Bitcoin blockchain.'''

    blockchainInfo = rpc.getblockchaininfo()
    block_height = blockchainInfo['blocks']
    return block_height - 6 # 6 blocks deep

max_height = GetBlockHeight()

def GetBlockRewards(max_height):
    '''Calculate the block reward for each block.

    For each block, calculate the block reward based on the initial reward of 50
    and the number of block reward halvings that have taken place. A halving occurs
    every 210000 blocks.
    '''

    halvings = 0
    block_rewards = []

    for i in range(0, max_height + 1):
        if i >= 210000 and i % 210000 == 0:
            halvings += 1
        block_reward = 50/2**halvings
        block_rewards.append(block_reward)
    
    block_rewards.pop(0) # Genesis block transaction cannot be retrieved

    return block_rewards

def ExtractData(start_height=0):
    '''Extract data from each block in the Bitcoin blockchain.

    Make rpc calls for each block, store the data in a list then convert the lists
    into a pandas dataframe and export the dataframe to a csv file.
    '''

    # Create lists to later append to
    block_coinbases = []
    block_time = []
    block_median_time = []
    block_difficulty = []
    block_chainwork = []
    block_transactions = []
    block_stripped_size = []
    block_size = []
    block_weight = []

    def GetCoinbases(block_height):
        '''Get the coinbase amount for each Bitcoin block.'''

        if block_height == 0: # Genesis block transaction cannot be retrieved
            return
            
        amnt = 0

        tx = block_info['tx'][0]
        encoded_tx = rpc.getrawtransaction(tx)
        decoded_tx = rpc.decoderawtransaction(encoded_tx)

        # Sum all values of recipients of the coinbase transaction
        for i in range(len(decoded_tx["vout"])):
            amnt += decoded_tx["vout"][i]["value"]

        return amnt
        
    # Get data from each block
    for block_height in tqdm(range(start_height, max_height)):
        block_hash = rpc.getblockhash(block_height)
        block_info = rpc.getblock(block_hash)

        # Get data and append to it's associated list
        block_time.append(block_info['time'])
        block_median_time.append(block_info['mediantime'])
        block_difficulty.append(float(block_info['difficulty']))
        block_chainwork.append(int(block_info['chainwork'], base=16)) # Convert Hex to Dec
        block_transactions.append(block_info['nTx'])
        block_stripped_size.append(block_info['strippedsize'])
        block_size.append(block_info['size'])
        block_weight.append(block_info['weight'])
        block_coinbases.append(float(GetCoinbases(block_height)))

    if start_height == 0:
        block_coinbases.insert(0, 'null') # Genesis block transaction cannot be retrieved

    # Convert lists to a dataframe
    df = pd.DataFrame(
        {
            'Block Height': range(start_height, max_height),
            'Block Reward': GetBlockRewards(max_height)[start_height:],
            'Coinbase': block_coinbases,
            'Time': block_time,
            'Median Time': block_median_time,
            'Difficulty': block_difficulty,
            'Chainwork': block_chainwork,
            'nTx': block_transactions,
            'Stripped Size': block_stripped_size,
            'Size': block_size,
            'Weight': block_weight,
        }
    )

    # Export data frame to CSV
    if os.path.getsize(file_path) == 0:
        df.to_csv(file_path, mode='w', index=False, header=True)
    else:
        df.to_csv(file_path, mode='a', index=False, header=False)

    print('\nComplete.')

def CheckData():
    '''Check data file and get data based on state.

    If the file isn't found, create it, extract data starting at height 0 and append
    it to file. Then show the data.
    
    If the file is empty, extract data starting at height 0 and append it to file. 
    Then show the data.

    If the file is outdated (max recorded height is lower than max actual height),
    extract data starting from max recorded height and append it to file.
    Then show the data.

    If the file is up to date (max recorded height is equal to max actual height),
    show the data. 
    '''

    print(f'\nChecking {file_name}...')

    # If file isn't found, create it
    if not file_path.is_file():
        print(f'\n{file_name} not found; creating file...')
        open(file_path, 'x')
        print('\nFile created.')
        print(f"\nGetting data from {max_height} blocks...\n")
        ExtractData(start_height=0)

    # If file is empty, populate it
    elif os.path.getsize(Path(f'data/BlockData.csv')) == 0:
        print(f'\n{file_name} is empty; populating file...')
        print(f"\nGetting data from {max_height} blocks...\n")
        ExtractData(start_height=0)
        
    # If file is outdated, update it
    elif pd.read_csv(file_path, low_memory=False).shape[0] < max_height:
        print(f'\n{file_name} is outdated; updating file...')
        print(f"\nGetting data from {max_height-pd.read_csv(file_path, low_memory=False).shape[0]} blocks...\n")
        ExtractData(start_height=pd.read_csv(file_path, low_memory=False).shape[0])

    # If file is up to date, pass
    elif max_height == pd.read_csv(file_path, low_memory=False).shape[0]:
        print(f'\n{file_name} is up to date.')
    
    # Read csv file
    df = pd.read_csv(file_path, low_memory=False)
    df.set_index('Block Height', inplace=True, drop=True)

    # Print data
    print(f"\n{'─'*os.get_terminal_size().columns}\n")
    print(f'{df}\n')

CheckData()

# Stop timer and print result
executionTime = (time.time() - startTime)
print(f'Execution time: {str(round(executionTime,3))}s\n')