# trillian
To build and test Trillian you need:
- Go 1.14 or later
- MySQL or MariaDB to provide the data storage layer

To fetch the code, dependencies, and build Trillian, run the following:
```
export GO111MODULE=auto
git clone https://github.com/google/trillian.git
cd trillian
go build ./...
```

For simple deployments, running in a container is an easy way to get up and running with a local database. To use Docker to run and interact with Trillian, use:
```
docker-compose -f examples/deployment/docker-compose.yml up
```

## Uso delle API
Possibly create a virtual environment:
```
python3.8 -m venv .venv
source .venv/bin/activate
```
Install the following Python library:
```
pip install grpcio
pip install grpcio-tools
pip install google-api-python-client
pip install pure-protobuf
```
Use protocol buffer compiler to produce Python output from the definitions of the protocol(file .proto). For every *namefile*.proto file in input, it generates *namefile*_pb2.py which contains our generated request and response classes and *namefile*_pb2_grpc.py which contains our generated client and server classes.
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
Afterwards, you can download the jupyter-notebook file in this repository, to see examples of use of the API.

## Experimental Beam Map Generation
Clone the Apache Beam repository:
```
git clone \
ssh://git@github.com/apache/beam.git
cd beam
```
Create a Python virtual environment:
```
python3.8 -m venv .venv
source .venv/bin/activate
```
Install setup.py requirement:
```
cd sdks/python
pip install -r build-requirements.txt
```
Install Apache Beam package in editable mode:
```
pip install -e .[gcp,test]
```
Install some libraries:
```
apt-get install liblzma-dev lzma
```
Install other libraries with pip:
```
pip3.8 install dill
pip3.8 install google-api-python-client
pip3.8 install future
pip3.8 install fastavro
pip3.8 install pylzma
pip3.8 install backports.lzma
pip3.8 install python-dateutil
pip3.8 install numpy
pip3.8 install confluent_kafka[avro]
pip3.8 install grpcio
pip3.8 install grpcio-tools
pip3.8 install typing_extensions
pip3.8 install oauth2client
pip3.8 install crcmod
```
Modify lzma.py file at line 27:
```
vim /usr/local/lib/python3.8/lzma.py
```
Write this code at line 27:
```
try:
    from _lzma import *
    from _lzma import \
    _encode_filter_properties, \
    _decode_filter_properties
except ImportError:
    from backports.lzma import *
    from backports.lzma import \
    _encode_filter_properties, \
    _decode_filter_properties
```
```
python -m apache_beam.runners.portability. \
local_job_service_main --port=8099
```
Go to the trillian/experimental/batchmap directory and run this command:
```
go run ./cmd/build/mapdemo.go \
--output=/tmp/mapv1 --runner=universal \
--endpoint=localhost:8099 \
--environment_type=LOOPBACK
```
Verifying that a particular key/value is set correctly within the tiles can be done with the command:
```
go run cmd/verify/verify.go --logtostderr \
--map_dir=/tmp/mapv1 --key=5
```
