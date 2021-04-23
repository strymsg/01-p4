## POC python redis

### Redis installation with docker

[redis image](https://hub.docker.com/_/redis)

```
docker run -p 6379:6379 --name redis-ts -d redis redis-server --appendonly yes
```
To connect use redis-cli of the last created container.
```
docker exec -it redis-ts redis-cli
```

### Connect using python

Once running, to use with python first install dependecies:

``` 
virtualenv --python=python3 venv
. venv/bin/activate

pip install redis

## now run the test program
python main.py
```

