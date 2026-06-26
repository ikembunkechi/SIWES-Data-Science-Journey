"""
SIWES Week 1: Object-Oriented Programming for Data Preprocessing
Author: Chibuike
Description: A script demonstrating how to use Python classes to encapsulate
             and clean raw data fields before analysis.
"""

class DataRecord:
    def __init__(self, record_id: int, student_name: str, raw_cgpa: str):
        self.record_id = record_id
        # Clean the name string immediately on instantiation
        self.student_name = self.clean_name(student_name)
        # Normalize the CGPA to a float value
        self.cgpa = self.normalize_cgpa(raw_cgpa)

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
                print(f"[Warning] Out-of-bounds CGPA detected for ID {self.record_id}: {raw_cgpa}")
                return 0.0
        except (ValueError, TypeError):
            print(f"[Error] Invalid numeric data format for ID {self.record_id}: '{raw_cgpa}'")
            return 0.0

    def display_summary(self):
        """Prints a structured summary of the processed data record."""
        print(f"Record [{self.record_id}] | Student: {self.student_name} | Cleaned CGPA: {self.cgpa}")


# --- TEST EXECUTION AREA ---
if __name__ == "__main__":
    print("--- Simulating Raw Ingestion Pipeline ---\n")

    # Raw, dirty dataset simulating real-world user or database inputs
    dirty_dataset = [
        {"id": 1, "name": "Chibuike Okeke  ", "cgpa": "4.57"},
        {"id": 2, "name": "Amadi Blessing", "cgpa": "3.8"},
        {"id": 3, "name": "Tunde Bakare ", "cgpa": "invalid_data_point"},  # Missing/corrupted data
        {"id": 4, "name": "Ngozi Obi", "cgpa": "6.2"},                        # Out-of-bounds anomaly
    ]

    processed_records = []

    # Iterating through dirty data and instantiating our OOP DataRecord objects
    for data in dirty_dataset:
        record = DataRecord(
            record_id=data["id"],
            student_name=data["name"],
            raw_cgpa=data["cgpa"]
        )
        processed_records.append(record)

    print("\n--- Processed & Cleaned Records ---")
    for record in processed_records:
        record.display_summary()