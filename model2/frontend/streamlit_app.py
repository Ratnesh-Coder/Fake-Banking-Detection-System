import streamlit as st
import time
import importlib.util

from utils.nonce_client import get_nonce
from utils.hash_utils import compute_response
from utils.verify_client import verify_response
from utils.h2_client import get_h2
from utils.j_verify import verify_j
from utils.key_client import get_key
from utils.sign_verify import verify_signature

# ==========================================================
# PAGE CONFIG
# ==========================================================

st.set_page_config(
    page_title="Fake Banking APK Detection System",
    page_icon="🔐",
    layout="wide"
)

# ==========================================================
# CUSTOM CSS
# ==========================================================

st.markdown("""
<style>

.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
    max-width: 1100px;
}

div[data-testid="stExpander"] {
    border: 1px solid #333;
    border-radius: 10px;
}

</style>
""", unsafe_allow_html=True)

# ==========================================================
# SIDEBAR
# ==========================================================

with st.sidebar:

    st.title("Secure Banking APK Authentication")
    st.divider()

    st.write("Authentication Flow")
    st.write("""
            • Load h₁ 
    
            • Receive NONCE
    
            • Generate RESPONSE
    
            • Verify h₁
    
            • Download h₂
    
            • Verify h₂
    
            • Receive KEY
    
            • Verify SIGNATURE
    
            • Merge Modules
    
            • Activate Application
        """)
    st.divider()

    st.caption("### Security Layers")
    st.success("SHA256")
    st.success("NONCE")
    st.success("HMAC")
    st.success("RSA")

# ==========================================================
# HEADER
# ==========================================================

st.title("🔐 Fake Banking APK Detection System")

st.caption("### Multi-Layer Security Framework")

with st.expander("System Architecture"):
    st.code("""
            APK:
            h₁
            SIGNATURE
            Public Key

            Server:
            h₂
            I
            J
            server_secret
            Private Key
            
            Runtime:
            downloaded_h2.py
            final_apk.py
        """)

st.divider()

# ==========================================================
# BUTTON
# ==========================================================

if st.button(
    "Start Authentication",
    use_container_width=True
):

    progress = st.progress(0)

    status = st.empty()

    # ======================================================
    # STEP 1
    # ======================================================

    progress.progress(10)

    status.info(
        "Loading initial executable module..."
    )
    time.sleep(2)

    with open("modules/h1.py", "r") as f:
        h1_text = f.read()

    st.subheader("STEP 1 · Load h₁")
    st.write("The application loads the initial executable module present inside the APK.")

    with st.expander("View h₁"):
        st.code(h1_text)

    st.success("Initial executable module loaded.")
    time.sleep(2)

    # ======================================================
    # STEP 2
    # ======================================================

    progress.progress(20)

    status.info("Requesting NONCE from server...")
    time.sleep(2)

    nonce = get_nonce()

    st.subheader("STEP 2 · Receive NONCE")

    st.write("The bank server generates a fresh nonce.")
    
    st.write(
        "NONCE Length",
        f"{len(nonce)} Characters"
    )

    with st.expander("View NONCE"):
        st.code(nonce)

    st.success("NONCE received.")
    time.sleep(2)

    # ======================================================
    # STEP 3
    # ======================================================

    progress.progress(30)

    status.info("Generating RESPONSE...")
    time.sleep(2)

    response = compute_response("modules/h1.py", nonce)

    st.subheader("STEP 3 · Generate RESPONSE")

    st.write("The client computes SHA256(h₁ || NONCE).")

    col1, col2 = st.columns(2)

    with col1:
        st.write("Input")
        st.code("h₁ || NONCE")

    with col2:
        st.write("Algorithm")
        st.code("SHA256")

    with st.expander("View RESPONSE"):
        st.code(response)

    st.success("RESPONSE generated.")
    time.sleep(2)

    # ======================================================
    # STEP 4
    # ======================================================

    progress.progress(40)

    status.info("Verifying h₁ integrity...")
    time.sleep(2)

    result = verify_response(response, nonce)

    st.subheader("STEP 4 · Verify h₁")

    st.write("The server computes the expected RESPONSE and compares it with the client RESPONSE.")

    col1, col2 = st.columns(2)
    
    with col1:
        st.write("Client RESPONSE")

        with st.expander("View RESPONSE"):
            st.code(response)
    
    with col2:
        st.write("Server EXPECTED RESPONSE")

        with st.expander("View EXPECTED RESPONSE"):
            st.code(result["expected_response"])
    
    st.code("RESPONSE == EXPECTED RESPONSE")

    if not result["valid"]:
        st.error("Fake APK detected.")
        st.stop()

    st.success("h₁ integrity verified.")
    time.sleep(2)

    # ======================================================
    # STEP 5
    # ======================================================

    progress.progress(50)

    status.info("Downloading h₂...")
    time.sleep(2)

    data = get_h2()

    h2_code = data["h2"]

    j = data["j"]
    
    with open("runtime/downloaded_h2.py", "w") as f:
        f.write(h2_code)

    st.subheader("STEP 5 · Download h₂")

    st.write("The server sends the protected module h₂ and integrity hash J.")

    col1, col2 = st.columns(2)

    with col1:
        st.write("Module", "h₂")
        with st.expander("View h₂"):
            st.code(h2_code)

    with col2:
        st.write("Hash", "J")
        with st.expander("View J"):
            st.code(j)
        
    st.success("h₂ downloaded successfully.")
    time.sleep(2)

    # ======================================================
    # STEP 6
    # ======================================================

    progress.progress(60)

    status.info("Verifying integrity of h₂...")
    time.sleep(2)

    valid_j, j_prime = verify_j(h2_code, j)

    st.subheader("STEP 6 · Verify h₂")

    st.write("The client computes J' and compares it with J.")

    col1, col2 = st.columns(2)

    with col1:
        st.write("Received J")

        with st.expander("View J"):
            st.code(j)

    with col2:
        st.write("Computed J'")

        with st.expander("View J'"):
            st.code(j_prime)

    st.code("J == J'")

    if not valid_j:
        st.error("Integrity verification failed.")
        st.stop()

    st.success("h₂ integrity verified.")
    time.sleep(2)

    # ======================================================
    # STEP 7
    # ======================================================

    progress.progress(70)

    status.info("Receiving KEY from server...")
    time.sleep(2)

    key = get_key()

    st.subheader("STEP 7 · Receive KEY")

    st.write("The server generates the HMAC-based KEY and sends it to the client.")

    st.code("KEY = HMAC(server_secret, I || J)")

    with st.expander("View KEY"):
        st.code(key)

    st.success("KEY received.")
    time.sleep(2)

    # ======================================================
    # STEP 8
    # ======================================================

    progress.progress(80)

    status.info("Loading digital signature...")
    time.sleep(2)

    with open("signature.txt","r") as f:
        signature = f.read().strip()

    st.subheader("STEP 8 · Load Signature")

    st.write("The APK already contains the bank's digital signature.")

    with st.expander("View Signature"):
        st.code(signature)

    st.success("Signature loaded.")
    time.sleep(2)

    # ======================================================
    # STEP 9
    # ======================================================

    progress.progress(90)

    status.info("Verifying digital signature...")
    time.sleep(2)

    valid_signature = verify_signature(key, signature)

    st.subheader("STEP 9 · Verify Signature")
    
    st.info("Only the bank possesses the private key. The application contains only the public key.")

    st.write("The public key verifies whether the bank signed the received KEY.")

    st.code("VERIFY(public_key, SIGNATURE, KEY)")

    if not valid_signature:
        st.error("Invalid signature.")
        st.stop()

    st.success("The public key successfully verified the bank's digital signature.")
    time.sleep(2)
    
    with open("modules/h1.py", "r") as f:
        h1_code = f.read()

    with open("runtime/downloaded_h2.py", "r") as f:
        h2_downloaded = f.read()

    merged_code = (
        h1_code
        + "\n\n"
        + h2_downloaded
    )

    with open("runtime/final_apk.py", "w") as f:
        f.write(merged_code)

    # ======================================================
    # STEP 10
    # ======================================================

    progress.progress(95)

    status.info("Generate Final APK")
    time.sleep(2)
    
    st.subheader("STEP 10 · Generate Final APK")
    
    st.write("After successful signature verification, h₁ and h₂ are merged to reconstruct the complete banking application.")
    
    st.code("""
            h₁
            +
            h₂
            ↓
            final_apk.py
        """)

    with st.expander("View Final APK"):
        st.code(merged_code)
    
    st.success("Final APK generated successfully.")

    spec = importlib.util.spec_from_file_location("final_apk", "runtime/final_apk.py")

    module = importlib.util.module_from_spec(spec)

    spec.loader.exec_module(module)

    features = module.banking_features()

    st.subheader("STEP 11 · Activate Application")
    time.sleep(2)
    
    progress.progress(100)

    st.write("The verified modules are merged and the banking application becomes active.")

    for feature in features:
        st.success(feature)

    status.success("Application activated.")
    time.sleep(2)

    # ======================================================
    # SECURITY SUMMARY
    # ======================================================

    st.divider()

    st.subheader("Security Summary")

    col1, col2 = st.columns(2)

    with col1:
        st.success("h₁ Verified")
        st.success("NONCE Verified")
        st.success("h₂ Verified")

    with col2:
        st.success("HMAC Verified")
        st.success("RSA Verified")
        st.success("Application Activated")

    # ======================================================
    # FINAL STATUS
    # ======================================================

    st.divider()

    st.success("""
               ### Application Authenticated Successfully

                ✓ Integrity Verified

                ✓ Authenticity Verified

                ✓ Signature Verified

                ✓ Banking Features Activated
            """)