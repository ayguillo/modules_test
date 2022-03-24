import pandas as pd

def handle(req) :
    filename = req("file")
    df = pd.read_csv(filename)
    return {
        "dataframe" : df
    }