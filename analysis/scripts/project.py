import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def load_and_process(url_or_path_to_csv_file):
    income = pd.read_csv("C:/Users/ongka/data301/solo-project/data/raw/raw")

    
    income = (
        pd.read_csv("C:/Users/ongka/data301/solo-project/data/raw/raw")
        .set_axis(['age','workclass','fnlwgt','education','education-num','marital-status','occupation','relationship','race','sex','capital-gain','capital-loss','hours-per-week','native-country','income'],axis=1,inplace=False)
        .replace('?',np.nan)
        .dropna()
        .replace("?",np.nan)
        .dropna()
    
    )



    income2 = (
        income
        .drop(['fnlwgt','education-num','occupation','capital-gain','capital-loss'],axis=1)
        .replace(' <=50K','0')
        .replace(' >50K','1')
    )

    return income2