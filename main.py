import pandas as pd


def analyze_business_data(file_path):
    data = pd.read_csv(file_path)

    report = {
        "total_records": len(data),
        "columns": list(data.columns),
        "summary": data.describe().to_dict()
    }

    return report


if __name__ == "__main__":
    result = analyze_business_data("data.csv")

    print("Business Report Generated")
    print(result)
