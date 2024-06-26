## Wiring Diagram

```mermaid
graph TB

subgraph SVS["State Variables"]
EE0[("Global")]
EES0(["X"])
EES0 --- EE0
EES1(["t"])
EES1 --- EE0
end

subgraph X4["Initialization Block"]
direction TB
X1["Initialization Control Action"]
X2["Update X Mechanism"]
X2 --> EES0
X3["Set Simulation Time Mechanism"]
X3 --> EES1
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
1. [[Initialization Control Action]]
2. [[Set Simulation Time Mechanism]]
3. [[Update X Mechanism]]

## Constraints

## Domain Spaces

## Codomain Spaces
1. [[Terminating Space]]

## All Spaces Used
1. [[Empty Space]]
2. [[Terminating Space]]
3. [[Update X Space]]

## Parameters Used

## Called By

## Calls

## All State Updates
1. [[Global]].[[Global State-X|X]]
2. [[Global]].[[Global State-t|t]]

