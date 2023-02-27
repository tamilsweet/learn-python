# Learning Python

Build Image
```
docker build -t rest-apis-flask-python .
```

Run docker
Linux
```
docker run -dp 5000:5000 -w /app -v "${pwd}:/app" rest-apis-flask-python
```
Windows
```
MSYS_NO_PATHCONV=1 docker run -dp 5000:5000 -w /app -v "//c/Learn/Python/learn-python:/app" rest-apis-flask-python
```