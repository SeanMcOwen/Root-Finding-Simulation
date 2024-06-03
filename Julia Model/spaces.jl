include("../../BlockScience/cadCAD.jl/src/spaces.jl")
include("types.jl")
using .Spaces: generate_space_type

generate_space_type((x=XType,), "Update X Space")
generate_space_type((y=ObjectiveValueType,), "Update Y Space")
generate_space_type((y_prime=ObjectiveDerivativeValueType,), "Update Y Prime Space")
generate_space_type((simulation_time=SecondsType, computation_time=SecondsType, action_name=ActionNameType,), "Computation Time Metric Space")
generate_space_type((simulation_time=SecondsType, x=XType, y=ObjectiveValueType, y_prime=ObjectiveDerivativeValueType, iteration_step=NumberIterationsType,), "State Metric Space")
