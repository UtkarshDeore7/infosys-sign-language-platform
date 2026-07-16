# Experiment 001 — Baseline Random Forest

## Objective
Train a baseline Random Forest classifier on normalized ASL landmark data.

## Dataset
- Source: ASL Alphabet Dataset (Kaggle)
- Samples: 63,579
- Features: 63 (21 landmarks x 3 coordinates)
- Classes: 28 ASL signs

## Normalization Strategy
Wrist-relative coordinates scaled by maximum hand distance.

## Model
Random Forest with 100 estimators.

## Expected Outcome
Establish baseline accuracy before hyperparameter tuning.