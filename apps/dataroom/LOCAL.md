# Self-Hosted Data Room — Local & Production Setup (`LOCAL.md`)

## 1. Run Locally (Zero External Dependencies)
```bash
python3 apps/dataroom/server.py --port 8082
```
Open `http://127.0.0.1:8082` in your browser.
- **Stage 1 Investor View:** `http://127.0.0.1:8082/?user=investor@precursor.vc`
- **Founder Admin View:** `http://127.0.0.1:8082/?user=kj@roboticdiscipline.com`
- **Multilingual Views:** Append `&lang=de` or `&lang=fr`.

## 2. Run Automated Tests
```bash
python3 -m unittest discover -s tests -v
```
