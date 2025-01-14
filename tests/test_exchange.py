from capitalgram.chain import ChainId
from capitalgram.exchange import Exchange, ExchangeType


def test_create_exchange():
    exchange = Exchange(
        chain_id=ChainId.ethereum,
        exchange_id=1,
        address="0x0000000000000000000000000000000000000000",
        exchange_type=ExchangeType.uniswap_v2,
        pair_count=0,
    )
    assert str(exchange) == "<Exchange <unknown> at 0x0000000000000000000000000000000000000000 on Ethereum>"

