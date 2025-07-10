module.exports = {
  networks: {
    development: {
      host: "127.0.0.1",
      port: 7545, // puerto de Ganache
      network_id: "*" // para cualquier red
    }
  },
  compilers: {
    solc: {
      version: "0.8.0"
  }
  }
};
