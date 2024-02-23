from sklearn.base import BaseEstimator, TransformerMixin
import numpy as np


class AddFeatures(BaseEstimator):

    def __init__(self, eps=1e-6):

        self.eps = eps

    def fit(self, X, y=None):
        return self

    def transform(self, X):

        Xo = X.copy()
        Xo['bal_per_product'] = Xo.Balance/(Xo.NumOfProducts + self.eps)
        Xo['bal_by_est_salary'] = Xo.Balance/(Xo.EstimatedSalary + self.eps)
        Xo['tenure_age_ratio'] = Xo.Tenure/(Xo.Age + self.eps)
        Xo['age_surname_enc'] = np.sqrt(Xo.Age) * Xo.Surname

        return Xo

    def fit_transform(self, X, y=None):

        return self.fit(X, y).transform(X)
