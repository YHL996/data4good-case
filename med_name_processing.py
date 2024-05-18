import pandas as pd
 
# Assuming df is your DataFrame. Replace this with your actual DataFrame loading or definition
# df = ...

df = pd.read_csv("data4good.csv")

# List of non-capitalized terms
non_capitalized_terms = [
    "ibuprofen", "over-the-counter antihistamines", "antibiotic therapy", "antibiotics", "acetaminophen",
    "aspirin", "sulfur cream", "antihistamines", "antibiotic ointment", "pain medication",
    "over-the-counter pain medication like acetaminophen", "radioactive iodine treatment", "antibiotic cream",
    "over-the-counter antihistamine", "anti-malarial medications", "paracetamol", "inhaler",
    "blood pressure medication", "antacid", "topical steroid cream", "antiretroviral medication",
    "antiviral medication", "over-the-counter pain relievers like acetaminophen",
    "over-the-counter pain relievers like ibuprofen or aspirin", "antacid tablets",
    "over-the-counter antihistamines", "lemon balm", "coal tar/salicylic acid", "coal tar/salicylic acid/sulfur",
    "pain relievers"
]
 
# Capitalize the first letter of the 'Text' column at every 6th, 12th, 18th, etc., indexes
for i in range(5, len(df), 6):  # Starting from index 5 (the 6th row) and stepping by 6
    if df.at[i, 'Text'].lower() not in non_capitalized_terms:
        df.at[i, 'Text'] = df.at[i, 'Text'].capitalize()
 
# Print or display the modified DataFrame
df.to_csv("data4good2.csv", index=False)