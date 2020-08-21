# Bitcoin Burn Balance
This repository maintains the total amount of bitcoins that have been 'burnt'. 
Bitcoin sent to genesis block payout address, and certain address strings that
is believed to have no private key associated with it are considered burnt as nobody
can spend those bitcoins. These addresses are valid Bitcoin addresses, that is they meet
the mathematical requirements of the address just that they have been created without
someone owning the private key associated with it.

**Technical description:**
Many bitcoins have been lost in the past either due to human error, or some protocol issues
which were fixed later. For example, due to an early problem in Bitcoin, fixed by BIP30, it 
was possible to create a coinbase transaction identical to a previous coinbase. This caused 
the coins created by that older coinbase to be irreversibly "overwritten". This happened in 
block 91842 (overwriting the coinbase of block 91812) and 91880 (overwriting the coinbase of 
block 91722). Each time, 50 BTC was lost.

There were cases where miners have claimed less BTC from the block subsidy than what could
have been claimed. For example, between block 162705 and block 169899, 193 blocks claimed 
less than allowed due to a bug, resulting in a total loss of 9.66184623 BTC.

Moreover, there are certain addresses where sending BTC to them is considered to be burnt.
For example, consider the address '1BitcoinEaterAddressDontSendf59kuE'. This address is 
perfectly valid but the odds of someone owning the private key to this address is absolutely
minimal. Finding the private key associated will mean brute forcing Bitcoin's entire private 
key space. The list of such addresses is associated in the "burn_address.txt" file.


