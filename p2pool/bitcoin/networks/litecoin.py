import os
import platform

from twisted.internet import defer

from .. import data, helper
from p2pool.util import pack


P2P_PREFIX = 'fbc0b6db'.decode('hex')
P2P_PORT = 9333
ADDRESS_VERSION = 48
RPC_PORT = 9332
RPC_CHECK = defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            (yield helper.check_genesis_block(bitcoind, '12a765e31ffd4059bada1e25190f6e98c99d9714d334efa41a195a7e7e04bfe2')) and
            (yield bitcoind.rpc_getblockchaininfo())['chain'] != 'test'
        ))
SUBSIDY_FUNC = lambda height: 50*100000000 >> (height + 1)//840000
POW_FUNC = lambda data: pack.IntType(256).unpack(__import__('minu_scrypt').getPoWHash(data))
BLOCK_PERIOD = 150 # s
SYMBOL = 'minu'
CONF_FILE_FUNC = lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'minidoge') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/minidoge/') if platform.system() == 'Darwin' else os.path.expanduser('~/.minidoge'), 'minidoge.conf')
BLOCK_EXPLORER_URL_PREFIX = 'http://explorer.minidoge.net/block/'
ADDRESS_EXPLORER_URL_PREFIX = 'http://explorer.minidoge.net/address/'
TX_EXPLORER_URL_PREFIX = 'http://explorer.minidoge.net/tx/'
SANE_TARGET_RANGE = (2**256//1000000000 - 1, 2**256//1000 - 1)
DUMB_SCRYPT_DIFF = 2**16
DUST_THRESHOLD = 0.03e8
