# 🚀 Getting Started with Email Filter ML Project

## Welcome! 👋

This guide will help you set up and start your email filtering machine learning project. Even if you're new to programming and ML, you'll be able to follow along step by step.

## 📋 Prerequisites

Before we begin, make sure you have:
- **Python 3.8+** installed on your computer
- Basic familiarity with Python (we'll learn as we go!)
- Your email data ready (we'll help you export it)

## 🛠️ Step 1: Set Up Your Environment

### 1.1 Create a Virtual Environment

Open your terminal/command prompt and navigate to the project directory:

```bash
cd Email_Filter_Automation
```

Create a virtual environment (this keeps your project dependencies separate):

```bash
# On macOS/Linux:
python3 -m venv email_ml_env
source email_ml_env/bin/activate

# On Windows:
python -m venv email_ml_env
email_ml_env\Scripts\activate
```

### 1.2 Install Dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt
```

### 1.3 Verify Installation

Test that everything is working:

```bash
python -c "import pandas, numpy, sklearn; print('✅ All packages installed successfully!')"
```

## 📧 Step 2: Prepare Your Email Data

### 2.1 Export Your Emails

You have several options for getting your email data:

#### Option A: Use Sample Data (Recommended for Learning)
```bash
python src/utils/data_collector.py
```
This will create sample data to help you learn the concepts.

#### Option B: Export from Gmail
1. Go to Gmail Settings > Labels
2. Create labels for your email categories (work, personal, newsletters, etc.)
3. Manually categorize some emails (this becomes your training data)
4. Use Gmail's export feature: Settings > Accounts > Download data
5. Convert the exported data to CSV format

#### Option C: Export from Outlook
1. Open Outlook
2. File > Open & Export > Import/Export
3. Choose "Export to a file" > "Outlook Data File (.pst)"
4. Convert PST to CSV using online converters

#### Option D: Export from Apple Mail
1. Select your mailbox in Apple Mail
2. Mailbox > Export Mailbox
3. Save as .mbox file
4. Convert to CSV format

### 2.2 Data Format Requirements

Your email data should be in CSV format with these columns:
- `subject`: Email subject line
- `sender`: Sender's email address
- `content`: Email body content
- `filter_label`: Your existing email category/filter
- `date`: Email date (optional but useful)

## 🎯 Step 3: Start Learning with Jupyter Notebooks

### 3.1 Launch Jupyter

```bash
jupyter notebook
```

This will open Jupyter in your browser.

### 3.2 Open the Data Exploration Notebook

1. Navigate to the `notebooks/` folder
2. Open `01_data_exploration.ipynb`
3. Follow the notebook step by step

## 📚 Step 4: Learning Path

### Phase 1: Data Understanding (Week 1)
- **Goal**: Understand your email data
- **Activities**:
  - Load and explore your email dataset
  - Analyze email categories and distributions
  - Identify patterns in subject lines and content
  - Clean and prepare data for ML

### Phase 2: Feature Engineering (Week 2)
- **Goal**: Create features for machine learning
- **Activities**:
  - Extract text features (word counts, keywords)
  - Create sender-based features
  - Add temporal features (time of day, day of week)
  - Normalize and scale features

### Phase 3: Model Building (Week 3-4)
- **Goal**: Build and train ML models
- **Activities**:
  - Implement baseline models (Naive Bayes, SVM)
  - Train and evaluate models
  - Compare model performance
  - Tune hyperparameters

### Phase 4: Evaluation & Deployment (Week 5)
- **Goal**: Evaluate and deploy your model
- **Activities**:
  - Measure model accuracy and performance
  - Interpret model predictions
  - Create a simple email classifier
  - Document your project

## 🎓 Key Concepts You'll Learn

### Machine Learning Concepts
- **Supervised Learning**: Training models with labeled data
- **Text Classification**: Categorizing text into predefined classes
- **Feature Engineering**: Creating useful inputs for ML models
- **Model Evaluation**: Measuring how well your model performs
- **Cross-validation**: Testing model reliability

### Technical Skills
- **Python Programming**: Data manipulation with pandas
- **Data Visualization**: Creating charts with matplotlib/seaborn
- **Text Processing**: Cleaning and analyzing text data
- **Scikit-learn**: Using Python's main ML library
- **Jupyter Notebooks**: Interactive development environment

## 📈 Success Metrics

Track your progress with these metrics:
- **Data Quality**: >90% of emails have complete information
- **Model Accuracy**: >85% correct predictions on test data
- **Learning**: Understanding of each concept implemented
- **Documentation**: Clear project documentation and code comments

## 🆘 Getting Help

### Common Issues & Solutions

**Issue**: "Module not found" errors
**Solution**: Make sure your virtual environment is activated and dependencies are installed

**Issue**: Jupyter notebook won't start
**Solution**: Install jupyter: `pip install jupyter`

**Issue**: Can't export emails from Gmail
**Solution**: Use the sample data first, then work on email export later

**Issue**: Model accuracy is low
**Solution**: 
1. Check data quality
2. Try different features
3. Experiment with different algorithms
4. Get more training data

### Resources for Learning

- **Python Basics**: [Python.org Tutorial](https://docs.python.org/3/tutorial/)
- **Pandas**: [Pandas Documentation](https://pandas.pydata.org/docs/)
- **Scikit-learn**: [Scikit-learn User Guide](https://scikit-learn.org/stable/user_guide.html)
- **Machine Learning**: [Introduction to Statistical Learning](https://www.statlearning.com/)

## 🎉 Next Steps

1. **Start with the sample data** to learn the concepts
2. **Follow the notebooks** step by step
3. **Ask questions** when you get stuck
4. **Experiment** with different approaches
5. **Document** your learning journey

## 💡 Tips for Success

- **Start small**: Begin with a subset of your data
- **Iterate**: Don't expect perfection on the first try
- **Experiment**: Try different approaches and learn from failures
- **Document**: Keep notes of what works and what doesn't
- **Celebrate**: Each small success is progress!

---

**Ready to begin?** Start with Step 1 and let's build something amazing together! 🚀

Remember: Every expert was once a beginner. The key is to start and keep going! 💪 