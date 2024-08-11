import pandas as pd
import nltk
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
from preprocess import clean_by_freq, clean_by_len, clean_by_stopwords, pos_tagger, words_lemmatizer

# 데이터 불러오기
df = pd.read_csv('imdb.tsv', delimiter="\t")

# 대소문자 통합
df['review'] = df['review'].str.lower()

# 문장 토큰화
df['sent_tokens'] = df['review'].apply(sent_tokenize)

# 품사 태깅
df['pos_tagged_tokens'] = df['sent_tokens'].apply(pos_tagger)

# 표제어 추출
df['lemmatized_tokens'] = df['pos_tagged_tokens'].apply(words_lemmatizer)

# 추가 전처리
stopwords_set = set(stopwords.words('english'))

df['cleaned_tokens'] = df['lemmatized_tokens'].apply(lambda x: clean_by_freq(x, 1))
df['cleaned_tokens'] = df['cleaned_tokens'].apply(lambda x: clean_by_len(x, 2))
df['cleaned_tokens'] = df['cleaned_tokens'].apply(lambda x: clean_by_stopwords(x, stopwords_set))

def combine(sentence):
    return ' '.join(sentence)

df['combined_corpus'] = df['cleaned_tokens'].apply(combine)

# 결과 출력
print(df[['combined_corpus']])
