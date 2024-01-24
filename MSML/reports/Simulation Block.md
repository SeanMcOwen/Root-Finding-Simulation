## Wiring Diagram

```mermaid
graph TB
subgraph X37[Simulation Block]
direction TB
subgraph X4[Initialization Block]
direction TB
X1[Initialization Control Action]
X2[Update X Mechanism]
X3[Set Simulation Time Mechanism]
X1-->X2
X2-->X3
end
subgraph X16[Calculate Dependent Variables Block]
direction LR
subgraph X9[Calculate Y Block]
direction TB
X5[Calculate Y Policy]
subgraph X8[ ]
direction LR
X6[Update Y Mechanism]
X7[Log Computation Time Metric Mechanism]
X6 ~~~ X7
end
X5-->X8
end
subgraph X14[Calculate Y Prime Block]
direction TB
X10[Calculate Y Prime Policy]
subgraph X13[ ]
direction LR
X11[Update Y Prime Mechanism]
X12[Log Computation Time Metric Mechanism]
X11 ~~~ X12
end
X10-->X13
end
X15[Increment Iteration Step Mechanism]
X9 ~~~ X14
X14 ~~~ X15
end
subgraph X36[Root Finding Block]
direction TB
X17[Iteration Controller Policy]
subgraph X22[Iteration Block]
direction TB
X18[Iteration Policy]
subgraph X21[ ]
direction LR
X19[Update X Mechanism]
X20[Log Computation Time Metric Mechanism]
X19 ~~~ X20
end
X18-->X21
end
subgraph X34[Calculate Dependent Variables Block]
direction LR
subgraph X27[Calculate Y Block]
direction TB
X23[Calculate Y Policy]
subgraph X26[ ]
direction LR
X24[Update Y Mechanism]
X25[Log Computation Time Metric Mechanism]
X24 ~~~ X25
end
X23-->X26
end
subgraph X32[Calculate Y Prime Block]
direction TB
X28[Calculate Y Prime Policy]
subgraph X31[ ]
direction LR
X29[Update Y Prime Mechanism]
X30[Log Computation Time Metric Mechanism]
X29 ~~~ X30
end
X28-->X31
end
X33[Increment Iteration Step Mechanism]
X27 ~~~ X32
X32 ~~~ X33
end
X35[Set Simulation Time Mechanism]
X17-->X22
X22-->X34
X34-->X35
end
X4-->X16
X16-->X36
end
```

## State<h3>Local States</h3><h2>Spaces</h2><h3>Terminating Space</h3><p>{}</p><h3>Empty Space</h3><p>{}</p><h3>Update Y Space</h3><p>{y: Objective Value Type}</p><h3>Update X Space</h3><p>{x: X Type}</p><h3>Update Y Prime Space</h3><p>{y_prime: Objective Derivative Value Type}</p><h3>Computation Time Metric Space</h3><p>{simulation_time: datetime,<br/>computation_time: Seconds Type,<br/>action_name: str}</p><h2>Behavioral Action Space</h2><h2>Control Action Space</h2><h3>Initialization Control Action</h3><p>Control action to begin the simulation</p><h4>Constraints:</h4>
<h2>Policies</h2><h3>Calculate Y Prime Policy</h3><p>The policy which calculates the value for the derivative of f.</p><h4>Preceded By:</h4>
<h4>Domain Spaces:</h4>
<p>1. Empty Space</p><h4>Followed By:</h4>
<p>1. Update Y Prime Mechanism</p><p>2. Log Computation Time Metric Mechanism</p><h4>Codomain Spaces:</h4>
<p>1. Update Y Prime Space</p><p>2. Computation Time Metric Space</p><h4>Constraints:</h4>
<h3>Calculate Y Policy</h3><p>The policy which calculates the value for f.</p><h4>Preceded By:</h4>
<h4>Domain Spaces:</h4>
<p>1. Empty Space</p><h4>Followed By:</h4>
<p>1. Update Y Mechanism</p><p>2. Log Computation Time Metric Mechanism</p><h4>Codomain Spaces:</h4>
<p>1. Update Y Space</p><p>2. Computation Time Metric Space</p><h4>Constraints:</h4>
<h3>Iteration Policy</h3><p>The policy which produces one iteration of the root finding algorithm.</p><h4>Preceded By:</h4>
<p>1. Iteration Controller Policy</p><h4>Domain Spaces:</h4>
<p>1. Empty Space</p><h4>Followed By:</h4>
<p>1. Update X Mechanism</p><p>2. Log Computation Time Metric Mechanism</p><h4>Codomain Spaces:</h4>
<p>1. Update X Space</p><p>2. Computation Time Metric Space</p><h4>Constraints:</h4>
<h3>Iteration Controller Policy</h3><p>The policy which controls whether another iteration should take place in a simulation.</p><h4>Preceded By:</h4>
<h4>Domain Spaces:</h4>
<p>1. Empty Space</p><h4>Followed By:</h4>
<p>1. Iteration Policy</p><h4>Codomain Spaces:</h4>
<p>1. Empty Space</p><h4>Constraints:</h4>
<h4>Policy Options:</h4>
<details><summary><b>1. Constant Iterations Policy Option</b></summary><p>A policy option which runs a constant number of iterations for any simulation.</p><p>Logic: If state["iteration_step"] < params["max_iterations"], call the iteration policy, otherwise terminate</p></details><details><summary><b>2. Tolerance Policy Option</b></summary><p>A policy option which runs a constant number of iterations for any simulation unless abs(y) is less than a tolerance.</p><p>Logic: If state["iteration_step"] < params["max_iterations"] and abs(state["y"]) > params["tolerance"], call the iteration policy, otherwise terminate</p></details><br/><h3>Calculate Y Prime Policy</h3><p>The policy which calculates the value for the derivative of f.</p><h4>Preceded By:</h4>
<h4>Domain Spaces:</h4>
<p>1. Empty Space</p><h4>Followed By:</h4>
<p>1. Update Y Prime Mechanism</p><p>2. Log Computation Time Metric Mechanism</p><h4>Codomain Spaces:</h4>
<p>1. Update Y Prime Space</p><p>2. Computation Time Metric Space</p><h4>Constraints:</h4>
<h3>Calculate Y Policy</h3><p>The policy which calculates the value for f.</p><h4>Preceded By:</h4>
<h4>Domain Spaces:</h4>
<p>1. Empty Space</p><h4>Followed By:</h4>
<p>1. Update Y Mechanism</p><p>2. Log Computation Time Metric Mechanism</p><h4>Codomain Spaces:</h4>
<p>1. Update Y Space</p><p>2. Computation Time Metric Space</p><h4>Constraints:</h4>
<h2>Mechanisms</h2><h3>Set Simulation Time Mechanism</h3><p>Mechanism for setting the current time of the simulation</p><h4>Preceded By:</h4>
<h4>Domain Spaces:</h4>
<p>1. Empty Space</p><h4>State Updates:</h4>
<h4>Constraints:</h4>
<h4>Logic:</h4>
<p>state['simulation_time'] = now()</p><h3>Increment Iteration Step Mechanism</h3><p>Mechanism for incrementing the iteration step by 1</p><h4>Preceded By:</h4>
<h4>Domain Spaces:</h4>
<p>1. Empty Space</p><h4>State Updates:</h4>
<h4>Constraints:</h4>
<h4>Logic:</h4>
<p>state['iteration_step'] += 1</p><h3>Log Computation Time Metric Mechanism</h3><p>The computation time metric is logged here</p><h4>Preceded By:</h4>
<p>1. Calculate Y Prime Policy</p><p>2. Iteration Policy</p><p>3. Calculate Y Policy</p><h4>Domain Spaces:</h4>
<p>1. Computation Time Metric Space</p><h4>State Updates:</h4>
<h4>Constraints:</h4>
<h4>Logic:</h4>
<p></p><h3>Update Y Prime Mechanism</h3><p>Mechanism for an update to the y_prime value</p><h4>Preceded By:</h4>
<p>1. Calculate Y Prime Policy</p><h4>Domain Spaces:</h4>
<p>1. Update Y Prime Space</p><h4>State Updates:</h4>
<h4>Constraints:</h4>
<h4>Logic:</h4>
<p></p><h3>Log Computation Time Metric Mechanism</h3><p>The computation time metric is logged here</p><h4>Preceded By:</h4>
<p>1. Calculate Y Prime Policy</p><p>2. Iteration Policy</p><p>3. Calculate Y Policy</p><h4>Domain Spaces:</h4>
<p>1. Computation Time Metric Space</p><h4>State Updates:</h4>
<h4>Constraints:</h4>
<h4>Logic:</h4>
<p></p><h3>Update Y Mechanism</h3><p>Mechanism for an update to the y value</p><h4>Preceded By:</h4>
<p>1. Calculate Y Policy</p><h4>Domain Spaces:</h4>
<p>1. Update Y Space</p><h4>State Updates:</h4>
<h4>Constraints:</h4>
<h4>Logic:</h4>
<p></p><h3>Log Computation Time Metric Mechanism</h3><p>The computation time metric is logged here</p><h4>Preceded By:</h4>
<p>1. Calculate Y Prime Policy</p><p>2. Iteration Policy</p><p>3. Calculate Y Policy</p><h4>Domain Spaces:</h4>
<p>1. Computation Time Metric Space</p><h4>State Updates:</h4>
<h4>Constraints:</h4>
<h4>Logic:</h4>
<p></p><h3>Update X Mechanism</h3><p>Mechanism for update to the x value</p><h4>Preceded By:</h4>
<p>1. Iteration Policy</p><p>2. Initialization Control Action</p><h4>Domain Spaces:</h4>
<p>1. Update X Space</p><h4>State Updates:</h4>
<h4>Constraints:</h4>
<h4>Logic:</h4>
<p></p><h3>Increment Iteration Step Mechanism</h3><p>Mechanism for incrementing the iteration step by 1</p><h4>Preceded By:</h4>
<h4>Domain Spaces:</h4>
<p>1. Empty Space</p><h4>State Updates:</h4>
<h4>Constraints:</h4>
<h4>Logic:</h4>
<p>state['iteration_step'] += 1</p><h3>Log Computation Time Metric Mechanism</h3><p>The computation time metric is logged here</p><h4>Preceded By:</h4>
<p>1. Calculate Y Prime Policy</p><p>2. Iteration Policy</p><p>3. Calculate Y Policy</p><h4>Domain Spaces:</h4>
<p>1. Computation Time Metric Space</p><h4>State Updates:</h4>
<h4>Constraints:</h4>
<h4>Logic:</h4>
<p></p><h3>Update Y Prime Mechanism</h3><p>Mechanism for an update to the y_prime value</p><h4>Preceded By:</h4>
<p>1. Calculate Y Prime Policy</p><h4>Domain Spaces:</h4>
<p>1. Update Y Prime Space</p><h4>State Updates:</h4>
<h4>Constraints:</h4>
<h4>Logic:</h4>
<p></p><h3>Log Computation Time Metric Mechanism</h3><p>The computation time metric is logged here</p><h4>Preceded By:</h4>
<p>1. Calculate Y Prime Policy</p><p>2. Iteration Policy</p><p>3. Calculate Y Policy</p><h4>Domain Spaces:</h4>
<p>1. Computation Time Metric Space</p><h4>State Updates:</h4>
<h4>Constraints:</h4>
<h4>Logic:</h4>
<p></p><h3>Update Y Mechanism</h3><p>Mechanism for an update to the y value</p><h4>Preceded By:</h4>
<p>1. Calculate Y Policy</p><h4>Domain Spaces:</h4>
<p>1. Update Y Space</p><h4>State Updates:</h4>
<h4>Constraints:</h4>
<h4>Logic:</h4>
<p></p><h3>Set Simulation Time Mechanism</h3><p>Mechanism for setting the current time of the simulation</p><h4>Preceded By:</h4>
<h4>Domain Spaces:</h4>
<p>1. Empty Space</p><h4>State Updates:</h4>
<h4>Constraints:</h4>
<h4>Logic:</h4>
<p>state['simulation_time'] = now()</p><h3>Update X Mechanism</h3><p>Mechanism for update to the x value</p><h4>Preceded By:</h4>
<p>1. Iteration Policy</p><p>2. Initialization Control Action</p><h4>Domain Spaces:</h4>
<p>1. Update X Space</p><h4>State Updates:</h4>
<h4>Constraints:</h4>
<h4>Logic:</h4>
<p></p><h2>Parameters</h2><p>f_prime</p><p>f</p><p>root_finding_method</p><p>max_iterations</p>