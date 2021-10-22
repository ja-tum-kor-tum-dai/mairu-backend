# mairu-backend

## Run Container

using Makefile

```
make up
```

using docker compose

```
docker compose up -d
```

## Stop Container

using Makefile

```
make down
```

Using Docker Compose

```
docker compose down --remove-orphans
```

## Seed Data

```
docker exec -it mairu-backend_api_1 /bin/sh
cd seed-data
python3 seed.py
```

## For The Contributors

Thanks for having an interest in this project.
Please read our guidelines in [CONTRIBUTING.md](https://github.com/ja-tum-kor-tum-dai/mairu-backend/blob/main/CONTRIBUTING.md) before starting a contribution.
