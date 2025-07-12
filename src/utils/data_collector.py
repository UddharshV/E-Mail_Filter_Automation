"""
Email Data Collection Utilities

This module provides guidance and utilities for collecting email data from various sources.
It includes functions to help export emails from different email clients.
"""

import os
import csv
import json
from typing import List, Dict, Optional
import pandas as pd


class EmailDataCollector:
    """Helper class for collecting email data from various sources."""
    
    def __init__(self, output_dir: str = "../data"):
        """
        Initialize the data collector.
        
        Args:
            output_dir: Directory to save collected data
        """
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)
    
    def create_sample_data(self) -> pd.DataFrame:
        """
        Create sample email data for testing and development.
        
        Returns:
            DataFrame with sample email data
        """
        sample_emails = [
            {
                'id': '1',
                'subject': 'Meeting tomorrow at 2pm',
                'sender': 'colleague@company.com',
                'content': 'Hi, let\'s meet tomorrow at 2pm to discuss the project. Please bring your notes.',
                'date': '2024-01-15 10:30:00',
                'filter_label': 'work'
            },
            {
                'id': '2',
                'subject': 'Weekly Newsletter - Tech Updates',
                'sender': 'newsletter@tech.com',
                'content': 'This week\'s top tech news: AI developments, new programming languages, and industry trends.',
                'date': '2024-01-15 09:00:00',
                'filter_label': 'newsletter'
            },
            {
                'id': '3',
                'subject': 'Your invoice #12345 is ready',
                'sender': 'billing@service.com',
                'content': 'Your invoice for $150.00 is ready for payment. Due date: January 30, 2024.',
                'date': '2024-01-15 08:15:00',
                'filter_label': 'billing'
            },
            {
                'id': '4',
                'subject': 'You won a prize!',
                'sender': 'spam@fake.com',
                'content': 'Congratulations! You\'ve won $1,000,000! Click here to claim your prize!',
                'date': '2024-01-15 07:45:00',
                'filter_label': 'spam'
            },
            {
                'id': '5',
                'subject': 'Project status update',
                'sender': 'manager@company.com',
                'content': 'The Q1 project is on track. We need to review the budget next week.',
                'date': '2024-01-14 16:30:00',
                'filter_label': 'work'
            },
            {
                'id': '6',
                'subject': 'Your order has shipped',
                'sender': 'orders@shop.com',
                'content': 'Your order #45678 has been shipped and will arrive in 3-5 business days.',
                'date': '2024-01-14 14:20:00',
                'filter_label': 'shopping'
            },
            {
                'id': '7',
                'subject': 'Security alert - new login',
                'sender': 'security@bank.com',
                'content': 'We detected a new login to your account. If this wasn\'t you, please contact us immediately.',
                'date': '2024-01-14 12:10:00',
                'filter_label': 'security'
            },
            {
                'id': '8',
                'subject': 'Monthly digest - AI research',
                'sender': 'research@ai.org',
                'content': 'Latest AI research papers and breakthroughs in machine learning and neural networks.',
                'date': '2024-01-14 11:00:00',
                'filter_label': 'newsletter'
            }
        ]
        
        return pd.DataFrame(sample_emails)
    
    def save_to_csv(self, df: pd.DataFrame, filename: str = "emails.csv") -> str:
        """
        Save email data to CSV file.
        
        Args:
            df: DataFrame containing email data
            filename: Name of the output file
            
        Returns:
            Path to the saved file
        """
        filepath = os.path.join(self.output_dir, filename)
        df.to_csv(filepath, index=False)
        print(f"✅ Saved {len(df)} emails to {filepath}")
        return filepath
    
    def save_to_json(self, df: pd.DataFrame, filename: str = "emails.json") -> str:
        """
        Save email data to JSON file.
        
        Args:
            df: DataFrame containing email data
            filename: Name of the output file
            
        Returns:
            Path to the saved file
        """
        filepath = os.path.join(self.output_dir, filename)
        df.to_json(filepath, orient='records', indent=2)
        print(f"✅ Saved {len(df)} emails to {filepath}")
        return filepath


def get_gmail_export_instructions() -> str:
    """
    Get instructions for exporting emails from Gmail.
    
    Returns:
        String with step-by-step instructions
    """
    return """
📧 Gmail Export Instructions:

Method 1: Using Gmail API (Recommended)
1. Go to Google Cloud Console
2. Create a new project
3. Enable Gmail API
4. Create credentials (OAuth 2.0)
5. Use the provided Python script to export emails

Method 2: Manual Export
1. Go to Gmail Settings > Labels
2. Create labels for your email categories
3. Manually categorize some emails
4. Use Gmail's export feature (Settings > Accounts > Download data)
5. Convert the .mbox file to CSV using a converter

Method 3: Using IMAP
1. Enable IMAP in Gmail settings
2. Use Python's imaplib to connect
3. Download emails and parse them
4. Save as CSV with your filter labels

Would you like me to create a script for any of these methods?
"""


def get_outlook_export_instructions() -> str:
    """
    Get instructions for exporting emails from Outlook.
    
    Returns:
        String with step-by-step instructions
    """
    return """
📧 Outlook Export Instructions:

Method 1: Export to PST
1. Open Outlook
2. Go to File > Open & Export > Import/Export
3. Choose "Export to a file"
4. Select "Outlook Data File (.pst)"
5. Choose the folder to export
6. Save the .pst file
7. Use a PST to CSV converter

Method 2: Using Python
1. Install the `exchangelib` library
2. Connect to your Exchange/Outlook account
3. Download emails programmatically
4. Save with your filter labels

Method 3: Manual Export
1. Select emails in Outlook
2. Right-click > Save As
3. Choose format (HTML, Text, etc.)
4. Convert to CSV format

Would you like me to create a script for any of these methods?
"""


def get_apple_mail_export_instructions() -> str:
    """
    Get instructions for exporting emails from Apple Mail.
    
    Returns:
        String with step-by-step instructions
    """
    return """
📧 Apple Mail Export Instructions:

Method 1: Export Mailbox
1. Open Apple Mail
2. Select the mailbox you want to export
3. Go to Mailbox > Export Mailbox
4. Choose location and save as .mbox file
5. Convert .mbox to CSV using a converter

Method 2: Using Python
1. Install the `mailbox` library
2. Parse the .mbox file
3. Extract email data
4. Save as CSV with your labels

Method 3: Manual Export
1. Select emails in Apple Mail
2. File > Export
3. Choose format (EML, PDF, etc.)
4. Convert to CSV format

Would you like me to create a script for any of these methods?
"""


def create_data_collection_script():
    """
    Create a comprehensive data collection script.
    """
    script_content = '''"""
Email Data Collection Script

This script helps you collect email data from various sources.
Run this script to get started with your email filtering ML project.
"""

import pandas as pd
import os
from utils.data_collector import EmailDataCollector

def main():
    print("📧 Email Data Collection for ML Project")
    print("=" * 50)
    
    # Initialize data collector
    collector = EmailDataCollector()
    
    print("\\n🎯 Choose your data source:")
    print("1. Create sample data (for testing)")
    print("2. Load existing CSV file")
    print("3. Get export instructions")
    
    choice = input("\\nEnter your choice (1-3): ").strip()
    
    if choice == "1":
        # Create sample data
        print("\\n🔧 Creating sample email data...")
        sample_df = collector.create_sample_data()
        
        # Save to CSV
        csv_path = collector.save_to_csv(sample_df, "sample_emails.csv")
        
        print(f"\\n✅ Sample data created successfully!")
        print(f"📁 File saved to: {csv_path}")
        print(f"📊 Dataset contains {len(sample_df)} emails")
        print(f"🏷️  Categories: {sample_df['filter_label'].unique().tolist()}")
        
        # Show sample data
        print("\\n📋 Sample data preview:")
        print(sample_df.head())
        
    elif choice == "2":
        # Load existing file
        file_path = input("\\nEnter path to your CSV file: ").strip()
        
        if os.path.exists(file_path):
            df = pd.read_csv(file_path)
            print(f"\\n✅ Loaded {len(df)} emails from {file_path}")
            print(f"📊 Columns: {df.columns.tolist()}")
            
            # Save to project data directory
            project_path = collector.save_to_csv(df, "emails.csv")
            print(f"📁 Copied to project directory: {project_path}")
        else:
            print("❌ File not found!")
            
    elif choice == "3":
        # Show export instructions
        print("\\n📧 Email Export Instructions")
        print("=" * 30)
        
        print("\\n🔍 For Gmail:")
        print(get_gmail_export_instructions())
        
        print("\\n🔍 For Outlook:")
        print(get_outlook_export_instructions())
        
        print("\\n🔍 For Apple Mail:")
        print(get_apple_mail_export_instructions())
        
    else:
        print("❌ Invalid choice!")

if __name__ == "__main__":
    main()
'''
    
    return script_content


if __name__ == "__main__":
    # Create the data collection script
    script_content = create_data_collection_script()
    
    # Save to file
    script_path = "../data_collection.py"
    with open(script_path, 'w') as f:
        f.write(script_content)
    
    print(f"✅ Created data collection script: {script_path}")
    print("Run this script to get started with your email data collection!") 