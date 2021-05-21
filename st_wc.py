import streamlit as st 
from wordcloud import WordCloud
import MeCab

st.title('日本語word cloud')

text = st.text_area('ここに入力してください', value='', height=500, max_chars=None, key=None, help=None)

#品詞の選択
word_class = st.multiselect('表示させる品詞の選択', ['名詞', '動詞', '形容詞', '副詞', '助詞', '助動詞'],'名詞')

# ラジオボタン
color = st.radio("color",('white','black','red', 'gold', 'green', 'blue', 'orange', 'pink'))

#width & height
width = st.number_input('画像の幅', 640, 1920, 1280)
height = st.number_input('画像の高さ', 480, 1080, 720)

# ボタン
button = st.button('Word Cloudの表示')

try:
    mecab = MeCab.Tagger()    
    parts = mecab.parse(text)
except RuntimeError as e:
    print(e)

if button:
    nouns = []
    for part in parts.split('\n')[:-2]:
        if '名詞' in word_class and '名詞' in part.split('\t')[4]:
            nouns.append(part.split('\t')[0])
        elif '動詞' in word_class and '動詞' in part.split('\t')[4]:
            nouns.append(part.split('\t')[0])
        elif '形容詞' in word_class and '形容詞' in part.split('\t')[4]:
            nouns.append(part.split('\t')[0])
        elif '副詞' in word_class and '副詞' in part.split('\t')[4]:
            nouns.append(part.split('\t')[0])
        elif '助詞' in word_class and '助詞' in part.split('\t')[4]:
            nouns.append(part.split('\t')[0])
        elif '助動詞' in word_class and '助動詞' in part.split('\t')[4]:
            nouns.append(part.split('\t')[0])

    words = ' '.join(nouns)

    font_path = 'corp_round_v1.ttf'
    wc = WordCloud(width=width, height=height, background_color=color, font_path=font_path)
    wc.generate(words)
    wc.to_file('wc.png')
    st.image('wc.png')
