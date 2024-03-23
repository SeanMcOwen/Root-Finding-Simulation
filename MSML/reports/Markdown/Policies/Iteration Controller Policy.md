## Description

The policy which controls whether another iteration should take place in a simulation.
## Called By
## Domain Spaces
1. [[Empty Space]]
## Followed By
1. [[Iteration Policy]]
## Codomain Spaces
1. [[Empty Space]]
## Constraints
## Parameters Used
1. [[max_iterations]]
## Metrics Used
## Policy Options
### 1. Constant Iterations Policy Option
#### Description
A policy option which runs a constant number of iterations for any simulation.
#### Logic
If state["iteration_step"] < params["max_iterations"], call the iteration policy, otherwise terminate

### 2. Tolerance Policy Option
#### Description
A policy option which runs a constant number of iterations for any simulation unless abs(y) is less than a tolerance.
#### Logic
If state["iteration_step"] < params["max_iterations"] and abs(state["y"]) > params["tolerance"], call the iteration policy, otherwise terminate

