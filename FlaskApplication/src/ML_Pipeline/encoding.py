import numpy as np
from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.base import BaseEstimator, TransformerMixin


class CategoricalEncoder(BaseEstimator, TransformerMixin):

    def __init__(self, cols=None, lcols=None, ohecols=None, tcols=None, reduce_df=False):

        if isinstance(cols, str):
            self.cols = [cols]
        else:
            self.cols = cols

        if isinstance(lcols, str):
            self.lcols = [lcols]
        else:
            self.lcols = lcols

        if isinstance(ohecols, str):
            self.ohecols = [ohecols]
        else:
            self.ohecols = ohecols

        if isinstance(tcols, str):
            self.tcols = [tcols]
        else:
            self.tcols = tcols

        self.reduce_df = reduce_df

    def fit(self, X, y):

        if self.cols is None:
            self.cols = [c for c in X if str(X[c].dtype) == 'object']

        for col in self.cols:
            if col not in X:
                raise ValueError('Column \''+col+'\' not in X')

        if self.lcols is None:
            self.lcols = [c for c in self.cols if X[c].nunique() <= 2]

        if self.ohecols is None:
            self.ohecols = [c for c in self.cols if (
                (X[c].nunique() > 2) & (X[c].nunique() <= 10))]

        if self.tcols is None:
            self.tcols = [c for c in self.cols if X[c].nunique() > 10]

        self.lmaps = dict()
        for col in self.lcols:
            self.lmaps[col] = dict(
                zip(X[col].values, X[col].astype('category').cat.codes.values))

        self.ohemaps = dict()
        for col in self.ohecols:
            self.ohemaps[col] = []
            uniques = X[col].unique()
            for unique in uniques:
                self.ohemaps[col].append(unique)
            if self.reduce_df:
                del self.ohemaps[col][-1]

        self.global_target_mean = y.mean().round(2)
        self.sum_count = dict()
        for col in self.tcols:
            self.sum_count[col] = dict()
            uniques = X[col].unique()
            for unique in uniques:
                ix = X[col] == unique
                self.sum_count[col][unique] = (y[ix].sum(), ix.sum())

        return self

    def transform(self, X, y=None):

        Xo = X.copy()

        for col, lmap in self.lmaps.items():

            Xo[col] = Xo[col].map(lmap)
            Xo[col].fillna(-1, inplace=True)

        for col, vals in self.ohemaps.items():
            for val in vals:
                new_col = col+'_'+str(val)
                Xo[new_col] = (Xo[col] == val).astype('uint8')
            del Xo[col]

        if y is None:
            for col in self.sum_count:
                vals = np.full(X.shape[0], np.nan)
                for cat, sum_count in self.sum_count[col].items():
                    vals[X[col] == cat] = (sum_count[0]/sum_count[1]).round(2)
                Xo[col] = vals
                Xo[col].fillna(self.global_target_mean, inplace=True)

        else:
            for col in self.sum_count:
                vals = np.full(X.shape[0], np.nan)
                for cat, sum_count in self.sum_count[col].items():
                    ix = X[col] == cat
                    if sum_count[1] > 1:
                        vals[ix] = ((sum_count[0]-y[ix].reshape(-1,)
                                     )/(sum_count[1]-1)).round(2)
                    else:
                        vals[ix] = ((y.sum() - y[ix]) /
                                    (X.shape[0] - 1)).round(2)

                Xo[col] = vals
                Xo[col].fillna(self.global_target_mean, inplace=True)

        return Xo

    def fit_transform(self, X, y=None):

        return self.fit(X, y).transform(X, y)
