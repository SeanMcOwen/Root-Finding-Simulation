## Wiring Diagram

```mermaid
graph TB

subgraph SVS["State Variables"]
EE0[("Global")]
EES0(["Y"])
EES0 --- EE0
end

subgraph X7["Calculate Y Block"]
direction TB
X1["Calculate Y Policy"]
subgraph X6[" "]
direction TB
X2["Update Y Mechanism"]
X2 --> EES0
X3["Log Computation Time Metric Mechanism"]
X4[Domain]

direction LR
direction TB
X4 --"Update Y Space"--> X2
X4 --"Computation Time Metric Space"--> X3
end
X1--"Update Y Space
Computation Time Metric Space"---->X6
end
```

## Description

Block Type: Stack Block
Block which calculates and updates the Y value.
## Components
1. [[Calculate Y Policy]]
2. [[Calculate Y Parallel Block]]

## All Blocks
1. [[Update Y Mechanism]]
2. [[Calculate Y Policy]]
3. [[Log Computation Time Metric Mechanism]]

## Constraints

## Domain Spaces
1. [[Empty Space]]

## Codomain Spaces
1. [[Empty Space]]

## All Spaces Used
1. [[Computation Time Metric Space]]
2. [[Terminating Space]]
3. [[Empty Space]]
4. [[Update Y Space]]

## Parameters Used
1. [[f]]

## Called By

## Calls

## All State Updates
1. [[Global]].Y

