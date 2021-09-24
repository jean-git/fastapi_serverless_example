# Dillinger
## _Example of an API using Fastapi running in docker or integrated with [Serverless framework](https://www.serverless.com/)_


## Running in Docker(Linux or WSL2)

First of all, you need installed [Docker](https://docs.docker.com/engine/install/) to run.

Clone this repo and run docker script to run server.

```sh
git clone https://github.com/jean-git/fastapi_serverless_example.git
cd fastapi_serverless_example
sh docker_build_and_run.sh
```
Verify the api default route by navigating to your server address in
your preferred browser.
```sh
127.0.0.1:8000
```

To check the API Docs, navigating to your server address in
your preferred browser.
```sh
127.0.0.1:8000/docs
```
## Running with Serverless in AWS

First of all, requires [Node.js](https://nodejs.org/) v12+ and AWS Access Key ID and AWS Secret Access Key to run.

Clone this repo, install the dependencies and deploy to AWS.

```sh
git clone https://github.com/jean-git/fastapi_serverless_example.git
cd fastapi_serverless_example
npm i
serverless deploy -v --stage dev
```
Verify the Serveless output to get API Address
