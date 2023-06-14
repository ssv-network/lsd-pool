# 🥩 Awesome SSV Staking Frontend 🥩

🚀 By staking their ETH to a staking contract, users receive a liquid staked derivative token called ssvETH. This allows them to earn compound interest on their staked ETH, while also being able to use the ssvETH tokens in other DeFi protocols without having to unstake their original ETH.

🙏 For aditional functionality and documentation check the amazing [scaffold-eth](https://github.com/scaffold-eth/scaffold-eth) repo this frontend is based on!

# Live Deployment

You can find our live demo deployment [Here](https://awesome-ssv-frontend-3.surge.sh/). You can stake your Goerli here or launch your own pool! 

# 🚀 Quick Start Frontend

Prerequisites: [Node (v18 LTS)](https://nodejs.org/en/download/) plus [Yarn (v1.x)](https://classic.yarnpkg.com/en/docs/install/) and [Git](https://git-scm.com/downloads)

🚨 If you are using a version < v18 you will need to remove `openssl-legacy-provider` from the `start` script in `package.json`

## Installation

> 1️⃣ clone/fork awesome SSV Staking repo:

```bash
git clone https://github.com/ssv-network/lsd-pool/ && cd lsd-pool
```

> 2️⃣ make sure you have the right network set

> 3️⃣ install and start the frontend:

```bash
cd frontend
yarn install
yarn react-app:start
```

📱 Open http://localhost:3000 to see the app

❗❗ Important : Make sure that your front end is connected to the correct chain in `frontend/packages/react-app/src/App.jsx`, either:

1. `const initialNetwork = NETWORKS.goerli;` for using the live Goerli network.

or

2. `const initialNetwork = NETWORKS.localhost;` if running with `yarn fork`.

# Frontend Editing

📝 Edit your frontend `App.jsx` in `packages/react-app/src`

📝 Point your frontend to your already deployed contracts by changing the `"address":` field either in `"goerli"` or `"localhost"` section in the file `packages/react-app/src/contracts/hardhat_contracts.json`

✏ Edit the home view and the manager view in `packages/react-app/src/views/Home.jsx` and `packages/react-app/src/views/Manager.jsx`respectively.

# Contract Deployment

🔏 Edit the smart contracts in `packages/hardhat/contracts`

💼 Add/Edit your deployment scripts in `packages/hardhat/deploy`

## 🚨 Local deployment (Goerli fork):

If you want to deploy the contracts locally using the Goerli fork you can do so with hardhat.

You will need to setup your RPC endpoint.

Update:
- `frontend/packages/hardhat/package.json` file and edit this line `"fork": "hardhat node --network hardhat --fork https://goerli.infura.io/v3/<YOUR_KEY>"` and input `<YOUR_KEY>`
- create env file by copying the example `cp packages\hardhat\example.env packages\hardhat\.env` and editing it, you need to put in your **deployer private key** for Goerli make sure you have goerliETH on it.
-   update fields  `GOERLI_INFURA_KEY=` and `GOERLI_DEPLOYER_PRIV_KEY=`

You can obtain one from [infura here](https://app.infura.io/).

Now run:

```bash
yarn fork
```

After setting up your `defaultNetwork` to `"localhost"` in `hardhat-config.js` you can run

🔏 Edit the smart contracts

grab `Account #0:` from the terminal running hardhat:

```bash
Started HTTP and WebSocket JSON-RPC server at http://127.0.0.1:8545/

Accounts
========

WARNING: These accounts, and their private keys, are publicly known.
Any funds sent to them on Mainnet or any other live network WILL BE LOST.

Account #0: 0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266 (10000 ETH)
Private Key: 0xac0974bec39a17e36ba4a6b4d238ff944bacb478cbed5efcae784d7bf4f2ff80

```
go to file `frontend\packages\hardhat\deploy\0_deploy_staking_pool.js` adn change these 2 constants to your deployer address:

```js
  const keyGenerator = "0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266";
  const withdrawal = "0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266";
```

now deploy:

```bash
yarn deploy --network localhost
```

Once done you can fund the pool :

```bash
yarn fund-pool
```

🎇 After this, your new staking pool and ssvETH contracts should reflect on automatically in `packages/react-app/src/contracts/localhost/`, `packages/react-app/src/contracts/external_contracts` and in `packages/react-app/src/contracts/hardhat_contracts`.

## 🚨 Goerli live deployment:

If you want to deploy on the live Goerli testnet, you'll only need :

1. Set up your `defaultNetwork` to `"goerli"` in `packages/hardhat/hardhat-config.js`
2. Create an `.env` file under `packages/hardhat` and set `"GOERLI_INFURA_KEY"` with your own Infura key and `"GOERLI_DEPLOYER_PRIV_KEY"` with your deployer wallet private key (for safety measures, make sure you have have no real funds on it). 

Then :

```bash
yarn deploy --network goerli
```

🎇 after this your new staking pool and ssvETH contracts should reflect on automatically in `packages/react-app/src/contracts/goerli/`

✅ you can also verify your staking pool contract on Goerli by using this :

```bash
yarn verify --constructor-args arguments.js --network goerli <NEW_DEPLOYED_CONTRACT_ADDRESS>
```

✅ and your ssvETH contract by using this :

```bash
yarn verify --network goerli <NEW_DEPLOYED_CONTRACT_ADDRESS>
```

❗❗ Important reminder : ❗❗

💥 Once you have your contracts deployed don't forget to set up the default network in `App.jsx` to match the one in `hardhat-config.js` !

# Show off to the world

🚨📡 To deploy to a public domain, use:

`yarn build`

followed by

`yarn surge` (can be problematic on windows, if running it, use WSL to run this command)

You will need to have a surge account and have the surge CLI installed. 
There is also the option to deploy to IPFS using `yarn ipfs` and `yarn s3` to deploy to an AWS bucket 🪣 There are scripts in the `packages/react-app/src/scripts` folder to help with this.`

---

# Backend

Now it's time to activate some validators beacon chain and use ssv network to run it!

### 🚀 [Click here, follow the readme and run Backend script](https://github.com/ssv-network/lsd-pool/blob/main/RUN_BACKEND.md)

All the backend functionality for this, namely

1. validator creation
2. validator activation with beacon chain
3. splitting your validator (DVT!) into multiple shares
4. registering validator share with ssv.network

are done for you out of the box!!!


💼 Add/Edit your deployment scripts in `packages/hardhat/scripts/deploy` for Goerli and in `packages/hardhat/deploy` for localhost (Goerli fork)

# Interested? Get involved

- build sth interesting on top, transferable NFT validators, Restaking app, or whatever else and **open PR**.

## Connect

Best way is via [ssv discord](https://discord.com/invite/ssvnetworkofficial) channel [#devs-support](https://discord.com/channels/723834989506068561/766640777815523330), ask there, tag the team directly and also @MarkoInEther and @Matty. They will help you to get to the right person.
