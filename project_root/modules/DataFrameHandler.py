import pandas as pd
import logging

class DataHandler:
    def __init__(self, file_path):
        self.file_path = file_path

    def load_data(self):
        raise NotImplementedError("This method should be overridden in child classes")

class CSVDataHandler(DataHandler):
    def load_data(self):
        try:
            data = pd.read_csv(self.file_path)
            logging.info("CSV data loaded successfully")
            return data
        except Exception as e:
            logging.error(f"Error loading CSV: {e}")
            raise

class PickleDataHandler(DataHandler):
    def load_data(self):
        try:
            data = pd.read_pickle(self.file_path)
            logging.info("Pickle data loaded successfully")
            return data
        except Exception as e:
            logging.error(f"Error loading Pickle file: {e}")
            raise

