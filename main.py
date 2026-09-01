import pandas as pd


def generate_report(file_path):
    data = pd.read_csv(file_path)

    report = {
        "total_sales": data["sales"].sum(),
        "total_customers": data["customers"].sum(),
        "best_product": data.loc[data["sales"].idxmax(), "product"]
    }

    return report


if __name__ == "__main__":
    report = generate_report("data.csv")

    print("AI Business Report")
    print("----------------")
    print(f"Total Sales: ${report['total_sales']}")
    print(f"Total Customers: {report['total_customers']}")
    print(f"Top Product: {report['best_product']}")
