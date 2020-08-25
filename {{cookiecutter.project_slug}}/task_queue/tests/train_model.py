from sklearn.linear_model import Ridge
from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error
from joblib import dump
import pandas as pd
import numpy as np
import logging

logging.basicConfig(
    format="%(levelname)s: %(message)s", 
    level=logging.INFO
)


class Model:
    model = None
    X_train = None
    X_test = None
    y_train = None
    y_test = None

    def train_model(self):
        df: pd.DataFrame = pd.DataFrame({
            "a": np.random.rand(500) * 10,
            "b": np.random.rand(500) * 5,
            "c": np.random.rand(500) * 2,
            "y": np.random.rand(500) * 50
        })

        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            df[[col for col in df.columns if col != "y"]], df.y
        )

        self.model = XGBRegressor()

        self.model.fit(self.X_train, self.y_train)

    def score_model(self):
        predictions = self.model.predict(self.X_test)
        score = mean_squared_error(self.y_test, predictions)
        logging.info(f"Model score: {score:.2}")

    def save_model(self):
        dump(self.model, "./model.joblib")


def main():
    model = Model()
    model.train_model()
    model.score_model()
    model.save_model()


if __name__ == "__main__":
    main()

