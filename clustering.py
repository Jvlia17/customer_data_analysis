import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans

from features import get_features

df = get_features()

features = df[[
    "age",
    "annual_income",
    "credit_limit",
    "utilization_ratio",
    "spending_to_income_ratio",
    "risk_score"
]].fillna(0)

kmeans = KMeans(n_clusters=3, random_state=42)
df["segment"] = kmeans.fit_predict(features)

print(df.groupby("segment").mean(numeric_only=True))

sns.scatterplot(
    data=df,
    x="annual_income",
    y="utilization_ratio",
    hue="segment"
)

plt.title("Customer Segments")
plt.show()