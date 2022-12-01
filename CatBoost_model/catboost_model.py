from catboost import CatBoostClassifier

class CatBoostModel:
    def __init__(self, args, output_dir):
        self.output_dir = output_dir
        self.model = CatBoostClassifier(iterations=args.iteration,
                                        random_seed=args.seed,
                                        eval_metric="AUC",
                                        early_stopping_rounds=args.early_stopping,
                                        train_dir=self.output_dir,
                                        learning_rate=args.lr,
                                        
                                        task_type="GPU",
                                        devices="0")
    
    def fit(self, X, y, cat_features, eval_set, verbose=100):
        self.model.fit(X, y, 
                       cat_features=cat_features, 
                       eval_set=eval_set,
                       verbose=verbose)
    
    def inference(self, X_test):
        return self.model.predict_proba(X_test)[:, 1]