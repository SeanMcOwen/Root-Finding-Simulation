## Wiring Diagram

```mermaid
graph TB
subgraph X18[Calculate Dependent Variables Block]
direction TB
subgraph X7[Calculate Y Block]
direction TB
X1[Calculate Y Policy]
subgraph X6[ ]
direction TB
X2[Update Y Mechanism]
X3[Log Computation Time Metric Mechanism]
X4[Domain]
X5[Codomain]
direction LR
direction TB
X4 --"Update Y Space"--> X2
X4 --"Computation Time Metric Space"--> X3
X2 --> X5
X3 --> X5
end
X1--"Update Y Space
Computation Time Metric Space"-->X6
end
subgraph X14[Calculate Y Prime Block]
direction TB
X8[Calculate Y Prime Policy]
subgraph X13[ ]
direction TB
X9[Update Y Prime Mechanism]
X10[Log Computation Time Metric Mechanism]
X11[Domain]
X12[Codomain]
direction LR
direction TB
X11 --"Update Y Prime Space"--> X9
X11 --"Computation Time Metric Space"--> X10
X9 --> X12
X10 --> X12
end
X8--"Update Y Prime Space
Computation Time Metric Space"-->X13
end
X15[Increment Iteration Step Mechanism]
X16[Domain]
X17[Codomain]
direction LR
direction TB
X16 --> X7
X16 --> X14
X16 --> X15
X7 --> X17
X14 --> X17
X15 --> X17
end
```

## Description

Block Type: Paralell Block
Block which updates the Y, Y Prime, and the iteration step.
## Components
1. [[Calculate Y Block]]
2. [[Calculate Y Prime Block]]
3. [[Increment Iteration Step Mechanism]]

## Constraints
## Domain Spaces
1. [[Empty Space]]

## Codomain Spaces
1. [[Empty Space]]

## Parameters Used
1. [[f_prime]]
2. [[f]]

## Called By

## Calls

