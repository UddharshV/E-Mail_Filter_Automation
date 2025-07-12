#!/usr/bin/env python3
"""
Test Setup Script for Email Filter ML Project

This script verifies that all components are working correctly.
Run this to ensure your environment is ready for development.
"""

import sys
import os

def test_imports():
    """Test that all required packages can be imported."""
    print("🔍 Testing package imports...")
    
    try:
        import pandas as pd
        print("✅ pandas imported successfully")
    except ImportError as e:
        print(f"❌ pandas import failed: {e}")
        return False
    
    try:
        import numpy as np
        print("✅ numpy imported successfully")
    except ImportError as e:
        print(f"❌ numpy import failed: {e}")
        return False
    
    try:
        import sklearn
        print("✅ scikit-learn imported successfully")
    except ImportError as e:
        print(f"❌ scikit-learn import failed: {e}")
        return False
    
    try:
        import matplotlib.pyplot as plt
        print("✅ matplotlib imported successfully")
    except ImportError as e:
        print(f"❌ matplotlib import failed: {e}")
        return False
    
    try:
        import seaborn as sns
        print("✅ seaborn imported successfully")
    except ImportError as e:
        print(f"❌ seaborn import failed: {e}")
        return False
    
    try:
        import nltk
        print("✅ nltk imported successfully")
    except ImportError as e:
        print(f"❌ nltk import failed: {e}")
        return False
    
    try:
        import jupyter
        print("✅ jupyter imported successfully")
    except ImportError as e:
        print(f"❌ jupyter import failed: {e}")
        return False
    
    return True

def test_data_loading():
    """Test that sample data can be loaded."""
    print("\n📊 Testing data loading...")
    
    try:
        import pandas as pd
        df = pd.read_csv('data/sample_emails.csv')
        print(f"✅ Sample data loaded: {len(df)} emails")
        print(f"📋 Categories: {df['filter_label'].unique()}")
        return True
    except Exception as e:
        print(f"❌ Data loading failed: {e}")
        return False

def test_email_parser():
    """Test the email parser functionality."""
    print("\n🔧 Testing email parser...")
    
    try:
        from src.utils.email_parser import EmailParser, clean_text
        parser = EmailParser()
        
        # Test text cleaning
        test_text = "Hello World! This is a TEST message."
        cleaned = clean_text(test_text)
        print(f"✅ Text cleaning works: '{cleaned}'")
        
        # Test keyword extraction
        from src.utils.email_parser import extract_keywords
        keywords = extract_keywords("This is a test message with important keywords")
        print(f"✅ Keyword extraction works: {keywords[:3]}")
        
        return True
    except Exception as e:
        print(f"❌ Email parser test failed: {e}")
        return False

def test_data_collector():
    """Test the data collector functionality."""
    print("\n📧 Testing data collector...")
    
    try:
        from src.utils.data_collector import EmailDataCollector
        collector = EmailDataCollector()
        sample_df = collector.create_sample_data()
        print(f"✅ Data collector works: {len(sample_df)} sample emails created")
        return True
    except Exception as e:
        print(f"❌ Data collector test failed: {e}")
        return False

def test_project_structure():
    """Test that project structure is correct."""
    print("\n📁 Testing project structure...")
    
    required_dirs = ['data', 'src', 'src/utils', 'src/preprocessing', 'src/evaluation', 'models', 'outputs', 'notebooks', 'config']
    required_files = ['README.md', 'requirements.txt', 'GETTING_STARTED.md', 'PROJECT_ASSESSMENT.md']
    
    for dir_path in required_dirs:
        if os.path.exists(dir_path):
            print(f"✅ Directory exists: {dir_path}")
        else:
            print(f"❌ Missing directory: {dir_path}")
            return False
    
    for file_path in required_files:
        if os.path.exists(file_path):
            print(f"✅ File exists: {file_path}")
        else:
            print(f"❌ Missing file: {file_path}")
            return False
    
    return True

def main():
    """Run all tests."""
    print("🚀 Email Filter ML Project - Setup Test")
    print("=" * 50)
    
    tests = [
        ("Package Imports", test_imports),
        ("Project Structure", test_project_structure),
        ("Data Loading", test_data_loading),
        ("Email Parser", test_email_parser),
        ("Data Collector", test_data_collector)
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        print(f"\n{'='*20} {test_name} {'='*20}")
        if test_func():
            passed += 1
            print(f"✅ {test_name} PASSED")
        else:
            print(f"❌ {test_name} FAILED")
    
    print(f"\n{'='*50}")
    print(f"📊 Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! Your environment is ready for development.")
        print("\n🚀 Next steps:")
        print("1. Run 'jupyter notebook' to start Jupyter")
        print("2. Open notebooks/01_data_exploration.ipynb")
        print("3. Follow the GETTING_STARTED.md guide")
        return True
    else:
        print("⚠️  Some tests failed. Please check the errors above.")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1) 