from get_dataset import get_dataset
from get_model import save_model
from get_model import create_model
from keras.models import model_from_json


def train_model(model, x_train, y_train):
    model.fit(x_train, y_train, validation_split=0.1, batch_size=10,epochs=3, shuffle=True)
    return model


def getAnExistModel():
    try:
        model_file = open('Data/Model/model.json', 'r')
        model = model_file.read()
        model_file.close()
        model = model_from_json(model)
        model.load_weights('Data/Model/weights.h5')
        return model
    except:
        main()
        return getAnExistModel()


def main():
    batch_size_for_capture = 300
    x_train, y_train = get_dataset(batch_size_for_capture)
    model = create_model()
    model = train_model(model, x_train, y_train)
    save_model(model)
    return model


if __name__ == '__main__':
    main()
