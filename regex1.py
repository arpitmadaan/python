import re 
txt = "ab12 cd34 ef56"
pattern = r"[a-zA-Z]{2}\d{2}"
matches1 = re.findall(pattern, txt)
print(matches1)

txt = "The rain in Spain"
pattern = r"[aeiou]{2,}"
matches2 = re.findall(pattern, txt)
print(matches2)

text = "Please contact us at support@example.com or sales@example.co.uk for further information."
pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
matches3 = re.findall(pattern, text)
print(matches3)

text = "The event is scheduled for 23-08-2023 or 23/08/2023."
pattern = r"\b\d{2}[-/]\d{2}[-/]\d{4}\b"
matches4 = re.findall(pattern, text)
print(matches4)

text = "Call us at +1-800-555-1234 or (123) 456-7890."
pattern = r"\+?\d{1,3}[-.\s]?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}"
matches5 = re.findall(pattern, text)
print(matches5)

text = "Visit our website at https://www.example.com or http://example.org for more information."
pattern = r"https?://(?:www\.)?[a-zA-Z0-9./]+"
matches6 = re.findall(pattern, text)
print(matches6)

text = "The server is located at 192.168.1.1 and the backup server is at 10.0.0.254."
pattern = r"\b(?:\d{1,3}\.){3}\d{1,3}\b"
matches7 = re.findall(pattern, text)
print(matches7)

