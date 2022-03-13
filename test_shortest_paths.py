from main import Graph,shortest_path
import pytest


def test_shortest_path_home_work():
    work_g=Graph()
    work_g.add_edge('home','bus station A',2)
    work_g.add_edge('home','bus station B',5)

    work_g.add_edge('home','work',45)

    work_g.add_edge('bus station A','shop A',10)
    work_g.add_edge('bus station B','shop B',15)


    work_g.add_edge('bus station A','bus station C',20)
    work_g.add_edge('bus station C','bus station D',24)

    work_g.add_edge('bus station B','bus station C',16)
    work_g.add_edge('bus station B','bus station D',15)

    work_g.add_edge('bus station c','work',14)
    work_g.add_edge('bus station D','work',13)

  # verify
    assert shortest_path(work_g,'home','work')['distance']==33
    assert shortest_path(work_g,'home','work')['path']== ['home', 'bus station B', 'bus station D', 'work']





# europe graph eu_g
# Let us assume we want to travel around Europe by train.
# We decide to visit the following cities:
# 'madrid', 'paris', 'frankfurt', 'amsterdam', 'zurich', 'milan', 'rom', 'vienna', 'berlin','hamburg'
# We create a graph with the cities as nodes, and edges between cities means that there are affordable tickets between cities. 
# In this example, each node represents a city in europe, and the edge-weight represents the distance by train between the two cities.
def europe_graph():
    
    eu_g=Graph()
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

    assert shortest_path(eu_g,'rom','madrid')['path']==['rom', 'milan', 'zurich', 'paris', 'madrid']
    assert shortest_path(eu_g,'vienna','amsterdam')['path']==['vienna', 'frankfurt', 'amsterdam']
    

# Test logic of shortest paths and graph   
# Home to work graph
test_shortest_path_home_work()
# Europe Cities graph
europe_graph()
