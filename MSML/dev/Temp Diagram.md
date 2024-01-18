```mermaid
graph TB
subgraph X5[Calculate Y Block]
direction TB
X1[Calculate Y Policy]
subgraph X4[Calculate Y Parallel Block]
direction LR
X2[Update Y Mechanism]
X3[Log Computation Time Metric Mechanism]
X2 ~~~ X3
end
X1-->X4
end
```