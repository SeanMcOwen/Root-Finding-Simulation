## Description

The policy which calculates the value for the derivative of f.
## Called By
## Domain Spaces
1. [[Empty Space]]
## Followed By
1. [[Update Y Prime Mechanism]]
2. [[Log Computation Time Metric Mechanism]]
## Codomain Spaces
1. [[Update Y Prime Space]]
2. [[Computation Time Metric Space]]
## Constraints
## Parameters Used
1. [[f_prime]]
## Metrics Used
## Policy Options
### 1. Calculate Y Prime Policy Basic
#### Description
Basic solving.
#### Logic
y_prime = params["f_prime"](state["X"])

