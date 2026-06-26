"""
SIWES Week 1-2: Object-Oriented Programming & Feature Engineering Logic
Author: Chibuike
Description: Enhancing the DataRecord class to automatically compute academic
             standing (honors classification) based on numerical CGPA thresholds.
"""

class DataRecord:
    def __init__(self, record_id: int, student_name: str, raw_cgpa: str):
        self.record_id = record_id
        self.student_name = self.clean_name(student_name)
        self.cgpa = self.normalize_cgpa(raw_cgpa)
        # Automatically compute academic standing upon creation
        self.academic_standing = self.get_academic_standing()

    def clean_name(self, name: str) -> str:
        """Removes trailing whitespaces and capitalizes the name properly."""
        if not name:
            return "Unknown Student"
        return name.strip().title()

    def normalize_cgpa(self, raw_cgpa: str) -> float:
        """Converts raw string CGPA to float and handles anomalies or missing values."""
        try:
            cleaned_value = float(raw_cgpa)
            if 0.0 <= cleaned_value <= 5.0:
                return round(cleaned_value, 2)
            else:
                return 0.0
        except (ValueError, TypeError):
            return 0.0

    def get_academic_standing(self) -> str:
        """
        Applies conditional rules to classify the student's academic tier.
        This represents basic rule-based feature engineering.
        """
        if self.cgpa >= 4.50:
            return "First Class (Honors List)"
        elif self.cgpa >= 3.50:
            return "Second Class Upper"
        elif self.cgpa >= 2.40:
            return "Second Class Lower"
        elif self.cgpa > 0.0:
            return "Third Class / Pass"
        else:
            return "Undetermined / Academic Probation"

    def display_summary(self):
        """Prints a structured summary of the processed data record."""
        print(f"ID: {self.record_id} | Name: {self.student_name:<20} | CGPA: {self.cgpa:<5} | Standing: {self.academic_standing}")


# --- TEST EXECUTION AREA ---
if __name__ == "__main__":
    print("--- Running Enhanced Data Processing Ingestion Pipeline ---\n")

    dirty_dataset = [
        {"id": 1, "name": "Chibuike Okeke  ", "cgpa": "4.57"},
        {"id": 2, "name": "Amadi Blessing", "cgpa": "3.8"},
        {"id": 3, "name": "Tunde Bakare ", "cgpa": "invalid_data_point"},
        {"id": 4, "name": "Ngozi Obi", "cgpa": "6.2"}, # High but invalid, goes to probation/0.0
        {"id": 5, "name": "Chioma Nwachukwu", "cgpa": "4.45"}
    ]

    processed_records = []

    for data in dirty_dataset:
        record = DataRecord(
            record_id=data["id"],
            student_name=data["name"],
            raw_cgpa=data["cgpa"]
        )
        processed_records.append(record)

    print("--- Final Cleaned Database Output ---")
    for record in processed_records:
        record.display_summary()