import pickle
from pandas import DataFrame
import matplotlib.pyplot as plt
import seaborn as sns
from .ProbabilityCalculator import ProbabilityCalculator

class PickleHandler(ProbabilityCalculator):
    """Handles data processing and statistical analysis for Pickle files."""

    def __init__(self, config, file_path):
        """
        Initializes the class with configuration constants and file path.
        Args:
            config (dict): Configuration dictionary.
            file_path (str): Path to the Pickle file.
        """
        super().__init__(config)
        self.file_path = file_path
        self.data = None

    def read_file(self):
        """
        Reads data from a Pickle file.
        Returns:
            DataFrame: Data loaded from the Pickle file.
        """
        with open(self.file_path, "rb") as f:
            self.data = pickle.load(f)
       
        if not isinstance(self.data, DataFrame):
            raise TypeError("Data loaded from Pickle must be a pandas DataFrame.")
       
        return self.data

    def calculate_joint_probabilities(self, data):
        """
        Calculates joint and conditional probabilities for Pickle data.
        Args:
            data (DataFrame): DataFrame containing data for probability calculations.
        Returns:
            dict: Joint probabilities for the data.
        """
        # Use super() to call the method from the parent class
        return super(PickleHandler, self).calculate_probabilities(data)


    def vector_operations(self, vector1, vector2):
        """
        Performs vector operations specific to statistical analysis.
        Args:
            vector1 (list): First vector.
            vector2 (list): Second vector.
        Returns:
            dict: Results of vector operations.
        """
        return super().vector_operations(vector1, vector2)

    def visualize_data(self, column, plot_type='histogram'):
        """
        Generates visualizations for a specified column in the data.
        Args:
            column (str): Column name to visualize.
            plot_type (str): Type of plot (e.g., histogram, box).
        """
        if column not in self.data.columns:
            raise KeyError(f"Column '{column}' not found in the data.")
       
        plt.figure(figsize=(10, 6))
        if plot_type == 'histogram':
            sns.histplot(self.data[column], kde=False)
        elif plot_type == 'box':
            sns.boxplot(y=self.data[column])
        else:
            raise ValueError(f"Unsupported plot type: {plot_type}")
       
        plt.title(f"{plot_type.capitalize()} Plot of {column}")
        plt.savefig(f"{self.config['output_folder']}/{column}_{plot_type}.png")
        plt.close()

