from sklearn.pipeline import Pipeline
from lightgbm import LGBMClassifier
from ML_Pipeline.feature_eng import AddFeatures
from ML_Pipeline.scaler import CustomScaler
from ML_Pipeline.encoding import CategoricalEncoder


lgb = LGBMClassifier(boosting_type='dart', min_child_samples=20,
                     n_jobs=- 1, importance_type='gain', num_leaves=31)
model = Pipeline(steps=[('categorical_encoding', CategoricalEncoder()),
                        ('add_new_features', AddFeatures()),
                        ('classifier', lgb)
                        ])


parameters = {'classifier__n_estimators': [201], 'classifier__max_depth': [6], 'classifier__num_leaves': [63], 'classifier__learning_rate': [0.1], 'classifier__colsample_bytree': [0.6, 0.8], 'classifier__reg_alpha': [0, 1, 10], 'classifier__reg_lambda': [0.1, 1, 5], 'classifier__class_weight': [{0: 1, 1: 3.0}]
              }
