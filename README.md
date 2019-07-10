# bitcoin-burn-balance
This repository maintains the total amount of bitcoins that have been 'burnt'. 
Bitcoins sent to genesis block payout address, and certain address strings that
is believed to have no private key associated with it are considered burnt as nobody
can spend those bitcoins. These addresses are valid Bitcoin addresses, that is they meet
the mathematical requirements of the address just that they have been created without
someone owning the private key associated with it.

**Technical description:**
For example, the address '1BitcoinEaterAddressDontSendf59kuE' ends with f59kuE. That isn't 
just random gibberish the first person to send to that address made up.  All or part of that
is the checksum (mathematical verification that the address is valid). The checksum is what 
prevents you from making something up completely, and it exists primarily to prevent accidental
spends to typo addresses (it isn't technically required, but because it exists, it is extremely
unlikely that you can type an address wrong and send coins). The address also must only contain 
valid characters as defined by base-58 encoding, which prevents that particular address from 
being all caps (uppercase o and i are not allowed in base-58).
