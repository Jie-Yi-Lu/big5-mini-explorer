import pandas as pd
import matplotlib.pyplot as plt


def plot_age_distribution(csv_path: str, output_path: str | None = None) -> None:
    df = pd.read_csv(csv_path, sep="\t", usecols=["age"])

    # Drop clearly invalid ages (0 or implausibly large)
    age = df["age"][(df["age"] >= 10) & (df["age"] <= 100)]

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.hist(age, bins=range(10, 101, 2), color="#4C72B0", edgecolor="white", linewidth=0.4)
    ax.set_title("Age Distribution of BIG5 Respondents", fontsize=14)
    ax.set_xlabel("Age")
    ax.set_ylabel("Count")
    ax.set_xlim(10, 100)
    fig.tight_layout()

    if output_path:
        fig.savefig(output_path, dpi=150)
        print(f"Saved to {output_path}")
    else:
        plt.show()


if __name__ == "__main__":
    plot_age_distribution(
        csv_path="data/raw/BIG5/data.csv",
        output_path="reports/age_distribution.png",
    )
