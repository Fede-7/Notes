## The Network Layer: The Control Plane

Lecture 21 

## Network Layer Routing: Link-State Algorithm

<sup>•</sup> The Link-State (LS) algorithm is a centralised approach that exploit full knowledge about the network in order to find the best path. 

<sup>•</sup> Such algorithms do not sufer from the count-to-infinity problem. 

• The LS algorithms are based on the Dijkstra algorithm. 

<sup>•</sup> Notice that such level of knowledge can be achieved in practice by having each node to broadcast link-state packets, containing IDs and costs of its atached links, to all other nodes in the network. 

<sup>•</sup> The basic version of the algorithm computes the shortest paths from a starting node to all possible destination nodes (so it must be executed on all nodes). 

## Network Layer Routing: Link-State Algorithm

<sup>•</sup> In LS before the computation of the shortest path, each router must discover the surrounding nodes and share such information with the others. This message exchange phase is basically done in 4 steps: 

1. Neighbors’ discovery: the router sends a specific “hello” message on all links, other routers reply it by sending their IDs. 

2. Costs setup: the router sets the distance or cost metric to each of its neighbors, which may depend on the actual costs (time, bandwidth, etc.) or set by the administrator. 

3. Packet construction: the router creates a packet that summarizes the IDs of the adjacent nodes and their costs. 

4. Packets exchange: the router sends this packet to all other routers in the network (broadcast) and receive similar packets from all of them. 

<sup>•</sup> After this process has been performed, each router possesses the “complete” knowledge about the topology of the network, now the shortest-path algorithm (Dijkstra) can be executed. 

## Network Layer Routing: Link-State Algorithm

## <sup>•</sup> The pseudocode:

```matlab
LinkState(x):
    N' = {x}
for all nodes v:
    if v is a neighbor of x then
    D(v) = c(x, v)
    else
    D(v) = ∞

repeat
    find w not in N' such that D(w) is minimum
    add w to N'
    for each neighbor v of w which is not in N':
    D(v) = min(D(v), D(w) + c(w, v))
until N' = N 
```

## • We use the data structure D(v) to store the distance from the current node to all possible destination nodes.

## <sup>•</sup> During the initialization phase:

• We assume that all costs are known! 

<sup>•</sup> Only distances to neighbours are set. 

## <sup>•</sup> During the construction phase:

• Select the closest node w. 

<sup>•</sup> Explore the neighbourhood of w, checking if the path through w is beter than the current one. 

• Exit when all nodes have been explored. 

## Network Layer Routing: Link-State Algorithm

<sup>•</sup> Let’s consider the previous example. Here we show how the LS algorithm works when invoked on the u node: 

• In this case, we will use an additional function p(x) to store the node preceding the selected one. 

• If we want to retrieve the path, we can just backtrack all predecessors until the current node is reached. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/277c0e71-9087-4102-83b0-e963429d5865/2b7497970e60ebc3a04ced90edc59230d3a1f62b93c7b1e9175c6985e2995f92.jpg)


<table><tr><td>step</td><td><eq>N&#x27;</eq></td><td><eq>D(v), p(v)</eq></td><td><eq>D(w), p(w)</eq></td><td><eq>D(x), p(x)</eq></td><td><eq>D(y), p(y)</eq></td><td><eq>D(z), p(z)</eq></td></tr><tr><td>0</td><td>u</td><td>2, u</td><td>5, u</td><td>1, u</td><td>∞</td><td>∞</td></tr><tr><td>1</td><td>ux</td><td>2, u</td><td>4, x</td><td></td><td>2, x</td><td>∞</td></tr><tr><td>2</td><td>uxy</td><td>2, u</td><td>3, y</td><td></td><td></td><td>4, y</td></tr><tr><td>3</td><td>uxyv</td><td></td><td>3, y</td><td></td><td></td><td>4, y</td></tr><tr><td>4</td><td>uxyvw</td><td></td><td></td><td></td><td></td><td>4, y</td></tr><tr><td>5</td><td>uxyvwz</td><td></td><td></td><td></td><td></td><td></td></tr></table>

## Network Layer Routing: Link-State Algorithm

<sup>•</sup> Let’s consider the previous 6- nodes example. Here we show how the LS algorithm works when invoked on the u node: 

• In this case, we will use an additional function p(x) to store the node preceding the selected one. 

<sup>•</sup> If we want to retrieve the path, we can just backtrack all predecessors until the current node is reached. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/277c0e71-9087-4102-83b0-e963429d5865/cf94dde01f60c58470788dcb83f61897d157fc8e6c717eb9a0f96103081ab32f.jpg)


<table><tr><td>step</td><td><eq>N&#x27;</eq></td><td><eq>D(v), p(v)</eq></td><td><eq>D(w), p(w)</eq></td><td><eq>D(x), p(x)</eq></td><td><eq>D(y), p(y)</eq></td><td><eq>D(z), p(z)</eq></td></tr><tr><td>0</td><td>u</td><td>2, u</td><td>5, u</td><td>1, u</td><td>∞</td><td>∞</td></tr><tr><td>1</td><td>ux</td><td>2, u</td><td>4, x</td><td></td><td>2, x</td><td>∞</td></tr><tr><td>2</td><td>uxy</td><td>2, u</td><td>3, y</td><td></td><td></td><td>4, y</td></tr><tr><td>3</td><td>uxyv</td><td></td><td>3, y</td><td></td><td></td><td>4, y</td></tr><tr><td>4</td><td>uxyvw</td><td></td><td></td><td></td><td></td><td>4, y</td></tr><tr><td>5</td><td>uxyvwz</td><td></td><td></td><td></td><td></td><td></td></tr></table>

## Network Layer Routing: Link-State Algorithm

<sup>•</sup> Let’s consider the previous 6- nodes example. Here we show how the LS algorithm works when invoked on the u node: 

• In this case, we will use an additional function p(x) to store the node preceding the selected one. 

<sup>•</sup> If we want to retrieve the path, we can just backtrack all predecessors until the current node is reached. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/277c0e71-9087-4102-83b0-e963429d5865/608c947a110b031c24262e823b36143a3d1156ca33b4222faf60fde4481a7e86.jpg)


<table><tr><td>step</td><td><eq>N&#x27;</eq></td><td><eq>D(v), p(v)</eq></td><td><eq>D(w), p(w)</eq></td><td><eq>D(x), p(x)</eq></td><td><eq>D(y), p(y)</eq></td><td><eq>D(z), p(z)</eq></td></tr><tr><td>0</td><td>u</td><td>2, u</td><td>5, u</td><td>1, u</td><td>∞</td><td>∞</td></tr><tr><td>1</td><td>ux</td><td>2, u</td><td>4, x</td><td></td><td>2, x</td><td>∞</td></tr><tr><td>2</td><td>uxy</td><td>2, u</td><td>3, y</td><td></td><td></td><td>4, y</td></tr><tr><td>3</td><td>uxyv</td><td></td><td>3, y</td><td></td><td></td><td>4, y</td></tr><tr><td>4</td><td>uxyvw</td><td></td><td></td><td></td><td></td><td>4, y</td></tr><tr><td>5</td><td>uxyvwz</td><td></td><td></td><td></td><td></td><td></td></tr></table>

## Network Layer Routing: Link-State Algorithm

<sup>•</sup> Let’s consider the previous 6- nodes example. Here we show how the LS algorithm works when invoked on the u node: 

• In this case, we will use an additional function p(x) to store the node preceding the selected one. 

<sup>•</sup> If we want to retrieve the path, we can just backtrack all predecessors until the current node is reached. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/277c0e71-9087-4102-83b0-e963429d5865/761f93e2de3a75dc1c3ab2c8e36f23a18a54e15beb305fdb907d6a75c1a57322.jpg)


<table><tr><td>step</td><td><eq>N&#x27;</eq></td><td><eq>D(v), p(v)</eq></td><td><eq>D(w), p(w)</eq></td><td><eq>D(x), p(x)</eq></td><td><eq>D(y), p(y)</eq></td><td><eq>D(z), p(z)</eq></td></tr><tr><td>0</td><td>u</td><td>2, u</td><td>5, u</td><td>1, u</td><td>∞</td><td>∞</td></tr><tr><td>1</td><td>ux</td><td>2, u</td><td>4, x</td><td></td><td>2, x</td><td>∞</td></tr><tr><td>2</td><td>uxy</td><td>2, u</td><td>3, y</td><td></td><td></td><td>4, y</td></tr><tr><td>3</td><td>uxyv</td><td></td><td>3, y</td><td></td><td></td><td>4, y</td></tr><tr><td>4</td><td>uxyvw</td><td></td><td></td><td></td><td></td><td>4, y</td></tr><tr><td>5</td><td>uxyvwz</td><td></td><td></td><td></td><td></td><td></td></tr></table>

## Network Layer Routing: Link-State Algorithm

<sup>•</sup> Let’s consider the previous 6- nodes example. Here we show how the LS algorithm works when invoked on the u node: 

• In this case, we will use an additional function p(x) to store the node preceding the selected one. 

<sup>•</sup> If we want to retrieve the path, we can just backtrack all predecessors until the current node is reached. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/277c0e71-9087-4102-83b0-e963429d5865/5cf75343acaee220c9ec1e0d2ac1969d01c9ef06621cf47f0c4c17cab362d660.jpg)


<table><tr><td>step</td><td><eq>N&#x27;</eq></td><td><eq>D(v), p(v)</eq></td><td><eq>D(w), p(w)</eq></td><td><eq>D(x), p(x)</eq></td><td><eq>D(y), p(y)</eq></td><td><eq>D(z), p(z)</eq></td></tr><tr><td>0</td><td>u</td><td>2, u</td><td>5, u</td><td>1, u</td><td>∞</td><td>∞</td></tr><tr><td>1</td><td>ux</td><td>2, u</td><td>4, x</td><td></td><td>2, x</td><td>∞</td></tr><tr><td>2</td><td>uxy</td><td>2, u</td><td>3, y</td><td></td><td></td><td>4, y</td></tr><tr><td>3</td><td>uxyv</td><td></td><td>3, y</td><td></td><td></td><td>4, y</td></tr><tr><td>4</td><td>uxyvw</td><td></td><td></td><td></td><td></td><td>4, y</td></tr><tr><td>5</td><td>uxyvwz</td><td></td><td></td><td></td><td></td><td></td></tr></table>

## Network Layer Routing: Link-State Algorithm

<sup>•</sup> Let’s consider the previous 6- nodes example. Here we show how the LS algorithm works when invoked on the u node: 

• In this case, we will use an additional function p(x) to store the node preceding the selected one. 

<sup>•</sup> If we want to retrieve the path, we can just backtrack all predecessors until the current node is reached. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/277c0e71-9087-4102-83b0-e963429d5865/f0376e46122209f7798b85540bfaca44d1a0bbd2136d93fc7e44a09068610f3b.jpg)


<table><tr><td>step</td><td><eq>N&#x27;</eq></td><td><eq>D(v), p(v)</eq></td><td><eq>D(w), p(w)</eq></td><td><eq>D(x), p(x)</eq></td><td><eq>D(y), p(y)</eq></td><td><eq>D(z), p(z)</eq></td></tr><tr><td>0</td><td>u</td><td>2, u</td><td>5, u</td><td>1, u</td><td>∞</td><td>∞</td></tr><tr><td>1</td><td>ux</td><td>2, u</td><td>4, x</td><td></td><td>2, x</td><td>∞</td></tr><tr><td>2</td><td>uxy</td><td>2, u</td><td>3, y</td><td></td><td></td><td>4, y</td></tr><tr><td>3</td><td>uxyv</td><td></td><td>3, y</td><td></td><td></td><td>4, y</td></tr><tr><td>4</td><td>uxyvw</td><td></td><td></td><td></td><td></td><td>4, y</td></tr><tr><td>5</td><td>uxyvwz</td><td></td><td></td><td></td><td></td><td></td></tr></table>

## Network Layer Routing: Link-State Algorithm

<sup>•</sup> As for the computational complexity, at each iteration we check all nodes of the network, except the source node, then a new source is selected. This means that we are removing one node from each iteration, so the total number of iterations is which is in the worst case. 

<sup>•</sup> This version of the algorithm is quite basic, complexity can be reduced by introducing more sophisticated data-structures (e.g., heaps), we can reach beter performance: . 

## • Pros:

<sup>•</sup> Faster convergence: all communications are performed simultaneously. 

<sup>•</sup> No count-to-infinity: the state of all links is propagated. 

## • Cons:

• Synchronous: nodes must receive information from the whole network before to start. 

## Network Layer Routing: DV vs. LS

• The DV and LS algorithms take complementary approaches to routing: 

<sup>•</sup> In the DV algorithm exploits local information about neighbors. 

<sup>•</sup> The LS algorithm requires global information about all nodes. 

• Message complexity: LS is more complex to implement as synchronous communication between all nodes is needed. In DV, communication is needed only if a best path changes. 

• Speed of convergence: DV requires time to converge, in the meantime we can have suboptimal paths. DV algorithms also sufer of count-to-infinity problem. 

• Robustness: LS is considered more robust as forwarding tables are calculated separately. Each node receives information from all other nodes and creates its own table. In DV all computations are chained, each node depends on the table of others. If one table is incorrect, all tables get the error. 

<sup>•</sup> In 1997 a malfunctioning router from a small ISP caused a chain reaction, which flooded backbone routers, and disconnected part of Internet for several hours. 

• In the end, both solutions are used in Internet. 