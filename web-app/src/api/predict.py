import numpy as np
import librosa
import pickle
from keras.models import load_model

# PATH wrt manage.py
MODEL = load_model('../../model/trained_model')
SCALER = pickle.load(open("../../model/scaler.pickle", "rb"))
ENCODER = pickle.load(open("../../model/encoder.pickle", "rb"))


def extract_features(data, sample_rate):
    result = np.array([])
    # Zero Crossing Rate
    zcr = np.mean(librosa.feature.zero_crossing_rate(y=data).T, axis=0)
    result = np.hstack((result, zcr))
    
    # Chroma_stft
    stft = np.abs(librosa.stft(data))
    chroma_stft = np.mean(librosa.feature.chroma_stft(S=stft, sr=sample_rate).T, axis=0)
    result = np.hstack((result, chroma_stft)) # stacking horizontally

    # MFCC
    mfcc = np.mean(librosa.feature.mfcc(y=data, sr=sample_rate).T, axis=0)
    result = np.hstack((result, mfcc)) # stacking horizontally

    # RMS(Root Mean Square) Value
    rms = np.mean(librosa.feature.rms(y=data).T, axis=0)
    result = np.hstack((result, rms)) # stacking horizontally

    # MelSpectogram
    mel = np.mean(librosa.feature.melspectrogram(y=data, sr=sample_rate).T, axis=0)
    result = np.hstack((result, mel)) # stacking horizontally
    
    return result


def get_features_from_audio_file(path):
    data, sample_rate = librosa.load(path, duration=2.5, offset=0.6)
    res = extract_features(data, sample_rate)
    return np.array(res)


def transform_audio_file(filepath):
    features = get_features_from_audio_file(filepath)
    features = np.reshape(features, (1,-1))
    features = SCALER.transform(features)
    features = np.expand_dims(features, axis=2)
    return features


def predict(file):
    features = transform_audio_file(filepath=file)
    preds = MODEL.predict(features)
    return ENCODER.inverse_transform(preds)[0][0]
