import pandas as pd
import logging

class ProbabilityCalculator:
    def __init__(self, df):
        self.df = df

    def calculate_and_export(self):
        # Validate required columns
        required_columns = ['District name', 'Category', 'Student group', '2021-2022 attendance rate - year to date']
        missing_columns = [col for col in required_columns if col not in self.df.columns]

        if missing_columns:
            logging.error(f"Missing required columns: {missing_columns}")
            return

        # Calculate joint counts and probabilities
        joint_counts = self.df.groupby(['District name', 'Category', 'Student group']).size()
        joint_probabilities = joint_counts / len(self.df)

        # Attendance rate calculations for 2021-2022
        attendance_rate_2021 = self.df['2021-2022 attendance rate - year to date']
        mean_attendance = attendance_rate_2021.mean()
        median_attendance = attendance_rate_2021.median()
        std_dev_attendance = attendance_rate_2021.std()

        logging.info(f"Joint Probabilities: {joint_probabilities}")
        logging.info(f"2021-2022 Attendance Rate - Mean: {mean_attendance}, Median: {median_attendance}, Std Dev: {std_dev_attendance}")

        joint_probabilities.to_csv("Output/joint_probabilities.csv")

        # Save statistical results
        statistics = pd.DataFrame({
            'Mean Attendance Rate': [mean_attendance],
            'Median Attendance Rate': [median_attendance],
            'Std Dev Attendance Rate': [std_dev_attendance]
        })
        statistics.to_csv("Output/statistics.csv")

