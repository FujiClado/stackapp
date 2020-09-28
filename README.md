## Environment Variables

- CACHING_SERVER
  
  - Redis host details / ip or service name.


- IPSTACK_KEY
  - ipstack api token.


 

## Example

#### Creating bridge network.
```

docker network create --driver bridge appnet
```


#### Creating redis container.

```
docker run \
-d \
--name redis \
--network appnet \
--restart always \
redis:latest
```

#### Creating ipstackapp container.

```
docker run \
-d \
--name ipstackapp \
--network appnet \
--restart always \
-p 80:8080 \
-e CACHING_SERVER="redis" \
-e IPSTACK_KEY="c8fe...f93e......bcfb4f9d0b89" \
fujikomalan/ipstack:latest 

```
