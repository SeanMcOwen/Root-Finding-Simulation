<h1>Root Finding Simulation Mathematical Specification</h1><h2>Summary</h2><p>This model aims to compare different methods for root finding in terms of both accuracy and computational time.</p><h2>Specification Tree</h2>├──Entities
│   ├──Dummy
├──State
│   ├──Dummy
│   │   ├──Variable A
│   │   ├──Variable B
│   │   ├──Variable C
│   ├──Global
├──Stateful Metrics
│   ├──Dummy Stateful Metrics
│   │   ├──dummy_metric
├──Spaces
│   ├──Terminating Space
│   ├──Empty Space
│   ├──Initialization Space
│   ├──Update X Space
│   ├──Update Y Space
│   ├──Update Y Prime Space
│   ├──None Space
│   ├──Computation Time Metric Space
│   ├──State Metric Space
├──Parameters
│   ├──Iteration
│   │   ├──max_iterations
│   │   ├──tolerance
│   │   ├──f
│   │   ├──f_prime
│   │   ├──root_finding_method
├──Boundary Actions
├──Control Actions
│   ├──Initialization Control Action
├──Policies
│   ├──Iteration Controller Policy
│   ├──Iteration Policy
│   ├──Calculate Y Policy
│   ├──Calculate Y Prime Policy
├──Mechanisms
│   ├──Update X Mechanism
│   ├──Log Computation Time Metric Mechanism
│   ├──Increment Iteration Step Mechanism
│   ├──Set Simulation Time Mechanism
│   ├──Update Y Mechanism
│   ├──Update Y Prime Mechanism
│   ├──Log State Metric Mechanism
