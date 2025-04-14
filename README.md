# Payslip Generator System

A Python-based system for generating and distributing employee payslips automatically.

[![Python Version](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Security Considerations](#security-considerations)
- [Contributing](#contributing)
- [License](#license)

## Overview

This system automates the process of generating and distributing employee payslips through email. It uses pandas for data management, FPDF for PDF generation, and Python's built-in email libraries for secure email distribution.

## Features

- Automatic payslip generation for multiple employees
- Professional PDF formatting with company branding
- Secure email distribution with attachments
- Support for custom email templates
- Automatic folder organization
- Salary calculation with allowances and deductions

## Requirements

- Python 3.7+
- Required packages:
  ```bash
  pandas
  fpdf
  ```
- Email account with SMTP access

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/payslip-generator.git
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Set up environment variables:
   ```bash
   # .env file
   EMAIL_SENDER=your_email@gmail.com
   EMAIL_PASSWORD=your_app_password
   SMTP_SERVER=smtp.gmail.com
   SMTP_PORT=587
   COMPANY_NAME=Your Company Name
   PAYSLIP_FOLDER=payslips
   ```

2. Create employee data:
   ```python
   df = pd.DataFrame({
       'Employee ID': ['20-A001', '20-A002'],
       'Name and Surname': ['John Doe', 'Jane Smith'],
       'Employee Email': ['john@example.com', 'jane@example.com'],
       'Basic Salary': [5000, 6000],
       'Allowances': [500, 600],
       'Deductions': [100, 150]
   })
   ```

3. Run the system:
   ```python
   from payslip_generator import PayslipGenerator, EmailSender

   # Initialize components
   config = Config()
   generator = PayslipGenerator(config)
   sender = EmailSender(config)

   # Generate and send payslips
   for _, employee in df.iterrows():
       pdf_path = generator.create_payslip_pdf(employee)
       sender.send_payslip(employee['Employee Email'], pdf_path)
   ```

## Configuration

The system uses environment variables for configuration. Create a `.env` file in the project root with your settings.

### Email Configuration

- `EMAIL_SENDER`: Your email address
- `EMAIL_PASSWORD`: Your email password (preferably an app password)
- `SMTP_SERVER`: SMTP server address
- `SMTP_PORT`: SMTP server port

### System Configuration

- `COMPANY_NAME`: Your company name
- `PAYSLIP_FOLDER`: Output folder for generated payslips

## Security Considerations

1. Email Credentials:
   - Use environment variables for sensitive information
   - Never commit credentials to version control
   - Consider using app passwords instead of regular passwords

2. Data Security:
   - Employee data should be handled according to privacy regulations
   - PDFs are stored locally in the specified folder
   - Email attachments are sent securely using TLS

3. File System:
  
