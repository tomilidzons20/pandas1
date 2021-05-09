import numpy as np
import pandas as pd
import xlrd
import openpyxl

# Zad1
# Wczytaj do DataFrame arkusz z narodzinami dzieci w Polsce
# dostępny w pliku /datasets/imiona.xlsx

imiona = pd.ExcelFile("imiona.xlsx")
df = pd.read_excel(imiona, header=0)
print("Zad1")
print(df)

# Zad2
# Z danych z zadania 1 wyświetl (korzystając w miarę możliwości z funkcji biblioteki Pandas):
# tylko te rekordy gdzie liczba nadanych imion była większa niż 1000 w danym roku
# tylko rekordy gdzie nadane imię jest takie jak Twoje
# sumę wszystkich urodzonych dzieci w całym danym okresie,
# sumę dzieci urodzonych w latach 2000-2005
# sumę urodzonych chłopców i dziewczynek
# najbardziej popularne imię dziewczynki i chłopca w danym roku ( czyli po 2 rekordy na rok),
# najbardziej popularne imię dziewczynki i chłopca w całym danym okresie,

print("\nZad2")
print("pkt. 1")
print(df[df["Liczba"] > 1000])
print("\npkt. 2")
print(df.loc[df["Imie"] == "JAKUB"])
print("\npkt. 3")
print(df["Liczba"].sum())
print("\npkt. 4")
print(df.loc[(df["Rok"] <= 2005) & (df["Rok"] >= 2000), "Liczba"].sum())
print("\npkt. 5")
print("Chlopcy =", df.loc[df["Plec"] == "M", "Liczba"].sum())
print("Dziewczyny =", df.loc[df["Plec"] == "K", "Liczba"].sum())
print("\npkt. 6")
ch = df.loc[df["Plec"] == "M"]
popch = ch.loc[ch.groupby("Rok")["Liczba"].idxmax()]
dz = df.loc[df["Plec"] == "K"]
popdz = dz.loc[dz.groupby("Rok")["Liczba"].idxmax()]
chdz = pd.concat([popch, popdz])
print(chdz.sort_values(by="Rok"))
print("\npkt. 7")
wch = ch[ch["Liczba"] == ch["Liczba"].max()]
wdz = dz[dz["Liczba"] == dz["Liczba"].max()]
print(pd.concat([wch, wdz]))

# Zad3
# Wczytaj plik /datasets/zamowieniana.csv a następnie wyświetl:
# listę unikalnych nazwisk sprzedawców (przetwarzając zwróconą pojedynczą kolumnę z DataFrame)
# 5 najwyższych wartości zamówień
# ilość zamówień złożonych przez każdego sprzedawcę
# sumę zamówień dla każdego kraju
# sumę zamówień dla roku 2005, dla sprzedawców z Polski
# średnią kwotę zamówienia w 2004 roku,
# zapisz dane za 2004 rok do pliku zamówienia_2004.csv a dane za 2005 do pliku zamówienia_2005.csv

df = pd.read_csv("zamowienia.csv", header=0, sep=";", decimal=".")
df["Data zamowienia"] = pd.to_datetime(df["Data zamowienia"])
print("\nZad3")
print("pkt. 1")
print(df["Sprzedawca"].unique())
print("\npkt. 2")
print(df.sort_values(by=["Utarg"], ascending=False).head(5))
print("\npkt. 3")
print(df.groupby("Sprzedawca")["idZamowienia"].nunique())
print("\npkt. 4")
print(df.groupby("Kraj")["idZamowienia"].nunique())
print("\npkt. 5")
p5 = df.loc[(df["Kraj"] == "Polska") & (df["Data zamowienia"].dt.year == 2004)]
print(p5["idZamowienia"].nunique())
print("\npkt. 6")
p6 = df.loc[df["Data zamowienia"].dt.year == 2004]
print("Srednia dla roku 2004 =", round(p6["Utarg"].mean(), 2))
print("\npkt. 7")
p6.to_csv("zamowienia_2004.csv", index=False, header=0, sep=";")
p7 = df.loc[df["Data zamowienia"].dt.year == 2005]
p7.to_csv("zamowienia_2005.csv", index=False, header=0, sep=";")
