## Wiring Diagram

```mermaid
graph TB

subgraph SVS["State Variables"]
EE0[("Global")]
EES0(["Y Prime"])
EES0 --- EE0
end

subgraph X5[" "]
direction TB
X1["Update Y Prime Mechanism"]
X1 --> EES0
X2["Log Computation Time Metric Mechanism"]
X3[Domain]

direction LR
direction TB
X3 --"Update Y Prime Space"--> X1
X3 --"Computation Time Metric Space"--> X2
end
```

## Description

Block Type: Parallel Block
Block which updates the Y prime value and logs the computation time it took from calculate Y prime policy.
## Components
1. [[Update Y Prime Mechanism]]
2. [[Log Computation Time Metric Mechanism]]

## All Blocks
1. [[Log Computation Time Metric Mechanism]]
2. [[Update Y Prime Mechanism]]

## Constraints

## Domain Spaces
1. [[Update Y Prime Space]]
2. [[Computation Time Metric Space]]

## Codomain Spaces
1. [[Empty Space]]

## All Spaces Used
1. [[Update Y Prime Space]]
2. [[Empty Space]]
3. [[Terminating Space]]
4. [[Computation Time Metric Space]]

## Parameters Used

## Called By

## Calls

## All State Updates
1. [[Global]].Y Prime

