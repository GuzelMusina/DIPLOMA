import pandas as pd
import numpy as np
import lightgbm as lgb
from sklearn.model_selection import train_test_split
import gc


class FeatureSelector():

    def __init__(self, data, labels=None):

        # Dataset and optional training labels
        self.data = data
        self.labels = labels

        if labels is None:
            print('No labels provided. Feature importance based methods are not available.')

        self.base_features = list(data.columns)
        self.one_hot_features = None

        # Dataframes recording information about features to remove
        self.record_missing = None
        self.record_single_unique = None
        self.record_collinear = None
        self.record_zero_importance = None
        self.record_low_importance = None
        self.missing_stats = None
        self.unique_stats = None
        self.corr_matrix = None
        self.feature_importances = None
        self.ops = {}
        self.one_hot_correlated = False

    def identify_missing(self, missing_threshold):
        self.missing_threshold = missing_threshold
        missing_series = self.data.isnull().sum() / self.data.shape[0]
        self.missing_stats = pd.DataFrame(missing_series).rename(columns={'index': 'feature', 0: 'missing_fraction'})
        self.missing_stats = self.missing_stats.sort_values('missing_fraction', ascending=False)

        record_missing = pd.DataFrame(missing_series[missing_series > missing_threshold]).reset_index().rename(columns=
        {
            'index': 'feature',
            0: 'missing_fraction'})

        to_drop = list(record_missing['feature'])

        self.record_missing = record_missing
        self.ops['missing'] = to_drop

        print('%d features with greater than %0.2f missing values.\n' % (
            len(self.ops['missing']), self.missing_threshold))

    def identify_zero_importance(self, task, eval_metric=None,
                                 n_iterations=10, early_stopping=True):

        if early_stopping and eval_metric is None:
            raise ValueError("""eval metric must be provided with early stopping. Examples include "auc" for classification or
                             "l2" for regression.""")

        if self.labels is None:
            raise ValueError("No training labels provided.")

        features = pd.get_dummies(self.data)
        self.one_hot_features = [column for column in features.columns if column not in self.base_features]

        self.data_all = pd.concat([features[self.one_hot_features], self.data], axis=1)

        feature_names = list(features.columns)

        features = np.array(features)
        labels = np.array(self.labels).reshape((-1,))

        feature_importance_values = np.zeros(len(feature_names))

        for _ in range(n_iterations):

            if task == 'regression':
                model = lgb.LGBMRegressor(n_estimators=1000, learning_rate=0.05, verbose=-1)

            if early_stopping:

                train_features, valid_features, train_labels, valid_labels = train_test_split(features, labels,
                                                                                              test_size=0.15,
                                                                                              stratify=labels)

                model.fit(train_features, train_labels, eval_metric=eval_metric,
                          eval_set=[(valid_features, valid_labels)],
                          early_stopping_rounds=100, verbose=-1)

                gc.enable()
                del train_features, train_labels, valid_features, valid_labels
                gc.collect()

            else:
                model.fit(features, labels)

            feature_importance_values += model.feature_importances_ / n_iterations

        feature_importances = pd.DataFrame({'feature': feature_names, 'importance': feature_importance_values})

        feature_importances = feature_importances.sort_values('importance', ascending=False).reset_index(drop=True)

        feature_importances['normalized_importance'] = feature_importances['importance'] / feature_importances[
            'importance'].sum()
        feature_importances['cumulative_importance'] = np.cumsum(feature_importances['normalized_importance'])

        record_zero_importance = feature_importances[feature_importances['importance'] == 0.0]

        to_drop = list(record_zero_importance['feature'])

        self.feature_importances = feature_importances
        self.record_zero_importance = record_zero_importance
        self.ops['zero_importance'] = to_drop

        print('\n%d features with zero importance after one-hot encoding.\n' % len(self.ops['zero_importance']))

        return self.feature_importances
