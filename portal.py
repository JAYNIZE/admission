import os

# Directory to store uploaded files and data
UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def save_admission_data(data):
    """Save student admission data to a file."""
    with open('admissions.txt', 'a') as file:
        file.write(f"{data}\n")

def save_file(file_name, file_content):
    """Save uploaded files."""
    file_path = os.path.join(UPLOAD_FOLDER, file_name)
    with open(file_path, 'wb') as file:
        file.write(file_content)
    print(f"File saved: {file_path}")

def handle_form_submission():
    """Simulate handling a student admission form."""
    print("=== Student Admission Portal ===")
    
    # Collect student details
    name = input("Full Name: ")
    email = input("Email: ")
    phone = input("Phone Number: ")
    national_id = input("National ID (Optional): ")
    password = input("Password: ")
    age = input("Age: ")
    gender = input("Gender (Male/Female/Other): ")
    department = input("Department: ")
    course = input("Course: ")
    medical_info = input("Medical Issues (if any, leave blank if none): ")
    
    # Simulate file uploads
    photo_filename = input("Profile Photo (optional, enter file name or leave blank): ")
    if photo_filename:
        # Simulate file content
        save_file(photo_filename, b"This is the simulated photo content")
    knec_filename = input("KNEC Certificate or Result Slip (required, enter file name): ")
    if knec_filename:
        # Simulate file content
        save_file(knec_filename, b"This is the simulated KNEC content")
    
    # Save all data into a text file
    admission_data = {
        "Name": name,
        "Email": email,
        "Phone": phone,
        "National ID": national_id,
        "Password": password,
        "Age": age,
        "Gender": gender,
        "Department": department,
        "Course": course,
        "Medical Info": medical_info,
        "Photo": photo_filename if photo_filename else "No photo uploaded",
        "KNEC Certificate": knec_filename if knec_filename else "No certificate uploaded",
    }
    
    save_admission_data(admission_data)
    print("\nForm submission successful! Data saved.")

if __name__ == "__main__":
    handle_form_submission()