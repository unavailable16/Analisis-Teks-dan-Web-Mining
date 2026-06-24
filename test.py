import pandas as pd, re, nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Download NLTK (sekali saja)
nltk.download('punkt')
nltk.download('stopwords')

# Load dataset
df = pd.read_csv("IMDB_Dataset.csv")

# Preprocessing
def clean_text(text):
    text = re.sub(r'[^a-zA-Z\s]', '', text.lower())
    stop_words = set(stopwords.words('english'))
    words = [w for w in word_tokenize(text) if w not in stop_words]
    return " ".join(words)

df["clean_review"] = df["review"].apply(clean_text)

# TF-IDF
X = TfidfVectorizer(max_features=5000).fit_transform(df["clean_review"])
y = df["sentiment"]

# Split + Training
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = MultinomialNB()
model.fit(X_train, y_train)

# Prediksi & Evaluasi
y_pred = model.predict(X_test)

print("Akurasi:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))
print(confusion_matrix(y_test, y_pred))

# Test review baru
reviews = [
    "This movie was amazing and very entertaining",
    "The movie was boring and a waste of time"
]

pred = model.predict(
    TfidfVectorizer(max_features=5000)
    .fit(df["clean_review"])
    .transform([clean_text(r) for r in reviews])
)

for r, p in zip(reviews, pred):
    print(f"{r} -> {p}")
