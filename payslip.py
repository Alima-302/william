import pandas as pd
from fpdf import FPDF
import smtplib
import ssl
from email.message import EmailMessage
import os

# Your email credentials
EMAIL_SENDER = 'alimawilliam20@gmail.com'      # <-- your email here
EMAIL_PASSWORD = 'pjpj umeh bksw nkrm'       # <-- your app password here
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587

# Load your employee data
df = pd.DataFrame({
    'Employee ID': [
        '20-A001', '20-A002', '20-A003', '20-A004', '20-A005',
        '20-A006', '20-A007', '20-A008', '20-A009', '20-A010',
        '20-A011', '20-A012', '20-A013', '20-A014', '20-A015'
    ],
    'Name and Surname': [
        'Alima William', 'Tendai Dyariwa', 'Mercy Phiri', 'Reece Kurungwa', 'Lloyd Chogari',
        'Kudzai Tivache', 'Nicole Ciriboto', 'Ephraim Buruvuru', 'Florance Karindi', 'Tinashe Utetete',
        'Abdullah Ali', 'Amaan Ayaan', 'Amos Sumani', 'Maryam Saidi', 'Jameelah Witness'
    ],
    'Employee Email': [
        'alimawilliam20@gmail.com', 'tendaitasha557@gmail.com', 'memecelly12@gmail.com', 'kurungwareece@gmail.com', 'sibandaartii15@gmail.com',
        'nicolaskudzai696@gmail.com', 'ciribotonicole@mail.com', 'Eoburuvuru@gmail.com', 'florencepkarindi@gmail.com', '',
        'Aliabdulah@gamail.com', 'amaan22@gmail.com', 'samos44@mail.com', 'maryamSaidi@gmail.com', 'jamwitness@gamail.yahoo'
    ],
    'Basic Salary': [500, 150, 300, 400, 220, 320, 200, 700, 720, 800, 820, 900, 920, 940, 1000],
    'Allowances': [50, 15, 30, 40, 22, 32, 20, 70, 72, 80, 0, 0, 0, 0, 0],
    'Deductions': [5, 1.50, 3, 4, 2.20, 3.20, 2, 7, 7.20, 8, 0, 0, 0, 0, 0]
})

# Calculate Net Salary
df['Net Salary'] = df['Basic Salary'] + df['Allowances'] - df['Deductions']

# Create folder for PDFs
output_folder = 'Payslips'
os.makedirs(output_folder, exist_ok=True)

# Function to create PDF payslips
class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 16)
        self.set_text_color(0, 102, 204)  # Blue color
        self.cell(0, 10, 'Alees Company', ln=True, align='C')
        self.cell(0, 10, 'PAYSLIP', ln=True, align='C')
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, 'Thank you for your dedication!', align='C')

def create_payslip_pdf(employee_data):
    for _, row in employee_data.iterrows():
        pdf = PDF()
        pdf.add_page()

        # Employee details
        pdf.set_font('Arial', '', 12)
        pdf.set_text_color(0, 0, 0)  # Black text
        pdf.cell(0, 10, f"Name: {row['Name and Surname']}", ln=True)
        pdf.cell(0, 10, f"Employee ID: {row['Employee ID']}", ln=True)
        pdf.cell(0, 10, f"Email: {row['Employee Email']}", ln=True)
        pdf.ln(10)

        # Table style inspired by the invoice
        pdf.set_fill_color(220, 220, 220)  # Light grey background
        pdf.cell(50, 10, "Description", 1, fill=True)
        pdf.cell(50, 10, "Amount ($)", 1, ln=True, fill=True)

        pdf.cell(50, 10, "Basic Salary", 1)
        pdf.cell(50, 10, f"{row['Basic Salary']:.2f}", 1, ln=True)

        pdf.cell(50, 10, "Allowances", 1)
        pdf.cell(50, 10, f"{row['Allowances']:.2f}", 1, ln=True)

        pdf.cell(50, 10, "Deductions", 1)
        pdf.cell(50, 10, f"{row['Deductions']:.2f}", 1, ln=True)

        pdf.set_font('Arial', 'B', 12)
        pdf.cell(50, 10, "Net Salary", 1)
        pdf.cell(50, 10, f"{row['Net Salary']:.2f}", 1, ln=True)

        # Save PDF
        pdf_file_name = os.path.join(output_folder, f"{row['Employee ID']}_Payslip.pdf")
        pdf.output(pdf_file_name)
        print(f"Generated payslip for {row['Name and Surname']}")

# Generate all payslips
create_payslip_pdf(df)

# Function to send email with attachment
def send_email(receiver_email, subject, body, attachment_path):
    msg = EmailMessage()
    msg['From'] = EMAIL_SENDER
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.set_content(body)

    # Attach the PDF
    with open(attachment_path, 'rb') as f:
        file_data = f.read()
        file_name = os.path.basename(attachment_path)

    msg.add_attachment(file_data, maintype='application', subtype='pdf', filename=file_name)

    # Send the email
    context = ssl.create_default_context()
    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls(context=context)
        server.login(EMAIL_SENDER, EMAIL_PASSWORD)
        server.send_message(msg)
        print(f"Email sent to {receiver_email}")

# Send the payslips via email
for _, row in df.iterrows():
    receiver_email = row['Employee Email']
    if receiver_email:  # Send only if email exists
        employee_id = row['Employee ID']
        pdf_path = os.path.join(output_folder, f"{employee_id}_Payslip.pdf")
        subject = "Your Payslip for This Month"
        body = f"""Dear {row['Name and Surname']},

Please find attached your payslip for this month.

If you have any questions, feel free to reach out.

Best regards,
HR Department
"""
        send_email(receiver_email, subject, body, pdf_path)
    else:
        print(f"Skipping {row['Name and Surname']} (no email address).")
