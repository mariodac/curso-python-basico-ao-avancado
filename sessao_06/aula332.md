## Dica: remover regras de tipos Unknown do linter do VS Code
Se você vem tendo problemas com tipagem `Unknown` no _linter_ do VS Code, talvez desativar essas regras possa facilitar sua vida.

Os tipos `Unknown`, geralmente, vêm de bibliotecas com tipagem parcial, e eles costumam dar um certo trabalho para solucionar (ou desativar).

A partir de agora, vou desativar todas as regras desse tipo do meu projeto. Isso me atrapalha a estudar para criar a aula, além de fazer perder tempo demais.

Para desativar essas regras, veja meu [settings.json](https://github.com/luizomf/cursopython2023/commit/97f87e371aa96719110a70233ba11840d6545f5c) (é o mesmo do nosso projeto).

Além disso, migrei o `python.analysis.typeCheckingMode` de "_strict_", para "_basic_" (pelo mesmo motivo).