# mairu-backend
## run container

using Makefile

```
make up
```

using docker compose

```
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
```

## seed data

```
docker exec -it mairu-backend_api_1 /bin/sh
cd seed-data
python3 seed.py
```
