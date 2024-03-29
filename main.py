# -*- coding: utf-8 -*-
"""main.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1dBbl13dlIWYXoi1YykI5sxWBWF4urp45
"""

from preprocess import *
from embeddings import *
from modelling.modelling import *
from modelling.data_model import *
import random
seed =0
random.seed(seed)
np.random.seed(seed)


def load_data():
    #load the input data
    df = get_input_data()
    return  df

def preprocess_data(df):
    # De-duplicate input data
    df =  de_duplication(df)
    # remove noise in input data
    df = noise_remover(df)
    # translate data to english
    # df[Config.TICKET_SUMMARY] = translate_to_en(df[Config.TICKET_SUMMARY].tolist())
    return df

def get_embeddings(df:pd.DataFrame):
    X = get_tfidf_embd(df)  # get tf-idf embeddings
    return X, df

# ??
# ?? WHERE DOES THIS REFERENCE?? - Answer - Data_model file
def get_data_object(X: np.ndarray, df: pd.DataFrame):
    return Data(X, df) # Data is the name of the Class in the Data Model file that called get_data_object() passes X and df to, therefore Data is an Object of type Data
#??

def perform_modelling(data: Data, df: pd.DataFrame, name):
    model_predict(data, df, name)


if __name__ == '__main__':
    # pre-processing steps
    df = load_data()
    df = preprocess_data(df)
    df[Config.INTERACTION_CONTENT] = df[Config.INTERACTION_CONTENT].values.astype('U')
    df[Config.TICKET_SUMMARY] = df[Config.TICKET_SUMMARY].values.astype('U')

    # data transformation
    #X, group_df = get_embeddings(df)
    X, df = get_embeddings(df)
    # data modelling
    data = get_data_object(X, df)
    # modelling
    perform_modelling(data, df, 'name')