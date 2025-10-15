import pandas as pd

# Load the raw data export from KATI
df = pd.read_excel("data/KATI_fraunhofer.xlsx")

# Stage 1: Filter by domain tags (e.g., include only records in education or management domains)
domain_mask = df['Domain Tags'].str.contains("Education", case=False, na=False) | \
              df['Domain Tags'].str.contains("Management", case=False, na=False)
df_stage1 = df[domain_mask].copy()
print(f"Stage 1 - After domain filter: {len(df_stage1)} records remain")

# Stage 2: Filter by keywords in Title/Abstract (e.g., must mention 'metaverse' or related terms)
keyword_mask = df_stage1['Title'].str.contains("metaverse", case=False, na=False) | \
               df_stage1['Abstract'].str.contains("metaverse", case=False, na=False)
# (Optionally include synonyms or related terms, e.g., virtual world, VR, etc.)
df_stage2 = df_stage1[keyword_mask].copy()
print(f"Stage 2 - After keyword filter: {len(df_stage2)} records remain")

# Stage 3: (Optional) Filter by full-text eligibility or additional criteria.
# This typically involves manual screening outside of code, but we document decisions.
# For example, ensure at least one of 'education'/'learning' appears in Abstract to confirm context:
context_mask = df_stage2['Abstract'].str.contains("educat", case=False, na=False) | \
               df_stage2['Abstract'].str.contains("training", case=False, na=False)
df_stage3 = df_stage2[context_mask].copy()
print(f"Stage 3 - After context filter: {len(df_stage3)} records remain")

# Relevance Scoring: assign a simple score based on term frequencies as illustration
def compute_relevance(row):
    text = str(row['Abstract']).lower()
    score = text.count("metaverse")
    score += text.count("education")
    # Add weights for other important factors if needed
    return score

df_stage3['RelevanceScore'] = df_stage3.apply(compute_relevance, axis=1)
df_stage3 = df_stage3.sort_values(by='RelevanceScore', ascending=False)

# Save the final included studies to a new Excel file
df_stage3.to_excel("data/included_studies.xlsx", index=False)
print("Included studies saved. Filtering complete.")
