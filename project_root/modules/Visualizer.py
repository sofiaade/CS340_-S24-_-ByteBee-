import matplotlib.pyplot as plt
import seaborn as sns

class Visualizer:
    @staticmethod
    def histogram(data, column, bins, output_path):
        plt.hist(data[column], bins=bins, alpha=0.7, color='blue')
        plt.title(f'Histogram of {column}')
        plt.xlabel(column)
        plt.ylabel('Frequency')
        plt.savefig(output_path)
        plt.close()

    @staticmethod
    def box_plot(data, column, output_path):
        sns.boxplot(x=data[column])
        plt.title(f'Box Plot of {column}')
        plt.xlabel(column)
        plt.savefig(output_path)
        plt.close()

    @staticmethod
    def scatter_plot(data, x_col, y_col, output_path):
        plt.scatter(data[x_col], data[y_col], c='green', alpha=0.5)
        plt.title(f'Scatter Plot: {x_col} vs {y_col}')
        plt.xlabel(x_col)
        plt.ylabel(y_col)
        plt.savefig(output_path)
        plt.close()

