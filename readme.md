# Package Classifier

This project dispatches packages into the correct stacks based on their size and mass.

## Rules

- A package is **bulky** if:
  - Volume ≥ 1,000,000 cm³
  - **OR** any dimension (width, height, length) ≥ 150 cm
- A package is **heavy** if:
  - Mass ≥ 20 kg

## Dispatch Rules

- **REJECTED**: Bulky **and** Heavy
- **SPECIAL**: Bulky **or** Heavy
- **STANDARD**: Neither bulky nor heavy

## How to Run

1. Run the tests:

```bash
python test_classifier.py
