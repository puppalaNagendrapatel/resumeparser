import spacy

nlp = spacy.load('en_core_web_sm')

def extract_details(text):
    doc = nlp(text)
    details = {
        'name': None,
        'experience': [],
        'education': [],
        'skills': []
    }

    # Extract Name
    for ent in doc.ents:
        if ent.label_ == 'PERSON':
            details['name'] = ent.text
            break

    # Extract Experience, Education, and Skills
    current_section = None
    for token in doc:
        if token.text.lower() in ['experience', 'education', 'skills']:
            current_section = token.text.lower()
            details[current_section].append('')
        elif current_section:
            if token.is_punct:
                continue
            details[current_section][-1] += token.text + ' '

    return details

# Example usage
resume_text = """
Nagendra puppala
Software Engineer

Experience:
- Student at Marri Laxman Reddy Institute of Technology and Management.
- Developed web applications using Python and JavaScript.

Education:
- Bachelor of Science in Informatio Technology.

Skills:
- Python
- JavaScript
- HTML
- CSS
"""

resume_details = extract_details(resume_text)
print("Resume Details:")
print(f"Name: {resume_details['name']}")
print("Experience:")
for experience in resume_details['experience']:
    print("- " + experience.strip())
print("Education:")
for education in resume_details['education']:
    print("- " + education.strip())
print("Skills:")
for skill in resume_details['skills']:
    print("- " + skill.strip())
