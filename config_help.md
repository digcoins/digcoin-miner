**account**: The EOS account name that you wish to mine with. You must have the private keys associated with this account's active permission.

**wallet_name**: The cleos wallet name that contains the private key for your account's active permission. If you didn't specify a name, this should be set to "default".

**wallet_password**: The password that was printed out when you used the `cleos wallet create` command.

**cleos_path**: The directory path where the cleos executable resides on your system. On Unix-like systems, find this with the command `which cleos`.

**num_threads**: The number of simultaneous mining threads you want to run. Each thread does roughly one mining attempt per block. The higher this value is, the more mining attempts will be done per block, and the more of your EOS resources will be used.

**verbose_errors**: Set to true to see error messages in the console.

**api_urls**: The list of blockchain node API URL's that you want to cycle through. It is recommended to use at least one URL per thread, more if possible. Most block producers have their own API endpoints, which can be found by appending `/bp.json` to their website URL. For example: `cypherglass.com/bp.json`