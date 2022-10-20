<<<<<<< HEAD
# Bitcoin Metrics

## About

BitcoinMetrics uses Python to extract and visualize data from the Bitcoin Blockchain.
* It connects to a Bitcoin node and makes rpc calls to get block data and stores the data in a csv file.
* It retrieves selected data from the csv file to use in chart visualizations.

## Examples

Time To Mine Each Bitcoin Block
![Time To Mine Each Bitcoin Block](https://github.com/callumr00/btcmetrics/blob/main/docs/img/1.png)

Size of Each Bitcoin Block
![Size of Each Bitcoin Block](https://github.com/callumr00/btcmetrics/blob/main/docs/img/1.png)

Weight of Each Bitcoin Block
![Weight of Each Bitcoin Block](https://github.com/callumr00/btcmetrics/blob/main/docs/img/1.png)

Difficulty of Each Bitcoin Block
![Difficulty of Each Bitcoin Block](https://github.com/callumr00/btcmetrics/blob/main/docs/img/1.png)

Number of Transactions in Each Bitcoin Block
![Number of Transactions in Each Bitcoin Block](https://github.com/callumr00/btcmetrics/blob/main/docs/img/1.png)

Total Number of Transactions on the Bitcoin Blockchain
![Total Number of Transactions on the Bitcoin Blockchain](https://github.com/callumr00/btcmetrics/blob/main/docs/img/1.png)

Bitcoin Issuance Schedule
![Bitcoin Issuance Schedule](https://github.com/callumr00/btcmetrics/blob/main/docs/img/1.png)

Bitcoin Supply Inflation
![Bitcoin Supply Inflation](https://github.com/callumr00/btcmetrics/blob/main/docs/img/1.png)

Average Transaction Fee in Each Bitcoin Block
![Average Transaction Fee in Each Bitcoin Block](https://github.com/callumr00/btcmetrics/blob/main/docs/img/1.png)

Sum of Transaction Fees in Each Bitcoin Block
![Sum of Transaction Fees in Each Bitcoin Block](https://github.com/callumr00/btcmetrics/blob/main/docs/img/1.png)

Sum of Transaction Fees in Each Bitcoin Block as a % of the Coinbase Amount
![Sum of Transaction Fees in Each Bitcoin Block as a % of the Coinbase Amount](https://github.com/callumr00/btcmetrics/blob/main/docs/img/1.png)

Coinbase Amount in Each Bitcoin Block
![Coinbase Amount in Each Bitcoin Block](https://github.com/callumr00/btcmetrics/blob/main/docs/img/1.png)

## Setup
### Cloning the project
```
git clone https://github.com/callumr00/btcmetrics.git
```

### Setting up
```
# Install Dependencies
pip install -r requirements.txt
```

### Data Set 
There is an included data set within the Github Repo. The data set is located [here](https://github.com/callumr00/btcmetrics/blob/main/sample/data/BlockData.csv). This data set is taken from a local Bitcoin node.

#### Update the data set
The data set included with the Github Repo will be slightly outdated by the time of your cloning. You may want to include the most recent blocks within the created visualizations. This requires connection to a Bitcoin node.

Run ExtractData.py to update the data set from your local node.
```
# Run ExtractData.py
cd sample; python ExtractData.py
```

#### Replace the data set
You may want to replace the data set with data from your own Bitcoin node to be assured of it's validity. This requires connection to a Bitcoin node.

Delete the current data set so that it can be replaced.
```
# Delete current data set
rm sample/data/blockData.csv
```

Navigate to where your Bitcoin node stores data and write to /.bitcoin/bitcoin.conf your desired username and password, used for the rpc connection.
```
# Create bitcoin.conf if it doesn't exist
touch /.bitcoin/bitcoin.conf

# Write to /.bitcoin/bitcoin.conf
rpcuser=[username]
rpcpassword=[password]
```

Write to sample/ConnectRPC.py the same username and password
```
usr = '[username]'
pw  = '[password]'
```

Run ExtractData.py to create a new data set from your local node.
```
# Run ExtractData.py
cd btcmetrics; cd sample; python ExtractData.py
```
For reference, this process takes me 4 hours to complete.

### Charts
You can create charts using the dataset stored at BitcoinMetrics/sample/data/blockData.csv. This does not require connection a Bitcoin node.

Run SelectChart.py to show the list of supported charts.
```
# Run SelectChart.py
cd sample; python SelectChart.py
```

Once ran, you will have a selection of charts to choose from, these are:

1. Block Time -- Time To Mine Each Bitcoin Block
2. Block Size -- Size of Each Bitcoin Block
3. Block Weight -- Weight of Each Bitcoin Block
4. Block Difficulty -- Difficulty of Each Bitcoin Block
5. Tx Per Block -- Number of Transactions in Each Bitcoin Block
6. Tx Total -- Total Number of Transactions on the Bitcoin Blockchain
7. Issuance Schedule -- Bitcoin Issuance Schedule
8. Supply Inflation -- Bitcoin Supply Inflation
9. Average Tx Fee -- Average Transaction Fee in Each Bitcoin Block
10. Total Tx Fees -- Sum of Transaction Fees in Each Bitcoin Block
11. Tx Fees as a % of Coinbase -- Sum of Transaction Fees in Each Bitcoin Block as a % of the Coinbase Amount
12. Block Coinbase -- Coinbase Amount in Each Bitcoin Block

Entered the associated number of the desired chart when prompted for an input.

![Terminal Output](https://github.com/callumr00/btcmetrics/blob/main/docs/img/TerminalOutput.png)

## License
This project is under the [MIT](https://github.com/callumr00/btcmetrics/blob/main/LICENSE) license.

## Changelog
You can find a list of implemented changes in the [CHANGELOG](https://github.com/callumr00/btcmetrics/blob/main/CHANGELOG.md).

## TODO
You can find a list of planned changes in the [TODO](https://github.com/callumr00/btcmetrics/blob/main/TODO.md).