# How To Mine
Digcoin is mined by executing the `mine` action on the `digcoinsmine` contract. The `miner` field should contain the account sending the transaction, and the `symbol` field should contain `4,DIG`. Mining can be done manually via cleos or a block explorer that supports interacting with contracts. However, this mining software has been provided to make things less tedious.

## Miner Setup
1. Install the latest version of `cleos` and `Python 3` on your system if they are not already installed. EOS tooklit install instructions can be found [here](https://developers.eos.io/eosio-home/docs/setting-up-your-environment).
2. If necessary, follow [these instructions](https://developers.eos.io/eosio-home/docs/wallets) to set up your cleos wallet.
3. Clone this repo and navigate to its base directory.
4. Navigate to the `miner` directory and open the `config.json` file in your text editor of choice. Fill out the necessary fields (see the [help](config_help.md) text for config help)
5. Run the command `python3 minedig.py config.json`
6. Have fun digging, and don't forget to hydrate! 

**DISCLAIMER: This mining software will execute privileged commands using your EOS account's active permission. The author of this software will not be held liable for any damages or loss of funds. Always verify unknown software before running it, and always use best security practices when handling your private keys.**

# Donations
If you find this software useful, a donation of any amount to the account `digcoinminer` would be greatly appreciated.
