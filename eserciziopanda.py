import pandas as pd


#leggo il csv per importare il dataset
df=pd.read_csv("file.csv")

#creo la funzione raggruppamento per raggruppare delle informazioni
gruppo = df.groupby(["Data", "Filiale"]).mean
#calcolo la media delle vendite giornaliere per filiale
media= gruppo["Vendite"].mean().reset_index()
#calcolo quale filiale ha venduto di più
vendita_massima = media.groupby("Filiale")["Vendite"].max()
#stampo tutto nel file csv
media.to_csv("media_vendite_per_filiale.csv", index=False) 
vendita_massima.to_csv("massimo_vendite_per_filiale.csv", header=["Vendite_max"])
