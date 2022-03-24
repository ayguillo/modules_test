import pandas as pd

def handle(req) :
    filename = req["file"]
    df = pd.read_csv(filename)
    df = df[['Description', 'Categorie 2']]
    df = df[df['Categorie 2'].notna()]
    df = df[df['Description'].notna()]
    df['Description'] = df['Description'].str.lower()
    df['Categorie 2'] = df['Categorie 2'].str.lower()
    return {
        "dataframe" : df.to_csv()
    }