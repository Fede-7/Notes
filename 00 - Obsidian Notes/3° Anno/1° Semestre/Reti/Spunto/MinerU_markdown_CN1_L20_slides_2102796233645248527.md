## The Network Layer: The Control Plane

Lecture 20 

## Network Layer Routing: Introduction

<sup>•</sup> We recall that, on packet receival, a router can perform 3 actions: 

<sup>•</sup> Forwarding the packet as is to a suitable neighbor. 

• Forwarding a modified/replaced packet (e.g., fragmentation, masquerading, etc.). 

• Dropping the packet (e.g., if expired). 

<sup>•</sup> There are diferent types of routers, some are very simple and are used by local administrators (for instance to connect LANs and WANs), others are used by ISPs to allow packets to be forwarded to the right device in the entire Internet. 

• As we saw, routers are equipped with forwarding tables that specify the local forward strategy (in the neighborhood of the router). The way these tables are created can be centralized or decentralized. 

• Routers have no knowledge about the rest of the network (at least on startup). 

## Network Layer Routing: Introduction

<sup>•</sup> To decide where packets should be forwarded routers make use of routing algorithms, which determine good paths (i.e., sequence of routes) from senders to receivers. 

<sup>•</sup> Typically, a “good” path is one that has the minimal cost (shortest or fastest path, etc.), in real-world there are also policy issues to be considered (e.g., rules specifying if an organization can talk with another etc.). 

• The routing problem is crucial for computer networks, but the general problem of finding “good paths” on a network (or a graph) is particularly relevant not only for computer networks (e.g., videogames, autonomous driving, robotics, etc.). 

## Network Layer Routing: Flooding

<sup>•</sup> Most simple approach is flooding: each router forwards all incoming packets to all links except for the one by which the packet is received. 

• All paths are explored (optimal one included), so the packet will surely be delivered if a path exists. 

<sup>•</sup> Packets going nowhere will eventually reach their hop limit and be discarded. 

<sup>•</sup> It is tremendously robust due to the redundancy of generated packets (e.g., if some routers are ofline alternative paths are always considered). 

<sup>•</sup> Flooding can be used in specific situations where redundancy is needed (e.g., broadcast of messages, military scenarios, etc.) but it is impractical in highperformance and large networks (such as Internet). 

<sup>•</sup> For typical computer networks a more sophisticated routing algorithm is needed. 

## Network Layer Routing: Problem Formulation

• We can formalize our network as a graph $G = ( N , E )$ , where: 

• N is a set of nodes (the routers of our network). 

• E is a set of edges (physical links) represented as a pair of nodes. 

• An edge also has a value representing its cost, which may reflect the physical length of the link, the link speed, or the monetary cost associated with a link. 

• We can formalize a generic cost as a function c such that, given a generic couple of nodes $( x , \bar { y } )$ 

• If $( \mathsf { x } , \mathsf { y } ) \in \mathsf { E }$ , then c(x,y) is the cost of the edge $( \mathsf { x } , \mathsf { y } )$ 

• If $( \mathsf { x } , \mathsf { y } ) \notin \mathsf { E }$ , then $c ( x , y ) = \infty$ 

• If $( \mathsf { x } , \mathsf { y } ) \in \mathsf { E }$ , then also $( \mathsf { y } , \mathsf { x } ) \in \mathsf { E }$ (undirected graph) and $\mathsf { c } ( \mathsf { x } , \mathsf { y } ) { = } \mathsf { c } ( \mathsf { y } , \mathsf { x } )$ 

## Network Layer Routing: Problem Formulation

• Following this formulation, a path in is a sequence of nodes such that all adjacent nodes are linked, formally: 

$$
(x _ {1}, x _ {2}, \dots , x _ {p}) \text {with} (x _ {1}, x _ {2}), \dots , (x _ {p - 1}, x _ {p}) \in E
$$

• The overall cost of the path is the sum of the links’ costs 

• Let’s call the set of all possible paths connecting the nodes u and z, we can define the best path as the path having minimum cost. 

## Network Layer Routing: Problem Formulation

<sup>•</sup> In this example we have a graph composed of 6 nodes 

<sup>•</sup> For instance, the best path between nodes u and w is: [exercise] 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/f6e9be20-30e9-4d4c-9184-5d1d19749f2e/c774b806ace67a0538409f45676602bf2647c03b403d63d72af3ba07ed7ae7b1.jpg)


## Network Layer Routing: Problem Formulation

<sup>•</sup> Algorithms able to find an optimal path between two nodes are called least-cost path algorithms (shortest-path in case of the same cost between all pairs of nodes). 

• In the case of computer networks, we are interested in finding such optimal path not for just two nodes but for all possible couples of nodes. 

<sup>•</sup> A routing algorithm converges when the shortest path for all couples of nodes in the network is found. 

<sup>•</sup> On networks there are 2 families of algorithms that are typically used: 

• Distance Vector. 

• Link State. 

## Network Layer Routing: Distance-Vector Algorithm

<sup>•</sup> The Distance-Vector (DV) algorithm is a decentralized approach that exploit local knowledge about the network combined with nodes communication to find the shortest paths. 

<sup>•</sup> It is based on the Bellman-Ford algorithm that is used to compute paths. 

<sup>•</sup> Here each node receives some information from one or more of its directly atached neighbors, performs a calculation, and then distributes the results of its calculation back to its neighbors. 

<sup>•</sup> This algorithm is asynchronous in that it does not require all of the nodes to be coordinated with each other. 

## Network Layer Routing: Distance-Vector Algorithm

Let’s denote with ${ \sf d } _ { \sf { x } } ( \sf y )$ the cost of the best path from node x to node y. From the Bellman equation we can derive the following one: 

$$
\mathrm{d} _ {\mathrm{x}} (\mathrm{y}) = \min _ {\mathrm{v}} \left\{\mathrm{c} (\mathrm{x}, \mathrm{v}) + \mathrm{d} _ {\mathrm{v}} (\mathrm{y}) \right\}
$$

This is quite intuitive: there must be and adjacent node v to x that lies on the best path from x to y, and the cost of the said best path is the cost of reaching v plus the best path between v and y. 

• If we are able to find such v we can just add it into the forwarding table and forward to it all packets directed to . 

• To do so, we should have an estimation of for all neighbors (the distance vector). 

## Network Layer Routing: Distance-Vector Algorithm

<sup>•</sup> Let’s try with a real example. Considering u and z, the best path is 

$$
\mathsf {U} \to \mathsf {X} \to \mathsf {Y} \to \mathsf {Z}
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/f6e9be20-30e9-4d4c-9184-5d1d19749f2e/4474ad10a7966a1f38909ba30123a5eaf08c0a08d07c7124af5eda7916b6b0c6.jpg)


## Network Layer Routing: Distance-Vector Algorithm

## • Now, for all the nodes along this optimal path the Bellman equation must hold.

<sup>•</sup> Let’s consider node u, which has 3 neighbours w, v, and x 

• For x we have $\mathsf { c } ( \mathsf { u } , \mathsf { x } ) { = } 1$ and ${ \sf d } _ { \sf x } ( \sf z ) { = } 3$ 

• For v we have $\mathsf { c } ( \mathsf { u } , \mathsf { v } ) { = } 2$ and ${ \mathsf { d } } _ { \mathsf { v } } ( z ) { = } 5$ 

• For w we have $\mathtt { c ( u , w ) } = 5$ and ${ \mathsf { d } } _ { \mathsf { w } } ( \mathsf { z } ) { = } 3$ 

Node x minimises the expression $\mathtt { C } ( \mathtt { U } , \mathtt { X } ) + \mathtt { d } _ { \mathtt { X } } ( \mathtt { Z } )$ therefore it is the next one on the optimal path. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/f6e9be20-30e9-4d4c-9184-5d1d19749f2e/baeef598aaa135f304dadf798d9abfda9c0c7bfd5dabad41c087ba0c67af2dca.jpg)


## Network Layer Routing: Distance-Vector Algorithm

• We can iterate this process on the next node of the path (which is x) and we will see that the Bellman equation stands (i.e., that node y, which is next in the path, will also minimize the expression, and so on). 

• If we have the distance vector for all nodes, we can easily use Bellman equation to compute the next hop in the path (forwarding table). 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/f6e9be20-30e9-4d4c-9184-5d1d19749f2e/0a3dd5e6ed8bacf5e01ffd689f07022c699396be8006ba65112dca5811b15b1d.jpg)


## Network Layer Routing: Distance-Vector Algorithm

## <sup>•</sup> The pseudocode:

DistanceVector(x)
for all nodes v
    if v is a neighbor of x then
    D $_{x}$ (v) = c(x,v)
    else
    D $_{x}$ (v) = ∞
for all neighbors w and destinations y
    D $_{w}$ (y) = ?
    send initial D $_{x}$ (·) to all neighbors

repeat
    if cost of a neighbor updated then
    for all nodes y
    D $_{x}$ (y) = min $_{v}$ {c(x,v) + D $_{v}$ (y)}
    if D $_{x}$ (y) changed for any destination y then
    send updated D $_{x}$ (·) to all neighbors
until false //forever 

• We use the data-structure $\mathsf { D } _ { \mathbf { w } } ( \mathbf { v } )$ to store the distance vectors from all nodes w to target nodes v. 

<sup>•</sup> During the initialization phase: <sup>•</sup> Only distances to neighbors are set. 

## <sup>•</sup> During the online phase:

<sup>•</sup> The news from the neighborhood are received. 

• Distance vectors are updated (Bellman equation). 

<sup>•</sup> Local changes are communicated to adjacent nodes. 

## Network Layer Routing: Distance-Vector Algorithm

## <sup>•</sup> To clarify this process let’s focus again on the path between u and z:

1. On start, u only knows its neighbors. The cost to z is infinity $( \mathsf { D } _ { \mathsf { u } } ( z ) = \infty )$ 

2. Node y wakes up and discovers a beter path to z, which is the direct link y-z with cost $2 \left( \mathsf { D } _ { \mathsf { v } } ( \mathsf { z } ) = \mathsf { c } ( \mathsf { y } , \mathsf { z } ) = 2 \right)$ . It communicates the good news to x. 

3. Node x discovers that the best path to z now passes through y with cost $3 \left( \mathrm { D } _ { \mathrm { x } } ( z ) = \mathsf { c } ( \mathsf { x } , \mathsf { y } ) + \mathrm { D } _ { \mathrm { y } } ( \mathsf { z } ) = 1 + 2 \right)$ , and forwards the good news to u. 

4. Node u receives the news. Now there is a path to z that costs less than infinity passing through $\mathsf { X } ( \mathsf { D } _ { \mathsf { u } } ( \mathsf { z } ) = \mathsf { c } ( \mathsf { u } , \mathsf { x } ) + \mathsf { D } _ { \mathsf { x } } ( \mathsf { z } ) = 1 +$ 3). 

<sup>•</sup> The same process takes place for all nodes/paths. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/f6e9be20-30e9-4d4c-9184-5d1d19749f2e/210ca0285ec5c6ef004fc0660c045b2fd3a0e49798da0e1f84dfe9d39ac3e20e.jpg)


## Network Layer Routing: Distance-Vector Algorithm

<sup>•</sup> As for the computational complexity, every time the cost of a node is updated, all nodes have to re-evaluate their edges. This process leads to a quadratic worst-case complexity. 

## • Pros:

• The algorithm is asynchronous, this facilitates the computation as routers can online and in any stage adapt to updated costs. 

## • Cons:

<sup>•</sup> Slow convergence: updates spread slowly as all nodes have to detect the change and send an updated to the adjacent ones. 

<sup>•</sup> Count-to-infinity: while improved paths are immediately recognized and adopted by the network, failures are detected slowly and may produce loops. 

## Network Layer Routing: Count-to-infinity

```txt
DistanceVector(x)
for all nodes v
    if v is a neighbor of x then
    D_x(v) = c(x,v)
    else
    D_x(v) = ∞
for all neighbors w and destinations y
    D_w(y) = ?
send initial D_x(·) to all neighbors

repeat
    if cost of a neighbor updated then
    for all nodes y
    D_x(y) = min_v{c(x,v) + D_y(y)}
    if D_x(y) changed for any destination y then
    send updated D_x(·) to all neighbors
until false //forever 
```

<sup>•</sup> The count-to-infinity problem is due to the “local” nature of the DV algorithm (which is also its power). 

<sup>•</sup> The local vector $( \mathsf { D } _ { \mathsf { x } } ( \mathsf { y } ) )$ is directly computed starting from the vectors of other nodes $( \mathsf { D } _ { \mathsf { v } } ( \mathsf { v } ) )$ 

• There is no indication about which nodes are in the best paths chosen by adjacent nodes. 

• Can I be sure that I’m not in the “best path” of my neighbors? 

## Network Layer Routing: Count-to-infinity

<sup>•</sup> Let’s consider this simplified example in which the link xy gets a sudden increment of cost and only y notice it! 

$$
\bullet D _ {y} (x) = 4,
$$

$$
\bullet D _ {y} (z) = 1,
$$

$$
\bullet D _ {x} (y) = 4,
$$

$$
\bullet D _ {x} (z) = 4 + D _ {y} (z) = 5,
$$

This is the initial situation before the increment $( \mathsf { c } ( \mathsf { x } , \mathsf { y } )$ is still $4 ) .$ . 

$$
\bullet D _ {z} (x) = 1 + D _ {y} (x) = 5,
$$

$$
\bullet D _ {z} (y) = 1.
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/f6e9be20-30e9-4d4c-9184-5d1d19749f2e/db6a79fa523d17768c912585da517f3ccfb68a5dd397bc550dfba2072c1e8431.jpg)


## Network Layer Routing: Count-to-infinity

<sup>•</sup> Let’s consider this simplified example in which the link xy gets a sudden increment of cost and only y notice it! 

$$
\bullet D _ {y} (x) = 4,
$$

$$
\bullet D _ {y} (z) = 1,
$$

$$
\bullet D _ {x} (y) = 4,
$$

$$
\bullet D _ {x} (z) = 4 + D _ {y} (z) = 5,
$$

Node y detects the increment and updates distance-vector to x: 

$$
\bullet D _ {z} (x) = 1 + D _ {y} (x) = 5,
$$

$$
D _ {y} (x) = \min \{6 0, 1 + D _ {z} (x) \} = 1 + D _ {z} (x) = 6,
$$

$$
\bullet D _ {z} (y) = 1.
$$

$$
\bullet \mathrm{D} _ {\mathrm{y}} (\mathbf {x}) = 1 + \mathrm{D} _ {\mathrm{z}} (\mathbf {x}) = 6,
$$

$$
\bullet D _ {y} (z) = 1,
$$

$$
\bullet D _ {x} (y) = 4,
$$

$$
\bullet D _ {x} (z) = 4 + D _ {y} (z) = 5,
$$

$$
\bullet D _ {z} (x) = 1 + D _ {y} (x) = 5,
$$

$$
\bullet D _ {z} (y) = 1.
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/f6e9be20-30e9-4d4c-9184-5d1d19749f2e/25085f9bce0d03562cf38fc2bcc6ae41442fb94b41037b513970a1a12f2fb27e.jpg)


## Network Layer Routing: Count-to-infinity

<sup>•</sup> Let’s consider this simplified example in which the link xy gets a sudden increment of cost and only y notice it! 

$$
\bullet D _ {y} (x) = 4,
$$

$$
\bullet D _ {y} (z) = 1,
$$

$$
\bullet D _ {x} (y) = 4,
$$

$$
\bullet D _ {x} (z) = 4 + D _ {y} (z) = 5,
$$

$$
\bullet D _ {z} (x) = 1 + D _ {y} (x) = 5,
$$

$$
\bullet D _ {z} (y) = 1.
$$

But vector $\sf D _ { \boldsymbol { v } } ( { \boldsymbol { \mathsf { x } } } )$ is used by z to compute the path to $\mathsf { X } ,$ so also $\sf D _ { z } ( x )$ must be updated! 

$$
\bullet D _ {y} (x) = 1 + D _ {z} (x) = 6,
$$

$$
\bullet D _ {y} (x) = 1 + D _ {z} (x) = 6,
$$

$$
\bullet D _ {y} (z) = 1,
$$

$$
\bullet D _ {y} (z) = 1,
$$

$$
\bullet D _ {x} (y) = 4,
$$

$$
\bullet D _ {x} (y) = 4,
$$

$$
\bullet D _ {x} (z) = 4 + D _ {y} (z) = 5,
$$

$$
\bullet D _ {x} (z) = 4 + D _ {y} (z) = 5,
$$

$$
\bullet D _ {z} (x) = 1 + D _ {y} (x) = 5,
$$

$$
\bullet \mathrm{D} _ {z} (\mathbf {x}) = 1 + \mathrm{D} _ {\mathbf {y}} (\mathbf {x}) = 7,
$$

$$
\bullet D _ {z} (y) = 1.
$$

$$
\bullet D _ {z} (y) = 1.
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/f6e9be20-30e9-4d4c-9184-5d1d19749f2e/a4848c11b7b98137e902096c550620dd89b5c43bb0ca853631c858189e97ff98.jpg)


## Network Layer Routing: Count-to-infinity

<sup>•</sup> Let’s consider this simplified example in which the link xy gets a sudden increment of cost and only y notice it! 

$$
\bullet D _ {y} (x) = 4,
$$

$$
\bullet D _ {y} (z) = 1,
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/f6e9be20-30e9-4d4c-9184-5d1d19749f2e/0114794ab254a73138c53abfd55697d3263a861533255054fe11db3c3070b0f6.jpg)


$$
\bullet D _ {x} (y) = 4,
$$

$$
\bullet D _ {x} (z) = 4 + D _ {y} (z) = 5,
$$

$$
\bullet D _ {z} (x) = 1 + D _ {y} (x) = 5,
$$

$$
\bullet D _ {z} (y) = 1.
$$

But vector $\sf D _ { z } ( x )$ is itself used by y to compute the path to $\mathsf { X } ,$ so $\sf D _ { \mathrm { y } } ( \mathrm { \pmb { x } ) }$ must be updated again! 

$$
\bullet D _ {y} (x) = 1 + D _ {z} (x) = 6,
$$

$$
\bullet D _ {y} (x) = 1 + D _ {z} (x) = 6,
$$

$$
\bullet \mathrm{D} _ {\mathrm{y}} (\mathbf {x}) = 1 + \mathrm{D} _ {\mathrm{z}} (\mathbf {x}) = 8,
$$

$$
\bullet D _ {y} (z) = 1,
$$

$$
\bullet D _ {y} (z) = 1,
$$

$$
\bullet D _ {y} (z) = 1,
$$

$$
\bullet D _ {x} (y) = 4,
$$

$$
\bullet D _ {x} (y) = 4,
$$

$$
\bullet D _ {x} (y) = 4,
$$

$$
\bullet D _ {x} (z) = 4 + D _ {y} (z) = 5,
$$

$$
\bullet D _ {x} (z) = 4 + D _ {y} (z) = 5,
$$

$$
\bullet D _ {x} (z) = 4 + D _ {y} (z) = 5,
$$

$$
\bullet D _ {z} (x) = 1 + D _ {y} (x) = 5,
$$

$$
\bullet D _ {z} (x) = 1 + D _ {y} (x) = 7,
$$

$$
\bullet D _ {z} (x) = 1 + D _ {y} (x) = 7,
$$

$$
\bullet D _ {z} (y) = 1.
$$

$$
\bullet D _ {z} (y) = 1.
$$

$$
\bullet D _ {z} (y) = 1.
$$

## Network Layer Routing: Count-to-infinity

<sup>•</sup> Let’s consider this simplified example in which the link xy gets a sudden increment of cost and only y notice it! 

$$
\bullet D _ {y} (x) = 4,
$$

$$
\bullet D _ {y} (z) = 1,
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/f6e9be20-30e9-4d4c-9184-5d1d19749f2e/8d99871a0288f09d9cb763f5a85215582d4259463a37936f6445ace9dd73b0a6.jpg)


$$
\bullet D _ {x} (y) = 4,
$$

$$
\bullet D _ {x} (z) = 4 + D _ {y} (z) = 5,
$$

$$
\bullet D _ {z} (x) = 1 + D _ {y} (x) = 5,
$$

$$
\bullet D _ {z} (y) = 1.
$$

This is a loop: the 2 vectors will be continuously updated until a stable configuration is reached. 

$$
\bullet D _ {y} (x) = 1 + D _ {z} (x) = 6,
$$

$$
\bullet D _ {y} (x) = 1 + D _ {z} (x) = 6,
$$

$$
\bullet \mathbf {D} _ {\mathrm{y}} (\mathbf {x}) = 1 + \mathbf {D} _ {\mathrm{z}} (\mathbf {x}) = 8,
$$

$$
\bullet D _ {y} (z) = 1,
$$

$$
\bullet D _ {y} (z) = 1,
$$

$$
\bullet D _ {y} (z) = 1,
$$

$$
\bullet D _ {x} (y) = 4,
$$

$$
\bullet D _ {x} (y) = 4,
$$

$$
\bullet D _ {x} (y) = 4,
$$

$$
\bullet D _ {x} (z) = 4 + D _ {y} (z) = 5,
$$

$$
\bullet D _ {x} (z) = 4 + D _ {y} (z) = 5,
$$

$$
\bullet D _ {x} (z) = 4 + D _ {y} (z) = 5,
$$

$$
\bullet D _ {z} (x) = 1 + D _ {y} (x) = 5,
$$

$$
\bullet \mathrm{D} _ {z} (\mathbf {x}) = 1 + \mathrm{D} _ {\mathrm{y}} (\mathbf {x}) = 9,
$$

$$
\bullet D _ {z} (x) = 1 + D _ {y} (x) = 7,
$$

$$
\bullet D _ {z} (y) = 1.
$$

$$
\bullet D _ {z} (y) = 1.
$$

$$
\bullet D _ {z} (y) = 1.
$$

## Network Layer Routing: Count-to-infinity

<sup>•</sup> This problem could have been avoided if x had also noticed/communicated the change of the x-y cost. 

<sup>•</sup> If x is malfunctioning or delayed for some reason (e.g., the high costs of x’s links may indicate that x is malfunctioning), it will take time to converge. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/f6e9be20-30e9-4d4c-9184-5d1d19749f2e/d84b0cc1014d547444d7f72833a4311e14812da70224a5de70d798a5e05bba95.jpg)


$$
\bullet D _ {y} (x) = \operatorname{MIN} \left\{c (y, x), c (y, z) + D _ {z} (x) \right\} = c (y, z) + D _ {z} (x) = 1 + 5 0 = 5 1,
$$

$$
\bullet D _ {y} (z) = \operatorname{MIN} \left\{c (y, z), c (y, x) + D _ {x} (z) \right\} = c (y, z) = 1,
$$

$$
\bullet D _ {x} (y) = \operatorname{MIN} \left\{c (x, y), c (x, z) + D _ {z} (y) \right\} = c (x, z) + D _ {z} (y) = 5 0 + 1 = 5 1,
$$

$$
\bullet D _ {x} (z) = \operatorname{MIN} \left\{c (x, z), c (x, y) + D _ {y} (z) \right\} = c (x, z) = 5 0,
$$

$$
\bullet D _ {z} (x) = \operatorname{MIN} \left\{c (z, x), c (z, y) + D _ {y} (x) \right\} = c (z, x) = 5 0,
$$

$$
\bullet D _ {z} (y) = \operatorname{MIN} \left\{c (z, y), c (z, x) + D _ {x} (y) \right\} = c (z, y) = 1.
$$

Costs convergence in case node x detects the change. 