# distribute-system
428
# MP0: Event Logging Report

**Group name:** nullptr

**Group member:** Xu Xiong(xuxiong2), Hanqi Wang(hanqiw3)

**Cluster name:** g05

## Instructions for running code

### Logger Server

1. Upload `logger.py` to the server node.
2. Run `python3 logger.py` command.
3. Wait for connections.
4. We use multi-threading to write log information for each node, after disconnection, we dump log info to `<node_name>.txt` file for graph evaluation.

### Client Node

1. Upload `generator.py` and `client.py` to each client node.

2. Run following command.

   ```python
   python3 -u generator.py 0.5 | python3 client.py node0 172.22.156.14 5000
   # 0.5 represents 0.5Hz
   # node0 is the name of client node
   # 172.22.156.14 is the address of the centralized server
   # 5000 is the port of the centralized server
   ```

### Graphs Evaluation

After disconnecting all the client nodes, we should have the log info at path `./s1` or `./s2` depends on the scenario.

#### Delay

For each node, we dump every message as the following format

`nodeName`  `nodeTime` `nodeData`  `serverTime  ` `len(nodeData)`  

to the `<node_name>.txt`. Then we measure delay by using $ServerTime - nodeTime$ at each second.

#### Bandwidth

We measure the bandwidth by calculating the sum of the length of `nodeData` at each second from the `<node_name>.txt`.

#### Scenario 1 ( **3 nodes, 0.5 Hz each, running for 100 seconds**)

1. Run `python3 Evaluation1.py` command.
2. Output image `s1.jpg`  in the same location as `Evaluation1.py`.
3. ![s1](https://i.loli.net/2021/09/12/wNetRFgu2qjfZbU.jpg)

#### Scenario 2 ( 8 nodes, 5 Hz each, running for 100 seconds)

1. Run `python3 Evaluation2.py` command.
2. Output image `s2.jpg`  in the same location as `Evaluation2.py`.
3. ![s2](https://i.loli.net/2021/09/12/fTuBlMF7xUW6V5c.jpg)
