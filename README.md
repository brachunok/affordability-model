# affordability-model
Sociohydrological Water Affordable Model

# What do


# Structure
* Code is where the actual code goes
* Data is where any input data goes
* Outputs is where intermediate code outputs and model runs go
* Analysis is where scripts which analyze outputs, make plots etc.. go

## Code

## Data
Data contains the files with inflow data for each source defined in the model.
Each inflow file must be a csv, with the first column as a series of dates formatted
YYYY-MM-DD, then subsequent columns are inflow values for these dates.
All dates have to match across inflow files. Each column after date represents
a drought scenario. All inflow files must have the same number of drought scenarios
and an error should pop up if that's not the case.

The length of the simulation (e.g. the number of time periods), the time-resolution of the simulation,
(e.g. whether it's a monthly or yearly time step), and the number of drought scenarios to test are
all determined by these input files.



## Config files
The configuration file is what passes all the important parameters to the model.

#### Rates
Rates are specified in 3 parts: fixed costs, tier prices, and tiers.

