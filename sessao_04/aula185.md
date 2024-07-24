# Criando e usando um requirements.txt

Criar arquivo com os pacotes instalados para poder ser reinstalado em outra máquina

```bash
pip freeze > requirements.txt
```

Instalar pacotes que estão salvos no arquivo requirements

```bash
pip install -r requirements.txt
```