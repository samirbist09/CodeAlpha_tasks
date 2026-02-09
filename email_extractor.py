import re

print(" Email Extraction Automation Script")

# Step 1: Ask user for text in ONE input
text = input("\nPaste text containing emails and press ENTER:\n")

# Step 2: Write text to input.txt
with open("input.txt", "w", encoding="utf-8") as file:
    file.write(text)

print(" input.txt created!")

# Step 3: Extract emails
emails = re.findall(
    r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+",
    text
)

unique_emails = sorted(set(emails))

# Step 4: Save output
with open("emails.txt", "w", encoding="utf-8") as file:
    file.write("Extracted Email Addresses\n")
    file.write("--------------------------\n")
    for email in unique_emails:
        file.write(email + "\n")
    file.write(f"\nTotal emails found: {len(unique_emails)}")

print("Email extraction completed!")
print(f" Emails found: {len(unique_emails)}")
print(" Saved in emails.txt")
