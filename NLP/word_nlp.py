import pandas as pd
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from preprocess import clean_by_freq, stemming_by_porter
from preprocess import clean_by_len
from preprocess import clean_by_stopwords


df = pd.read_csv('imdb.tsv', delimiter='\t')

# 대소문자 통합
df['review'] = df['review'].str.lower()

# 단어 토큰화
df['word_tokens'] = df['review'].apply(word_tokenize)

# 데이터 정제
stopwords_set = set(stopwords.words('english'))

df['cleaned_tokens'] = df['word_tokens'].apply(lambda x: clean_by_freq(x, 1))
df['cleaned_tokens'] = df['cleaned_tokens'].apply(lambda x: clean_by_len(x, 2))
df['cleaned_tokens'] = df['cleaned_tokens'].apply(lambda x: clean_by_stopwords(x, stopwords_set))

# 어간 추출
df['stemmed_tokens'] = df['cleaned_tokens'].apply(stemming_by_porter)

print(df['stemmed_tokens'][0])
