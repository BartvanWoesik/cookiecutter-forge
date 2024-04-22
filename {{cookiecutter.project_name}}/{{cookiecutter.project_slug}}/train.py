import numpy as np
import pandas as pd
from functools import partial
import hydra
from hydra.utils import instantiate
from model_forge.data.dataset import Dataset
from model_forge.model.model_evaluator import ModelEvaluator
from model_forge.model.model_orchastrator import ModelOrchestrator



@hydra.main(config_path="../conf", config_name="config.yaml", version_base=None)
def main(cfg): 

   # Create a simp le dataset
    # Create a simp le dataset
    X = np.array(       [1,2,3,4,5,6,6,6,6,6,6]*100)
    train = np.array(   [1,1,1,0,0,0,0,0,0,1,1]*100)
    test = np.array(    [0,0,0,1,1,1,1,1,1,0,0]*100)
    y = np.array(       [0,1,0,1,0,1,0,1,0,1,0]*100)
    df = partial(pd.DataFrame, {'X': X.flatten(),"train": train, "test": test,  'target': y})
    dataset = Dataset.create_from_pipeline(
            df,
            instantiate(cfg.data_pipeline),
            target_column="target",
            splits_columns=["train", "test"],
        )


    model_orchestrator = ModelOrchestrator(cfg)
    model = model_orchestrator.create_pipeline()
    


    # Train the model on the training data
    model.fit(dataset.X_train, dataset.y_train)

    # Make predictions on the testing data
    y_pred = model.predict(dataset.X_test)

    # Print the predicted values
    print("Predicted values:", y_pred)


if __name__ == "__main__":
    main()