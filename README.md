# dijkstra_algorithm
08 Assignment: Graphs
Abel Camacho Guardian

## Create graphs and calculate shortest path(s). 

We can create graphs using the class Graph.
  ```sh
eu_g=Graph()
  ```
The class graph assumes that the graphs are undirected weighted graph, and that there are no isolated nodes.
We add new edges to the graph using the method add_edge, as follows
```
eu_g.add_edge('madrid','paris',1270)
eu_g.add_edge('paris','frankfurt',586)
eu_g.add_edge('amsterdam','frankfurt',439)
eu_g.add_edge('frankfurt','zurich',305)

eu_g.add_edge('zurich','milan',217)
eu_g.add_edge('milan','rom',470)
eu_g.add_edge('zurich','vienna',592)
eu_g.add_edge('zurich','paris',489)

eu_g.add_edge('zurich','berlin',844)
eu_g.add_edge('vienna','berlin',681)
eu_g.add_edge('vienna','frankfurt',716)
eu_g.add_edge('berlin','hamburg',289)
eu_g.add_edge('amsterdam','hamburg',463)
```
The above graph wil create the graph shown in Figure 1.

![](https://user-images.githubusercontent.com/25433668/158068153-1218a225-376c-4d4c-8d7b-83e020782814.png)

The nodes in a graph can be retrieved using the functions get_nodes.

```
eu_g.get_nodes()
```

<p>
  <b>Output: </b> ['madrid', 'paris', 'frankfurt', 'amsterdam', 'zurich', 'milan', 'rom', 'vienna', 'berlin', 'hamburg']
  </p>
We get the neigbours from Frankfurt as follows

```
eu_g.get_neighbours('frankfurt')
```
<p>
  <b>Output: </b> ['paris', 'amsterdam', 'zurich', 'vienna']
</p>


We can comute the shortest path from Rom to all other cities using the function.

```
dijkstra_algorithm(eu_g,'rom')
```
<p style="background-color:gray;">
<b>Output: </b>
  ({'madrid': 2446,
  'paris': 1176,
  'frankfurt': 992,
  'amsterdam': 1431,
  'zurich': 687,
  'milan': 470,
  'vienna': 1279,
  'berlin': 1531,
  'hamburg': 1820,
  'rom': 0},
 {'rom': ['rom'],
  'milan': ['rom', 'milan'],
  'zurich': ['rom', 'milan', 'zurich'],
  'frankfurt': ['rom', 'milan', 'zurich', 'frankfurt'],
  'vienna': ['rom', 'milan', 'zurich', 'vienna'],
  'paris': ['rom', 'milan', 'zurich', 'paris'],
  'berlin': ['rom', 'milan', 'zurich', 'berlin'],
  'amsterdam': ['rom', 'milan', 'zurich', 'frankfurt', 'amsterdam'],
  'madrid': ['rom', 'milan', 'zurich', 'paris', 'madrid'],
  'hamburg': ['rom', 'milan', 'zurich', 'berlin', 'hamburg']})
</p>  

To get the shortest path between Rom and Amsterdam, we can use the function shortest_path
```
shortest_path(eu_g,'rom','amsterdam')
```
<p style="background-color:gray;">
<b>Output: </b> {'distance': 1431,
 'path': ['rom', 'milan', 'zurich', 'frankfurt', 'amsterdam']} 
</p>

## Further extensions
- Allow for directed and undirected graphs.
- Allow for graphs with isolated nodes.
