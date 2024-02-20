## Wiring Diagram

```mermaid
graph TB
subgraph X7[Calculate Y Prime Block]
direction TB
X1[Calculate Y Prime Policy]
subgraph X6[ ]
direction TB
X2[Update Y Prime Mechanism]
X3[Log Computation Time Metric Mechanism]
X4[Domain]
X5[Codomain]
direction LR
direction TB
X4 --"Update Y Prime Space"--> X2
X4 --"Computation Time Metric Space"--> X3
X2 --> X5
X3 --> X5
end
X1--"Update Y Prime Space
Computation Time Metric Space"-->X6
end
```

## Description

Block Type: Stack Block
Block which calculates and updates the Y prime value.
## Components
1. [[Calculate Y Prime Policy]]
2. [[Calculate Y Prime Parallel Block]]

## Constraints
## Domain Spaces
1. [[Empty Space]]

## Codomain Spaces
1. [[Empty Space]]

## Parameters Used
1. [[f_prime]]

## Called By

## Calls
