// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Votacion {
    struct Voto {
        address votante;
        uint candidato;
    }

    Voto[] public votos;
    mapping(address => bool) public haVotado;

    function votar(uint _candidato) public {
        require(!haVotado[msg.sender], "Ya votaste.");
        votos.push(Voto(msg.sender, _candidato));
        haVotado[msg.sender] = true;
    }

    function totalVotos() public view returns (uint) {
        return votos.length;
    }
}
