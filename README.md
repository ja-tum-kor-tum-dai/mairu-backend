# mairu-backend

## run container

using Makefile

```
make up
```

using docker compose

```
docker network create -d bridge mairu | true
docker compose up -d
```

## stop container

using Makefile

```
make down
```

using docker compose

```
docker compose down --remove-orphans
docker network rm mairu | true
```
