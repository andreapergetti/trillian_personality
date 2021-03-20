# trillian
To build and test Trillian you need:
- Go 1.14 or later
- MySQL or MariaDB to provide the data storage layer

Si scarica il codice, si fa la build e si esegue un test:
```
export GO111MODULE=auto
git clone https://github.com/google/trillian.git
cd trillian
go build ./...
go run ./...
```
Per eseguire un test di integrazione bisogna avere un istanza di MySQL in esecuzione e configurata come indicato successivamente.
Si crea un istanza di MySQL in ascolto sul localhost(127.0.0.1) sulla porta 3306.
```
    docker run \
    --name=database \
    --env=MYSQL_ALLOW_EMPTY_PASSWORD=yes \
    --mount=source=trillian-data,target=/var/lib/mysql \
    --publish=3306:3306 mariadb:10.4
```

In seguito si crea un database con nome *test* con le tabelle appropriate:
```
./scripts/resetdb.sh
```
Se c'è un errore nel collegamento al database cambiare tra le variabili di ambiente nel file *./scripts/resetdb.sh* il nome dell'host(riga 33) da *localhost* a *127.0.0.1*

Per controllare il corretto funzionamento end-to-end si può eseguire un test di integrazione:
```
./integration/integration_test.sh
```
Questo script esegue un test multi-processo. Vengono creati un Trillian server in modalità di Log insieme a un Trillian signer, viene fatto il log di molte foglie nel merkle tree e viene controllato che esse siano integrate correttamente.


Per un semplice sviluppo, eseguirlo in un container e eseguire un database locale. Per usare Docker per eseguirlo e interagire con Trillian usare i seguenti comandi:
```
docker-compose -f examples/deployment/docker-compose.yml up
```

## Uso delle API
Possibilmente creare un ambiente virtuale:
```
python3.8 -m venv .venv
source .venv/bin/activate
```
Installare le seguenti librerie con Python:
```
pip install grpcio
pip install grpcio-tools
pip install google-api-python-client
pip install pure-protobuf
```

Usare il compilatore del protocol buffer che a partire dalle definizioni del protocollo(file .proto) riesce a generare automaticamente delle definizioni in codice Python.
```
python3.8 -m grpc_tools.protoc \
--proto_path=. --python_out=. \
--grpc_python_out=. \
trillian_admin_api.proto \
trillian_log_api.proto	trillian.proto 

cd crypto/keyspb
python3.8 -m grpc_tools.protoc \
--proto_path=. --python_out=. \
--grpc_python_out=. keyspb.proto

cd crypto/sigpb
python3.8 -m grpc_tools.protoc \
--proto_path=. --python_out=. \
--grpc_python_out=. sigpb.proto
```
In seguito, si può usare il codice presente nel jupyter-notebook(installarlo con pip install notebook), presente in questa repository, per usare le API.