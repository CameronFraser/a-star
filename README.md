# A\* Pathfinding Algorithm

### Steps to run

1. Clone repo and run example script `python example.py`

2. Adjust start and goal parameters in the example.py script to try different paths

This was partially done in Udacity's Intro to Self Driving Car Nanodegree. I ported my solution to run locally and rewrote the visualization logic to reduce dependencies.

The heuristic being used is Euclidean distance calculated by `h(n) = sqrt((x1 - x2)**2 + (y1 - y2)**2)`

Below is an example of the generated network with the shortest path between 8 and 35 highlighted
![Shortest path between node 8 and 35](/network.png?raw=true)
