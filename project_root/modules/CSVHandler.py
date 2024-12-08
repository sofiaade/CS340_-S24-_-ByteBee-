# CSVHandler.py

import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
from modules.BaseHandler import BaseHandler

class CSVHandler(BaseHandler):
    """Handles CSV file operations."""
    #

    def read_file(self):
        """Reads a CSV file into a pandas DataFrame."""
        self.data = pd.read_csv(self.file_path)
        return self.data
        #

    def visualize(self, column, plot_type='histogram'):
        """
        Creates a visualization for a specified column.
        Args:
            column (str): Column name to visualize.
            plot_type (str): Type of plot (e.g., 'histogram', 'box').
        """
        plt.figure(figsize=(10, 6))
        if plot_type == 'histogram':
            sns.histplot(self.data[column], kde=False)
        elif plot_type == 'box':
            sns.boxplot(y=self.data[column])
        else:
            raise ValueError(f"Unsupported plot type: {plot_type}")

        plt.title(f"{plot_type.capitalize()} of {column}")
        plt.savefig(f"{self.config['output_folder']}/{column}_{plot_type}.png")
        plt.close()

#
