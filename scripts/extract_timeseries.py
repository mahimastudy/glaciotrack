import pandas as pd
import matplotlib.pyplot as plt
import argparse

def main(file_path):
    df = pd.read_csv(file_path, parse_dates=["date"])
    df.set_index("date", inplace=True)

    plt.figure(figsize=(10,6))
    plt.plot(df.index, df["vertical_mm"], label="Vertical")
    plt.legend()
    plt.title("VLBI Vertical Displacement")
    plt.ylabel("mm")
    plt.show()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", required=True)
    args = parser.parse_args()
    main(args.file)
