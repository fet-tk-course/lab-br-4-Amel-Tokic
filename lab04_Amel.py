# Ime: Amel
# Datum: 25.03.2026.
# Lab 4 --- Python za FastAPI

from unittest import result


student = [
    {"ime": "Amina", "godina": 3, "email": "amina.aa@untz.ba", "aktivan": True},
    {"ime": "Amel", "godina": 2, "email": "amel.tokic@untz.ba", "aktivan": True},
    {"ime": "Adnan", "godina": 1, "email": "adnan.bb@untz.ba", "aktivan": True}
]

def ispisni_poziv (func):
    def wrapper(*args, **kwargs):
        print(f"POzivam: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@ispisni_poziv
def get_student_info(name: str, year: int, email: str) -> dict:
    return {
        "ime": name,
        "godina": year,
        "email": email,
        "greeting": f"Hello {name}, vi ste {year} godina studija"
    }


    # for s in student:
    #     print(s)


    # for s in student:
    #     print(s["ime"])


#FUnkcija za greeting
# result = get_student_info("Amel", 3, "amel.tokic@untz.ba")
# print(result)

rezultat = get_student_info("Amel", 3, "amel.tokic@untz.ba")
print(rezultat)

#Dodavanje klase 

class Course:
    def __init__(self, name: str, code: str, credits: int, professor: str):
        self.name = name
        self.code = code
        self.credits = credits
        self.professor = professor

    def description(self) -> str:
        return f"{self.code} - {self.name} ({self.credits} kredita) - Profesor: {self.professor}"

course1 = Course("Signali i sistemi", "SS101", 3, "Dr. Amel")
course2 = Course("Baze podataka", "BP202", 4, "Dr. Amina")

print(course1.description())
print(course2.description())

###Zadatak samostalno
print ("\n\n")

# Lista od 4 studenta
students = [
    {"ime": "Amina", "godina": 3, "email": "amina.aa@untz.ba"},
    {"ime": "Amel", "godina": 2, "email": "amel.tokic@untz.ba"},
    {"ime": "Adnan", "godina": 1, "email": "adnan.bb@untz.ba"},
    {"ime": "Fatima", "godina": 2, "email": "fatima.cc@untz.ba"}
]

def filter_by_year(students, year):
    return [s for s in students if s["godina"] == year]

def print_registry(students):
    for student in students:
        print(f"{student['ime']}, {student['email']}")

# Ispis rezultata

print("Studenti druge godine:")
year_2_students = filter_by_year(students, 2)
print_registry(year_2_students)

print("\nSvi studenti:")
print_registry(students)
