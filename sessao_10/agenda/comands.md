Iniciar o projeto Django

```powershell
python -m venv venv
.\venv\bin\activate
pip install django
django-admin startproject project .
python manage.py runserver
python manage.py startapp contact
```

Migrando a base de dados do Django

```powershell
python manage.py makemigrations
python manage.py migrate
```

Criando e modificando a senha de um super usuário
```powershell
python manage.py createsuperuser
python manage.py changepassword USERNAME
```

Traduções com Django
```powershell
python manage.py compilemessages -l "pt_BR" -i 'venv_django' #-i para ignorar arquivos do ambiente virtual
python manage.py makemessages -l "pt_BR" -i 'venv_django' #-i para ignorar arquivos do ambiente virtual
```

Shell interativo do Django
```python
python manage.py shell
from contact.models import Contact
c = Contact(first_name="Simone") # cria um contato (lazy)
c.save() # salva na base de dados, cria um contato (não lazy)
c.last_name = 'Teixeira' # edita o campo last_name
c.phone='2225959201' # edita o campo phone
c.save() # salva as alterações na base de dados
c.delete() # apaga o registro da base de dados
c.save() # cria novamente o contato mas com um novo id
c = Contact.objects.get(id=1) # retorna um contato da base de dados pelo id
c.pk # retorna o id (primary key) do contato
c = Contact.objects.all() # retorna todos os contatos da base de dados
c = Contact.objects.filter(id=10) # retorna os contato filtrado pelo parâmetro informado
c = Contact.objects.all().order_by('-id') # retorna todos os contatos da base de dados em ordem decrescente
from django.contrib.auth.models import User
user = User.objects.create_user(username='usuario', password='123456') # cria um usuário com username e password (não lazy)
user.is_staff = True # habilita usuário como membro staff
user.save() # salva alterações
user.delete() # apaga o usuário
```

Configurar o git -> [Tutorial em vídeo](https://www.youtube.com/watch?v=SnTBOhYFr28&feature=youtu.be)

```powershell
git config --global user.name 'Seu nome'
git config --global user.email 'seu_email@gmail.com'
git config --global init.defaultBranch main
# Configure o .gitignore
git init
git add .
git commit -m 'Mensagem'
git remote add origin URL_DO_GIT
```

Enviar\Receber atualizações no repositório GitHub

```powershell
# enviar
git push -u origin main 
# receber
git pull -u origin main 
```
Utilize -u para gravar origin main, os posteriores comandos será apenas git push