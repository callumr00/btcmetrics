# Import modules

from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException

# Variables

# Set login credentials -> /mnt/btc/.bitcoin/bitcoin.conf
usr = 'usr'
pw  = 'pw'

# Connect to node
rpc = AuthServiceProxy("http://%s:%s@127.0.0.1:8332"%(usr, pw))