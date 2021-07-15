# Pastebin Ripoff

This project is a ripoff of the service pastebin provides. I wrote this code as an scalability exercise.
The code in this project is organized like this:

- Load balancer: picks a webserver from a list, and forwards the request to that webserver. Uses Round Robin to pick the next webserver.
- Webserver: a particular instance of a server, which will solve this request using Read/Write API, when corresponding.
- Read API: API in charge of obtaining existing pastes. Will communicate with both the SQL and NoSQL services.
- Write API: API in charge of creating new pastes. Will communicate with both the SQL and NoSQL services.
- NoSQL: The server where the NoSQL store (in this case, MongoDB) is running. The texts of the pastes are stored here.
- SQL: The server where the SQL (in this case, sqlite) is running.

The design can be expressed through this diagram:

![](https://raw.githubusercontent.com/mancusarasa/pastebin_rip_off/main/diagram.png "Main components of this app")

This design is a solution to the "Design Pastebin" exercise, taken from https://github.com/donnemartin/system-design-primer/tree/master/solutions/system_design.

# How to use the REST API
Once all the daemons are up and running, you should only communicate with them through the load balancer, like so:

```
curl -X POST http://localhost:3000/pastes/ --data '{"text": "this is a new paste"}' -H "Content-Type: application/json" # this creates a new paste
curl -X GET http://localhost:3000/pastes/3950ac7030 # this retrieves a particular paste. note that this id will probably be invalid in your runs, since ids are generated with random data (read from /dev/urandom)
curl -X GET http://localhost:3000/pastes # this retrieves all the pastes
```

# Dependencies
The machine/container/whatever where the NoSQL daemon is running should have MongoDB installed and running:

```
sudo apt-get install -y mongodb-org
sudo service mongod start
```

Also, all the machines/containers/whatever where any of the daemons are running should have
python3.6 and virtualenv installed.

```
sudo apt-get install -y python3-virtualenv python3.6
```

For each of these services (load_balancer, nosql, sql, webserver) you should:
- Create a virtualenv (`mkdir venv && virtualenv --python=python3.6 ./venv/`)
- Install the dependencies listed for the service (`./venv/bin/activate && pip install -r requirements.txt`)
- Start the service (`python api.py`)
