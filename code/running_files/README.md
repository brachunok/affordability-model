# How to use this
(1) make a configuration file. they will have object pairs in them which
describe the parameter and then the value(s) it can take
(2) make sure there's just a space between them, and no blank lines before or
after the parameters

(3) once you have a config file, run the model_running file with the name of
the config file as an argument. It will read the parameters, and instantiate
a class of SantaCruz with the given parameters.

TODO: If any parameters are arrays,
the model will be run for all combinations of all array values. e.g. if the
first parameter is [1,2] and the second is [a,b], the model will be run for
1,a 2,a, 1,b 2,b and the result

(4) then we will use the other methods (simulate) to actually run the model

## Good practice for extending this
Parameters go in the config file; e.g. things which change the way the model
runs.

TODO: Policies are going to go as an argument to the optimize ()