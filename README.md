Fork of Rohan's code. 

To run an interactive example in collab:
* Select [interactive.ipynb](https://github.com/huskeypm/systems_modelling_toolkit/blob/main/interactive.ipynb)
* Click its [Open in Colab](https://colab.research.google.com/github/huskeypm/systems_modelling_toolkit/blob/main/interactive.ipynb) button
  
.ipynb notes:
- This script is built to read from and write to .csv/.json files. When troubleshooting or tweaking parameters for this model, the easiest way of doing so is to open the .csv files and edit them manually. However, if you try to do this editing inside of google sheets, it will NOT work due to google changing the file type upon being opened in google sheets. If you do end up opening the file in google sheets and making an edit, you will need to download said file as a .csv, and re-upload it to the drive for the colab script to recognize it.
- The easiest way to use the .ipynb scripts is to run them in a Jupyter Notebook. If you are logged into any of the workstations on campus, opening a terminal and typing "jupyter notebook" should open a session inside your web browser. Since the jupyter notebook pulls from the files local to your machine, you can edit the .csv files however you like, as long as the data structure and file type remain the same. 

In progress:
* `myrun.py` gives an example run
* `myplot.py` plots those data

Notes:
* fitting is disabled at the moment







Python notes:

- The setup.sh and requirements.txt files should have everything that is needed to construct your coding environment. 

Model Example Tutorial:

<img width="722" height="168" alt="Untitled Diagram drawio(2)" src="https://github.com/user-attachments/assets/02f0f8be-b9e5-4fca-b209-7fcd4dea2035" />

The base functionality of this code model has three input files that the user can manipulate. 

- substrate.csv

- interactions.csv 

- rates.csv

For each of these, I will explain what inputs are needed to model the above system and roughly what each input means. The names of these files can be changed, just ensure that your script is pointing to the correct file location when you run the model 

 -substrate.csv-
 <img width="1017" height="184" alt="image" src="https://github.com/user-attachments/assets/7997262b-ff90-4f58-9194-c4c361093e32" />

Within this csv, you will define each of your species terms amongst a few others. 
- The first column of the csv must contain the index of the substrates.
- "name" column contains the reaction species
- "initial_value" defines the initial conditions used to solve the ODE function. Can be left as 0 but can also be assigned an exact value if the starting amount of said substrate is known.
  
- "substrate_type" which can be defined as:
  - "enzyme" if that species has reversible kinetics
  - "Stimulus" if that species is acting as a reaction driver or inhibitor
  - "receptor" TBD
  - "other" TBD
  
- "activation_rate" is essentially the rate of generation of a species within an equilibrium reaction.
- "deactivation_rate" is essentially the rate of degradation of a species within an equilibrium reaction.

  
- Note: The above two terms can be thought about in two ways

   * A. if the (activation_rate)/(deactivation_rate) is greater than 1, the forward reaction will be favored. If (activation_rate)/(deactivation_rate) is less than 1, the reverse reaction will be favored.  
   * B. Lets say you have a stimulant species "Stim" that acts on a system like the model above. If you wanted said species to be added into the system gradually, you can define a term under the "activation_rate" column that will modulate the addition of that species into the system. The same paradigm is true for a stimulus that gradually decays, except you would define a term under "deactivation_rate". If you want the stimulus to be added/removed from your system instantaneously, leave one or both terms blank.

- "total_amt" refers to the total amount of that species in the system. This term comes in handy when you are working with multiple forms of the same species and want to constrain the total summed quantity of all forms of that species to a total amount.
- "other_state" is where you would input an alternative form of a species. For example, a phosphorylated version of the base species.
- "active_time_ranges" defines the time ranges for which each species is active. If a species is set to be of substrate_type stimulus, then you MUST define an active time range for that species. If that entry is left empty, the script will assume that species is active across the entire simulation time. 

 -interactions.csv-
 <img width="446" height="165" alt="image" src="https://github.com/user-attachments/assets/60626ada-f6ff-4fa4-a9f2-11056665594f" />

Within this csv, you will define how each species interacts with each other among a few other things. 
- The first column of the csv must contain the index of the substrates.
- "name" column contains the interaction name
- "resultant" states what species is generated or consumed when applied a driving force(stimulus)
- "stimulus" states which species acts as the driver for the generation or consumption of the resultant
- "rate" defines a coeffiencent representing the rate of the driving/inhibiting reaction defined be the resultant and stimulus on the same row
- "effect" is defined as either "-1" or "+1", where the sign indicates whether the resultant is consumed/inhibited (-1) or generated (+1) as a result of the driver.
- "Kd and n" are the coefficients of the Hill function. If these entries are NOT blank, Hill mechanics will be applied to that reaction


 -rates.csv-
 <img width="585" height="361" alt="image" src="https://github.com/user-attachments/assets/51b1653e-7d6d-4596-b2da-96ae8fe4d7ab" />

This csv is where you will define the boundaries of all the individual reaction coefficients listed in the other files. However, it also contains fitting constraints for the fitting portion of this code (tutorial coming soon)
- The first column of the csv must contain the index of each rate coefficient
- the "name" column should contain all of your coefficients defined in both substrates.csv and interactions.csv
- the "value" column contains temporary variables for those coefficients
~~columns past this point are only really relevent to the fitting code 
- "lower_bound" is the lower boundary of possible values that the coefficient can be when being fitted to data.
- "upper_bound" is the upper boundary of possible values that the coefficient can be when being fitted to data.
- "bound_type" tells the fitting code if that coefficient is a real number or an integer
- "fixed" is either True (the coefficient is fixed to entry in the "value" column of the same row) or False





More to come...







