# 🏋️ Weight Converter

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

A lightweight Python utility that effortlessly converts weight between kilograms (kg) and pounds (lbs).

## ✨ Features

- 🔄 Seamless conversion between kg and lbs
- 🔧 Simple and intuitive user interface
- 🚀 Instant calculation with accurate results

## 📋 Requirements

- Python 3.x

## 🚀 Installation

```bash
# Clone the repository
git clone https://github.com/Naeem-360/weight-converter.git

# Navigate to the project directory
cd weight-converter
```

## 💻 Usage

Run the script using Python:

```bash
python weight_converter.py
```

## 📝 Example

```
Weight: 70
(K)g or (L)bs: K
Weight in Lbs: 154.0

Weight: 154
(K)g or (L)bs: L
Weight in Kg: 69.3
```

## 🧮 How It Works

The script uses the following conversion formula:
- 1 kg = 2.2 lbs

## 📄 Source Code

```python
weight = int(input("Weight: "))
unit = input("(K)g or (L)bs: ")
if unit.upper() == "L":
    converted = weight / 2.2
    print("Weight in Kg: ", converted)
else:
    converted = weight * 2.2
    print("Weight in Lbs: ", converted)
```

## 📝 Notes

- The script accepts weight as an integer input
- Unit selection is case-insensitive (both 'k' and 'K' work for kilograms)
- Results are displayed with floating-point precision

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/yourusername/weight-converter/issues).

## 📜 License

This project is [MIT](https://opensource.org/licenses/MIT) licensed.


