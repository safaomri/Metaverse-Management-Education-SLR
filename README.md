# Metaverse-Management-Education-SLR
This repository contains the complete materials for a systematic literature review on “Metaverse in Management Education.” The review investigates how metaverse technologies are being applied in management education, what challenges and opportunities they present, and synthesizes current knowledge to identify gaps and future research directions.

This repo contains the reproducible pipeline for second-stage screening and theoretical relevance scoring used in the IJMR SLR.

## Contents
├─ data/
│  ├─ KATI_export.xlsx              # raw export from Fraunhofer INT KATI
│  └─ included_set.xlsx             # final post-filter set (+ decisions)
├─ code/
│  ├─ 01_clean_normalize.py
│  ├─ 02_rules_filtering.py
│  ├─ 03_relevance_scoring.py
│  └─ utils.py
├─ logs/
│  ├─ prisma_counts.csv
│  └─ decisions_audit.csv
└─ environment.yml                  # or requirements.txt

## Environment
- Python 3.11
- pandas, numpy, regex, openpyxl, matplotlib

Create environment:
conda env create -f environment.yml
conda activate slr-metaverse

## Reproduce
python code/01_clean_normalize.py
python code/02_rules_filtering.py
python code/03_relevance_scoring.py

Outputs:
- logs/prisma_counts.csv – counts per rule (for PRISMA)
- logs/decisions_audit.csv – title/abstract decisions + reasons
- data/included_set.xlsx – final set for full-text synthesis

## Citation

