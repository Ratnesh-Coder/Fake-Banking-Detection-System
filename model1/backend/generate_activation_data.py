import hashlib

# ==========================================================
# Generate I from h1.py
# ==========================================================

with open("../frontend/modules/h1.py", "rb") as f:
    h1_data = f.read()

I = hashlib.sha256(h1_data).hexdigest()

# ==========================================================
# Generate J from h2.py
# ==========================================================

with open("modules/h2.py", "rb") as f:
    h2_data = f.read()

J = hashlib.sha256(h2_data).hexdigest()

# ==========================================================
# Generate Signature
# ==========================================================

SIGNATURE = hashlib.sha256(
    (I + J).encode()
).hexdigest()

# ==========================================================
# Update config.py
# ==========================================================

config_path = "config.py"

with open(config_path, "w") as f:
    f.write(f'ORIGINAL_HASH = "{I}"\n')

# ==========================================================
# Update h2_hash.txt
# ==========================================================

with open("storage/h2_hash.txt", "w") as f:
    f.write(J)

# ==========================================================
# Update frontend signature
# ==========================================================

with open("../frontend/signature.txt", "w") as f:
    f.write(SIGNATURE)

# ==========================================================
# Success Message
# ==========================================================

print("=" * 60)
print(" Authentication Data Generated Successfully ")
print("=" * 60)

print(f"\n✓ ORIGINAL_HASH updated in config.py")
print(f"✓ h2_hash.txt updated")
print(f"✓ signature.txt updated")

print("\nGenerated Values")
print("-" * 60)

print("I         :", I)
print("J         :", J)
print("SIGNATURE :", SIGNATURE)

print("\nSystem is ready for execution.")
print("=" * 60)