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

## State
<h3>Global State</h3><table>
      <tr>
        <th>Name</th>
        <th>Description</th>
        <th>Type</th>
        <th>Symbol</th>
        <th>Domain</th>
      </tr><tr><td>X</td><td></td><td>X Type</td><td></td><td></td></tr><tr><td>Iteration Step</td><td></td><td>Number of Iterations Type</td><td></td><td></td></tr><tr><td>t</td><td></td><td>Seconds Type</td><td></td><td></td></tr><tr><td>Y</td><td></td><td>Objective Value Type</td><td></td><td></td></tr><tr><td>Y Prime</td><td></td><td>Objective Derivative Value Type</td><td></td><td></td></tr></table><h3>Local States</h3><h2>Spaces</h2><h3>Update Y Prime Space</h3><p>{y_prime: Objective Derivative Value Type}</p><h3>Terminating Space</h3><p>{}</p><h3>Computation Time Metric Space</h3><p>{simulation_time: Seconds Type,<br/>computation_time: Seconds Type,<br/>action_name: Action Name Type}</p><h3>Empty Space</h3><p>{}</p><h3>Update X Space</h3><p>{x: X Type}</p><h3>Update Y Space</h3><p>{y: Objective Value Type}</p><h2>Behavioral Action Space</h2><h2>Control Action Space</h2><h3>Initialization Control Action</h3><p>Control action to begin the simulation</p><h4>Constraints:</h4>
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
<p>1. Global.t</p><h4>Constraints:</h4>
<h4>Logic:</h4>
<p>state['simulation_time'] = now()</p><h3>Increment Iteration Step Mechanism</h3><p>Mechanism for incrementing the iteration step by 1</p><h4>Preceded By:</h4>
<h4>Domain Spaces:</h4>
<p>1. Empty Space</p><h4>State Updates:</h4>
<p>1. Global.Iteration Step</p><h4>Constraints:</h4>
<h4>Logic:</h4>
<p>state['iteration_step'] += 1</p><h3>Log Computation Time Metric Mechanism</h3><p>The computation time metric is logged here</p><h4>Preceded By:</h4>
<p>1. Calculate Y Prime Policy</p><p>2. Iteration Policy</p><p>3. Calculate Y Policy</p><h4>Domain Spaces:</h4>
<p>1. Computation Time Metric Space</p><h4>State Updates:</h4>
<h4>Constraints:</h4>
<h4>Logic:</h4>
<p></p><h3>Update Y Prime Mechanism</h3><p>Mechanism for an update to the y_prime value</p><h4>Preceded By:</h4>
<p>1. Calculate Y Prime Policy</p><h4>Domain Spaces:</h4>
<p>1. Update Y Prime Space</p><h4>State Updates:</h4>
<p>1. Global.Y Prime</p><h4>Constraints:</h4>
<h4>Logic:</h4>
<p></p><h3>Log Computation Time Metric Mechanism</h3><p>The computation time metric is logged here</p><h4>Preceded By:</h4>
<p>1. Calculate Y Prime Policy</p><p>2. Iteration Policy</p><p>3. Calculate Y Policy</p><h4>Domain Spaces:</h4>
<p>1. Computation Time Metric Space</p><h4>State Updates:</h4>
<h4>Constraints:</h4>
<h4>Logic:</h4>
<p></p><h3>Update Y Mechanism</h3><p>Mechanism for an update to the y value</p><h4>Preceded By:</h4>
<p>1. Calculate Y Policy</p><h4>Domain Spaces:</h4>
<p>1. Update Y Space</p><h4>State Updates:</h4>
<p>1. Global.Y</p><h4>Constraints:</h4>
<h4>Logic:</h4>
<p></p><h3>Log Computation Time Metric Mechanism</h3><p>The computation time metric is logged here</p><h4>Preceded By:</h4>
<p>1. Calculate Y Prime Policy</p><p>2. Iteration Policy</p><p>3. Calculate Y Policy</p><h4>Domain Spaces:</h4>
<p>1. Computation Time Metric Space</p><h4>State Updates:</h4>
<h4>Constraints:</h4>
<h4>Logic:</h4>
<p></p><h3>Update X Mechanism</h3><p>Mechanism for update to the x value</p><h4>Preceded By:</h4>
<p>1. Iteration Policy</p><p>2. Initialization Control Action</p><h4>Domain Spaces:</h4>
<p>1. Update X Space</p><h4>State Updates:</h4>
<p>1. Global.X</p><h4>Constraints:</h4>
<h4>Logic:</h4>
<p></p><h3>Increment Iteration Step Mechanism</h3><p>Mechanism for incrementing the iteration step by 1</p><h4>Preceded By:</h4>
<h4>Domain Spaces:</h4>
<p>1. Empty Space</p><h4>State Updates:</h4>
<p>1. Global.Iteration Step</p><h4>Constraints:</h4>
<h4>Logic:</h4>
<p>state['iteration_step'] += 1</p><h3>Log Computation Time Metric Mechanism</h3><p>The computation time metric is logged here</p><h4>Preceded By:</h4>
<p>1. Calculate Y Prime Policy</p><p>2. Iteration Policy</p><p>3. Calculate Y Policy</p><h4>Domain Spaces:</h4>
<p>1. Computation Time Metric Space</p><h4>State Updates:</h4>
<h4>Constraints:</h4>
<h4>Logic:</h4>
<p></p><h3>Update Y Prime Mechanism</h3><p>Mechanism for an update to the y_prime value</p><h4>Preceded By:</h4>
<p>1. Calculate Y Prime Policy</p><h4>Domain Spaces:</h4>
<p>1. Update Y Prime Space</p><h4>State Updates:</h4>
<p>1. Global.Y Prime</p><h4>Constraints:</h4>
<h4>Logic:</h4>
<p></p><h3>Log Computation Time Metric Mechanism</h3><p>The computation time metric is logged here</p><h4>Preceded By:</h4>
<p>1. Calculate Y Prime Policy</p><p>2. Iteration Policy</p><p>3. Calculate Y Policy</p><h4>Domain Spaces:</h4>
<p>1. Computation Time Metric Space</p><h4>State Updates:</h4>
<h4>Constraints:</h4>
<h4>Logic:</h4>
<p></p><h3>Update Y Mechanism</h3><p>Mechanism for an update to the y value</p><h4>Preceded By:</h4>
<p>1. Calculate Y Policy</p><h4>Domain Spaces:</h4>
<p>1. Update Y Space</p><h4>State Updates:</h4>
<p>1. Global.Y</p><h4>Constraints:</h4>
<h4>Logic:</h4>
<p></p><h3>Set Simulation Time Mechanism</h3><p>Mechanism for setting the current time of the simulation</p><h4>Preceded By:</h4>
<h4>Domain Spaces:</h4>
<p>1. Empty Space</p><h4>State Updates:</h4>
<p>1. Global.t</p><h4>Constraints:</h4>
<h4>Logic:</h4>
<p>state['simulation_time'] = now()</p><h3>Update X Mechanism</h3><p>Mechanism for update to the x value</p><h4>Preceded By:</h4>
<p>1. Iteration Policy</p><p>2. Initialization Control Action</p><h4>Domain Spaces:</h4>
<p>1. Update X Space</p><h4>State Updates:</h4>
<p>1. Global.X</p><h4>Constraints:</h4>
<h4>Logic:</h4>
<p></p><h2>Parameters</h2><h3>f_prime</h3><p>Description: The objective function derivative</p><p>Symbol: None</p><p>Domain: None</p><p>Parameter Class: behavioral</p><h3>root_finding_method</h3><p>Description: The functional parameterization for the root finding method to use</p><p>Symbol: None</p><p>Domain: None</p><p>Parameter Class: functional</p><h3>f</h3><p>Description: The objective function</p><p>Symbol: None</p><p>Domain: None</p><p>Parameter Class: behavioral</p><h3>max_iterations</h3><p>Description: The maximum number of iterations for the simulation</p><p>Symbol: None</p><p>Domain: None</p><p>Parameter Class: system</p>