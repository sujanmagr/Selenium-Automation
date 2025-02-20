import random
courses=["QA", "MERN", "Cyber security", "Web Devlopment", "SEO"]
def random_courses():
    return random.choice(courses)
subject=random_courses()
print(subject)