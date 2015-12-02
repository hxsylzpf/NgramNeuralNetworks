from load_rotten import read_rotten_pickle
from load_cr import read_cr_pickle
from load_imdb import read_imdb_pickle
from load_mpqa import read_mpqa_pickle
from load_sst import read_sst_sent_pickle, read_sst_kaggle_pickle, read_kaggle_raw
from load_subj import read_subj_pickle
from load_trec import read_trec_pickle
from load_yelp import read_train_data, read_test_data
from load_tweet import read_tweet_pickle

ROTTEN_TOMATOES = 'rotten'
CUSTOMER_REVIEW = 'cr'
MPQA = 'mpqa'
SST_SENT = 'sst_sent'
SST_SENT_POL = 'sst_sent_polarity'
SST_KAGGLE = 'sst_kaggle'
TREC = 'trec'
SUBJ = 'subj'
IMDB = 'imdb'