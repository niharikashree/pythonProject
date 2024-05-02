#PEDESTRIAN SAFETY ANALYSIS TOOL USING CRUD OPERATIONS AND CONDUCTING SAFETY ANALYSIS WITH RECOMMENDING SAFETY IMPROVEMENT AND UPLOADING IT TO A FILE 

class SafetyReport:
    def __init__(self, report_id, date, location, description, conditions, severity):
        self.report_id = report_id
        self.date = date
        self.location = location
        self.description = description
        self.conditions = conditions
        self.severity = severity

class PedestrianSafetyTool:
    def __init__(self):
        self.reports = []
        self.analysis_id_counter = 1
        self.improvement_id_counter = 1
        self.file_name = "safety_reports.txt"

    def create_safety_report(self, date, location, description, conditions, severity):
        report_id = len(self.reports) + 1
        report = SafetyReport(report_id, date, location, description, conditions, severity)
        self.reports.append(report)
        self.update_file()
        return report

    def read_safety_reports(self):
        if not self.reports:
            print("No safety reports available.")
        else:
            print("All Safety Reports:")
            for report in self.reports:
                print(f"Report ID: {report.report_id}, Date: {report.date}, Location: {report.location}, Description: {report.description}, Conditions: {report.conditions}, Severity: {report.severity}")

    def update_safety_report(self, report_id, new_severity):
        for report in self.reports:
            if report.report_id == report_id:
                report.severity = new_severity
                self.update_file()
                print(f"Updated Safety Report - ID: {report.report_id}, Severity: {report.severity}")
                return
        print("Safety Report with given ID not found.")

    def delete_safety_report(self, report_id):
        for report in self.reports:
            if report.report_id == report_id:
                self.reports.remove(report)
                self.update_file()
                print("Safety Report deleted successfully.")
                return
        print("Safety Report with given ID not found.")

    def conduct_pedestrian_safety_analysis(self, report_id):
        for report in self.reports:
            if report.report_id == report_id:
                severity = report.severity
                print(f"Safety analysis conducted for report ID {report_id}: Severity - {severity}")
                return
        print("Safety Report with given ID not found.")

    def recommend_safety_improvement(self, report_id):
        for report in self.reports:
            if report.report_id == report_id:
                conditions = report.conditions
                print(f"Recommendation for report ID {report_id}: Conditions - {conditions}")
                return
        print("Safety Report with given ID not found.")

    def update_file(self):
        with open(self.file_name, 'w') as file:
            for report in self.reports:
                file.write(f"{report.report_id}, {report.date}, {report.location}, {report.description}, {report.conditions}, {report.severity}\n")

    def process_file(self):
        try:
            with open(self.file_name, 'r') as file:
                lines = file.readlines()
                for line in lines:
                    self.process_line(line.strip())
        except FileNotFoundError:
            print("File not found.")

    def process_line(self, line):
        parts = line.split(",")
        if len(parts) >= 6:
            report_id = int(parts[0].strip())
            date = parts[1].strip()
            location = parts[2].strip()
            description = parts[3].strip()
            conditions = parts[4].strip()
            severity = ",".join(parts[5:]).strip() 
            self.create_safety_report(date, location, description, conditions, severity)
        else:
            print("Invalid line format:", line)

    def display_menu(self):
        while True:
            print("\nMenu:")
            print("1. Read Safety Reports")
            print("2. Conduct Safety Analysis")
            print("3. Recommend Safety Improvement")
            print("4. Update Safety Report")
            print("5. Delete Safety Report")
            print("6. Create Safety Report")
            print("7. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                self.read_safety_reports()
            elif choice == '2':
                report_id = int(input("Enter Report ID for analysis: "))
                self.conduct_pedestrian_safety_analysis(report_id)
            elif choice == '3':
                report_id = int(input("Enter Report ID for recommendation: "))
                self.recommend_safety_improvement(report_id)
            elif choice == '4':
                report_id = int(input("Enter Report ID to update: "))
                new_severity = int(input("Enter New Severity: "))
                self.update_safety_report(report_id, new_severity)
            elif choice == '5':
                report_id = int(input("Enter Report ID to delete: "))
                self.delete_safety_report(report_id)
            elif choice == '6':
                date = input("Enter Date: ")
                location = input("Enter Location: ")
                description = input("Enter Description: ")
                conditions = input("Enter Conditions: ")
                severity = input("Enter Severity: ")
                self.create_safety_report(date, location, description, conditions, severity)
            elif choice == '7':
                print("Exiting program...")
                break
            else:
                print("Invalid choice. Please enter a valid option.")

tool = PedestrianSafetyTool()
tool.process_file()
tool.display_menu()
