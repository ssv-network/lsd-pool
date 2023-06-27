const hre = require("hardhat");

const localChainId = "31337";

module.exports = async ({ getNamedAccounts, deployments, getChainId }) => {
  const { deploy } = deployments;
  const { deployer } = await getNamedAccounts();
  const keyGenerator = "0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266";
  const withdrawal = "0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266";
  const operatorIds = [4, 9, 17, 76];

  const depositAddress = "0xff50ed3d0ec03ac01d4c79aad74928bff48a7b2b";
  const ssvNetworkContract = "0xAfdb141Dd99b5a101065f40e3D7636262dce65b3";
  const ssvTokenAddress = "0x3a9f01091C446bdE031E39ea8354647AFef091E7";

  const stakingpool = await deploy("StakingPool", {
    from: deployer,
    args: [
      keyGenerator,
      depositAddress,
      withdrawal,
      ssvNetworkContract,
      ssvTokenAddress,
      operatorIds,
    ],
    log: true,
  });

  console.log(`StakingPool deployed to ${stakingpool.address}`);
};
module.exports.tags = ["StakingPool"];
