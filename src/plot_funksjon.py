import matplotlib.pyplot as plt

def plott_smart_scatter(
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




