## Wiring Diagram

```mermaid
graph TB
subgraph X5[ ]
direction TB
X1[Update Y Prime Mechanism]
X2[Log Computation Time Metric Mechanism]
X3[Domain]
X4[Codomain]
direction LR
direction TB
X3 --"Update Y Prime Space"--> X1
X3 --"Computation Time Metric Space"--> X2
X1 --> X4
X2 --> X4
end
```

## Description

Block Type: Paralell Block
Block which updates the Y prime value and logs the computation time it took from calculate Y prime policy.
## Components
1. [[Update Y Prime Mechanism]]
2. [[Log Computation Time Metric Mechanism]]

## Constraints
## Domain Spaces
1. [[Update Y Prime Space]]
2. [[Computation Time Metric Space]]

## Codomain Spaces
1. [[Empty Space]]

## Parameters Used

## Called By

## Calls

