# Interview_SMART

Un sistem inteligent pentru intervievare, traducere și asistență automată bazată pe AI și tehnologii RAG.

**URL de acces**: [interview_smart.sudo-ai.com](https://interview_smart.sudo-ai.com)

## Despre aplicație

Interview_SMART este o platformă completă care facilitează interviurile și întâlnirile online multilingve, oferind traducere în timp real, asistență cu răspunsuri sugerate și analiza CV-urilor. Platforma utilizează tehnologii moderne de inteligență artificială, inclusiv sisteme RAG (Retrieval-Augmented Generation) și modele de procesare a limbajului natural pentru a oferi o experiență de comunicare optimizată în context internațional.

## Caracteristici principale

### Traducere și asistență lingvistică
- Captare voce și detectare automată a limbii
- Traducere în timp real prin DeepL API
- Afișare text original și traducere simultană
- Suport inițial pentru Germană-Engleză, cu planuri de extindere

### Sistem de interviu inteligent
- Analiză CV și recomandări personalizate
- Generare de scrisori de intenție
- Simulator de preinterviu
- Sugestii de răspunsuri bazate pe documentație
- Programare și management interviuri

### Sistem RAG bazat pe documente
- Încărcare și procesare documente PDF
- Indexare și căutare semantică
- Extragere informații relevante pentru întrebări
- Generare răspunsuri fundamentate

### Managementul utilizatorilor
- Înregistrare și autentificare (email, social media, GitHub)
- Dashboard administrator
- Dashboard utilizator cu statistici și progres
- Management de interviuri și teste

## Tehnologii utilizate

- **Backend**: Django, Django REST Framework
- **Frontend**: React
- **Bază de date**: PostgreSQL
- **AI și ML**: HuggingFace Transformers, Sentence Transformers
- **Procesare PDF**: PyMuPDF, PyPDF2
- **Traducere**: DeepL API
- **Speech-to-Text**: (Google Speech API/Whisper/Web Speech API)
- **Indexare vectorială**: FAISS/Pinecone
- **Autentificare**: OAuth, JWT

## Plan de implementare

Dezvoltarea aplicației este împărțită în 5 etape principale:

### Etapa 1: Baza aplicației
- Instalare și configurare inițială
- Sistem de înregistrare/logare (email + social media + GitHub)
- Dashboard management utilizatori
- Dashboard utilizator (management interviuri, training, quiz tests, progress)
- Structură de bază pentru analiza interviurilor (CV, job, recomandări, scrisori, simulare)

### Etapa 2: Baza de date și API
- Definitivarea schemei bazei de date
- Testare API și integrări
- Sincronizare pip și dependințe
- Implementare sistem RAG pentru documente

### Etapa 3: Sistemul de traducere
- Integrare DeepL API
- Testare inițială Germană-Engleză
- Implementare și testare voice detection
- Pregătire pentru extindere la mai multe limbi

### Etapa 4: Sistemul de interviu
- Protocol acțiune-reacție
- Analiză răspunsuri
- Recomandări bazate pe documentație
- Fine-tuning și optimizare

### Etapa 5: Finalizare
- Verificare și îmbunătățire interfață
- Implementare sistem de plată
- Conformitate legală (GDPR, Cookies, T&C, Privacy Policy)
- Testare finală și lansare

## Conformitate GDPR

Aplicația respectă legislația europeană privind protecția datelor:
- Acord explicit la înregistrare
- Mecanisme de ștergere a contului și datelor
- Descărcare date personale (portabilitate)
- Politică transparentă privind stocarea datelor
- Sistem de raportare a breșelor de securitate
- Documentație completă

## Instalare și rulare

### Cerințe preliminare
- Python 3.8+
- Node.js 14+
- PostgreSQL
- Cont DeepL API

### Instalare
```bash
# Clonare repository
git clone https://github.com/username/Interview_SMART.git
cd Interview_SMART

# Configurare mediu virtual Python
python -m venv venv
source venv/bin/activate  # pe Windows: venv\Scripts\activate

# Instalare dependințe backend
pip install -r requirements.txt

# Instalare dependințe frontend
cd frontend
npm install
cd ..

# Configurare bază de date
python manage.py migrate
```

### Configurare
Creați un fișier `.env` în directorul rădăcină cu următoarele variabile:
```
DEBUG=True
SECRET_KEY=your_secret_key
DATABASE_URL=postgresql://user:password@localhost:5432/interview_smart
DEEPL_API_KEY=your_deepl_api_key
```

### Rulare pentru dezvoltare
```bash
# Rulare backend
python manage.py runserver

# Rulare frontend (într-un terminal separat)
cd frontend
npm start
```

### Deployment
Aplicația este deployată pe:
- URL: https://interview_smart.sudo-ai.com
- Infrastructură: [Specificați detalii despre server/cloud]
- CI/CD: [Specificați pipeline-ul de deployment dacă este relevant]

## Contribuție

Contribuțiile sunt binevenite! Vă rugăm să consultați fișierul CONTRIBUTING.md pentru detalii despre procesul de contribuție și standardele de cod.

## Licență

[Specificați licența aici]

## Contact

[Informații de contact]