import numpy as np
import pandas as pd
from parse import parse_interactions, parse_substrates, parse_rates
from network import Network

# 1. Parse your baseline topology 
DATAPATH="./data/test_case/"
interactions = parse_interactions(DATAPATH + "interactions.csv")
substrates = parse_substrates(DATAPATH + "substrates.csv")
rates = parse_rates(DATAPATH + "rates.csv")

n = Network("custom_run", rates, substrates, interactions)

# 2. Load the fitted parameters (this overwrites the base rates in memory)
#n.load_adapter(DATAPATH + "adapter_expanded.json")

# 3. Setup time resolution (e.g., 1000 minutes, 10000 steps)
time = np.linspace(0, 999, num=10000)

# 4. Dial in your custom conditions
# Example: Dosing with 2.0 AU of LPS and 1.5 AU of ATP from t=0 to t=60
n.apply_stimuli(
    stimuli=["Stim"], 
    amts=[1.0], 
    time_ranges=[[120, 180]]
)

# 5. Run the ODEs
y = n.y(time, steady_state_fold_normalization=False)

# 6. Save the track and reset for the next condition
n.store_track(y, time, DATAPATH + "/output/my_custom_run.csv")
n.reset_stimuli()

for s in n.substrates.keys():
    print(f"{s} = {n.represent_rate(279, s)}")




from plotter import doit
csv_path = DATAPATH + "/output/my_custom_run.csv"
fig_sav = DATAPATH + "/output/figure.png"
df = pd.read_csv(csv_path)
doit(df, fig_sav)