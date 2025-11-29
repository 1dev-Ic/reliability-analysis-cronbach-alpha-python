import pandas as pd
import numpy as np

# === Load your cleaned dataset ===
file_path = "Cleaned_data.xlsx"  # Adjust path if needed
df = pd.read_excel(file_path)

# === Likert scale mapping ===
likert_map = {
    "Strongly Disagree": 1,
    "Disagree": 2,
    "Undecided": 3,
    "Agree": 4,
    "Strongly Agree": 5,
    "Strongl": 5  # Fix truncated labels
}

# === Cronbach's Alpha Function ===
def cronbach_alpha(data):
    data = data.replace(likert_map).apply(pd.to_numeric, errors='coerce')
    k = data.shape[1]
    item_variances = data.var(axis=0, ddof=1)
    total_score = data.sum(axis=1)
    total_variance = total_score.var(ddof=1)
    if total_variance == 0 or k <= 1:
        return np.nan
    return (k / (k - 1)) * (1 - item_variances.sum() / total_variance)

# === Detect usable columns (numeric/Likert only) ===
numeric_or_likert = df.replace(likert_map).apply(pd.to_numeric, errors='coerce')
scale_columns = numeric_or_likert.dropna(axis=1, how='all').columns.tolist()

# === Run Cronbach’s Alpha on all selected columns ===
alpha_value = cronbach_alpha(df[scale_columns])

# === Print results ===
print(f"Cronbach's Alpha for all scale columns: {alpha_value:.3f}")
print(f"Columns included in the calculation: {scale_columns}")
