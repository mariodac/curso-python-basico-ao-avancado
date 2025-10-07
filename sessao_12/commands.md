# Construir container Docker
`docker-compose up --build`

# Construir container Docker e forçar recriação
`docker-compose up --build --force-recreate`

# Construir container Docker e forçar recriação sem criar vários containers
`docker-compose up --build --force-recreate --remove-orphans --renew-anon-volumes`

# Subir container Docker em segundo plano
`docker-compose up -d`

# Rodar comandos no container Docker
`docker-compose run --rm djangoapp python -V`

# Rodar comandos no container Docker com shell
`docker-compose run --rm djangoapp /bin/sh -c "echo $SECRET_KEY"`

# Rodar comandos no container Docker com shell iterativo
`docker exec -it djangoapp /bin/sh`

# Rodar comandos no container Docker com shellscript
`docker-compose run --rm djangoapp migrate.sh`

# Sempre que alterar volumes, Dockerfile ou variáveis, faça:
```bash
docker-compose down -v
docker-compose build --no-cache
docker-compose up -d
```