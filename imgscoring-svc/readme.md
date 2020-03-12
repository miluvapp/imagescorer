```
cd Kerja\Face Detection\Code\imgscoring-svc
```

1. `set FLASK_APP=main.py`
2. `set FLASK_ENV=development`
3. `flask run`

## Deploy

    set PATH=%PATH%;%APPDATA%\npm
    serverless deploy

## activate venv

    venv\scripts\activate

## npm 

    npm init 
    npm install serverless-<package must install>

## docker 

### build 

    docker build -t imgscoring-svc .

### run 

    docker run --name imgscoring-svc -p 80:80 imgscoring-svc

### logs 

    docker logs -f imgscoring-svc

### stop (turn off server)

    docker stop imgscoring-svc
### rm 

    docker rm imgscoring-svc

### ps

    docker ps

### 

    docker container 