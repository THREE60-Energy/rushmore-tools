def read_test_data(report_name: str):
    with open(f"test_data//{report_name.lower()}_dump.txt") as f:
        data = f.read()
    return list(eval(data))
