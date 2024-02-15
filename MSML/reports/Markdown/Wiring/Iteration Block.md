## Wiring Diagram

```mermaid
graph TB
subgraph X7[Iteration Block]
direction TB
X1[Iteration Policy]
subgraph X6[ ]
direction TB
X2[Update X Mechanism]
X3[Log Computation Time Metric Mechanism]
X4[Domain]
X5[Codomain]
direction LR
direction TB
X4 --"Update X Space"--> X2
X4 --"Computation Time Metric Space"--> X3
X2 --> X5
X3 --> X5
end
X1--"Update X Space
Computation Time Metric Space"-->X6
end
```

## Description

Block Type: Stack Block
Block which calculates one iteration.
## Components
1. [[Iteration Policy]]
2. [[Iteration Parallel Block]]

## Constraints
## Domain Spaces
1. [[Empty Space]]

## Codomain Spaces
1. [[Empty Space]]

## Parameters Used
1. [[root_finding_method]]

## Called By

## Calls

