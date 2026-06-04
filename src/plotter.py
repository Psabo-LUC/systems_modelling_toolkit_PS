import pandas as pd
import matplotlib.pyplot as plt

def doit(df, save_path="./figure.png"):
  # The first column is the time steps, but it's missing a header name in the CSV.
  # We will rename it to 'Time' and set it as the index.
  df.rename(columns={df.columns[0]: 'Time'}, inplace=True)
  df.set_index('Time', inplace=True)

  # 2. Select which substrates you actually want to see. 
  # (Plotting all 16 at once gets messy, so specify the key ones here)
  substrates_to_plot = ["A", "B", "C", "Stim"]

  # 3. Create the plot
  plt.figure(figsize=(8, 5))
  for substrate in substrates_to_plot:
      if substrate in df.columns:
          plt.plot(df.index, df[substrate], label=substrate)

  # 4. Format it exactly like the author's internal network.py grapher
  plt.xlabel("Time (mins)", fontsize=12)
  plt.ylabel("Concentration (AU)", fontsize=12)
  plt.legend(loc="upper right", fontsize=10)
  plt.title("Pathway Activation Over Time")

  # Save and show
  plt.tight_layout()
  plt.savefig(save_path, dpi=300)
  print("Saved plot to figure.png")


if __name__ == "__main__":
  # 1. Load the CSV
  csv_path = "../outputs/ex.csv"  # Change this to your CSV path
  df = pd.read_csv(csv_path)
  doit(df)




