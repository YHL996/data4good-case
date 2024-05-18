import csv
import re

input_file = 'gptoutputty.csv'  # Replace with the path to your input CSV file
output_file = 'data4good.csv'  # Replace with the path for the output CSV file

# change ? and none to None
def clean_text(text):
    if "?" in text or "none" in text.lower():
        return "None"
    else:
        return text

# set lowercase of the first letter
def capitalize_text(text, row_number):
    if (row_number - 3) % 6 in [0, 1, 2, 3]:
        if text[0:4] == "AIDS" or text[0:4] == "GERD":
            return text
        else:
            if text == "None":
                return text
            else:    
                return text[0].lower() + text[1:]
    return text

#delete full stops
def delete_full_stop_text(text, row_number):
    if (row_number) % 6 in [1, 3, 4, 5, 6]:
        if text[-1] == ".":
            return text[:-1]
        else:    
            return text
    return text

#delete titles of names
def delete_title(text, row_number):
    if (row_number) % 6 in [1]:
        if "Miss" in text or "Mr" in text or "Mrs" in text or "Sr" in text or "Ms" in text:
            return text.lstrip("Mr.").lstrip("Mrs.").lstrip("Ms.").lstrip("Sr.").lstrip("Ms").lstrip("Miss").lstrip("Mr").lstrip("Mrs").lstrip("Sr").strip()
        else:    
            return text
    return text

def contains_numbers(text):
    return any(char.isdigit() for char in text)
def concatenate_numbers(text):
    numbers = re.findall(r'\d+', text)
    return ''.join(numbers)

#delete letter other than the numbers of age
def maintain_number_age(text, row_number):
    if (row_number) % 6 in [2]:
        if contains_numbers(text):
            return concatenate_numbers(text)
        else:    
            return 77
    return text

#delete and after ,
def delete_and(text, row_number):
    if (row_number - 3) % 6 in [0, 1, 2, 3]:
        if ", and " in text:
            return text.replace(", and ",", ")
        else:    
            return text
    return text

# Open input and output CSV files
with open(input_file, 'r', newline='', encoding='utf-8') as csvfile_in, open(output_file, 'w', newline='', encoding='utf-8') as csvfile_out:
    reader = csv.DictReader(csvfile_in)
    fieldnames = reader.fieldnames

    writer = csv.DictWriter(csvfile_out, fieldnames=fieldnames)
    writer.writeheader()

    for i, row in enumerate(reader, start=1):
        
         # Update the 'Text' column using the clean_text function
        row['Text'] = clean_text(row['Text'])
        row['Text'] = capitalize_text(row['Text'], i)
        row['Text'] = delete_full_stop_text(row['Text'], i)
        row['Text'] = delete_title(row['Text'], i)
        row['Text'] = maintain_number_age(row['Text'], i)
        row['Text'] = delete_and(row['Text'], i)
        
        writer.writerow(row)

print("CSV file processing complete. Updated data is saved to", output_file)

