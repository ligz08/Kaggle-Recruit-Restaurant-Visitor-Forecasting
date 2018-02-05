import xgboost as xgb
from bayes_opt import BayesianOptimization
import pandas as pd
import numpy as np





class XGB_Tuner:
    def __init__(self, params_range, train_dmatrix, val_dmatrix):
        self.tuned = False
        self.params_range = params_range
        self.optimizer = None
        self.tuned_params = None
        self.train_dmatrix = train_dmatrix
        self.val_dmatrix = val_dmatrix

    def xgb_evaluate(self, min_child_weight, colsample_bytree, max_depth, subsample, gamma):
        params = {
            'objective': 'reg:linear',
            'eta': 0.1,
            'seed': 2018,
            'max_depth': int(max_depth),
            'min_child_weight': int(min_child_weight),
            'colsample_bytree': colsample_bytree,
            'subsample': subsample,
            'gamma': gamma
        }

        eval_setting = [(self.train_dmatrix, 'train'), (self.val_dmatrix, 'eval')]

        m = xgb.train(params=params,
                      dtrain=self.train_dmatrix,
                      num_boost_round=100000,
                      evals=eval_setting,
                      early_stopping_rounds=50,
                      verbose_eval=False
                      )

        best_score = m.best_score
        return -best_score



    def tune(self, init_points=8, n_iter=42):
        self.optimizer = BayesianOptimization(f=self.xgb_evaluate, pbounds=self.params_range, verbose=0)
        self.optimizer.maximize(init_points, n_iter)

        params_table = pd.DataFrame(self.optimizer.res['all']['params'])
        params_table['score'] = np.negative(self.optimizer.res['all']['values'])
        params_table.sort_values(by='score', inplace=True)

        self.tuned_params = params_table.loc[0,:].drop('score').to_dict()
        for int_param in ['max_depth', 'min_child_weight']:
            if int_param in self.tuned_params:
                self.tuned_params[int_param] = int(self.tuned_params[int_param])

        self.tuned = True

    def get_tuned_params(self, init_points=8, n_iter=42):
        if not self.tuned:
            self.tune(init_points, n_iter)

        return self.tuned_params
