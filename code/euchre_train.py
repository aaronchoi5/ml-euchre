import numpy
import pandas
from keras.models import Sequential, model_from_json
from keras.layers import Dense, Dropout
from keras.wrappers.scikit_learn import KerasClassifier
from keras.utils import np_utils
from sklearn import datasets, preprocessing
from sklearn.model_selection import cross_val_score, KFold
from sklearn.preprocessing import LabelEncoder
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from keras.callbacks import EarlyStopping
import argparse

pa = argparse.ArgumentParser()
pa.add_argument('-f', '--file', action='store', nargs=1, dest='FILENAME',
            help='Euchre.py overview log CSV filename',
            metavar='*.csv', required=True)
args = pa.parse_args()

raw_csv = args.FILENAME[0]

if not (os.path.isfile(raw_csv) and os.access(raw_csv, os.R_OK)):
    print ('ERROR - File Does Not Exist / Is Not Readable')
    exit()

# fix random seed for reproducibility
seed = 7
numpy.random.seed(seed)

# load dataset
dataframe = pandas.read_csv(raw_csv)
dataset = dataframe.values
Y = dataset[:, 0]
X = dataset[:, 1:25].astype(float)

# encode class values as integers
encoder = LabelEncoder()
encoder.fit(Y)
encoded_Y = encoder.transform(Y)
# convert integers to dummy variables (i.e. one hot encoded)
dummy_y = np_utils.to_categorical(encoded_Y)


# define baseline model
def baseline_model():
    # create model
    model = Sequential()
    model.add(Dense(8, input_dim=24, activation='relu'))
    model.add(Dropout(0.2))
    model.add(Dense(4, activation='softmax'))
    # Compile model
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    return model

def save_model(model):
    # saving model
    json_model = model.to_json()
    open('model_architecture.json', 'w').write(json_model)
    # saving weights
    model.save_weights('model_weights.h5', overwrite=True)

def load_model():
    # loading model
    model = model_from_json(open('model_architecture.json').read())
    model.load_weights('model_weights.h5')
    model.compile(loss='categorical_crossentropy', optimizer='adam')
    return model

#X_train, X_test, Y_train, Y_test = train_test_split(X, dummy_y, test_size=0.3, random_state=seed)

#estimator = KerasClassifier(build_fn=baseline_model, epochs=200, batch_size=5, verbose=2)

early_stopping = EarlyStopping(monitor='val_loss', patience=15)

model = baseline_model()
history = model.fit(X, dummy_y, validation_split=0.2, callbacks=[early_stopping], epochs=200, batch_size=10, verbose=1)

print(history.history.keys())

# summarize history for accuracy
plt.plot(history.history['acc'])
plt.plot(history.history['val_acc'])
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()
# summarize history for loss
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()

# save
#save_model(model)

# load
#model = load_model()

# predictions
#predictions = model.predict_classes(X, verbose=1)
#print(predictions)
# reverse encoding
#for pred in predictions:
    #print(pred)

#kfold = KFold(n_splits=10, shuffle=True, random_state=seed)

#results = cross_val_score(estimator, X, dummy_y, cv=kfold)
#print("Baseline: %.2f%% (%.2f%%)" % (results.mean() * 100, results.std() * 100))
