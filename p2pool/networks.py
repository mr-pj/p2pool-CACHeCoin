from p2pool.bitcoin import networks
from p2pool.util import math

# CHAIN_LENGTH = number of shares back client keeps
# REAL_CHAIN_LENGTH = maximum number of shares back client uses to compute payout
# REAL_CHAIN_LENGTH must always be <= CHAIN_LENGTH
# REAL_CHAIN_LENGTH must be changed in sync with all other clients
# changes can be done by changing one, then the other

nets = dict(
    cachecoin=math.Object(
        PARENT=networks.nets['cachecoin'],
        SHARE_PERIOD=120, # seconds
        CHAIN_LENGTH=12*60*60//120, # shares
        REAL_CHAIN_LENGTH=12*60*60//120, # shares
        TARGET_LOOKBEHIND=30, # shares
        SPREAD=36, # blocks
        IDENTIFIER='65375c4f7a4d584f'.decode('hex'),
        PREFIX='642a2c6524364268'.decode('hex'),
        P2P_PORT=2226,
        MIN_TARGET=4,
        MAX_TARGET=2**256//2**20 - 1,
        PERSIST=False,
        WORKER_PORT=8336,
        BOOTSTRAP_ADDRS='207.30.158.106 p2cache.syware.de q39.qhor.net q30.qhor.net'.split(' '),
        ANNOUNCE_CHANNEL='#cachecoin-bots',
        VERSION_CHECK=lambda v: True,
    ),
)
for net_name, net in nets.iteritems():
    net.NAME = net_name
