# -*- coding: utf-8 -*-
"""RECOMMENDATION SYSTEM.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/19aIbcT0L001rhP3O0zXmX-blP1USe7Gk
"""

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

# Step 1: Create a dataset (symptoms and recommendations)
# This is a simulated dataset; in real-world scenarios, this could be a database of symptoms, diagnoses, and treatments.
data = {
    'Symptom': [
        'fever headache cough',
        'chest pain difficulty breathing',
        'abdominal pain nausea vomiting',
        'sore throat fatigue fever',
        'skin rash itching swelling'
    ],
    'Recommendation': [
        'Paracetamol, Rest, Fluids',
        'Aspirin, See a doctor immediately',
        'Antacid, Hydration, Consult a doctor',
        'Throat lozenges, Rest, Hydration',
        'Antihistamine, Anti-inflammatory cream'
    ]
}

# Step 2: Load the dataset into a DataFrame
df = pd.DataFrame(data)

# Step 3: Use TF-IDF to convert the symptoms to numerical data
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(df['Symptom'])


# Step 4: Define a function to recommend treatments based on input symptoms
def recommend_treatment(input_symptom, df, tfidf_matrix):
    # Convert the input symptom to TF-IDF matrix
    input_symptom_tfidf = tfidf.transform([input_symptom])

    # Calculate cosine similarity between input symptoms and dataset symptoms
    cosine_similarities = linear_kernel(input_symptom_tfidf, tfidf_matrix).flatten()

    # Get the index of the most similar symptom
    most_similar_idx = cosine_similarities.argmax()

    # Retrieve the recommendation from the DataFrame
    recommendation = df['Recommendation'].iloc[most_similar_idx]

    return recommendation


# Step 5: Input symptoms and get the recommendation
input_symptom = 'fever cough tired'  # Example input symptom from the user

# Get the recommendation for the input symptom
recommendation = recommend_treatment(input_symptom, df, tfidf_matrix)

print(f"Input Symptoms: {input_symptom}")
print(f"Recommended Treatment: {recommendation}")