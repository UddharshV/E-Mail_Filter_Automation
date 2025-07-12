# Git Guide for Email Filter ML Project

## 🎯 Overview

This guide helps you maintain a clean, professional git repository while keeping your personal development notes separate.

## 📁 What Gets Committed vs. Ignored

### ✅ **Will Be Committed (Professional Files)**
- `README.md` - Project overview
- `GETTING_STARTED.md` - Setup instructions
- `PROJECT_ASSESSMENT.md` - Project analysis
- `requirements.txt` - Dependencies
- `src/` - Source code
- `notebooks/` - Jupyter notebooks
- `data/sample_emails.csv` - Sample data
- `models/__init__.py` - Model package
- `outputs/README.md` - Outputs documentation
- `.gitignore` - Git ignore rules

### ❌ **Will Be Ignored (Personal/Development Files)**
- `outputs/*.csv` - Model predictions
- `outputs/*.png` - Generated charts
- `*.pkl`, `*.joblib` - Large model files
- `data/real_emails/` - Personal email data
- `notes/` - Personal notes
- `TODO.md` - Personal todos
- `*.log` - Log files
- `.venv/` - Virtual environment
- `.DS_Store` - OS files

## 🚀 Daily Git Workflow

### **Manual Git Commands (Recommended)**
```bash
# Check what's changed
git status

# Add all files (respecting .gitignore)
git add .

# Commit with a message
git commit -m "Update: 2024-01-15 - Added feature engineering module"

# Push to remote (if you have one)
git push origin main
```

## 📝 Good Commit Messages

### ✅ **Professional Examples:**
```
"Add email preprocessing pipeline"
"Implement Naive Bayes classifier"
"Update data exploration notebook"
"Fix text cleaning function"
"Add model evaluation metrics"
```

### ❌ **Avoid These:**
```
"stuff"
"wip"
"fix"
"update"
"changes"
```

## 🏗️ Setting Up Your Repository

### **First Time Setup:**
```bash
# Initialize git repository
git init

# Add remote (if you have one)
git remote add origin <your-repo-url>

# Add all files and make first commit
git add .
git commit -m "Initial commit: Email Filter ML Project setup"
```

### **Daily Workflow:**
1. **Work on your project** (code, notebooks, etc.)
2. **Test your changes** (`python test_setup.py`)
3. **Review what will be committed** (`git status`)
4. **Add your changes** (`git add .`)
5. **Commit with descriptive message** (`git commit -m "Your message"`)
6. **Push to remote** (`git push origin main`)

## 📋 Personal Notes Strategy

### **Keep Personal Notes Separate:**
- Create a `notes/` directory (ignored by git)
- Use files like `notes/learning_log.md`
- Keep personal todos in `notes/TODO.md`
- Document experiments in `notes/experiments.md`

### **Example Personal Files (Not Committed):**
```
notes/
├── learning_log.md          # Your learning journey
├── TODO.md                  # Personal todos
├── experiments.md           # Trial and error notes
└── ideas.md                # Future feature ideas
```

## 🔍 Checking What Will Be Committed

### **Before Committing:**
```bash
# See what files are tracked
git status

# See what files are ignored
git status --ignored

# See what will be committed
git diff --cached
```

### **Common Commands:**
```bash
# View commit history
git log --oneline

# See recent changes
git diff HEAD~1

# Check if files are ignored
git check-ignore filename
```

## 🎯 Professional Repository Tips

### **Keep It Clean:**
- ✅ Commit working code only
- ✅ Use descriptive commit messages
- ✅ Keep commits focused and small
- ✅ Test before committing

### **What Makes a Good Repository:**
- Clear project structure
- Professional documentation
- Working code examples
- Clean commit history
- No personal notes or sensitive data

## 🆘 Troubleshooting

### **If Files Are Being Ignored:**
```bash
# Check if file is ignored
git check-ignore filename

# Force add if needed (be careful!)
git add -f filename
```

### **If You Committed Personal Notes:**
```bash
# Remove from last commit (but keep file)
git reset --soft HEAD~1

# Remove file from tracking
git rm --cached personal_file.md

# Commit again without personal file
git commit -m "Your message"
```

### **If You Need to Update .gitignore:**
```bash
# Remove cached files that are now ignored
git rm -r --cached .
git add .
git commit -m "Update .gitignore"
```

## 📚 Additional Resources

- **Git Documentation**: https://git-scm.com/doc
- **GitHub Guides**: https://guides.github.com/
- **Git Best Practices**: https://git-scm.com/book/en/v2

---

**Remember**: The goal is to maintain a professional, clean repository that showcases your ML skills while keeping your personal development process separate! 🚀 