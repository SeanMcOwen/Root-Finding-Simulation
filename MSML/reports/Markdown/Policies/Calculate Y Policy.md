## Description

The policy which calculates the value for f.
## Called By
## Domain Spaces
1. [[Empty Space]]
## Followed By
1. [[Update Y Mechanism]]
2. [[Log Computation Time Metric Mechanism]]
## Codomain Spaces
1. [[Update Y Space]]
2. [[Computation Time Metric Space]]
## Constraints
## Parameters Used
1. [[f]]
## Metrics Used
## Policy Options
### 1. Calculate Y Policy Basic
#### Description
Basic solving.
#### Logic
y = params["f"](state["x"])

