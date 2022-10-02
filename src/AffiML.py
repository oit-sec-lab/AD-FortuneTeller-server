import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
import optuna.integration.lightgbm as lgb
import createCSV

# dataset
df = pd.read_csv("data/csv/result.csv")

# id,url,domain,network,extend,regex1,regex2,regex3,regex4,regex5,virustotal,isaffi
X = df[["domain", "network", "extend", "regex1", "regex2", "regex3", "regex4", "regex5", "virustotal"]]
y = df["isaffi"]

# split
X_train,X_test,y_train,y_test = train_test_split(X,y, test_size=0.3, shuffle=True, random_state=3)

# make Dataset
lgb_train = lgb.Dataset(X_train, y_train)
lgb_eval = lgb.Dataset(X_test, y_test, reference=lgb_train)

# param
params = {
    'objective': 'binary',
    'metric': 'binary_logloss',
    'verbosity': -1,
}
print(df)
# train
model = lgb.train(
    params,
    lgb_train,
    valid_sets = lgb_eval,
    verbose_eval = 50,
    num_boost_round = 1000,
    early_stopping_rounds = 100
)


# save model
model.save_model('model/model.h5')

# predict
y_pred = model.predict(X_test, num_iteration=model.best_iteration)

#bst = lgb.Booster(model_file='model.h5')
#ypred = bst.predict(X_test, num_iteration=bst.best_iteration)

# clamp 0 1
y_pred = np.where(y_pred > 0.5, 1, 0)
print(y_pred)

from sklearn.metrics import accuracy_score
acc = accuracy_score(y_test, y_pred)
print(acc)