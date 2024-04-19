# Sistema bancário com Python

Sistema bancário simples realizado como desafio de projeto no bootcamp Python AI backend da DIO patrocinado pela VIVO.

## Funções propostas

### Depósito

Para depositar, a única condição é que seu depósito seja de um valor positivo maior que zero (depósito > 0). Cada depósito será registrado no histórico do extrato.

### Saque

Para sacar, existem mais condições, onde um saque também tem que ser positivo maior que zero (saque > 0), mas tem um limite de até 500 reais (saque <= 500). Além disso, o saque não pode exceder o valor do saldo atual da conta (saque <= saldo), e há um limite de até três saques diários (limite_saque = 3). Cada saque será registrado no histórico do extrato.

### Extrato

Somente mostra o extrato da conta após as operações de depósito e saque realizadas, no formato "OPERAÇÃO: R$ 0.00", e ao final mostrando o saldo no mesmo formato sendo OPERAÇÃO = saldo.
