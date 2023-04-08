from sklearn import preprocessing as pre
from argparse import ArgumentParser
from scipy import signal


import scipy.io as sio
import neurokit2 as nk
import pandas as pd
import numpy as np
import math


def preprocessing_and_feature_extraction_ECG(file_name_csv,raw):
    data_ECG={}
    for participant in range(0,23):
        for video in range(0,18):
            # load raw baseline and stimuli data for left and right
            basl_l=raw['DREAMER'][0,0]['Data'][0,participant]['ECG'][0,0]['baseline'][0,0][video,0][:,0]
            stim_l=raw['DREAMER'][0,0]['Data'][0,participant]['ECG'][0,0]['stimuli'][0,0][video,0][:,0]
            basl_r=raw['DREAMER'][0,0]['Data'][0,participant]['ECG'][0,0]['baseline'][0,0][video,0][:,1]
            stim_r=raw['DREAMER'][0,0]['Data'][0,participant]['ECG'][0,0]['stimuli'][0,0][video,0][:,1]
            # process with neurokit
            ecg_signals_b_l,info_b_l=nk.ecg_process(basl_l,sampling_rate=256)
            ecg_signals_s_l,info_s_l=nk.ecg_process(stim_l,sampling_rate=256)
            ecg_signals_b_r,info_b_r=nk.ecg_process(basl_r,sampling_rate=256)
            ecg_signals_s_r,info_s_r=nk.ecg_process(stim_r,sampling_rate=256)
            # divide stimuli features by baseline features
            # would be interesting to compare classification accuracy when we
            # don't do this
            features_ecg_l=nk.ecg_intervalrelated(ecg_signals_s_l)/nk.ecg_intervalrelated(ecg_signals_b_l)
            features_ecg_r=nk.ecg_intervalrelated(ecg_signals_s_r)/nk.ecg_intervalrelated(ecg_signals_b_r)
            # average left and right features
            # would be interesting to compare classification accuracy when we
            # rather include both left and right features
            features_ecg=(features_ecg_l+features_ecg_r)/2
            if not len(data_ECG):
                data_ECG=features_ecg
            else:
                data_ECG=pd.concat([data_ECG,features_ecg],ignore_index=True)


def preprocessing(raw, feature):
    overall=signal.firwin(9,[0.0625,0.46875],window='hamming')
    theta=signal.firwin(9,[0.0625,0.125],window='hamming')
    alpha=signal.firwin(9,[0.125,0.203125],window='hamming')
    beta=signal.firwin(9,[0.203125,0.46875],window='hamming')
    filtedData=signal.filtfilt(overall,1,raw)
    filtedtheta=signal.filtfilt(theta,1,filtedData)
    filtedalpha=signal.filtfilt(alpha,1,filtedData)
    filtedbeta=signal.filtfilt(beta,1,filtedData)
    ftheta,psdtheta=signal.welch(filtedtheta,nperseg=256)
    falpha,psdalpha=signal.welch(filtedalpha,nperseg=256)
    fbeta,psdbeta=signal.welch(filtedbeta,nperseg=256)
    feature.append(max(psdtheta))
    feature.append(max(psdalpha))
    feature.append(max(psdbeta))
    return feature


def driver():
    description = "Biosignal Emotions project BHS 2020."
    parser = ArgumentParser(__file__, description)

# main scripting details could go here
if __name__ == "__main__":
   driver()
 
