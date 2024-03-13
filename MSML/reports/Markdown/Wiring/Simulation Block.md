## Wiring Diagram

```mermaid
graph TB
subgraph X51[Simulation Block]
direction TB
subgraph X4[Initialization Block]
direction TB
X1[Initialization Control Action]
X2[Update X Mechanism]
X3[Set Simulation Time Mechanism]
X1--"Update X Space"-->X2
X2--->X3
end
subgraph X22[Calculate Dependent Variables Block]
direction TB
subgraph X11[Calculate Y Block]
direction TB
X5[Calculate Y Policy]
subgraph X10[ ]
direction TB
X6[Update Y Mechanism]
X7[Log Computation Time Metric Mechanism]
X8[Domain]
X9[Codomain]
direction LR
direction TB
X8 --"Update Y Space"--> X6
X8 --"Computation Time Metric Space"--> X7
X6 --> X9
X7 --> X9
end
X5--"Update Y Space
Computation Time Metric Space"-->X10
end
subgraph X18[Calculate Y Prime Block]
direction TB
X12[Calculate Y Prime Policy]
subgraph X17[ ]
direction TB
X13[Update Y Prime Mechanism]
X14[Log Computation Time Metric Mechanism]
X15[Domain]
X16[Codomain]
direction LR
direction TB
X15 --"Update Y Prime Space"--> X13
X15 --"Computation Time Metric Space"--> X14
X13 --> X16
X14 --> X16
end
X12--"Update Y Prime Space
Computation Time Metric Space"-->X17
end
X19[Increment Iteration Step Mechanism]
X20[Domain]
X21[Codomain]
direction LR
direction TB
X20 --> X11
X20 --> X18
X20 --> X19
X11 --> X21
X18 --> X21
X19 --> X21
end
subgraph X50[Root Finding Block]
direction TB
X23[Iteration Controller Policy]
subgraph X30[Iteration Block]
direction TB
X24[Iteration Policy]
subgraph X29[ ]
direction TB
X25[Update X Mechanism]
X26[Log Computation Time Metric Mechanism]
X27[Domain]
X28[Codomain]
direction LR
direction TB
X27 --"Update X Space"--> X25
X27 --"Computation Time Metric Space"--> X26
X25 --> X28
X26 --> X28
end
X24--"Update X Space
Computation Time Metric Space"-->X29
end
subgraph X48[Calculate Dependent Variables Block]
direction TB
subgraph X37[Calculate Y Block]
direction TB
X31[Calculate Y Policy]
subgraph X36[ ]
direction TB
X32[Update Y Mechanism]
X33[Log Computation Time Metric Mechanism]
X34[Domain]
X35[Codomain]
direction LR
direction TB
X34 --"Update Y Space"--> X32
X34 --"Computation Time Metric Space"--> X33
X32 --> X35
X33 --> X35
end
X31--"Update Y Space
Computation Time Metric Space"-->X36
end
subgraph X44[Calculate Y Prime Block]
direction TB
X38[Calculate Y Prime Policy]
subgraph X43[ ]
direction TB
X39[Update Y Prime Mechanism]
X40[Log Computation Time Metric Mechanism]
X41[Domain]
X42[Codomain]
direction LR
direction TB
X41 --"Update Y Prime Space"--> X39
X41 --"Computation Time Metric Space"--> X40
X39 --> X42
X40 --> X42
end
X38--"Update Y Prime Space
Computation Time Metric Space"-->X43
end
X45[Increment Iteration Step Mechanism]
X46[Domain]
X47[Codomain]
direction LR
direction TB
X46 --> X37
X46 --> X44
X46 --> X45
X37 --> X47
X44 --> X47
X45 --> X47
end
X49[Set Simulation Time Mechanism]
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

## Constraints
## Domain Spaces

## Codomain Spaces
1. [[Terminating Space]]

## Parameters Used
1. [[f]]
2. [[f_prime]]
3. [[max_iterations]]
4. [[root_finding_method]]

## Called By

## Calls

