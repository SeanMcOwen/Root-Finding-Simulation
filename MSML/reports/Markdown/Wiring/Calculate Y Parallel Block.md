## Wiring Diagram

```mermaid
graph TB
subgraph X5[ ]
direction TB
X1[Update Y Mechanism]
X2[Log Computation Time Metric Mechanism]
X3[Domain]
X4[Codomain]
direction LR
direction TB
X3 --"Update Y Space"--> X1
X3 --"Computation Time Metric Space"--> X2
X1 --> X4
X2 --> X4
end
```

## Description

Block Type: Paralell Block
Block which updates the Y value and logs the computation time it took from calculate Y policy.
## Components
1. [[Update Y Mechanism]]
2. [[Log Computation Time Metric Mechanism]]

## Constraints
## Domain Spaces
1. [[Update Y Space]]
2. [[Computation Time Metric Space]]

## Codomain Spaces
1. [[Empty Space]]

## Parameters Used

## Called By

## Calls

