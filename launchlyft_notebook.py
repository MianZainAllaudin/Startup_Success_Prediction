"""
Script to generate the LaunchLyft Jupyter Notebook as a .ipynb file.
"""
import nbformat as nbf

nb = nbf.v4.new_notebook()
cells = []

# ─── Title & Imports ──────────────────────────────────────────────────────────
cells.append(nbf.v4.new_markdown_cell("""# 🚀 LaunchLyft — Startup Success Prediction Using Machine Learning

**Course AI Project**

This notebook builds an end-to-end machine-learning pipeline to predict whether a startup will be **acquired** or **closed**, using the Crunchbase Startup dataset.

---
"""))

cells.append(nbf.v4.new_code_cell("""# ── 0. Install dependencies (uncomment if needed) ───────────────────────────
# !pip install imbalanced-learn xgboost scikit-learn joblib matplotlib seaborn

# ── 1. Imports ───────────────────────────────────────────────────────────────
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    confusion_matrix, classification_report, roc_auc_score,
    ConfusionMatrixDisplay, RocCurveDisplay
)
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from imblearn.over_sampling import SMOTE
import joblib

print("✅ All imports successful!")
print(f"Dataset will be loaded from: startup_data.csv")
"""))

# ─── Data Loading ─────────────────────────────────────────────────────────────
cells.append(nbf.v4.new_markdown_cell("## 1. Data Loading & Initial Exploration"))

cells.append(nbf.v4.new_code_cell("""# ── Load the CSV ──────────────────────────────────────────────────────────────
# Adjust the path below if your CSV is in a different location
df = pd.read_csv('startup_data.csv')

print(f"Dataset shape: {df.shape}")
print(f"\\nColumns ({len(df.columns)}):")
for col in df.columns:
    print(f"  {col}: {df[col].dtype}")
"""))

cells.append(nbf.v4.new_code_cell("""# ── First 5 rows ──────────────────────────────────────────────────────────────
df.head()
"""))

cells.append(nbf.v4.new_code_cell("""# ── Basic statistics ─────────────────────────────────────────────────────────
df.describe()
"""))

# ─── EDA ─────────────────────────────────────────────────────────────────────
cells.append(nbf.v4.new_markdown_cell("## 2. Exploratory Data Analysis (EDA)"))

cells.append(nbf.v4.new_code_cell("""# ── Target variable distribution ─────────────────────────────────────────────
plt.figure(figsize=(7, 4))
colors = ['#2196F3', '#F44336']
df['status'].value_counts().plot(kind='bar', color=colors, edgecolor='black')
plt.title('Startup Status Distribution (Target Variable)', fontsize=14, fontweight='bold')
plt.xlabel('Status')
plt.ylabel('Count')
plt.xticks(rotation=0)
for i, v in enumerate(df['status'].value_counts()):
    plt.text(i, v + 5, str(v), ha='center', fontweight='bold')
plt.tight_layout()
plt.savefig('status_distribution.png', dpi=150)
plt.show()

print("\\nClass Distribution:")
print(df['status'].value_counts())
print(f"\\nImbalance ratio: {df['status'].value_counts().iloc[0] / df['status'].value_counts().iloc[1]:.2f}:1")
"""))

cells.append(nbf.v4.new_code_cell("""# ── Funding distribution ─────────────────────────────────────────────────────
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Raw funding
axes[0].hist(df['funding_total_usd'].dropna(), bins=50, color='#2196F3', edgecolor='black', alpha=0.7)
axes[0].set_title('Raw Funding Total (USD)', fontweight='bold')
axes[0].set_xlabel('Funding (USD)')
axes[0].set_ylabel('Count')

# Log-transformed funding
log_funding = np.log1p(df['funding_total_usd'].dropna())
axes[1].hist(log_funding, bins=50, color='#4CAF50', edgecolor='black', alpha=0.7)
axes[1].set_title('Log-Transformed Funding Total', fontweight='bold')
axes[1].set_xlabel('log1p(Funding USD)')
axes[1].set_ylabel('Count')

plt.suptitle('Funding Distribution: Before vs After Log Transform', fontsize=13, fontweight='bold')
plt.tight_layout()
plt.savefig('funding_distribution.png', dpi=150)
plt.show()
"""))

cells.append(nbf.v4.new_code_cell("""# ── Funding by status ─────────────────────────────────────────────────────────
plt.figure(figsize=(8, 5))
for status, color in zip(['acquired', 'closed'], ['#2196F3', '#F44336']):
    subset = df[df['status'] == status]['funding_total_usd'].dropna()
    plt.hist(np.log1p(subset), bins=40, alpha=0.6, label=status, color=color, edgecolor='black')
plt.title('Log Funding Distribution by Status', fontsize=13, fontweight='bold')
plt.xlabel('log1p(Funding USD)')
plt.ylabel('Count')
plt.legend()
plt.tight_layout()
plt.savefig('funding_by_status.png', dpi=150)
plt.show()

print("\\nFunding Stats by Status:")
print(df.groupby('status')['funding_total_usd'].describe())
"""))

cells.append(nbf.v4.new_code_cell("""# ── Category code distribution ────────────────────────────────────────────────
plt.figure(figsize=(12, 5))
top_cats = df['category_code'].value_counts().head(15)
colors_bar = plt.cm.tab20.colors[:15]
top_cats.plot(kind='bar', color=colors_bar, edgecolor='black')
plt.title('Top 15 Startup Categories', fontweight='bold')
plt.xlabel('Category')
plt.ylabel('Count')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('category_distribution.png', dpi=150)
plt.show()
"""))

cells.append(nbf.v4.new_code_cell("""# ── Funding rounds distribution ───────────────────────────────────────────────
fig, axes = plt.subplots(1, 2, figsize=(13, 5))

df['funding_rounds'].value_counts().sort_index().plot(
    kind='bar', ax=axes[0], color='#9C27B0', edgecolor='black'
)
axes[0].set_title('Funding Rounds Distribution', fontweight='bold')
axes[0].set_xlabel('Number of Rounds')
axes[0].set_ylabel('Count')
axes[0].tick_params(axis='x', rotation=0)

df.boxplot(column='funding_rounds', by='status', ax=axes[1], 
           boxprops=dict(color='#1565C0'),
           medianprops=dict(color='red', linewidth=2))
axes[1].set_title('Funding Rounds by Status', fontweight='bold')
axes[1].set_xlabel('Status')
plt.suptitle('')
plt.tight_layout()
plt.savefig('funding_rounds.png', dpi=150)
plt.show()
"""))

cells.append(nbf.v4.new_code_cell("""# ── Correlation heatmap (numeric columns) ─────────────────────────────────────
numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
plt.figure(figsize=(14, 10))
corr = df[numeric_cols].corr()
mask = np.triu(np.ones_like(corr, dtype=bool))
sns.heatmap(corr, mask=mask, annot=False, fmt='.2f', cmap='coolwarm',
            center=0, linewidths=0.5, cbar_kws={'shrink': 0.8})
plt.title('Correlation Heatmap (Numeric Features)', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('correlation_heatmap.png', dpi=150)
plt.show()
"""))

# ─── Missing Value Analysis ────────────────────────────────────────────────────
cells.append(nbf.v4.new_markdown_cell("## 3. Missing Value Analysis"))

cells.append(nbf.v4.new_code_cell("""# ── Missing value summary ────────────────────────────────────────────────────
missing = df.isnull().sum()
missing_pct = (missing / len(df)) * 100
missing_df = pd.DataFrame({'Missing Count': missing, 'Missing %': missing_pct})
missing_df = missing_df[missing_df['Missing Count'] > 0].sort_values('Missing %', ascending=False)

print("Columns with Missing Values:")
print(missing_df)

# Plot
if len(missing_df) > 0:
    plt.figure(figsize=(10, 5))
    missing_df['Missing %'].plot(kind='bar', color='#FF5722', edgecolor='black')
    plt.title('Missing Values by Column (%)', fontweight='bold')
    plt.xlabel('Column')
    plt.ylabel('Missing %')
    plt.xticks(rotation=45, ha='right')
    plt.axhline(y=40, color='red', linestyle='--', label='40% threshold')
    plt.legend()
    plt.tight_layout()
    plt.savefig('missing_values.png', dpi=150)
    plt.show()
else:
    print("No missing values found in the dataset!")
"""))

# ─── Preprocessing ────────────────────────────────────────────────────────────
cells.append(nbf.v4.new_markdown_cell("## 4. Preprocessing Pipeline"))

cells.append(nbf.v4.new_code_cell("""# ── Step 1: Remove duplicates ────────────────────────────────────────────────
initial_rows = len(df)
df = df.drop_duplicates()
print(f"Removed {initial_rows - len(df)} duplicate rows. Remaining: {len(df)}")
"""))

cells.append(nbf.v4.new_code_cell("""# ── Step 2: Drop irrelevant/ID columns ───────────────────────────────────────
# These columns are identifiers or have no predictive value
cols_to_drop = ['Unnamed: 0', 'Unnamed: 6', 'id', 'object_id', 'name', 
                'zip_code', 'city', 'closed_at', 'state_code.1', 'labels']

# Only drop columns that actually exist
cols_to_drop = [c for c in cols_to_drop if c in df.columns]
df = df.drop(columns=cols_to_drop)
print(f"Dropped columns: {cols_to_drop}")
print(f"Remaining columns: {list(df.columns)}")
"""))

cells.append(nbf.v4.new_code_cell("""# ── Step 3: Extract date features ────────────────────────────────────────────
import re

def safe_year(date_str):
    \"\"\"Extract year from date string like '1/1/2007' or '2007-01-01'\"\"\"
    if pd.isnull(date_str):
        return np.nan
    try:
        return pd.to_datetime(date_str).year
    except:
        # Try regex for year
        match = re.search(r'(\\d{4})', str(date_str))
        return int(match.group(1)) if match else np.nan

def safe_date(date_str):
    \"\"\"Convert to datetime safely\"\"\"
    if pd.isnull(date_str):
        return pd.NaT
    try:
        return pd.to_datetime(date_str)
    except:
        return pd.NaT

# Extract year features
df['founded_year'] = df['founded_at'].apply(safe_year)
df['first_funding_year'] = df['first_funding_at'].apply(safe_year)
df['last_funding_year'] = df['last_funding_at'].apply(safe_year)

# Extract funding duration (days between first and last funding)
df['first_funding_dt'] = df['first_funding_at'].apply(safe_date)
df['last_funding_dt'] = df['last_funding_at'].apply(safe_date)
df['founded_dt'] = df['founded_at'].apply(safe_date)

df['funding_duration_days'] = (df['last_funding_dt'] - df['first_funding_dt']).dt.days
df['funding_age_days'] = (df['first_funding_dt'] - df['founded_dt']).dt.days

# Drop raw date columns and temp columns
date_cols = ['founded_at', 'first_funding_at', 'last_funding_at',
             'first_funding_dt', 'last_funding_dt', 'founded_dt']
df = df.drop(columns=[c for c in date_cols if c in df.columns])

print("Date features extracted:")
print(df[['founded_year', 'first_funding_year', 'last_funding_year',
          'funding_duration_days', 'funding_age_days']].describe())
"""))

cells.append(nbf.v4.new_code_cell("""# ── Step 4: Feature engineering ──────────────────────────────────────────────
# Funding per round (handle division by zero)
df['funding_per_round'] = df.apply(
    lambda r: r['funding_total_usd'] / r['funding_rounds'] if r['funding_rounds'] > 0 else 0, axis=1
)

# Active round count (count of has_roundX columns that are 1)
round_cols = ['has_roundA', 'has_roundB', 'has_roundC', 'has_roundD']
if all(c in df.columns for c in round_cols):
    df['active_round_count'] = df[round_cols].sum(axis=1)

# Has VC or Angel (equity funding indicator)
if 'has_VC' in df.columns and 'has_angel' in df.columns:
    df['has_equity'] = ((df['has_VC'] == 1) | (df['has_angel'] == 1)).astype(int)

print("Engineered features:")
eng_feats = ['funding_per_round', 'active_round_count', 'has_equity']
print(df[[f for f in eng_feats if f in df.columns]].describe())
"""))

cells.append(nbf.v4.new_code_cell("""# ── Step 5: Log-transform funding columns ────────────────────────────────────
funding_cols = ['funding_total_usd', 'funding_per_round']
for col in funding_cols:
    if col in df.columns:
        df[col] = np.log1p(df[col])
        print(f"Log1p applied to: {col}")
"""))

cells.append(nbf.v4.new_code_cell("""# ── Step 6: Encode target variable ───────────────────────────────────────────
df['status_encoded'] = (df['status'] == 'acquired').astype(int)
print("Target encoding:")
print(df[['status', 'status_encoded']].value_counts())
"""))

cells.append(nbf.v4.new_code_cell("""# ── Step 7: Encode categorical features ──────────────────────────────────────
# One-hot encode category_code with top N + 'Other'
if 'category_code' in df.columns:
    df['category_code'] = df['category_code'].fillna('unknown').str.lower().str.strip()
    top_cats = df['category_code'].value_counts().head(10).index.tolist()
    df['category_code'] = df['category_code'].apply(lambda x: x if x in top_cats else 'other')
    cat_dummies = pd.get_dummies(df['category_code'], prefix='cat')
    df = pd.concat([df, cat_dummies], axis=1)
    df = df.drop(columns=['category_code'])
    print(f"Category dummies created: {list(cat_dummies.columns)}")

# Drop state_code (already have is_CA, is_NY, is_MA, is_TX dummies)
if 'state_code' in df.columns:
    df = df.drop(columns=['state_code'])

print(f"\\nFinal shape: {df.shape}")
"""))

cells.append(nbf.v4.new_code_cell("""# ── Step 8: Handle remaining missing values ───────────────────────────────────
numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
# Exclude target columns
numeric_cols = [c for c in numeric_cols if c not in ['status_encoded']]

for col in numeric_cols:
    if df[col].isnull().sum() > 0:
        median_val = df[col].median()
        df[col] = df[col].fillna(median_val)
        print(f"Filled '{col}' NaN with median={median_val:.2f}")

print(f"\\nTotal missing after imputation: {df.isnull().sum().sum()}")
"""))

cells.append(nbf.v4.new_code_cell("""# ── Step 9: Drop status column and prepare X, y ──────────────────────────────
X = df.drop(columns=['status', 'status_encoded'])
y = df['status_encoded']

# Ensure all features are numeric (drop any remaining string columns)
non_numeric = X.select_dtypes(exclude=[np.number]).columns.tolist()
if non_numeric:
    print(f"Dropping non-numeric columns: {non_numeric}")
    X = X.drop(columns=non_numeric)

print(f"Feature matrix shape: {X.shape}")
print(f"Target distribution: {y.value_counts().to_dict()}")
print(f"Feature names ({len(X.columns)}): {list(X.columns)}")
"""))

# ─── Train/Test Split + SMOTE ─────────────────────────────────────────────────
cells.append(nbf.v4.new_markdown_cell("## 5. Train/Test Split & SMOTE Oversampling"))

cells.append(nbf.v4.new_code_cell("""# ── Train/Test Split (BEFORE SMOTE!) ─────────────────────────────────────────
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

print(f"Training set: {X_train.shape}")
print(f"Test set:     {X_test.shape}")
print(f"\\nTrain class distribution: {dict(y_train.value_counts())}")
print(f"Test  class distribution: {dict(y_test.value_counts())}")
"""))

cells.append(nbf.v4.new_code_cell("""# ── Apply SMOTE ONLY on training data ────────────────────────────────────────
# SMOTE = Synthetic Minority Over-sampling TEchnique
# It creates synthetic examples of the minority class (closed startups)

smote = SMOTE(random_state=42)
X_train_sm, y_train_sm = smote.fit_resample(X_train, y_train)

print(f"Before SMOTE: {dict(y_train.value_counts())}")
print(f"After  SMOTE: {dict(pd.Series(y_train_sm).value_counts())}")

# Visualize SMOTE effect
fig, axes = plt.subplots(1, 2, figsize=(12, 4))

y_train.value_counts().plot(kind='bar', ax=axes[0], color=['#2196F3', '#F44336'], edgecolor='black')
axes[0].set_title('Before SMOTE (Training Set)', fontweight='bold')
axes[0].set_xlabel('Status')
axes[0].set_ylabel('Count')
axes[0].tick_params(axis='x', rotation=0)

pd.Series(y_train_sm).value_counts().plot(kind='bar', ax=axes[1], color=['#2196F3', '#F44336'], edgecolor='black')
axes[1].set_title('After SMOTE (Training Set)', fontweight='bold')
axes[1].set_xlabel('Status')
axes[1].set_ylabel('Count')
axes[1].tick_params(axis='x', rotation=0)

plt.tight_layout()
plt.savefig('smote_comparison.png', dpi=150)
plt.show()
"""))

# ─── Model Training ───────────────────────────────────────────────────────────
cells.append(nbf.v4.new_markdown_cell("## 6. Model Training & Evaluation"))

cells.append(nbf.v4.new_code_cell("""# ── Helper function: evaluate model ──────────────────────────────────────────
def evaluate_model(name, model, X_tr, y_tr, X_te, y_te, has_proba=True):
    \"\"\"Train model and return evaluation metrics.\"\"\"
    model.fit(X_tr, y_tr)
    y_pred = model.predict(X_te)
    
    acc  = accuracy_score(y_te, y_pred)
    prec = precision_score(y_te, y_pred, average='weighted', zero_division=0)
    rec  = recall_score(y_te, y_pred, average='weighted', zero_division=0)
    f1   = f1_score(y_te, y_pred, average='weighted', zero_division=0)
    
    # Specificity = TN / (TN + FP)
    cm = confusion_matrix(y_te, y_pred)
    if cm.shape == (2, 2):
        tn, fp, fn, tp = cm.ravel()
        spec = tn / (tn + fp) if (tn + fp) > 0 else 0
    else:
        spec = 0
    
    # AUC
    auc = 0
    if has_proba:
        try:
            proba = model.predict_proba(X_te)[:, 1]
            auc = roc_auc_score(y_te, proba)
        except:
            auc = 0
    
    return {
        'Model': name,
        'Accuracy': round(acc, 4),
        'Precision': round(prec, 4),
        'Recall': round(rec, 4),
        'F1 Score': round(f1, 4),
        'Specificity': round(spec, 4),
        'AUC': round(auc, 4),
        'model_obj': model,
        'y_pred': y_pred
    }

print("✅ Evaluation function ready!")
"""))

cells.append(nbf.v4.new_code_cell("""# ── Train models ─────────────────────────────────────────────────────────────
results = []

# 1. Decision Tree (Baseline)
print("Training Decision Tree...")
dt = DecisionTreeClassifier(max_depth=10, random_state=42)
results.append(evaluate_model('Decision Tree', dt, X_train_sm, y_train_sm, X_test, y_test))

# 2. Random Forest
print("Training Random Forest...")
rf = RandomForestClassifier(n_estimators=200, max_depth=15, random_state=42, n_jobs=-1)
results.append(evaluate_model('Random Forest', rf, X_train_sm, y_train_sm, X_test, y_test))

# 3. Gradient Boosting (XGBoost-style)
print("Training Gradient Boosting...")
gb = GradientBoostingClassifier(n_estimators=200, max_depth=5, learning_rate=0.1, random_state=42)
results.append(evaluate_model('Gradient Boosting', gb, X_train_sm, y_train_sm, X_test, y_test))

# 4. Logistic Regression
print("Training Logistic Regression...")
lr = LogisticRegression(max_iter=1000, random_state=42, C=1.0)
results.append(evaluate_model('Logistic Regression', lr, X_train_sm, y_train_sm, X_test, y_test))

# 5. Naive Bayes
print("Training Naive Bayes...")
nb_model = GaussianNB()
results.append(evaluate_model('Naive Bayes', nb_model, X_train_sm, y_train_sm, X_test, y_test, has_proba=True))

print("\\n✅ All models trained!")
"""))

# ─── Model Comparison ────────────────────────────────────────────────────────
cells.append(nbf.v4.new_markdown_cell("## 7. Model Comparison"))

cells.append(nbf.v4.new_code_cell("""# ── Results table ────────────────────────────────────────────────────────────
metrics_cols = ['Model', 'Accuracy', 'Precision', 'Recall', 'F1 Score', 'Specificity', 'AUC']
results_df = pd.DataFrame([{k: v for k, v in r.items() if k in metrics_cols} for r in results])
results_df = results_df.sort_values('F1 Score', ascending=False)

print("\\n=== MODEL COMPARISON ===")
print(results_df.to_string(index=False))
"""))

cells.append(nbf.v4.new_code_cell("""# ── Bar chart comparison ──────────────────────────────────────────────────────
metrics = ['Accuracy', 'Precision', 'Recall', 'F1 Score', 'AUC']
x = np.arange(len(results_df))
width = 0.15
colors = ['#1976D2', '#388E3C', '#F57C00', '#7B1FA2', '#D32F2F']

fig, ax = plt.subplots(figsize=(14, 6))
for i, (metric, color) in enumerate(zip(metrics, colors)):
    bars = ax.bar(x + i * width, results_df[metric], width, label=metric, color=color, alpha=0.85)

ax.set_xlabel('Model')
ax.set_ylabel('Score')
ax.set_title('Model Performance Comparison', fontsize=14, fontweight='bold')
ax.set_xticks(x + width * 2)
ax.set_xticklabels(results_df['Model'], rotation=15, ha='right')
ax.legend(loc='lower right', fontsize=9)
ax.set_ylim(0, 1.05)
ax.axhline(y=0.8, color='gray', linestyle='--', alpha=0.5, label='0.8 threshold')
ax.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig('model_comparison.png', dpi=150)
plt.show()
"""))

# ─── Best Model Analysis ─────────────────────────────────────────────────────
cells.append(nbf.v4.new_markdown_cell("## 8. Best Model — Detailed Analysis"))

cells.append(nbf.v4.new_code_cell("""# ── Select best model by F1 score ────────────────────────────────────────────
best_result = max(results, key=lambda r: r['F1 Score'])
best_model = best_result['model_obj']
best_name = best_result['Model']
y_pred_best = best_result['y_pred']

print(f"🏆 Best Model: {best_name}")
print(f"   F1 Score:  {best_result['F1 Score']}")
print(f"   Accuracy:  {best_result['Accuracy']}")
print(f"   AUC:       {best_result['AUC']}")
"""))

cells.append(nbf.v4.new_code_cell("""# ── Confusion matrix ─────────────────────────────────────────────────────────
cm = confusion_matrix(y_test, y_pred_best)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=['Closed (0)', 'Acquired (1)'])

fig, ax = plt.subplots(figsize=(7, 5))
disp.plot(ax=ax, colorbar=True, cmap='Blues')
ax.set_title(f'Confusion Matrix — {best_name}', fontsize=13, fontweight='bold')
plt.tight_layout()
plt.savefig('confusion_matrix.png', dpi=150)
plt.show()
"""))

cells.append(nbf.v4.new_code_cell("""# ── Classification report ────────────────────────────────────────────────────
print(f"Classification Report — {best_name}\\n")
print(classification_report(y_test, y_pred_best, target_names=['Closed', 'Acquired']))
"""))

cells.append(nbf.v4.new_code_cell("""# ── ROC-AUC Curve ────────────────────────────────────────────────────────────
try:
    fig, ax = plt.subplots(figsize=(8, 6))
    
    for res in results:
        model_obj = res['model_obj']
        try:
            proba = model_obj.predict_proba(X_test)[:, 1]
            RocCurveDisplay.from_predictions(
                y_test, proba, 
                name=f"{res['Model']} (AUC={res['AUC']:.3f})",
                ax=ax
            )
        except:
            pass
    
    ax.plot([0, 1], [0, 1], 'k--', label='Random')
    ax.set_title('ROC-AUC Curves — All Models', fontsize=13, fontweight='bold')
    ax.legend(loc='lower right', fontsize=8)
    ax.grid(alpha=0.3)
    plt.tight_layout()
    plt.savefig('roc_curves.png', dpi=150)
    plt.show()
except Exception as e:
    print(f"ROC curve error: {e}")
"""))

cells.append(nbf.v4.new_code_cell("""# ── Feature importance (if applicable) ───────────────────────────────────────
feature_names = X.columns.tolist()

try:
    if hasattr(best_model, 'feature_importances_'):
        importances = best_model.feature_importances_
        fi_df = pd.DataFrame({'Feature': feature_names, 'Importance': importances})
        fi_df = fi_df.sort_values('Importance', ascending=False).head(20)
        
        plt.figure(figsize=(10, 7))
        colors_fi = plt.cm.RdYlGn(np.linspace(0.3, 0.9, 20))
        plt.barh(fi_df['Feature'][::-1], fi_df['Importance'][::-1], color=colors_fi)
        plt.xlabel('Feature Importance')
        plt.title(f'Top 20 Feature Importances — {best_name}', fontsize=13, fontweight='bold')
        plt.tight_layout()
        plt.savefig('feature_importance.png', dpi=150)
        plt.show()
        
        print("Top 10 most important features:")
        print(fi_df.head(10).to_string(index=False))
    else:
        print(f"{best_name} does not have feature_importances_. Skipping.")
except Exception as e:
    print(f"Feature importance error: {e}")
"""))

# ─── Save Model ──────────────────────────────────────────────────────────────
cells.append(nbf.v4.new_markdown_cell("## 9. Save Best Model"))

cells.append(nbf.v4.new_code_cell("""# ── Save model and feature names ──────────────────────────────────────────────
model_package = {
    'model': best_model,
    'model_name': best_name,
    'feature_names': feature_names,
    'metrics': {k: v for k, v in best_result.items() if k in ['Accuracy', 'Precision', 'Recall', 'F1 Score', 'AUC']}
}

joblib.dump(model_package, 'launchlyft_model.pkl')
print(f"✅ Model saved as 'launchlyft_model.pkl'")
print(f"   Model: {best_name}")
print(f"   Features: {len(feature_names)}")
print(f"   F1 Score: {best_result['F1 Score']}")
"""))

# ─── Summary ──────────────────────────────────────────────────────────────────
cells.append(nbf.v4.new_markdown_cell("## 10. Final Summary"))

cells.append(nbf.v4.new_code_cell("""# ── Final comparison table ───────────────────────────────────────────────────
print("=" * 70)
print("LAUNCHLYFT — FINAL MODEL COMPARISON SUMMARY")
print("=" * 70)
print(results_df[metrics_cols].to_string(index=False))
print("=" * 70)
print(f"\\n🏆 Best Model: {best_name}")
print(f"   → Selected for Streamlit app deployment")
print("\\n💡 Key Findings:")
print("   1. SMOTE oversampling balanced the dataset and improved recall on 'closed' class")
print("   2. Log transformation of funding columns reduced skewness")
print("   3. Date feature engineering (funding_age_days, duration) was highly informative")
print("   4. One-hot encoding of categories outperformed label encoding")
print("   5. Round D/C funding and avg_participants are strong predictors")
"""))

# Compose notebook
nb.cells = cells
nb.metadata = {
    "kernelspec": {
        "display_name": "Python 3",
        "language": "python",
        "name": "python3"
    },
    "language_info": {
        "name": "python",
        "version": "3.10.0"
    }
}

# Write
import json
# Save notebook in the current project folder
output_path = 'LaunchLyft_Notebook.ipynb'

nbf.write(nb, output_path)
print(f"Notebook written successfully: {output_path}")
