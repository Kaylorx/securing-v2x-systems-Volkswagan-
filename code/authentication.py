import hmac
import hashlib

SECRET_KEY = b'super_secret_key'  # Shared secret

def generate_hmac(data):
    return hmac.new(SECRET_KEY, data.encode(), hashlib.sha256).hexdigest()

def verify_hmac(data, received_hmac):
    calculated_hmac = generate_hmac(data)
    return hmac.compare_digest(calculated_hmac, received_hmac)

# Example Usage
data = "vehicle_data_string"
hmac_value = generate_hmac(data)
print("HMAC:", hmac_value)

# Verification
if verify_hmac(data, hmac_value):
    print("Data integrity verified.")
else:
    print("Data tampered!")
