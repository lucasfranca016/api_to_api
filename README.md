# Running a Redis Server on Windows

### IMPORTANT!

Redis won't work in some Windows versions. Instead, you should set up a Redis Server on WSL or use Docker to make it work.

### Redis Server on WSL, step by step

Updating packages...

```sudo apt update && sudo apt upgrade -y```

Installing Redis...

```sudo apt install redis-server -y```

Running Redis Server

```redis-server```

To test it, open a new WSL terminal and type:

```redis-cli ping```

If it's working, it will respond **PONG**

Now, you have to type ```fastapi dev``` on your VScode terminal and it will work