# record.py

class HealthRecord:
    def __init__(self, patient_id, name, age, diagnosis, treatment):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.diagnosis = diagnosis
        self.treatment = treatment

    def to_dict(self):
        return {
            'patient_id': self.patient_id,
            'name': self.name,
            'age': self.age,
            'diagnosis': self.diagnosis,
            'treatment': self.treatment
        }

    def __str__(self):
        return f"{self.name} (ID: {self.patient_id}) - {self.diagnosis} treated with {self.treatment}"
