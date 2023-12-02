## System Diagram

## State

1. x: The current value for x, a scalar variable
2. y: The current value for y, the dependent variable
3. iteration_step: The value for the iteration which the algorithm is on

## Parameters

### System

1. max_iterations: The maximum number of iterations that the algorithm is allowed to conduct
2. tolerance: The tolerance to determine if iteartions can stop

### Behavioral

None

### Functional

1. f: The function which is being minimized
2. f_prime: The derivative of the minimized function
3. root_finding_method: The root finding method utilized, which can be of the types:
- Bisection
- Newton
- Secant
- Steffensen