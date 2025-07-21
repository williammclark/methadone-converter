# Morphine Equivalent Methadone Dosage Conveter

A simple Python library for calculating opioid dosage conversions based on the mathematical formula presented by **Fudin et al.** in *The Journal of Pain Research*.

## 📘 Background

This library implements a nonlinear formula for morphine equivalent dose conversion, originally proposed in:

> Fudin, J., et al. (2015). Mathematical Model for Methadone Conversion Examined. *Journal of Pain Research*, 8, 753–755. https://doi.org/10.2147/JPR.S95209

The formula accounts for nonlinear pharmacokinetics at higher doses, improving upon linear conversion tables.

## Formula
The following formula is applied:
<img width="778" height="120" alt="image" src="https://github.com/user-attachments/assets/5f10db62-43b6-425d-a152-a4691f9f90fb" />

Where x is the oral morphine equivalent dose.

## Disclaimer
This tool is provided for educational and research purposes only. It is not a substitute for professional medical advice, diagnosis, or treatment. Always consult a licensed healthcare provider for decisions involving opioid conversion.

## License
MIT
