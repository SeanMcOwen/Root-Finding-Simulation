## Wiring Diagram

```mermaid
graph TB

subgraph SVS["State Variables"]
EE0[("Global")]
EES0(["Y Prime"])
EES0 --- EE0
end

subgraph X7["Calculate Y Prime Block"]
direction TB
X1["Calculate Y Prime Policy"]
subgraph X6[" "]
direction TB
X2["Update Y Prime Mechanism"]
X2 --> EES0
X3["Log Computation Time Metric Mechanism"]
X4[Domain]

direction LR
direction TB
X4 --"Update Y Prime Space"--> X2
X4 --"Computation Time Metric Space"--> X3
end
X1--"Update Y Prime Space
Computation Time Metric Space"---->X6
end
```

## Description

Block Type: Stack Block
Block which calculates and updates the Y prime value.
## Components
1. [[Calculate Y Prime Policy]]
2. [[Calculate Y Prime Parallel Block]]

## All Blocks
1. [[Calculate Y Prime Policy]]
2. [[Log Computation Time Metric Mechanism]]
3. [[Update Y Prime Mechanism]]

## Constraints

## Domain Spaces
1. [[Empty Space]]

## Codomain Spaces
1. [[Empty Space]]

## All Spaces Used
1. [[Computation Time Metric Space]]
2. [[Empty Space]]
3. [[Terminating Space]]
4. [[Update Y Prime Space]]

## Parameters Used
1. [[f_prime]]

## Called By

## Calls

## All State Updates
1. [[Global]].[[Global State-Y Prime|Y Prime]]

