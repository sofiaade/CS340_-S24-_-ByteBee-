import numpy as np
import logging

class VectorOperations:
    @staticmethod
    def dot_product(vec1, vec2):
        return np.dot(vec1, vec2)

    @staticmethod
    def angle_between(vec1, vec2):
        dot_prod = np.dot(vec1, vec2)
        magnitude = np.linalg.norm(vec1) * np.linalg.norm(vec2)
        return np.arccos(dot_prod / magnitude)

    @staticmethod
    def demo_operations():
        vec1 = np.array([1, 2, 3])
        vec2 = np.array([4, 5, 6])

        logging.info(f"Dot Product: {VectorOperations.dot_product(vec1, vec2)}")
        logging.info(f"Angle Between Vectors: {VectorOperations.angle_between(vec1, vec2)}")

