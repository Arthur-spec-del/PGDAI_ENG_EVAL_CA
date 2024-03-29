# -*- coding: utf-8 -*-
"""random_trees_embedding.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_CYsAf-oHscDFySwmLyzgs9BUn4XoaBS
"""

# Random Trees Embedding
#from - https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html#sklearn.ensemble.RandomForestClassifier

from sklearn.ensemble import RandomForestClassifier

import numpy as np
import pandas as pd
from model.base import BaseModel
from sklearn.metrics import classification_report, confusion_matrix
from numpy import *
import random
num_folds = 0
seed =0
# Data
np.random.seed(seed)
random.seed(seed)
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
pd.set_option('display.max_colwidth', 200)


class Random_Forest_Embedding(BaseModel):
    def __init__(self,
                 model_name: str,
                 embeddings: np.ndarray,
                 y: np.ndarray) -> None:
        super(Random_Forest_Embedding, self).__init__()
        self.model_name = model_name
        self.embeddings = embeddings
        self.y = y
        #self.mdl = RandomForest(n_estimators=1000, random_state=seed, class_weight='balanced_subsample')
        self.mdl = RandomForestClassifier(max_depth=2, random_state=0)

        self.predictions = None
        self.data_transform()

    def train(self, data) -> None:
        self.mdl = self.mdl.fit(data.X_train, data.y_train)

    def predict(self, X_test: pd.Series):
        predictions = self.mdl.predict(X_test)
        self.predictions = predictions
        #self.score(X, y)
        self.coef_
        #self.intercept_
        #self.decision_function([[2., 2.]])


    def print_results(self, data):
        print(classification_report(data.y_test, self.predictions))


    def data_transform(self) -> None:
        ...