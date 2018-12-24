# chameleon-problem

project for solving "Chameleon problem" (and also for getting some experience in Python).

## Problem:
```
On the Sebur island lived chameleons. There were 13 red, 16 green and 17 blue ones.
In case when two chameleons of different colors met, they change their color to
another (e.g. was one red and one green - they became two blue chameleons).
Is it possible for all chameleons to become one color?
```

## Implementation
For representing state of the chameleons on the island I created a `State` class (see [here](https://github.com/Nazar910/chameleon-problem/blob/master/state.py)).
It has usefull methods like checking if all chameleons already of one color or create new state like red_met_blue() which returns new state object with updated chameleons count.

### Algorithms:
To solve "chameleons problem" I used three graph traversing algorithms:
- depth first search DFS ([implementation](https://github.com/Nazar910/chameleon-problem/blob/master/depth_first_search.py))
- breadth first search BFS ([implementation](https://github.com/Nazar910/chameleon-problem/blob/master/breadth_first_search.py))
- A* algorithm (A star) ([implementation](https://github.com/Nazar910/chameleon-problem/blob/master/a_star.py))

## Tests
You can check that all works by running tests.

Run one:
```fish
python a_star.test.py
```
Or launching all of them (fish shell example)
```fish
bash -c './run_tests.sh'
```
for bash or zsh use
```bash
./run_tests.sh
```


## Conclusion
So, what are the results. All three algorithms found state (red=0, green=46, blue=0) as the state where all chameleons have one color.
About algorithms:
- DFS is the easiest for the understanding and I suppose for the implementation. But it mostly depends on your luck to find the right state (so in 93 step it found final state with path of 89 steps see [test](https://github.com/Nazar910/chameleon-problem/blob/master/depth_first_search.test.py))
- BFS is much nicer because it garantees to find the shortest path and it found one in 17 steps (see [test](https://github.com/Nazar910/chameleon-problem/blob/master/breadth_first_search.test.py)) but made more than 180 000 steps.
- A* is the most difficult for understanding of the 3 algoritthms but it is the most effective one. It uses [cost](https://github.com/Nazar910/chameleon-problem/blob/master/a_star.py#L60) and [heuristic](https://github.com/Nazar910/chameleon-problem/blob/master/a_star.py#L17) estimates to guide the direction of search. As a result it found the shortest path (17 steps) in only about 3000 steps (see [test](https://github.com/Nazar910/chameleon-problem/blob/master/a_star.test.py))
