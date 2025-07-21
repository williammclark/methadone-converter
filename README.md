# Morphine Equivalent Methadone Dosage Conveter

A simple Python library for calculating opioid dosage conversions based on the mathematical formula presented by **Fudin et al.** in *The Journal of Pain Research*.

## Background

This library implements a nonlinear formula for morphine equivalent dose conversion, originally proposed in:

> Fudin, J., et al. (2015). Mathematical Model for Methadone Conversion Examined. *Journal of Pain Research*, 8, 753–755. https://doi.org/10.2147/JPR.S95209

The formula accounts for nonlinear pharmacokinetics at higher doses, improving upon linear conversion tables.

## Formula
The following formula is applied:
```math
\frac{a}{b} \cdot \left\{ c - d \cdot \sin\left( \frac{e}{\left( \frac{f}{a} \right)^{h} + 1} \right) - \sin\left( \frac{e}{\left( \frac{g}{a} \right)^{h} + 1} \right) \right\}
```
Where a is the oral morphine equivalent dose.
| Symbol | Name               | Value | Description                                      |
| ------ | ------------------ | ----- | ------------------------------------------------ |
| `a`    | Input Dose         | *x*   | The oral morphine equivalent dose (MED)          |
| `b`    | Normalizing Factor | 21    ||
| `c`    | Offset Constant    | 5.7   | Base value for the conversion output             |
| `d`    | Scaling Factor     | 3     | Scales the first sine wave                       |
| `e`    | Sine Numerator     | 90    | Numerator for sine transformation                |
| `f`    | First Numerator    | 100   | Used in the first sine input calculation         |
| `g`    | Second Numerator   | 310   | Used in the second sine input calculation        |
| `h`    | Exponent           | 100   | Exponent applied in the denominator of sine args |


## Disclaimer
This tool is provided for educational and research purposes only. It is not a substitute for professional medical advice, diagnosis, or treatment. Always consult a licensed healthcare provider for decisions involving opioid conversion.

## License
MIT
