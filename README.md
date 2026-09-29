# 🔐 Fake Banking Detection System

### Secure APK Verification and Integrity Detection System

The **Fake Banking Detection System** is a security-focused prototype designed to detect unauthorized or modified banking applications by verifying the integrity and authenticity of application components before execution.

The project explores a secure client-server verification mechanism in which an application's executable components are divided into separate parts and verified using **cryptographic hashing, nonces, RSA signatures, and server-side validation**.

---

## 🎯 Problem Statement

Fake and modified banking applications can be used to imitate legitimate applications and potentially compromise sensitive user information.

A traditional application launch does not necessarily provide a mechanism for a remote server to verify that the application code running on the client has not been modified.

This project explores a mechanism in which the application must successfully pass multiple integrity and authenticity checks before the protected application component is released and executed.

---

## 💡 Proposed Solution

The system divides the application into two components:

```text
H1 → Initial verification component
H2 → Protected application component
```

The client first sends information derived from **H1** to the server.

The server verifies the integrity of H1 before allowing the client to obtain H2.

The second model extends this process by introducing:

- Nonce-based challenge-response verification
- SHA-256 hashing
- RSA-based digital signatures
- Public/private key cryptography
- H2 integrity verification

This creates a multi-stage verification process before the final application component is executed.

---

# 🧩 System Models

## Model 1 — Hash-Based Verification

The first model uses cryptographic hashing to verify the integrity of the initial application component.

### Verification Flow

```text
                         CLIENT
                           │
                           │
                           ▼
                         H1.py
                           │
                      SHA-256(H1)
                           │
                           ▼
                     Hash of H1 (I')
                           │
                           │
                           ▼
                         SERVER
                           │
                  Compare I' with I
                           │
                     ┌─────┴─────┐
                     │           │
                   Match      Mismatch
                     │           │
                     ▼           ▼
                Generate J     Reject
                     │
                     ▼
               Send H2 + J
                     │
                     ▼
                  CLIENT
                     │
                  SHA-256(H2)
                     │
                     ▼
                    J'
                     │
              Compare J' with J
                     │
                ┌────┴────┐
                │         │
              Match    Mismatch
                │         │
                ▼         ▼
         Generate KEY    Reject
                │
                ▼
        Verify Signature
                │
           ┌────┴────┐
           │         │
         Valid     Invalid
           │         │
           ▼         ▼
      Application   Reject
       Activated
```

---

# 🔒 Model 2 — Nonce and Signature-Based Verification

Model 2 extends the first model by adding a **nonce-based challenge-response mechanism** and **RSA digital signatures**.

### Verification Flow

```text
                         CLIENT
                           │
                           │
                           ▼
                    Request NONCE
                           │
                           ▼
                         SERVER
                           │
                    Generate NONCE
                           │
                           ▼
                      Send NONCE
                           │
                           ▼
                         CLIENT
                           │
                      H1 + NONCE
                           │
                      SHA-256(...)
                           │
                           ▼
                       RESPONSE
                           │
                           │
                           ▼
                         SERVER
                           │
                  Verify RESPONSE
                           │
                     ┌─────┴─────┐
                     │           │
                   Valid       Invalid
                     │           │
                     ▼           ▼
                Send H2 + J     Reject
                     │
                     ▼
                    CLIENT
                     │
                  SHA-256(H2)
                     │
                     ▼
                    J'
                     │
              Compare J' with J
                     │
                ┌────┴────┐
                │         │
              Match    Mismatch
                │         │
                ▼         ▼
              Valid      Reject
                │
                ▼
               SERVER
                │
          Generate KEY using
       HMAC(Server_Secret, I' || J)
                │
                ▼
             Send KEY
                │
                ▼
              CLIENT
                │
        Load APK Signature
                │
                ▼
       Verify RSA Signature
                │
           ┌────┴────┐
           │         │
         Valid     Invalid
           │         │
           ▼         ▼
        Merge H1    Reject
          + H2
           │
           ▼
      Final Application
           │
           ▼
     Activate Banking
        Features
           │
           ▼
     Session Management
           │
       ┌───┴────┐
       │        │
     Valid    Expired
       │        │
       ▼        ▼
   Continue   Terminate
```

---

## 🔑 Cryptographic Components

### SHA-256

SHA-256 is used to calculate cryptographic hashes of application components.

For example:

```text
H1 → SHA-256 → I'
H2 → SHA-256 → J'
```

The calculated hashes are compared with trusted values maintained by the server.

---

### Nonce

A **nonce** is a randomly generated value used for challenge-response authentication.

The server generates a nonce:

```text
NONCE
```

The client then calculates:

```text
RESPONSE = SHA256(H1 || NONCE)
```

The server verifies the response before continuing the verification process.

The use of a fresh nonce is intended to prevent simple replay of a previously captured response.

---

### RSA Digital Signature

Model 2 also contains an RSA public/private key pair.

The server uses its private key to generate a digital signature, while the client uses the corresponding public key to verify it.

Conceptually:

```text
Server Private Key
        │
        ▼
     Signing
        │
        ▼
    Signature
        │
        ▼
     Client
        │
        ▼
Public Key Verification
```

---

### Model 1

Uses:

- SHA-256 hashing
- H1 verification
- H2 hash verification
- Client-server communication
- Streamlit frontend

### Model 2

Adds:

- Nonce generation
- Challenge-response verification
- RSA key pair
- Digital signatures
- H1 verification
- H2 verification
- Final application verification

---

# 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| **Python** | Core implementation |
| **Flask** | Backend API |
| **Streamlit** | Frontend/demo interface |
| **SHA-256** | Integrity hashing |
| **RSA** | Digital signatures |
| **Cryptographic keys** | Authentication and verification |
| **HTTP/REST APIs** | Client-server communication |

---

---

# 🚀 Getting Started

## Prerequisites

Install:

- Python 3
- pip
- Git

Verify Python:

```bash
python --version
```

Verify pip:

```bash
pip --version
```

---

## Model 1

Navigate to the Model 1 backend:

```bash
cd model1/backend
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

Start the backend:

```bash
python app.py
```

Open another terminal and navigate to:

```bash
cd model1/frontend
```

Install the frontend dependencies:

```bash
pip install -r requirements.txt
```

Run Streamlit:

```bash
streamlit run streamlit_app.py
```

---

## Model 2

Navigate to:

```bash
cd model2
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Start the backend:

```bash
cd backend
python app.py
```

In another terminal:

```bash
cd frontend
streamlit run streamlit_app.py
```

---

# 🎯 Project Objective

The main objective of this project is to demonstrate how cryptographic integrity checks and client-server verification can be combined to detect modified or unauthorized application components.

The project explores a layered verification approach rather than relying on a single hash comparison.

---

# ⚠️ Project Status

**Research / Security Prototype**

This project is an experimental security prototype intended for learning, demonstration, and further development.

It should **not be considered a production-ready banking security solution** without additional security analysis, threat modeling, secure key management, hardened communication, platform-level protections, and independent security testing.

---

# 🔐 Security Considerations

The project contains cryptographic demonstration material, including RSA keys.

**Never commit private keys to a public GitHub repository.**

Before publishing this project publicly:

1. Remove any private key such as `private.pem`.
2. Generate a new key pair.
3. Store private keys outside the repository.
4. Add private-key paths to `.gitignore`.
5. Do not commit passwords, tokens, or other secrets.

Example:

```gitignore
# Private cryptographic keys
*.pem

# Python cache
__pycache__/
*.pyc

# Environment variables
.env
```

---

# 📚 Concepts Demonstrated

This project provides practical implementation experience with:

- Application integrity verification
- Cryptographic hashing
- SHA-256
- Nonce-based challenge-response
- Client-server authentication concepts
- RSA public-key cryptography
- Digital signatures
- Secure component delivery concepts
- Flask REST APIs
- Streamlit interfaces
- Python application architecture

---

# 👨‍💻 Author

**Ratnesh**

Engineering Student

GitHub:  
https://github.com/Ratnesh-Coder

---

## 📄 License

This project is currently maintained as a personal/student security research project.
