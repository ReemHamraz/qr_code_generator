# QR Code Generator

A simple and efficient QR code generator that works in two ways:
- Command-Line Interface (CLI)
- Web Application Interface

This project allows users to generate QR codes for any text, URL, or data string, either directly from the terminal or through a lightweight web interface.

---

## Features

### CLI Version
- Generate QR codes directly from the terminal
- Save output as an image file (PNG)
- Fast, dependency-light, easy to integrate into scripts
- Supports custom output file names and paths

### Web Version
- User-friendly web UI
- Input any text or URL and download the generated QR code
- Real-time QR preview
- Simple backend built using Python

---

## Technologies Used
- Python 3.x
- qrcode / qrcode[pil]
- Flask or FastAPI (depending on your implementation)
- Pillow for image processing

---

## Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/qr-code-generator.git
cd qr-code-generator

