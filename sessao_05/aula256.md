
## Exercício com Abstração, Herança, Encapsulamento e Polimorfismo
[RESOLUÇÃO](aula256.py)
Criar um sistema bancário (extremamente simples) que tem clientes, contas e
um banco. A ideia é que o cliente tenha uma conta (poupança ou corrente)
e que possa sacar/depositar nessa conta. Contas correntetem um limite extra.

**Conta (ABC)**

- ContaCorrente
- ContaPoupanca

**Pessoa (ABC)**

- Cliente
    - Cliente -> Conta


**Banco**
- Banco -> Cliente
- Banco -> Conta

### Dicas:
Criar classe Cliente que herda da classe Pessoa (Herança)

Criar classe Conta que herda da classe Banco (Herança)
- Pessoa tem nome e idade (com getters)
- Cliente **TEM** conta (Agregação da classe ContaCorrente ou ContaPoupanca)

Criar classes ContaPoupanca e ContaCorrente que herdam de Conta

Criar classe Banco para AGREGAR classes de clientes e de contas (Agregação)

Banco será responsável autenticar o cliente e as contas da seguinte maneira:

Banco tem contas e clientes (Agregação)
* Checar se agência é daquele banco
* Checar se o cliente é daquele banco
* Checar se a conta é daquele banco

Só será possível sacar se passar na autenticação do banco (descrita acima)
Banco autentica por um método
"