import optuna.integration.lightgbm as lgb
import numpy as np
import createCSV

def load_model():
    bst = lgb.Booster(model_file='model/model.h5')
    return bst

def predict(data):
    # load model
    bst = load_model()
    # predict
    y_pred = bst.predict(data, num_iteration=bst.best_iteration)
    # clamp 0 1
    y_pred = np.where(y_pred > 0.5, 1, 0)
    return y_pred

def main():
    print(createCSV.results)
    
if __name__ == '__main__':
    main()