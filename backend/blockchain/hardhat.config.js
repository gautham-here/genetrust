require("@nomicfoundation/hardhat-toolbox");
require("dotenv").config({ path: "../backend/.env" });  // reuse backend .env

/** @type import('hardhat/config').HardhatUserConfig */
module.exports = {
  solidity: {
    version: "0.8.20",
    settings: {
      optimizer: { enabled: true, runs: 200 },
    },
  },

  networks: {
    // ── Local dev node (hardhat node) ──────────────────────────────────────
    localhost: {
      url: "http://127.0.0.1:8545",
    },

    // ── Polygon Amoy public testnet (free, no cost) ────────────────────────
    // Free RPC via Alchemy or Infura (both have free tiers):
    //   https://www.alchemy.com  →  create app → choose Polygon Amoy
    //   https://www.infura.io    →  create project → Polygon PoS / Amoy
    // Fund your wallet with free MATIC from:
    //   https://faucet.polygon.technology  (choose Amoy)
    amoy: {
      url: process.env.POLYGON_AMOY_RPC_URL || "https://rpc-amoy.polygon.technology",
      accounts: process.env.DEPLOYER_PRIVATE_KEY
        ? [process.env.DEPLOYER_PRIVATE_KEY]
        : [],
      chainId: 80002,
    },
  },

  // Optional: verify contracts on Polygonscan (free API key)
  etherscan: {
    apiKey: {
      polygonAmoy: process.env.POLYGONSCAN_API_KEY || "",
    },
    customChains: [
      {
        network: "polygonAmoy",
        chainId: 80002,
        urls: {
          apiURL:     "https://api-amoy.polygonscan.com/api",
          browserURL: "https://amoy.polygonscan.com",
        },
      },
    ],
  },
};