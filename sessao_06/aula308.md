# Básico do protocolo HTTP (HyperText Transfer Protocol)
O módulo requests para requisições HTTP no Python
HTTP (HyperText Transfer Protocol) é um protocolo usado para enviar e receber
dados na Internet. Ele funciona no modo cliente/servidor, onde o cliente
(seu navegador, por exemplo) faz uma requisição ao servidor
(site, por exemplo), que responde com os dados adequados.

A mensagem de requisição do cliente deve incluir dados como:
- O método HTTP
  - leitura (safe) - GET, HEAD (cabeçalhos), OPTIONS (métodos suportados)
  - escrita - POST, PUT (substitui), PATCH (atualizar), DELETE
- O endereço do recurso a ser acessado (/users/)
- Os cabeçalhos HTTP (Content-Type, Authorization)
- O Corpo da mensagem (caso necessário, de acord com o método HTTP)

A mensagem de resposta do servidor deve incluir dados como:
- código de status HTTP (200 sucess, 404 Not found, 301 Moved Permanetly)
- Os cabeçalhos HTTP (Content-Type, Accept)
- O corpo da mensagem (Pode estar em vazio em alguns casos)

[Documentação códigos de status](https://developer.mozilla.org/pt-BR/docs/Web/HTTP/Status)