## Wiring Diagram

```mermaid
graph TB

subgraph SVS["State Variables"]
EE0[("Global")]
EES0(["Iteration Step"])
EES0 --- EE0
EES1(["X"])
EES1 --- EE0
EES2(["Y"])
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
X2 --> EES1
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
X6 --> EES2
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
X13 --> EES2-Prime
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
X19 --> EES0
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
X25 --> EES1
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
X32 --> EES2
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
X39 --> EES2-Prime
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
X45 --> EES0
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
1. [[Calculate Y Policy]]
2. [[Calculate Y Prime Policy]]
3. [[Increment Iteration Step Mechanism]]
4. [[Initialization Control Action]]
5. [[Iteration Controller Policy]]
6. [[Iteration Policy]]
7. [[Log Computation Time Metric Mechanism]]
8. [[Set Simulation Time Mechanism]]
9. [[Update X Mechanism]]
10. [[Update Y Mechanism]]
11. [[Update Y Prime Mechanism]]

## Constraints

## Domain Spaces

## Codomain Spaces
1. [[Terminating Space]]

## All Spaces Used
1. [[Computation Time Metric Space]]
2. [[Empty Space]]
3. [[Terminating Space]]
4. [[Update X Space]]
5. [[Update Y Prime Space]]
6. [[Update Y Space]]

## Parameters Used
1. [[f]]
2. [[f_prime]]
3. [[max_iterations]]
4. [[root_finding_method]]

## Called By

## Calls

## All State Updates
1. [[Global]].[[Global State-Iteration Step|Iteration Step]]
2. [[Global]].[[Global State-X|X]]
3. [[Global]].[[Global State-Y|Y]]
4. [[Global]].[[Global State-Y Prime|Y Prime]]
5. [[Global]].[[Global State-t|t]]

