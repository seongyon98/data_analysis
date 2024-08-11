from collections import Counter
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from nltk.stem import PorterStemmer
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet as wn

# 등장 빈도 기준 정제 함수
def clean_by_freq(tokenized_words, cut_off_count):
    # 파이썬의 Counter 모듈을 통해 단어의 빈도수 카운트하여 단어 집합 생성
    vocab = Counter(tokenized_words)
    
    # 빈도수가 cut_off_count 이하인 단어 set 추출
    uncommon_words = {key for key, value in vocab.items() if value <= cut_off_count}
    
    # uncommon_words에 포함되지 않는 단어 리스트 생성
    cleaned_words = [word for word in tokenized_words if word not in uncommon_words]

    return cleaned_words


# 단어 길이 기준 정제 함수
def clean_by_len(tokenized_words, cut_off_length):
    # 길이가 cut_off_length 이하인 단어 제거
    cleaned_by_freq_len = []
    
    for word in tokenized_words:
        if len(word) > cut_off_length:
            cleaned_by_freq_len.append(word)

    return cleaned_by_freq_len


# 불용어 제거 함수
def clean_by_stopwords(tokenized_words, stop_words_set):
    cleaned_words = []
    
    for word in tokenized_words:
        if word not in stop_words_set:
            cleaned_words.append(word)
            
    return cleaned_words


# 포터 스테머 어간 추출 함수
def stemming_by_porter(tokenized_words):
    porter_stemmer = PorterStemmer()
    porter_stemmed_words = []

    for word in tokenized_words:
        stem = porter_stemmer.stem(word)
        porter_stemmed_words.append(stem)

    return porter_stemmed_words


# 품사 태깅 함수
def pos_tagger(tokenized_sents):
    pos_tagged_words = []

    for sentence in tokenized_sents:
        # 단어 토큰화
        tokenized_words = word_tokenize(sentence)
    
        # 품사 태깅
        pos_tagged = pos_tag(tokenized_words)
        pos_tagged_words.extend(pos_tagged)
    
    return pos_tagged_words

def penn_to_wn(tag):
    if tag.startswith('J'):
        return wn.ADJ
    elif tag.startswith('N'):
        return wn.NOUN
    elif tag.startswith('R'):
        return wn.ADV
    elif tag.startswith('V'):
        return wn.VERB

def words_lemmatizer(pos_tagged_words):
    lemmatizer = WordNetLemmatizer()
    lemmatized_words = []

    for word, tag in pos_tagged_words:
        wn_tag = penn_to_wn(tag)

        if wn_tag in (wn.NOUN, wn.ADJ, wn.ADV, wn.VERB):
            lemmatized_words.append(lemmatizer.lemmatize(word, wn_tag))
        else:
            lemmatized_words.append(word)

    return lemmatized_words
