# docker-cluster
Trial for creating docker cluster images and making containers run in parallel using docker compose

## How to use
1. To clone repository to your local - `git clone https://github.com/bhargavchintam/docker-cluster.git`
2. To navigate to repo folder - `cd docker-cluster`
3. To build docker cluster in parallel - `docker-compose build --parallel`
4. To run the cluster in parallel - `docker-compose up -d`
5. To view services/containers running - `docker ps` (To see parallel services/containers in running state)
6. To view each container logs - `docker logs [container id]` (You can view logs during the service/container durinf execution/run)
7. To terminate cluster `docker-compose down` or `Ctrl+C`

## Note:
Steps 1 to 4 will create an docker cluster to create images and run those images.</br>
Here, we need to edit the `docker-compose.yml` file to as create the multiple docker images.

This should run 3 python scripts.
