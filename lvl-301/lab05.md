# Deploying a Simple Blog to Heroku

> Node.js
>
> > is an open source, cross-platform runtime environment, which allows you to build server-side and networking applications.and it is written in JavaScript

# **Heroku** : is a cloud application platform it turn local server into a world wide server.

### To creat our first web page we will declare some veriables

`var http = require("http");`
`var fs = require("fs");`
`var path = require("path");`
`var mime = require("mime");`

- The first one will give you the key to Node's HTTP functionality.
- The second one is for possibility to interact with the file system.
- The third one allows you to handle file paths.
  -The last one allows you to determine a file's MIME-type.

### Then Create `package.json` to contain project information

### The third step create **send404()** function to handle 404 error (which usually appears when requested file doesn't exist).

`function send404(response) { response.writeHead(404, {"Content-type" : "text/plain"}); response.write("Error 404: resource not found"); response.end(); }`

### To deploy our project:

- from the folder that hold our project create a new repo with this command `git init`
- the `git add .`
- Now, We should commit our file to repo `git commit -m "YOUR_COMMENT"`
- Then We should create our Heroky application `heroku create`. Heroku will generate a random name for your application and we can change it.
- every heroku app starts with no **branches and no code** o, the first time we deploy our project, we need to specify a remote branch to push to: `git push heroku Branch_Name`
