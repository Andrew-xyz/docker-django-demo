# Docker Django Demo

Demo repository for a Django Docker implementation. Full Docker documentation is available [here](https://docs.docker.com/).

## Common Docker Commands

Docker commands are used to manipulate images and containers on a one-to-one basis. These are often used for building images and micro-managing networks at the container level.

```yaml
$ docker ps                                            # Prints to console all running services
$ docker images                                        # Prints to console all local images
$ docker build -t andrewxyz/docker-django-image ./demo # Builds an image with the designated tag from the given context (./demo)
$ docker run -it andrewxyz/docker-django-image         # Spins up a container with the selected image
$ docker run -it \                                     # Same command, but with flags for:
    -dp 8080:8000                                      #    Detatched mode, Port mapping
    --name docker-django-container \                   #    Container naming
    andrewxyz/docker-django-image
$ docker inspect andrewxyz/docker-django-container     # Shows runtime details for the selected container
$ docker exec -it docker-django-container /bin/bash    # Shells into the selected container
$ docker kill docker-django-container                  # Stops the running container
$ docker rmi andrewxyz/docker-django-image             # Removes the selected image from the host filesystem

$ docker system prune -a                               # Cleans up the host of any unused images
$ docker volume prune                                  # Cleans up the host of any unused volumes
$ docker volume ls                                     # Lists volumes
$ docker volume rm postgres                            # Removes the selected volume from the host filesystem
```

## Common Docker Compose Commands

Docker compose commands serve as an instruction set for how images and containers are run, applying tags and settings in a consistent way. This also provides a means for networking between containers.

```yaml
$ docker compose up                                    # Starts the docker compose network, building or pulling images as needed
$ docker compose up --build                            # Optional build switch to force image rebuilds from cache
$ docker compose up -d                                 # Runs the docker compose network in detatched mode
$ docker compose -f docker-compose.yml up              # Designates a docker compose file to run
$ docker compose exec app /bin/bash                    # Shells into the selected container
$ docker compose down                                  # Brings the docker compose network down
```

## Common Docker Hub Commands

Simple commands for interfacing with the DockerHub registry, available [here](https://hub.docker.com/).

```yaml
$ docker login                                         # Logs the user in to a DockerHub account
$ docker pull postgres:latest                          # Pulls the selected image
$ docker push andrewxyz/docker-django-image            # Pushes the selected image to DockerHub
```
