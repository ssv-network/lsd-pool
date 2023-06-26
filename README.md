# LSD staking pool powered by SSV

This repo showcases how to **create and run LSD staking pool** leveraging ssv.network.

If you are looking for other resources to help you start building, check out [awesome-ssv](https://github.com/bloxapp/awesome-ssv) repo, a curated list of SSV tools & projects & guides.

This lsd-pool is separated from the awesome-ssv of which it was a part of in the past.

### Description

Launch a minimalistic fully working LSD staking pool.

It is **for learning purposes ONLY** and NOT to be used in production!

It consists of Frontend based on scaffold-eth, backend creating + managing validators and smart contracts to manage ETH, mint an LSD token (ssvETH).

It leverages ssv.network to **run validators in a distributed and decentralized manner**.

## Video walkthrough

### With Frontend 

[![Video walkthrough & launchig 🌈LSD pool](http://img.youtube.com/vi/CK-4xPgiU-w/0.jpg)](http://www.youtube.com/watch?v=CK-4xPgiU-w "Repo walkthrough & launchig 🌈LSD pool")

### Without Frontend 

[![Video walkthrough & launchig 🌈LSD pool](http://img.youtube.com/vi/CiV76rOY4go/0.jpg)](http://www.youtube.com/watch?v=CiV76rOY4go "Repo walkthrough & launchig 🌈LSD pool")


**NOTE:**

- **Readmes always take precedence** - Some parts of this video may be outdated.
- Video goes into **more detail and gives more background**. If you have some experience with this stuff you can safely skip it and follow READMEs only.

### Credits

Huge thanks to

- [@RohitAudit](https://github.com/RohitAudit) who develops & maintains all the **backend** magic on whose [repo-Garuda](https://github.com/RohitAudit/ssv-service) this minimalistic LSD staking pool is based on.

- [@nibthebear](https://github.com/TIM88-DOT) who has developed the **frontend**, js deployment, and revamped the **smart contracts**.

## How it works

- Staking has never been so easy, thanks to SSV, you can stake your ETH and earn ssvETH without running your own validator! 🤑

![image](https://github.com/ssv-network/lsd-pool/assets/37876756/c7840bd7-2f4c-478b-9c1c-0c4b29b157bf)

### User Actions

- Users stake their ETH to a staking contract for which he is minted a liquid staked derivative token, ssvETH.

- Creates an Ethereum validator key and gives it to the staking pool to deposit for activation

- Generates keyshares from the validator keystore and stakes them with the SSV nodes

- Saves the keystore and keyshares for verification at a later stage

## How to deploy?

### 1. Front End plus Smart contracts - Scaffold-eth framework

If you want to deploy smart contract together with frontend using scaffold-eth framework (hardhat + react) built in `JS` continue to [RUN_SMART_CONTRACTS_AND_FRONTEND.md](/RUN_SMART_CONTRACTS_AND_FRONTEND.md).

It will navigate you through the remaining process.

## OR

### 2. Smart Contracts Only - Brownie framework

If you want to deploy smart contracts only using brownie framework built in `PY` continue to [RUN_SMART_CONTRACTS_ONLY.md](/RUN_SMART_CONTRACTS_ONLY.md).

It will navigate you through the remaining process.

## What to build?

This repo is meant to give you a head start in building a cool prototype of the next big staking app. Build something interesting on top such as transferable NFT validators, Restaking app, or whatever else, and **open PR**.

### SSV projects & resources

Other relevant tools and resources can be found in **[awesome-ssv](https://github.com/bloxapp/awesome-ssv)** repo or linked below.

- [Tools](https://github.com/bloxapp/awesome-ssv#tools)
- [Notification services](https://github.com/bloxapp/awesome-ssv#notification-services)
- [Staking pools](https://github.com/bloxapp/awesome-ssv#staking-pools)
- [Staking services](https://github.com/bloxapp/awesome-ssv#staking-services)
- [Operator services](https://github.com/bloxapp/awesome-ssv#operator-services)
- [Tutorials](https://github.com/bloxapp/awesome-ssv#tutorials)
- [How to contribute](https://github.com/bloxapp/awesome-ssv#how-to-contribute)
- [How to add your project](https://github.com/bloxapp/awesome-ssv#how-to-add-your-project)

#### Get funding

You can hop into SSV discord channel [#devs-support](https://discord.com/channels/723834989506068561/766640777815523330) and get feedback on your ideas. You may also check [active grants](https://grants.ssv.network/) directly. If you are considering applying for one, write in SSV discord and tag @Matty and @MarkoInEther. They will be happy to help you draft a rock star grant application.

#### Connect with teams

The best way is via discord channel [#devs-support](https://discord.com/channels/723834989506068561/766640777815523330), ask there, tag the team directly, and also @MarkoInEther and @Matty. They will help you to get to the right person.

#### Documentation

You can **read the full documentation** at [docs.ssv.network](https://docs.ssv.network/).

### How to contribute

#### Join the Buidlers

Start getting familiar with DVT staking, go to [SSV Discord](https://discord.gg/invite/ssvnetworkofficial) and check out `#dev-support` channel. If you cannot see it claim a role.

#### Fix errors

If you see any typos in the tutorials, have a suggestion for better phrasing or see a bug in the code **open a PR!**.

#### Suggest improvements

Do you think some things could be done better in the repo? Do you have ideas how to expand it?
**Open an issue** and share it in the `#dev-support channel`.
If your featere is usefull for the ecosystem SSV DAO may fund you developing it!

#### LICENSE

MIT License
