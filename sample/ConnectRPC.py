from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException

# Set login credentials -> /mnt/btc/.bitcoin/bitcoin.conf
usr = 'callum'
pw  = '4D1C39DBB90939FBD720474946B9450AE04743157C7B32AF2EB643699CE4B23B'

# Connect to node
rpc = AuthServiceProxy("http://%s:%s@127.0.0.1:8332"%(usr, pw))