
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error
import numpy as np

def last_og_forbered_data(file_path, temp_col):
    df = pd.read_csv("trondheim_vaerdata_full.csv", parse_dates = ['Tidspunkt'])

    #Ekstraherer året og dagen i året fra datoen
    df['year'] = df['Tidspunkt'].dt.year 
    df['day_of_year'] = df['Tidspunkt'].dt.dayofyear 
    #Håndterer manlende verdier
    #Interpolerer manglende temperaturverdier (Legger inn nærliggende verdier)
    df[temp_col] = df[temp_col].interpolate() 

    #Fjerner rader hvor temperaturen fortsatt er NaN etter interpolasjon
    df = df.dropna(subset=[temp_col]) 
    return df

 
def vis_tidsserie(df, x_col, y_col, tittel, y_label):
    #Visualiserer Temperatur over tid
    plt.figure(figsize=(12, 4)) 
    sns.lineplot(data=df, x=x_col, y=y_col) 
    plt.title(tittel) 
    plt.xlabel("Dato") 
    plt.ylabel(y_label) 
    plt.tight_layout() 
    plt.show() 

 
def vis_nedbør_søyler(df, dato_col, nedbor_col, intervall = 'M', tittel = 'Nedbør over tid', y_label = 'Nedbør (mm)'):
#Visualiserer månedlig nedbør i søylediagram
    nedbor = df.resample(intervall, on = dato_col).sum(numeric_only = True) 
    plt.figure(figsize=(10, 4)) 
    nedbor[nedbor_col].plot(kind='bar') 
    plt.title(tittel) 
    plt.ylabel(y_label) 
    plt.tight_layout() 
    plt.show() 

 
def vis_scatter(df, x_col, y_col, tittel, x_label, y_label):
#Visualiserer Temperatur vs Nedbør i scatterplot
    plt.figure(figsize=(8, 5)) 
    sns.scatterplot(data=df, x=x_col, y=y_col, alpha=0.5) 
    plt.title(tittel) 
    plt.xlabel(x_label) 
    plt.ylabel(y_label) 
    plt.tight_layout() 
    plt.show() 

 
#Modelltrening
def tren_og_evaluer_modell(df, temp_col):
    features = df[['year', 'day_of_year']] 
    target = df[temp_col] 

    #Deler opp datasettet
    #Trener modellen på data fra 2025
    #Tester modellen på temperaturene for 2025
    X_train = features[df['year'] < 2025] 
    X_test = features[df['year'] == 2025] 
    y_train = target[df['year'] < 2025] 
    y_test = target[df['year'] == 2025] 

    #Initialiserer og trener en lineær regresjonsmodell
    model = LinearRegression() 
    model.fit(X_train, y_train) 
    #Evaluerer modellen på testdata (2025)
    y_pred = model.predict(X_test) 

    #Beregmer feil mål
    print("MAE:", mean_absolute_error(y_test, y_pred)) 
    print("RMSE:", np.sqrt(mean_squared_error(y_test, y_pred))) 

    return model

 
#Predikasjon for 2026
def prediker_for_aar(model, aar, skuddaar = False):
    dager = 366 if skuddaar else 365
    future = pd.DataFrame({ 
        'year': [aar] * dager, 
        'day_of_year': list(range(1, dager + 1)) 
}) 
    #Bruker modellen til å forutsi temperaturene for 2026
    future['predicted_temperature'] = model.predict(future) 
    

    #Visualisering av prediksjonen 
    plt.figure(figsize=(10, 4)) 
    plt.plot(future['day_of_year'], future['predicted_temperature']) 
    plt.title("Forventet daglig temperatur i {aar} (lineær regresjon)") 
    plt.xlabel("Dag i året") 
    plt.ylabel("Predikert temperatur (°C)") 
    plt.tight_layout() 
    plt.show()



#Predikasjon
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

def prediker_daglig_variable(
    df,
    variabel,
    label,
    prediksjonsår=2026,
    farge="darkred",
    plot=True
):
    #Gjør dag for dag lineær regresjon på gitt variabel og predikerer for et nytt år
    prediksjoner = []

    for day in range(1, 367):  # Inkluderer skuddårsdager
        df_day = df[df['day_of_year'] == day]

        if df_day['year'].nunique() < 2:
            continue

        X = df_day[['year']]
        y = df_day[variabel]

        model = LinearRegression()
        model.fit(X, y)

        pred = model.predict(pd.DataFrame({'year': [prediksjonsår]}))[0]
        prediksjoner.append((day, pred))

    df_pred = pd.DataFrame(prediksjoner, columns=['day_of_year', label])
    df_pred['date'] = pd.to_datetime(f"{prediksjonsår}-01-01") + pd.to_timedelta(df_pred['day_of_year'] - 1, unit='D')

    if plot:
        plt.figure(figsize=(14, 5))
        plt.plot(df_pred['date'], df_pred[label], 'o-', color=farge, label=label)
        plt.title(f"Daglig predikert {label.lower()} for {prediksjonsår}")
        plt.xlabel("Dato")
        plt.ylabel(label)
        plt.grid(True)
        plt.legend()
        plt.tight_layout()
        plt.show()

    return df_pred


