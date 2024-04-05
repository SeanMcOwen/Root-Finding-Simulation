## Wiring Diagram

```mermaid
graph TB

subgraph SVS["State Variables"]
EE0[("Global")]
EES0(["Iteration Step"])
EES0 --- EE0
EES1(["Y"])
EES1 --- EE0
EES2(["Y Prime"])
EES2 --- EE0
end

subgraph X18["Calculate Dependent Variables Block"]
direction TB
subgraph X7["Calculate Y Block"]
direction TB
X1["Calculate Y Policy"]
subgraph X6[" "]
direction TB
X2["Update Y Mechanism"]
X2 --> EES1
X3["Log Computation Time Metric Mechanism"]
X4[Domain]

direction LR
direction TB
X4 --"Update Y Space"--> X2
X4 --"Computation Time Metric Space"--> X3
end
X1--"Update Y Space
Computation Time Metric Space"---->X6
end
subgraph X14["Calculate Y Prime Block"]
direction TB
X8["Calculate Y Prime Policy"]
subgraph X13[" "]
direction TB
X9["Update Y Prime Mechanism"]
X9 --> EES1-Prime
X10["Log Computation Time Metric Mechanism"]
X11[Domain]

direction LR
direction TB
X11 --"Update Y Prime Space"--> X9
X11 --"Computation Time Metric Space"--> X10
end
X8--"Update Y Prime Space
Computation Time Metric Space"---->X13
end
X15["Increment Iteration Step Mechanism"]
X15 --> EES0
X16[Domain]

direction LR
direction TB
X16 --> X7
X16 --> X14
X16 --> X15
end
```

## Description

Block Type: Parallel Block
Block which updates the Y, Y Prime, and the iteration step.
## Components
1. [[Calculate Y Block]]
2. [[Calculate Y Prime Block]]
3. [[Increment Iteration Step Mechanism]]

## All Blocks
1. [[Update Y Prime Mechanism]]
2. [[Calculate Y Policy]]
3. [[Calculate Y Prime Policy]]
4. [[Log Computation Time Metric Mechanism]]
5. [[Update Y Mechanism]]
6. [[Increment Iteration Step Mechanism]]

## Constraints

## Domain Spaces
1. [[Empty Space]]

## Codomain Spaces
1. [[Empty Space]]

## All Spaces Used
1. [[Terminating Space]]
2. [[Empty Space]]
3. [[Computation Time Metric Space]]
4. [[Update Y Prime Space]]
5. [[Update Y Space]]

## Parameters Used
1. [[f]]
2. [[f_prime]]

## Called By

## Calls

## All State Updates
1. [[Global]].Iteration Step
2. [[Global]].Y
3. [[Global]].Y Prime

