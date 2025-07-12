#!/usr/bin/env python3
"""
Quick Start Script for Email Filter ML Project

This script provides an easy way to get started with the project.
It will help you set up your environment and begin learning.
"""

import os
import sys
import subprocess
import webbrowser
from pathlib import Path

def print_banner():
    """Print project banner."""
    print("🚀 Email Filter ML Project - Quick Start")
    print("=" * 50)
    print("Build a machine learning model to automatically")
    print("categorize your emails based on existing filters!")
    print("=" * 50)

def check_environment():
    """Check if the environment is properly set up."""
    print("🔍 Checking environment...")
    
    # Check if virtual environment is activated
    if '.venv' in sys.prefix or 'email_ml_env' in sys.prefix:
        print("✅ Virtual environment is activated")
    else:
        print("⚠️  Virtual environment not detected")
        print("   Run: source .venv/bin/activate or source email_ml_env/bin/activate")
        return False
    
    # Check if required files exist
    required_files = ['data/sample_emails.csv', 'notebooks/01_data_exploration.ipynb']
    for file_path in required_files:
        if os.path.exists(file_path):
            print(f"✅ {file_path} exists")
        else:
            print(f"❌ {file_path} missing")
            return False
    
    return True

def show_menu():
    """Show the main menu."""
    print("\n🎯 What would you like to do?")
    print("1. Start Jupyter Notebook (recommended)")
    print("2. Run data exploration")
    print("3. View project documentation")
    print("4. Test the setup")
    print("5. Exit")
    
    while True:
        try:
            choice = input("\nEnter your choice (1-5): ").strip()
            if choice in ['1', '2', '3', '4', '5']:
                return choice
            else:
                print("Please enter a number between 1 and 5")
        except KeyboardInterrupt:
            print("\n\nGoodbye! 👋")
            sys.exit(0)

def start_jupyter():
    """Start Jupyter notebook."""
    print("\n🚀 Starting Jupyter Notebook...")
    print("This will open Jupyter in your browser.")
    print("Navigate to notebooks/01_data_exploration.ipynb to begin!")
    
    try:
        # Start Jupyter in the background
        subprocess.Popen(['jupyter', 'notebook'], 
                        cwd=os.getcwd(),
                        stdout=subprocess.DEVNULL,
                        stderr=subprocess.DEVNULL)
        
        print("✅ Jupyter is starting...")
        print("📖 Opening browser in 3 seconds...")
        
        import time
        time.sleep(3)
        
        # Open browser to Jupyter
        webbrowser.open('http://localhost:8888')
        
        print("🌐 Browser should open automatically")
        print("📁 Navigate to: notebooks/01_data_exploration.ipynb")
        
    except Exception as e:
        print(f"❌ Error starting Jupyter: {e}")
        print("Try running 'jupyter notebook' manually")

def run_data_exploration():
    """Run a quick data exploration."""
    print("\n📊 Running quick data exploration...")
    
    try:
        import pandas as pd
        import matplotlib.pyplot as plt
        
        # Load sample data
        df = pd.read_csv('data/sample_emails.csv')
        
        print(f"📧 Loaded {len(df)} sample emails")
        print(f"🏷️  Categories: {list(df['filter_label'].unique())}")
        
        # Show basic statistics
        print("\n📈 Basic Statistics:")
        print(f"   - Average subject length: {df['subject'].str.len().mean():.1f} characters")
        print(f"   - Average content length: {df['content'].str.len().mean():.1f} characters")
        print(f"   - Most common category: {df['filter_label'].value_counts().index[0]}")
        
        # Show sample emails
        print("\n📋 Sample Emails:")
        for i, (_, row) in enumerate(df.head(3).iterrows(), 1):
            print(f"   {i}. {row['subject']} ({row['filter_label']})")
        
        print("\n✅ Data exploration complete!")
        print("💡 Ready to start building your ML model!")
        
    except Exception as e:
        print(f"❌ Error during data exploration: {e}")

def show_documentation():
    """Show available documentation."""
    print("\n📚 Available Documentation:")
    print("=" * 30)
    
    docs = [
        ("README.md", "Project overview and structure"),
        ("GETTING_STARTED.md", "Step-by-step setup guide"),
        ("PROJECT_ASSESSMENT.md", "Detailed project analysis"),
        ("notebooks/01_data_exploration.ipynb", "Data exploration tutorial")
    ]
    
    for doc, description in docs:
        if os.path.exists(doc):
            print(f"✅ {doc}")
            print(f"   {description}")
        else:
            print(f"❌ {doc} (missing)")
    
    print("\n💡 Tip: Open these files in your text editor to read them")

def test_setup():
    """Run the setup test."""
    print("\n🧪 Running setup test...")
    
    try:
        result = subprocess.run(['python', 'test_setup.py'], 
                              capture_output=True, text=True)
        
        if result.returncode == 0:
            print("✅ All tests passed!")
        else:
            print("❌ Some tests failed:")
            print(result.stdout)
            print(result.stderr)
            
    except Exception as e:
        print(f"❌ Error running tests: {e}")

def main():
    """Main function."""
    print_banner()
    
    if not check_environment():
        print("\n❌ Environment not ready. Please:")
        print("1. Activate virtual environment: source email_ml_env/bin/activate")
        print("2. Install dependencies: pip install -r requirements.txt")
        print("3. Run this script again")
        return
    
    print("✅ Environment is ready!")
    
    while True:
        choice = show_menu()
        
        if choice == '1':
            start_jupyter()
        elif choice == '2':
            run_data_exploration()
        elif choice == '3':
            show_documentation()
        elif choice == '4':
            test_setup()
        elif choice == '5':
            print("\n👋 Goodbye! Happy coding!")
            break
        
        if choice != '5':
            input("\nPress Enter to continue...")

if __name__ == "__main__":
    main() 