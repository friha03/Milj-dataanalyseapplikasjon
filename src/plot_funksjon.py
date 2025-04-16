import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd

#2D plots
def plott_smart_scatter_2D(
    df,
    x_col,
    y_col,
    color_col,
    x_label,
    y_label,
    title,
    colorbar_label="",
    text_labels_col=None,
    size=80
):
    plt.figure(figsize=(10, 6))
    scatter = plt.scatter(
        df[x_col],
        df[y_col],
        c=df[color_col],
        cmap="coolwarm",
        s=size,
        edgecolors="k"
    )

    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.colorbar(label=colorbar_label)
    plt.grid(True)

    if text_labels_col:
        for i, row in df.iterrows():
            plt.text(row[x_col], row[y_col], str(row[text_labels_col].strftime("%Y-%m-%d")), fontsize=9, ha="right", va="bottom")

    plt.tight_layout()
    plt.show()




#3D plots
def plott_smart_scatter_3D(
    df,
    x_col,
    y_col,
    z_col,
    dato_col,
    x_label,
    y_label,
    z_label,
    title,
    colorbar_label="Nedbør (mm)",
    farge_kart="plasma",
    prikk_str=120
):
    # Konverter dato
    df[dato_col] = pd.to_datetime(df[dato_col])
    labels = df[dato_col].dt.strftime("%Y-%m-%d")

    # Verdier til plottet
    x = df[x_col]
    y = df[y_col]
    z = df[z_col]

    # Plottet
    fig = plt.figure(figsize=(12, 8))
    ax = fig.add_subplot(111, projection='3d')

    scatter = ax.scatter(
        x, y, z,
        c=z,
        cmap=farge_kart,
        s=prikk_str,
        edgecolors="black",
        linewidths=0.7
    )

    # Legg til datomerking på punktene
    for i in range(len(df)):
        ax.text(x.iloc[i], y.iloc[i], z.iloc[i], labels.iloc[i], size=7, zorder=1)

    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.set_zlabel(z_label)
    ax.set_title(title)

    fig.colorbar(scatter, label=colorbar_label)

    plt.tight_layout()
    plt.show()

def opprett_liste_over_fire_subplots():
    plot_configuration = [
    { 
        "y_col" : "Temperatur (°C)", 
        "y_label" : "Temperatur (°C)", 
        "title" : "Temperatur over tid",
        "farge" : "blue", 
        "subplot_index" : (2, 2, 1)
    },
    {   
        "y_col" : "Vindhastighet (km/t)", 
        "y_label" : "Vindhastighet (km/t)", 
        "title" : "Vindhastighet over tid",
        "farge" : "red", 
        "subplot_index" : (2, 2, 2)
    },
    {
        "y_col" : "Trykk", 
        "y_label" : "Trykk (Pa)", 
        "title" : "Trykk over tid",
        "farge" : "green", 
        "subplot_index" : (2, 2, 3)
    },
    {
        "y_col" : "Nedbør (mm)", 
        "y_label" : "Nedbør (mm)", 
        "title" : "Nedbør over tid",
        "farge" : "purple", 
        "subplot_index" : (2, 2, 4)
    }
    ]

    plt.figure(figsize=(12, 10))
    
    return plot_configuration


#Generelle plots
def forenklet_plot_funksjon(
    df,
    x_col,
    y_col,
    subplot_index,
    x_label,
    y_label,
    title, 
    farge,
    marker = "o", 
    linestyle = "-",
    xticks_rotation = 45,
    plot_type = "line"
):
    plt.subplot(*subplot_index)

    if plot_type == "scatter":
        plt.scatter(df[x_col], df[y_col], color = farge, marker = marker)
    else: 
        plt.plot(df[x_col], df[y_col], color = farge, marker=marker, linestyle=linestyle)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.xticks(rotation = xticks_rotation)

