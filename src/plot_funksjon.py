import matplotlib.pyplot as plt

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
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd

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



