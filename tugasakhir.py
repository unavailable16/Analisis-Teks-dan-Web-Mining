import pandas as pd
import re
import nltk

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Download resource NLTK (hanya pertama kali)
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')

# ==========================
# 1. Load Dataset
# ==========================

df = pd.read_csv("IMDB_Dataset.csv")

print("Jumlah Data:")
print(df.shape)

print("\nContoh Data:")
print(df.head())

# ==========================
# 2. Text Preprocessing
# ==========================

def preprocess_text(text):

    # Lowercase
    text = text.lower()

    # Hapus karakter selain huruf
    text = re.sub(r'[^a-zA-Z\s]', '', text)

    # Tokenisasi
    tokens = word_tokenize(text)

    # Stopword Removal
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word not in stop_words]

    return " ".join(tokens)

print("\nMelakukan preprocessing...")

df['clean_review'] = df['review'].apply(preprocess_text)

# ==========================
# 3. TF-IDF
# ==========================

vectorizer = TfidfVectorizer(max_features=5000)

X = vectorizer.fit_transform(df['clean_review'])

y = df['sentiment']

print("\nUkuran TF-IDF Matrix:")
print(X.shape)

# ==========================
# 4. Split Data
# ==========================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# ==========================
# 5. Training Model
# ==========================

model = MultinomialNB()

model.fit(X_train, y_train)

# ==========================
# 6. Prediksi
# ==========================

y_pred = model.predict(X_test)

# ==========================
# 7. Evaluasi
# ==========================

print("\nAkurasi:")
print(accuracy_score(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

# ==========================
# 8. Uji Review Baru
# ==========================

new_reviews = [

    "This movie was amazing and very entertaining",

    "The movie was boring and a waste of time"

]

clean_reviews = [
    preprocess_text(review)
    for review in new_reviews
]

vector_reviews = vectorizer.transform(clean_reviews)

predictions = model.predict(vector_reviews)

print("\nHASIL PREDIKSI")

for review, pred in zip(new_reviews, predictions):
    print(f"\nReview : {review}")
    print(f"Sentimen : {pred}")