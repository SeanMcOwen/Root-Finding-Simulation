## Wiring Diagram

```mermaid
graph TB

subgraph SVS["State Variables"]
EE0[("Global")]
EES0(["Y"])
EES0 --- EE0
EES1(["Iteration Step"])
EES1 --- EE0
EES2(["X"])
EES2 --- EE0
EES3(["Y Prime"])
EES3 --- EE0
EES4(["t"])
EES4 --- EE0
end

subgraph X51["Simulation Block"]
direction TB
subgraph X4["Initialization Block"]
direction TB
X1["Initialization Control Action"]
X2["Update X Mechanism"]
X2 --> EES2
X3["Set Simulation Time Mechanism"]
X3 --> EES4
X1--"Update X Space"--->X2
X2--->X3
end
subgraph X22["Calculate Dependent Variables Block"]
direction TB
subgraph X11["Calculate Y Block"]
direction TB
X5["Calculate Y Policy"]
subgraph X10[" "]
direction TB
X6["Update Y Mechanism"]
X6 --> EES0
X7["Log Computation Time Metric Mechanism"]
X8[Domain]

direction LR
direction TB
X8 --"Update Y Space"--> X6
X8 --"Computation Time Metric Space"--> X7
end
X5--"Update Y Space
Computation Time Metric Space"---->X10
end
subgraph X18["Calculate Y Prime Block"]
direction TB
X12["Calculate Y Prime Policy"]
subgraph X17[" "]
direction TB
X13["Update Y Prime Mechanism"]
X13 --> EES0-Prime
X14["Log Computation Time Metric Mechanism"]
X15[Domain]

direction LR
direction TB
X15 --"Update Y Prime Space"--> X13
X15 --"Computation Time Metric Space"--> X14
end
X12--"Update Y Prime Space
Computation Time Metric Space"---->X17
end
X19["Increment Iteration Step Mechanism"]
X19 --> EES1
X20[Domain]

direction LR
direction TB
X20 --> X11
X20 --> X18
X20 --> X19
end
subgraph X50["Root Finding Block"]
direction TB
X23["Iteration Controller Policy"]
subgraph X30["Iteration Block"]
direction TB
X24["Iteration Policy"]
subgraph X29[" "]
direction TB
X25["Update X Mechanism"]
X25 --> EES2
X26["Log Computation Time Metric Mechanism"]
X27[Domain]

direction LR
direction TB
X27 --"Update X Space"--> X25
X27 --"Computation Time Metric Space"--> X26
end
X24--"Update X Space
Computation Time Metric Space"---->X29
end
subgraph X48["Calculate Dependent Variables Block"]
direction TB
subgraph X37["Calculate Y Block"]
direction TB
X31["Calculate Y Policy"]
subgraph X36[" "]
direction TB
X32["Update Y Mechanism"]
X32 --> EES0
X33["Log Computation Time Metric Mechanism"]
X34[Domain]

direction LR
direction TB
X34 --"Update Y Space"--> X32
X34 --"Computation Time Metric Space"--> X33
end
X31--"Update Y Space
Computation Time Metric Space"---->X36
end
subgraph X44["Calculate Y Prime Block"]
direction TB
X38["Calculate Y Prime Policy"]
subgraph X43[" "]
direction TB
X39["Update Y Prime Mechanism"]
X39 --> EES0-Prime
X40["Log Computation Time Metric Mechanism"]
X41[Domain]

direction LR
direction TB
X41 --"Update Y Prime Space"--> X39
X41 --"Computation Time Metric Space"--> X40
end
X38--"Update Y Prime Space
Computation Time Metric Space"---->X43
end
X45["Increment Iteration Step Mechanism"]
X45 --> EES1
X46[Domain]

direction LR
direction TB
X46 --> X37
X46 --> X44
X46 --> X45
end
X49["Set Simulation Time Mechanism"]
X49 --> EES4
X23-.->X30
X30--->X48
X48--->X49
X49--->X23
end
X4--->X22
X22--->X50
end
```

## Description

Block Type: Stack Block
Block which encapsulates the full simulation.
## Components
1. [[Initialization Block]]
2. [[Calculate Dependent Variables Block]]
3. [[Root Finding Block]]

## All Blocks
1. [[Update Y Mechanism]]
2. [[Log Computation Time Metric Mechanism]]
3. [[Update X Mechanism]]
4. [[Iteration Policy]]
5. [[Set Simulation Time Mechanism]]
6. [[Update Y Prime Mechanism]]
7. [[Initialization Control Action]]
8. [[Calculate Y Policy]]
9. [[Iteration Controller Policy]]
10. [[Calculate Y Prime Policy]]
11. [[Increment Iteration Step Mechanism]]

## Constraints

## Domain Spaces

## Codomain Spaces
1. [[Terminating Space]]

## All Spaces Used
1. [[Computation Time Metric Space]]
2. [[Terminating Space]]
3. [[Update X Space]]
4. [[Empty Space]]
5. [[Update Y Space]]
6. [[Update Y Prime Space]]

## Parameters Used
1. [[f]]
2. [[max_iterations]]
3. [[f_prime]]
4. [[root_finding_method]]

## Called By

## Calls

## All State Updates
1. [[Global]].Y
2. [[Global]].Iteration Step
3. [[Global]].X
4. [[Global]].Y Prime
5. [[Global]].t

