 # API
### **client_connected_to_server**
Check all the clients that have access to a specific server

| Field  | Type   | Description |
| -----  | ----   | ----------- |
| server | string | Name of the server |
<br />
### **server_connected_to_client**
Check all servers to which a client has access

| Field  | Type   | Description |
| -----  | ----   | ----------- |
| client | string | Name of the client |
<br />
### **verify_inclusion**
Verify if at a specific instant of time a client has access to a server

| Field           | Type   | Description |
| -----           | ----   | ----------- |
| client          | string | Name of the client |
| resource_server | string | Name of the server |
| time            | string | Time to check the inclusion proof |
<br />
### **insert_jwt**
Decode a JSON Web Token, insert the information extracted in a leaf of a Merkle Tree and then return the inclusion proof

| Field                   | Type                     | Description        |
| -----                   | ----                     | -----------        |
| token                   | string                   | JSON Web Token     |
| authorization_server_pk | EllipticCurvePublicKey   | Public key of the authorization server |
