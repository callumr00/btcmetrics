import os
from pathlib import Path

from context import rpc

# Print title in terminal where title = project name and script name
project = os.path.basename(os.path.dirname(os.path.dirname(__file__)))
script, _ = os.path.splitext(os.path.basename(__file__))
print('\n', f'{project} | {script}'.center(os.get_terminal_size().columns, ' '))

test_height = int(input(f'\nEnter Block Height: '))

def BlockRewards(test_height):
    '''Calculate the block reward for each block.

    For each block, calculate the block reward based
    on the initial reward of 50 and the number of
    block reward halvings that have taken place. A
    halving occurs every 210000 blocks.
    '''
    halvings = 0
    block_rewards = []

    for i in range(0, test_height + 1):
        if i >= 210000 and i % 210000 == 0:
            halvings += 1
        block_reward = 50/2**halvings
        block_rewards.append(block_reward)

    return block_rewards[test_height]

def ExtractData(start_height=0):
    '''Print data from a single block in the Bitcoin blockchain.'''

    block_hash = rpc.getblockhash(test_height)
    print(f'\nBlock Hash:\n{block_hash}\n')

    block_info = rpc.getblock(block_hash)
    print(f'Block Info:\n{block_info}\n')

    print(f'Time:\n{block_info["time"]}\n')
    print(f'Median Time:\n{block_info["mediantime"]}\n')
    print(f'Difficulty:\n{block_info["difficulty"]}\n')
    print(f'Chainwork (Hex):\n{block_info["chainwork"]}\n')
    print(f'Chainwork (Dec):\n{int(block_info["chainwork"], base=16)}\n')
    print(f'Number of Transactions:\n{block_info["nTx"]}\n')
    print(f'Stripped Size:\n{block_info["strippedsize"]}\n')
    print(f'Size:\n{block_info["size"]}\n')
    print(f'Weight:\n{block_info["weight"]}\n')

    # Get the value of the coinbase transaction
    coinbase = block_info['tx'][0]
    print(f'Coinbase TX Hash:\n{block_info["tx"][0]}\n')
    encoded_tx = rpc.getrawtransaction(coinbase)
    print(f'Raw Coinbase TX:\n{rpc.getrawtransaction(coinbase)}\n')
    decoded_tx = rpc.decoderawtransaction(encoded_tx)
    print(f'Decoded Coinbase TX:\n{rpc.decoderawtransaction(encoded_tx)}\n')

    def GetCoinbase():
        amnt = 0

        tx = block_info['tx'][0]
        encoded_tx = rpc.getrawtransaction(tx)
        decoded_tx = rpc.decoderawtransaction(encoded_tx)

        for i in range(len(decoded_tx["vout"])):
            amnt += decoded_tx["vout"][i]["value"]

        return amnt

    print(f'Coinbase Value:\n{float(decoded_tx["vout"][0]["value"])}\n')

    print(f'Block Reward:\n{BlockRewards(test_height)}\n')

    print(f'Tx Fees:\n{round(float(decoded_tx["vout"][0]["value"]) - BlockRewards(test_height),8)}\n')

ExtractData(test_height)