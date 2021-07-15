"""Generic units used in data models used in Capitalgram.

Types aliases are used to give human-readable meaning for various arguments and return values.
"""


#: 64-bit integer based primary key
PrimaryKey = int

#: Ethereum address that does *not* use EIP-55 checksumming https://github.com/ethereum/EIPs/blob/master/EIPS/eip-55.md
NonChecksummedAddress = str

#: Used in exchange rates, volumes and prices in candle data.
#: Normally you should not use float for pricing,
#: but because we are already losing a lot of accuraty in float conversion
#: and our price data is not for exact transactions, but for modelling,
#: this is ok.
USDollarAmount = float

#: Seconds since 1.1.1970 as UTC time as integer.
UNIXTimestamp = int

#: EVM block number from 1 to infinity
BlockNumber = int

#: Multiplier as 1/10000 or 0.01%
BasisPoint = int