import pandas as pd
import matplotlib.pyplot as plt

from python.features import get_features

from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import (
    classification_report,
    confusion_matrix,
    roc_curve,
    roc_auc_score
)

# =========================
# LOAD DATA
# =========================
df = get_features()

print("START")
print("SHAPE:", df.shape)

# =========================
# FEATURES / TARGET
# =========================
X = df.drop(columns=["responded", "customer_id"])
y = df["responded"]

X = X.select_dtypes(include=["number"])

# =========================
# TRAIN / TEST SPLIT
# =========================
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# =========================
# MODEL
# =========================
pipeline = Pipeline([
    ("model", RandomForestClassifier(
        n_estimators=300,
        max_depth=6,
        random_state=42,
        class_weight="balanced"
    ))
])

pipeline.fit(X_train, y_train)

# =========================
# PREDICTIONS
# =========================
y_pred = pipeline.predict(X_test)
y_proba = pipeline.predict_proba(X_test)[:, 1]

# =========================
# METRICS
# =========================
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

auc = roc_auc_score(y_test, y_proba)
print("AUC:", round(auc, 4))

# =========================
# CONFUSION MATRIX
# =========================
cm = confusion_matrix(y_test, y_pred)

plt.figure()
plt.imshow(cm, cmap="Blues")
plt.title("Confusion Matrix")
plt.colorbar()
plt.xticks([0, 1], ["No Response", "Response"])
plt.yticks([0, 1], ["No Response", "Response"])

for i in range(2):
    for j in range(2):
        plt.text(j, i, cm[i, j], ha="center", va="center")

plt.show()

# =========================
# ROC CURVE
# =========================
fpr, tpr, _ = roc_curve(y_test, y_proba)

plt.figure()
plt.plot(fpr, tpr, label=f"AUC = {auc:.2f}")
plt.plot([0, 1], [0, 1], linestyle="--")

plt.title("ROC Curve")
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.legend()
plt.show()

# =========================
# FEATURE IMPORTANCE
# =========================
importances = pipeline.named_steps["model"].feature_importances_

feat_imp = pd.DataFrame({
    "feature": X.columns,
    "importance": importances
}).sort_values("importance", ascending=True)

plt.figure()
plt.barh(feat_imp["feature"], feat_imp["importance"])
plt.title("Feature Importance (Random Forest)")
plt.show()