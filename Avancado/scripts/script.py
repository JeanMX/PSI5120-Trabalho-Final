import argparse
import os
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import joblib

def parse_args():
    """
    Parse arguments
    """
    parser = argparse.ArgumentParser()

    # hyperparameter sent by the client are passed as command-line argument to the script
    # We don't use these but I left them in as a useful template for future development

    # Hiperparâmetros do modelo (passados pelo Estimator)
    parser.add_argument('--max-depth', type=int, default=None)
    parser.add_argument('--n_jobs', type=int, default=None)
    parser.add_argument('--n-estimators', type=int, default=100)

    # Caminho para o diretório de dados de treino
    parser.add_argument('--train', type=str, default=os.environ.get('SM_CHANNEL_TRAIN'))
    parser.add_argument('--test', type=str, default=os.environ.get('SM_CHANNEL_TEST'))

    # Caminho para salvar o modelo treinado
    parser.add_argument('--model-dir', type=str, default=os.environ.get('SM_MODEL_DIR'))

    return parser.parse_known_args()

def load_dataset(path):
    """
    Load entire dataset
    """

     # Carregar os dados de treino
    train_data = pd.read_csv(os.path.join(args.train, "train.csv"), header=None)
    
    y = train_data.iloc[:, 0]  # Primeira coluna (rótulo)
    X = train_data.iloc[:, 1:]  # Todas as outras colunas (features)

    return X, y

def start(args):
    """
    Train a Random Forest"
    """

    print("Training mode")

    try:
        X_train, y_train = load_dataset(args.train)

        hyperparameter = {
            "max_depth": args.max_depth,
            "n_jobs": args.n_jobs,
            "n_estimators": args.n_estimators
        }

        print("Training...")

        model = RandomForestRegressor(n_estimators=args.n_estimators, max_depth=args.max_depth, n_jobs=args.n_jobs)

        model.fit(X_train, y_train)
        
        # Salvar o modelo no diretório especificado
        joblib.dump(model, os.path.join(args.model_dir, "model.joblib"))
        
        print("Train done")

    except Exception as e:
        print("Exception during training " + str(e) + "\\n")
        
def model_fn(model_dir):
    """
    Função que será usada para carregar o modelo no SageMaker
    """
    model = joblib.load(os.path.join(model_dir, "model.joblib"))
    return model

def predict_fn(input_data, model):
    """
    Apply model to the incoming request
    """
    return model.predict(input_data)

if __name__ == '__main__':

    args, _ = parse_args()
    start(args)
