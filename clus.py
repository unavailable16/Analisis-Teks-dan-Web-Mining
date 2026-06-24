import pandas as pd, re, nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

# Download NLTK
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
vectorizer = TfidfVectorizer(max_features=5000)
X = vectorizer.fit_transform(df["clean_review"])

# Clustering (2 cluster)
model = KMeans(n_clusters=2, random_state=42)
df["cluster"] = model.fit_predict(X)

# Hasil
print(df[["review", "cluster"]].head(10))

# Kata penting tiap cluster
terms = vectorizer.get_feature_names_out()

for i in range(2):
    center_words = model.cluster_centers_[i].argsort()[-10:]
    print(f"\nCluster {i}:")
    print([terms[j] for j in center_words])
