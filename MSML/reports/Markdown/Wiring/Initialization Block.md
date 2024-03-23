## Wiring Diagram

```mermaid
graph TB

subgraph SVS["State Variables"]
EE0[("Global")]
EES0(["t"])
EES0 --- EE0
EES1(["X"])
EES1 --- EE0
end

subgraph X4["Initialization Block"]
direction TB
X1["Initialization Control Action"]
X2["Update X Mechanism"]
X2 --> EES1
X3["Set Simulation Time Mechanism"]
X3 --> EES0
X1--"Update X Space"--->X2
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

## All Blocks
1. [[Update X Mechanism]]
2. [[Initialization Control Action]]
3. [[Set Simulation Time Mechanism]]

## Constraints

## Domain Spaces

## Codomain Spaces
1. [[Terminating Space]]

## All Spaces Used
1. [[Update X Space]]
2. [[Empty Space]]
3. [[Terminating Space]]

## Parameters Used

## Called By

## Calls

## All State Updates
1. [[Global]].t
2. [[Global]].X

