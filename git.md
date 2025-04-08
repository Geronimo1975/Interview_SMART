# Crearea unui repository GitHub din terminal cu GitHub CLI (gh)

## Instalare GitHub CLI

Pentru a crea repository-ul direct din terminal, folosim GitHub CLI (`gh`).

### Pasul 1: Instalează GitHub CLI (dacă nu este instalat):
```bash
sudo apt install gh
```

### Pasul 2: Autentificare GitHub CLI
```bash
gh auth login
```
- Alege **GitHub.com**
- Alege **HTTPS**
- Alege **Paste an authentication token**
- Introdu token-ul GitHub

---

## Creare repository direct din terminal

### Pasul 1: Navighează în directorul proiectului
```bash
cd /cale/catre/proiectul-tau
```

### Pasul 2: Inițializează Git
```bash
git init
```

### Pasul 3: Adaugă toate fișierele în staging
```bash
git add .
```

### Pasul 4: Fă un commit
```bash
git commit -m "Primul commit"
```

### Pasul 5: Creează repository-ul pe GitHub
```bash
gh repo create Interview_SMART --public --source=. --remote=origin
```
- **--public**: Repository public (folosește `--private` pentru privat)
- **--source=.**: Folosește directorul curent
- **--remote=origin**: Setează remote-ul

### Pasul 6: Trimite fișierele pe GitHub
```bash
git push -u origin main
```

## Verificare
Accesează repository-ul pe GitHub pentru a vedea fișierele încărcate:
```
https://github.com/geronimo1975/Interview_SMART
```

Dacă întâmpini probleme sau ai nevoie de alte sugestii, spune-mi! 😊🚀

