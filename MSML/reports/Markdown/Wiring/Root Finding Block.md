## Wiring Diagram

```mermaid
graph TB

subgraph SVS["State Variables"]
EE0[("Global")]
EES0(["X"])
EES0 --- EE0
EES1(["t"])
EES1 --- EE0
EES2(["Iteration Step"])
EES2 --- EE0
EES3(["Y"])
EES3 --- EE0
EES4(["Y Prime"])
EES4 --- EE0
end

subgraph X28["Root Finding Block"]
direction TB
X1["Iteration Controller Policy"]
subgraph X8["Iteration Block"]
direction TB
X2["Iteration Policy"]
subgraph X7[" "]
direction TB
X3["Update X Mechanism"]
X3 --> EES0
X4["Log Computation Time Metric Mechanism"]
X5[Domain]

direction LR
direction TB
X5 --"Update X Space"--> X3
X5 --"Computation Time Metric Space"--> X4
end
X2--"Update X Space
Computation Time Metric Space"---->X7
end
subgraph X26["Calculate Dependent Variables Block"]
direction TB
subgraph X15["Calculate Y Block"]
direction TB
X9["Calculate Y Policy"]
subgraph X14[" "]
direction TB
X10["Update Y Mechanism"]
X10 --> EES3
X11["Log Computation Time Metric Mechanism"]
X12[Domain]

direction LR
direction TB
X12 --"Update Y Space"--> X10
X12 --"Computation Time Metric Space"--> X11
end
X9--"Update Y Space
Computation Time Metric Space"---->X14
end
subgraph X22["Calculate Y Prime Block"]
direction TB
X16["Calculate Y Prime Policy"]
subgraph X21[" "]
direction TB
X17["Update Y Prime Mechanism"]
X17 --> EES3-Prime
X18["Log Computation Time Metric Mechanism"]
X19[Domain]

direction LR
direction TB
X19 --"Update Y Prime Space"--> X17
X19 --"Computation Time Metric Space"--> X18
end
X16--"Update Y Prime Space
Computation Time Metric Space"---->X21
end
X23["Increment Iteration Step Mechanism"]
X23 --> EES2
X24[Domain]

direction LR
direction TB
X24 --> X15
X24 --> X22
X24 --> X23
end
X27["Set Simulation Time Mechanism"]
X27 --> EES1
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

## All Blocks
1. [[Update X Mechanism]]
2. [[Calculate Y Prime Policy]]
3. [[Iteration Policy]]
4. [[Log Computation Time Metric Mechanism]]
5. [[Update Y Mechanism]]
6. [[Increment Iteration Step Mechanism]]
7. [[Iteration Controller Policy]]
8. [[Calculate Y Policy]]
9. [[Update Y Prime Mechanism]]
10. [[Set Simulation Time Mechanism]]

## Constraints

## Domain Spaces
1. [[Empty Space]]

## Codomain Spaces
1. [[Terminating Space]]

## All Spaces Used
1. [[Update Y Prime Space]]
2. [[Computation Time Metric Space]]
3. [[Terminating Space]]
4. [[Empty Space]]
5. [[Update X Space]]
6. [[Update Y Space]]

## Parameters Used
1. [[f]]
2. [[f_prime]]
3. [[max_iterations]]
4. [[root_finding_method]]

## Called By

## Calls

## All State Updates
1. [[Global]].X
2. [[Global]].t
3. [[Global]].Iteration Step
4. [[Global]].Y
5. [[Global]].Y Prime

