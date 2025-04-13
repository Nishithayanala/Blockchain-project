from blockchain import Blockchain
from record import HealthRecord

def main():
    bc = Blockchain()

    while True:
        print("\n--- Electronic Health Records (Blockchain) ---")
        print("1. Add New Health Record")
        print("2. View Blockchain")
        print("3. Validate Blockchain")
        print("5. View Patient Record by ID")  # New option added here
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            pid = input("Patient ID: ")
            name = input("Name: ")
            age = int(input("Age: "))
            diagnosis = input("Diagnosis: ")
            treatment = input("Treatment: ")

            record = HealthRecord(pid, name, age, diagnosis, treatment)
            bc.add_block(record)
            print("✔️ Record added to blockchain.")

        elif choice == "2":
            bc.print_chain()

        elif choice == "3":
            print("✅ Blockchain is valid." if bc.is_chain_valid() else "❌ Blockchain is NOT valid!")

        elif choice == "4":
            print("👋 Exiting...")
            break

        elif choice == "5":
            search_id = input("Enter Patient ID to search: ")
            record = bc.get_record_by_id(search_id)
            if record:
                     print("\n🔍 Patient Record Found:")
        # Formatted output for patient record
                     print(f"{record.name} (ID: {record.patient_id}) - {record.diagnosis} treated with {record.treatment}")
            else:
                 print("❌ No record found with that Patient ID.")

        else:
            print("❌ Invalid option. Try again.")

if __name__ == "__main__":
    main()
