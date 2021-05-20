# trillian
----
- [Personality](#personality)
----


<a name="personality"></a>
## Personality
The personality want to simulate an Authorization server, which can authorize a client to access a server by generating a JSON Web Token with specific information, and a Trillian server, that can decode the JWT and log the information extracted in a Merkle Tree.   
The class and the methods of this personality are in the [authorization_log.py](./authorization_log.py) module. You can watch an example of use of this module in the [personality.ipynb](./personality.ipynb) notebook.
You can find the documentation of the personality's API in the [api.md](./api.md).

<br/>

To build and test you need:
- Python 3.8 or later
- MySQL or MariaDB to provide the data storage layer

<br/>

Install dependencies written in the [Pipfile.lock](./Pipfile.lock) file using pipenv:
```
pipenv install --ignore-pipfile
```

<br/>

For simple deployments, running in a container is an easy way to get up and running with a local database. To use Docker to run and interact with the personality, use:
```
docker-compose -f docker-compose.yml up
```
