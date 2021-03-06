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

- Then in other terminals create as many clients as you want:
```bash
$ python3 client.py
```
#### Here you go, now you are able to send and receive messages. 

## Example


https://user-images.githubusercontent.com/59284695/166151814-93210655-1e23-46b0-b27f-5753d07dca85.mov


## Features
In order to respond to a 100% safety of our messaging, we implemented some features that allows us not to experience troubles with message-leak in case when the server crashes. Under the hood, we implemented another RSA encoding on the server side that encodes keys passed by the client. Thus messages are never being passed decoded inside a server. Every user has his own keys, so that every person is able to receive the same message but encoded differently. This guarantees complete security of messagging, and even if its full power can't be totaly seen in this simple example, this method has a huge power when it takes a serious projects.
