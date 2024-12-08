import logging
from modules.DataFrameHandler import CSVDataHandler, PickleDataHandler
from modules.ProbabilityCalculator import ProbabilityCalculator
from modules.VectorOperations import VectorOperations
from modules.Visualizer import Visualizer
from Config import CONFIG

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    logging.info("Starting the application")

    # Read CSV data
    csv_handler = CSVDataHandler(CONFIG["input_csv"])
    df = csv_handler.load_data()
    logging.info("Loaded CSV data")

    # Read pickle data
    pickle_handler = PickleDataHandler(CONFIG["input_pickle"])
    data_from_pickle = pickle_handler.load_data()
    logging.info("Loaded Pickle data")

    # Probability calculations
    prob_calc = ProbabilityCalculator(df)
    prob_calc.calculate_and_export()

    # Visualize Attendance Rates (e.g., Histogram, Box plot)
    visualizer = Visualizer()
    visualizer.histogram(df, '2021-2022 attendance rate - year to date', 20, "Output/histogram.png")
    visualizer.box_plot(df, '2021-2022 attendance rate - year to date', "Output/boxplot.png")

    # Vector operations (if needed)
    vector_ops = VectorOperations()
    vector_ops.demo_operations()

if __name__ == "__main__":
    main()

