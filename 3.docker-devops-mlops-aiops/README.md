# Commands used in the Hands On
```
docker --version
docker pull nginx
docker images
docker run -d -p 8080:80 nginx
docker ps
docker stop <container_id>


docker build -t custom-nginx .
docker container run -d --name custom-nginx -p 8080:80 custom-nginx
docker ps
docker tag custom-nginx yourusername/custom-nginx
docker push yourusername/custom-nginx
```