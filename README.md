# Mairu Backend

Mairu (from Thai word "ไม่รู้")

This repository is the backend of the Mairu application, the application that can answer any questions with the answer is "ไม่รู้" (meaning as the same "don't know").
We created it for fun and in short times during the [Stupid Hackathon Thailand #5](https://stupidhackth.github.io/5/) event.

Mairu backend is built on [FastAPI](https://fastapi.tiangolo.com/) framework.


## Running on Local Environment

### Requirement

You need to install this in your local environment.
- [Python 3](https://www.python.org/downloads/)
- [MongoDB](https://www.mongodb.com/)

### Setup The Project

#### Installing the dependency libraries

Run this command
```
pip install -r requirements.txt
```

#### Setting your Database

Open `src/main.py` and `src/seed.py`, change the line
```py
client = MongoClient("replace this to your MongoDB url here")
```

### Running The Project

Run this command
```
uvicorn main:app --reload --host 0.0.0.0 --port 80
```
Now, you can ready to go.
The backend application will run on `localhost:80`.

## Running on Docker Container

### Requirement
You need [Docker](https://www.docker.com/) and [docker-compose](https://docs.docker.com/compose/) to run in container.



## Run container

Using Makefile
```
make up
```

Using docker-compose
```
docker compose up -d
```

## Stop Container

Using Makefile
```
make down
```

Using docker-compose
```
docker compose down --remove-orphans
```

## To Seed Initial Data

For a local environment, simply run to your local
```
python3 seed.py
```

For a container, you need to execute /bin/sh to open the container shell and run `seed.py`
```
docker exec -it mairu-backend_api_1 /bin/sh
cd seed-data
python3 seed.py
```

## For The Contributors

Thanks for having an interest in this project.
Please read our guidelines in [CONTRIBUTING.md](https://github.com/ja-tum-kor-tum-dai/mairu-backend/blob/main/CONTRIBUTING.md) before starting a contribution.
