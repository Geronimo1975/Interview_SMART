# Creating a GitHub repository from the terminal using GitHub CLI (gh)

## Installing GitHub CLI

To create the repository directly from the terminal, we use GitHub CLI (`gh`).

### Step 1: Install GitHub CLI (if not already installed):
```bash
sudo apt install gh
```

### Step 2: Authenticate with GitHub CLI
```bash
gh auth login
```
- Choose **GitHub.com**
- Choose **HTTPS**
- Choose **Paste an authentication token**
- Enter your GitHub token

---

## Creating a repository directly from the terminal

### Step 1: Navigate to your project directory
```bash
cd /path/to/your-project
```

### Step 2: Initialize Git
```bash
git init
```

### Step 3: Add all files to staging
```bash
git add .
```

### Step 4: Make a commit
```bash
git commit -m "First commit"
```

### Step 5: Create the repository on GitHub
```bash
gh repo create Interview_SMART --public --source=. --remote=origin
```
- **--public**: Public repository (use `--private` for private)
- **--source=.**: Uses the current directory
- **--remote=origin**: Sets the remote

### Step 6: Push the files to GitHub
```bash
git push -u origin main
```

## Verification
Visit the repository on GitHub to see the uploaded files:
```
https://github.com/geronimo1975/Interview_SMART
```

If you encounter any issues or need further assistance, let me know! 😊🚀

