Employee Payslip Generator and Email Sender
This project generates PDF payslips for employees and automatically emails them their payslips using Python.

Features
Create personalized PDF payslips for each employee.

Automatically email the generated payslips to employees.

Calculates net salary (basic salary + allowances - deductions).

Saves all generated payslips in a local folder (Payslips/).

Tech Stack
Python 3

Pandas - for data manipulation.

FPDF - for PDF generation.

smtplib, ssl, email - for sending emails.

Installation
Clone this repository or download the script.

Install required Python libraries:

bash
Copy
Edit
pip install pandas fpdf
Set up your Gmail account:

Use an App Password if you have 2FA enabled on your Gmail account.

Update your EMAIL_SENDER and EMAIL_PASSWORD in the script.

Make sure "Less secure app access" is enabled (if not using App Passwords). (App Passwords recommended)

How It Works
Load Employee Data:

A sample employee dataset is created within the script using a pandas DataFrame.

Each employee has details like ID, name, email, basic salary, allowances, and deductions.

Generate Payslips:

For each employee, a PDF payslip is generated summarizing their salary details.

Payslips are saved in the Payslips/ directory.

Send Payslips via Email:

Each employee (with a valid email) receives their payslip as an email attachment.

Error Handling:

If an employee email is missing, the script will skip sending an email to them.

Project Structure
bash
Copy
Edit
.
├── Payslips/               # Generated payslips saved here
├── script.py               # Main Python script (your provided code)
├── README.md               # Project documentation
Important Notes
Credentials Safety: Never hard-code real email credentials in your production code. Use environment variables or configuration files.

Email Deliverability: Some emails may land in the Spam folder if sent in bulk.

Empty Email Addresses: The script gracefully skips employees without an email.

Sample Output
A PDF payslip will look like:

yaml
Copy
Edit
Alees Company
PAYSLIP

Name: John Doe
Employee ID: 20-A001
Email: john@example.com

Description      Amount ($)
Basic Salary     500.00
Allowances       50.00
Deductions       5.00
Net Salary       545.00

Thank you for your dedication!
License
This project is open-source and free to use!