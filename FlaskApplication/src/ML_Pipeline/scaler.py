from sklearn.base import BaseEstimator, TransformerMixin
import numpy as np


class CustomScaler(BaseEstimator, TransformerMixin):

    def __init__(self, scale_cols=None):

        self.scale_cols = scale_cols

    def fit(self, X, y=None):

        if self.scale_cols is None:
            self.scale_cols = [c for c in X if ((str(X[c].dtype).find(
                'float') != -1) or (str(X[c].dtype).find('int') != -1))]

        self.maps = dict()
        for col in self.scale_cols:
            self.maps[col] = dict()
            self.maps[col]['mean'] = np.mean(X[col].values).round(2)
            self.maps[col]['std_dev'] = np.std(X[col].values).round(2)

        return self

    def transform(self, X):

        Xo = X.copy()

        for col in self.scale_cols:
            Xo[col] = (Xo[col] - self.maps[col]['mean']) / \
                self.maps[col]['std_dev']

        return Xo

    def fit_transform(self, X, y=None):

        return self.fit(X).transform(X)
