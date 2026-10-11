import matplotlib.pyplot as plt

def test_matplotlib():
    plt.plot([1, 2, 3], [4, 5, 6])
    plt.savefig("test_plot.png")
    plt.close()
    print("matplotlib: Побудовано та збережено графік 'test_plot.png'")