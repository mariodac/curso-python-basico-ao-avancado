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