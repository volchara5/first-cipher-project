# Caesar Cipher Encryptor & Decryptor 🔐

A simple Python CLI tool to encrypt and decrypt text using the classic Caesar cipher. It supports both Russian and English alphabets.

## ✨ Features
- Full support for Russian and English letters.
- Circular shift protection via the `%` operator (loops from 'я' back to 'а').
- Preserves spaces, punctuation marks, and special characters without changes.

## 🚀 How to Run
1. Make sure you have Python 3 installed.
2. Download the Python script and run it via terminal:
   ```bash
   python main.py
   ```

## 📝 Examples
**Encryption (Шифрование):**
- Input text: `Привет, мир!`
- Shift step: `2`
- Result: `Рстгёф, окт!`

**Decryption (Дешифрование):**
- Input text: `Фнпн Спттйя ож рпоауэ`
- Shift step: `1` (in decryption mode)
- Result: `Умом Россию не понять`

## 🛠 Technologies Used
- Python 3.x
- `.isalpha()` method for character filtering
- Modulo operator `%` for alphabet boundaries wrap-around
