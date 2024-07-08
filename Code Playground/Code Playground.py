import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("number" , help = "first number")
    parser.add_argument("operation" , choices=["hi"])
    args = parser.parse_args()