## Wiring Diagram

```mermaid
graph TB

subgraph SVS["State Variables"]
EE0[("Global")]
EES0(["X"])
EES0 --- EE0
end

subgraph X7["Iteration Block"]
direction TB
X1["Iteration Policy"]
subgraph X6[" "]
direction TB
X2["Update X Mechanism"]
X2 --> EES0
X3["Log Computation Time Metric Mechanism"]
X4[Domain]

direction LR
direction TB
X4 --"Update X Space"--> X2
X4 --"Computation Time Metric Space"--> X3
end
X1--"Update X Space
Computation Time Metric Space"---->X6
end
```

## Description

Block Type: Stack Block
Block which calculates one iteration.
## Components
1. [[Iteration Policy]]
2. [[Iteration Parallel Block]]

## All Blocks
1. [[Iteration Policy]]
2. [[Log Computation Time Metric Mechanism]]
3. [[Update X Mechanism]]

## Constraints

## Domain Spaces
1. [[Empty Space]]

## Codomain Spaces
1. [[Empty Space]]

## All Spaces Used
1. [[Computation Time Metric Space]]
2. [[Empty Space]]
3. [[Terminating Space]]
4. [[Update X Space]]

## Parameters Used
1. [[root_finding_method]]

## Called By

## Calls

## All State Updates
1. [[Global]].[[Global State-X|X]]

