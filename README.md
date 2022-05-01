# Lab 3. Cryptography
Here we implemented RSA alghoritm together with message integrity in order to make safe messaging for a chat application.

## RSA
This algorithm is known as an open-key cypher, where the sender generates a pair of public keys and encodes a message with them, thus sending encoded message and a key to the receiver. The receiver in turn, decodes a message with the pair of private keys.

### Implementation
You can check our implementation of the algorithm [here](../main/rsa.py)


## Usage
- First create a server:
```bash
$ python3 server.py
```

- Then in other terminals create as many client as you want:
```bash
$ python3 client.py
```
#### Here you go, now you are able to send and receive messages. 

## Example
