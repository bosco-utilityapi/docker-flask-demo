# Docker Flask Demo

Demonstrating simple Flask app for Docker. The app returns the server's environment variables via HTML and JSON.


## Handling Images and Containers


### Create an Image

Create a Docker image and name it `env_vars`:

    $ docker build -t env_vars .


### List Images

List your Docker images; you should see `env_vars`:

    $ docker image ls
    REPOSITORY      TAG             IMAGE ID        CREATED         SIZE
    env_vars        latest          d00da963e813    2 hours ago     157MB

### Run an Image

Run the image in a container

    $ docker run -d -p 8000:8000 --name env_vars_app env_vars
    da9aabbbb93b5d4831b2215ca3dda6f36846a48bece040a893731a0321a95653

* `-d` detaches the container to background
* `-p` forwards image's port 8000 to host
* `--name` names the container `env_vars_app`


### Access the services of a Running Container

Now that the container is running, access the HTML output with your browser:

* [http://127.0.0.1:8000](http://127.0.0.1:8000)

Whereas the /api endpoint gives your JSON:

* [http://127.0.0.1:8000/api ](http://127.0.0.1:8000/api)


### List Containers

To see your running Docker containers:

    $ docker container ls
    CONTAINER ID    IMAGE       COMMAND             CREATED         STATUS          PORTS                   NAMES
    da9aabbbb93b    env_vars    "python app.py"     4 minutes ago   Up 5 minutes    0.0.0.0:8000->8000/tcp  env_vars_app

To see *ALL* your Docker containers, including those that are not running, add the `--all` options:

    $ docker container ls --all


### Access Bash Shell in a Container

Since this Docker image was created with a bash shell, you can login to it with:

    $ docker exec -u root -it env_vars_app bash
    root@host:/#

Use the exit command (or ^d) to return to your host:

    root@host:/# exit
    exit


### Stop a Container

To stop a running container:

    $ docker container stop env_vars_app
    env_vars_app

### Restart a Container

Once a container has stopped, you can restart it:

    $ docker container restart env_vars_app
    env_vars_app

### Remove a Container Permanently

Once a container has stopped, you can also remove it permanently. Note that you are removing the container and not the image; your image will still be available to start a new container.

    $ docker container rm env_vars_app
    env_vars_app

### Remove an Image Permanently

When you've stopped a container and no longer needs its corresponding image, you can remove the image altogether:

    $ docker image rm env_vars
    Untagged: env_vars:latest
    Deleted: sha256:d00da963e813dcc1b3e3baa63636077058cdef5139d403e245c48d08882290cd
    Deleted: sha256:a64b17e41d5b0e924e92e7c31070fe79b95acaaaa50f7a0cfc54d5cec88e1707
    Deleted: sha256:05825e4693dfc0c7f4a34bb35954fcc3a74b49c87d3f1ba8255780648a200a51
    Deleted: sha256:8dff0fd8a9f6eea63f51cb0d5b3130c22355963b65d867088ee9775d63a75cc8
    Deleted: sha256:a85431eb14f16fe384a3853cdf7b844b2016d2c2e60b4b483ebc1de53eb8c5e8
    Deleted: sha256:dcf6b155de7e129c6bc132dea3d30692c0dafc6d1b5896248c2d5c1b4a080002
    Deleted: sha256:e09959cf57e6a2d45882ca3db08e2916a22015dd62e9baad18a45566f9c0a6e7
    Deleted: sha256:18942a2d87a52be2d6c6540bb50efc17fd8f60d4acf577ed5b63ee5e476b2817
    Deleted: sha256:1843c822ffd439344d05f7eebc31281e3474dec8d07ede0446127bc57ad42bf2
    Deleted: sha256:65510889879def8da5337083b759438c85632dbd1040496722dcf1d9b030b774
