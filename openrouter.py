# Example: reuse your existing OpenAI setup
import os
import openai
import json
import pandas as pd



# Replace with your OpenRouter API key
OPENROUTER_API_KEY = "replace with your key"

# OpenRouter API base URL
openai.api_base = "https://openrouter.ai/api/v1"
openai.api_key = OPENROUTER_API_KEY

YOUR_SITE_URL = "http://localhost:3000"  # Replace with your actual site URL for testing
YOUR_APP_NAME = "YourAppName"  # Replace with your actual app name

#load the json file
with open('transcripts.json', 'r') as file:
    key_dialog = json.load(file)

# result csv file
result_df = pd.read_csv("modified_file2.csv")

# Specify the path to your CSV file
csv_file_path = 'test.csv'  # Replace with the actual path to your CSV file
# Load the CSV file into a Pandas DataFrame
df = pd.read_csv(csv_file_path)
for index, row in df.iterrows():
    id_value = row["Id"]
    transcript_value = key_dialog[str(row["Transcript"])]
    question_value = row["Question"] 

    compare_text = result_df.loc[result_df['Id'] == id_value, 'Text'].values[0]

    if result_df.loc[result_df['Id'] == id_value, 'Check'].isna().values[0]:

        prompt1 = "1. Please read a script, a question, and an answer to the question. Then, please help me check if the answer is correct. If correct, please reply only 'Yes'. If not correct, please give me a correct answer in short keywords. Your answer should be in English. Be super concise. No leading phrases. Do not elaborate.\n"
        prompt2 = f"Script: {transcript_value} \nQuestion: {question_value} \nAnswer: {compare_text}"


        response = openai.ChatCompletion.create(
                model = "open-orca/mistral-7b-openorca",
                messages=[
                {"role": "system", "content": f"Your are a helpful assistant."}, 
                {"role": "user", "content": prompt1 +  prompt2}],
                headers={
                    "HTTP-Referer": YOUR_SITE_URL,
                    "X-Title": YOUR_APP_NAME,
                },
            )

        api_response = response.choices[0].message["content"]
        
        print("content " + prompt1 +  prompt2)
        print(api_response)
        # Add values to the csv
        result_df.loc[result_df['Id'] == id_value, 'Check'] = api_response
        result_df.to_csv("modified_file2.csv", index=False)
