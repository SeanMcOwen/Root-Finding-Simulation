## Wiring Diagram

```mermaid
graph TB
subgraph X4[Initialization Block]
direction TB
X1[Initialization Control Action]
X2[Update X Mechanism]
X3[Set Simulation Time Mechanism]
X1--"Update X Space"-->X2
X2--->X3
end
```

## Description

Block Type: Stack Block
Block which handles the initialization.
## Components
1. [[Initialization Control Action]]
2. [[Update X Mechanism]]
3. [[Set Simulation Time Mechanism]]

## Constraints
## Domain Spaces

## Codomain Spaces
1. [[Terminating Space]]

## Parameters Used

## Called By

## Calls

