## Wiring Diagram

```mermaid
graph TB
subgraph X28[Root Finding Block]
direction TB
X1[Iteration Controller Policy]
subgraph X8[Iteration Block]
direction TB
X2[Iteration Policy]
subgraph X7[ ]
direction TB
X3[Update X Mechanism]
X4[Log Computation Time Metric Mechanism]
X5[Domain]
X6[Codomain]
direction LR
direction TB
X5 --"Update X Space"--> X3
X5 --"Computation Time Metric Space"--> X4
X3 --> X6
X4 --> X6
end
X2--"Update X Space
Computation Time Metric Space"-->X7
end
subgraph X26[Calculate Dependent Variables Block]
direction TB
subgraph X15[Calculate Y Block]
direction TB
X9[Calculate Y Policy]
subgraph X14[ ]
direction TB
X10[Update Y Mechanism]
X11[Log Computation Time Metric Mechanism]
X12[Domain]
X13[Codomain]
direction LR
direction TB
X12 --"Update Y Space"--> X10
X12 --"Computation Time Metric Space"--> X11
X10 --> X13
X11 --> X13
end
X9--"Update Y Space
Computation Time Metric Space"-->X14
end
subgraph X22[Calculate Y Prime Block]
direction TB
X16[Calculate Y Prime Policy]
subgraph X21[ ]
direction TB
X17[Update Y Prime Mechanism]
X18[Log Computation Time Metric Mechanism]
X19[Domain]
X20[Codomain]
direction LR
direction TB
X19 --"Update Y Prime Space"--> X17
X19 --"Computation Time Metric Space"--> X18
X17 --> X20
X18 --> X20
end
X16--"Update Y Prime Space
Computation Time Metric Space"-->X21
end
X23[Increment Iteration Step Mechanism]
X24[Domain]
X25[Codomain]
direction LR
direction TB
X24 --> X15
X24 --> X22
X24 --> X23
X15 --> X25
X22 --> X25
X23 --> X25
end
X27[Set Simulation Time Mechanism]
X1-.->X8
X8--->X26
X26--->X27
X27--->X1
end
```

## Description

Block Type: Stack Block
Block which handles all aspects of using the root finding algorithm.
## Components
1. [[Iteration Controller Policy]]
2. [[Iteration Block]]
3. [[Calculate Dependent Variables Block]]
4. [[Set Simulation Time Mechanism]]

## Constraints
## Domain Spaces
1. [[Empty Space]]

## Codomain Spaces
1. [[Terminating Space]]

## Parameters Used
1. [[max_iterations]]
2. [[f]]
3. [[f_prime]]
4. [[root_finding_method]]

## Called By

## Calls

