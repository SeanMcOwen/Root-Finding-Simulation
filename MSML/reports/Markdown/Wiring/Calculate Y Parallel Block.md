## Wiring Diagram

```mermaid
graph TB

subgraph SVS["State Variables"]
EE0[("Global")]
EES0(["Y"])
EES0 --- EE0
end

subgraph X5[" "]
direction TB
X1["Update Y Mechanism"]
X1 --> EES0
X2["Log Computation Time Metric Mechanism"]
X3[Domain]

direction LR
direction TB
X3 --"Update Y Space"--> X1
X3 --"Computation Time Metric Space"--> X2
end
```

## Description

Block Type: Parallel Block
Block which updates the Y value and logs the computation time it took from calculate Y policy.
## Components
1. [[Update Y Mechanism]]
2. [[Log Computation Time Metric Mechanism]]

## All Blocks
1. [[Update Y Mechanism]]
2. [[Log Computation Time Metric Mechanism]]

## Constraints

## Domain Spaces
1. [[Update Y Space]]
2. [[Computation Time Metric Space]]

## Codomain Spaces
1. [[Empty Space]]

## All Spaces Used
1. [[Empty Space]]
2. [[Update Y Space]]
3. [[Computation Time Metric Space]]
4. [[Terminating Space]]

## Parameters Used

## Called By

## Calls

## All State Updates
1. [[Global]].[[Global State-Y|Y]]

