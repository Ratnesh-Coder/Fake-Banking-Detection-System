# # Run command: streamlit run streamlit_app.py
# # To activate venv: venv/Scripts/activate

# import streamlit as st
# import hashlib
# import importlib.util
# from utils.api_client import verify_apk

# st.title("Fake Banking APK Detection System")

# st.info("System Status: Ready for Verification")

# st.markdown("""
# ### Verification Workflow

# 1. Compute I'
# 2. Verify h₁ with Bank Server
# 3. Receive h₂ and J
# 4. Generate KEY
# 5. Verify SIGNATURE
# 6. Activate Banking Features
# """)

# if st.button("Start Verification"):

#     try:
#         with open("modules/h1.py", "rb") as f:
#             h1_data = f.read()

#         apk_hash = hashlib.sha256(h1_data).hexdigest()
        
#         result = verify_apk(apk_hash)

#         if result["status"] == "VALID":
            
#             st.success("✅ h₁ verified successfully")
            
#             J = result["j"]
            
#             KEY = hashlib.sha256(
#                 (apk_hash + J).encode()
#             ).hexdigest()
            
#             with open("signature.txt", "r") as f:
#                 SIGNATURE = f.read().strip()
            
#             with st.expander("Security Details"):
#                 st.write("Computed I':", apk_hash)
#                 st.write("Received J:", J)
#                 st.write("Generated KEY:", KEY)
#                 st.write("Stored SIGNATURE:", SIGNATURE)
            
#             if KEY == SIGNATURE:
                
#                 st.success("✅ Application Activated")
                
#                 h2_code = result["h2"]
                
#                 with open("runtime/downloaded_h2.py", "w") as f:
#                     f.write(h2_code)
                
#                 spec = importlib.util.spec_from_file_location(
#                     "downloaded_h2",
#                     "runtime/downloaded_h2.py"
#                 )
                
#                 if spec is None or spec.loader is None:
#                     st.error("Failed to load h₂ module.")
#                     st.stop()
                
#                 module = importlib.util.module_from_spec(spec)
                
#                 spec.loader.exec_module(module)
                
#                 features = module.banking_features()
                
#                 st.subheader("Activated Banking Features")
                
#                 for i, feature in enumerate(features, 1):
#                     st.success(f"{i}. {feature}")
                
#             else:
#                 st.error("❌ Activation Failed")
            
#         else:
#             st.error("❌ h₁ verification failed")

#     except Exception as e:
#         st.error(f"Error: {e}")
#         st.divider()
#         st.caption(
#             "Distributed Banking APK Authentication Framework"
#         )






import streamlit as st
import hashlib
import importlib.util
import time

from utils.api_client import verify_apk

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

.block-container{
    padding-top:2rem;
    padding-bottom:2rem;
    max-width:1100px;
}

div[data-testid="stExpander"]{
    border:1px solid #333;
    border-radius:10px;
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

• Compute I'

• Verify h₁

• Download h₂

• Generate KEY

• Verify SIGNATURE

• Activate Application

""")

    st.divider()

    st.caption("Security Layers")

    st.success("SHA256")

    st.success("RSA")

# ==========================================================
# HEADER
# ==========================================================

st.title("🔐 Fake Banking APK Detection System")

with st.expander("System Architecture"):

    st.code("""
APK:
    h₁
    SIGNATURE
    Public Key

Server:
    I
    J
    h₂
    Private Key
""")

st.divider()

# ==========================================================
# BUTTON
# ==========================================================

if st.button(
    "Start Verification",
    use_container_width=True
):

    progress = st.progress(0)

    status = st.empty()

    # ======================================================
    # STEP 1
    # ======================================================

    progress.progress(15)

    status.info(
        "Loading initial executable module..."
    )

    time.sleep(2)

    with open(
        "modules/h1.py",
        "r"
    ) as f:

        h1_text = f.read()

    st.subheader("STEP 1 · Load h₁")

    st.write(
        "The application loads the initial executable module present inside the APK."
    )

    with st.expander("View h₁"):

        st.code(h1_text)

    st.success("Initial executable module loaded.")

    time.sleep(2)

    # ======================================================
    # STEP 2
    # ======================================================

    progress.progress(30)

    status.info(
        "Computing I'..."
    )

    time.sleep(2)

    with open(
        "modules/h1.py",
        "rb"
    ) as f:

        h1_data = f.read()

    apk_hash = hashlib.sha256(
        h1_data
    ).hexdigest()

    st.subheader("STEP 2 · Compute I'")

    st.write(
        "The client computes SHA256(h₁) to generate I'."
    )

    col1, col2 = st.columns(2)

    with col1:

        st.write("Input")

        st.code("h₁")

    with col2:

        st.write("Algorithm")

        st.code("SHA256")

    with st.expander("View I'"):

        st.code(apk_hash)

    st.success("I' generated successfully.")

    time.sleep(2)

    # ======================================================
    # STEP 3
    # ======================================================

    progress.progress(45)

    status.info(
        "Verifying h₁..."
    )

    time.sleep(2)

    result = verify_apk(apk_hash)

    st.subheader("STEP 3 · Verify h₁")

    st.write(
        "The server compares the received I' with the stored hash I."
    )

    col1, col2 = st.columns(2)

    with col1:

        st.write("Client I'")

        with st.expander("View I'"):

            st.code(apk_hash)

    with col2:

        st.write("Server I")

        with st.expander("View I"):

            st.code(result["hash"])

    st.code("I == I'")

    if result["status"] != "VALID":

        st.error("Fake APK detected.")

        st.stop()

    st.success("h₁ verified successfully.")

    time.sleep(2)

    # ======================================================
    # STEP 4
    # ======================================================

    progress.progress(60)

    status.info(
        "Downloading h₂..."
    )

    time.sleep(2)

    h2_code = result["h2"]

    J = result["j"]

    with open(
        "runtime/downloaded_h2.py",
        "w"
    ) as f:

        f.write(h2_code)

    st.subheader("STEP 4 · Download h₂")

    st.write(
        "The server sends the protected module h₂ together with its integrity hash J."
    )

    col1, col2 = st.columns(2)

    with col1:

        with st.expander("View h₂"):

            st.code(h2_code)

    with col2:

        with st.expander("View J"):

            st.code(J)

    st.success("h₂ downloaded successfully.")

    time.sleep(2)
    
        # ======================================================
    # STEP 5
    # ======================================================

    progress.progress(75)

    status.info(
        "Generating KEY..."
    )

    time.sleep(2)

    KEY = hashlib.sha256(
        (apk_hash + J).encode()
    ).hexdigest()

    st.subheader("STEP 5 · Generate KEY")

    st.write(
        "The client generates the authentication KEY using the verified application hash I' and integrity hash J."
    )

    st.code(
        "KEY = SHA256(I' || J)"
    )

    with st.expander("View KEY"):

        st.code(KEY)

    st.success("KEY generated successfully.")

    time.sleep(2)

    # ======================================================
    # STEP 6
    # ======================================================

    progress.progress(90)

    status.info(
        "Loading and verifying digital signature..."
    )

    time.sleep(2)

    with open(
        "signature.txt",
        "r"
    ) as f:

        SIGNATURE = f.read().strip()

    st.subheader("STEP 6 · Verify Signature")

    st.info(
        "The APK already contains the bank's digital signature."
    )

    st.write(
        "The generated KEY is compared with the stored digital signature."
    )

    col1, col2 = st.columns(2)

    with col1:

        st.write("Generated KEY")

        with st.expander("View KEY"):

            st.code(KEY)

    with col2:

        st.write("Stored SIGNATURE")

        with st.expander("View SIGNATURE"):

            st.code(SIGNATURE)

    st.code(
        "KEY == SIGNATURE"
    )

    if KEY != SIGNATURE:

        st.error(
            "Digital signature verification failed."
        )

        st.stop()

    st.success(
        "Digital signature verified successfully."
    )

    time.sleep(2)

    # ======================================================
    # STEP 7
    # ======================================================

    progress.progress(100)

    status.info(
        "Activating banking application..."
    )

    time.sleep(2)

    spec = importlib.util.spec_from_file_location(
        "downloaded_h2",
        "runtime/downloaded_h2.py"
    )

    if spec is None or spec.loader is None:

        st.error(
            "Unable to load h₂ module."
        )

        st.stop()

    module = importlib.util.module_from_spec(
        spec
    )

    spec.loader.exec_module(
        module
    )

    features = module.banking_features()

    st.subheader(
        "STEP 7 · Activate Application"
    )

    st.write(
        "The verified banking module is activated and all banking features become available."
    )

    for feature in features:

        st.success(feature)

    status.success(
        "Application activated."
    )

    time.sleep(2)

    # ======================================================
    # SECURITY SUMMARY
    # ======================================================

    st.divider()

    st.subheader(
        "Security Summary"
    )

    col1, col2 = st.columns(2)

    with col1:

        st.success("h₁ Verified")

        st.success("SHA256 Verified")

    with col2:

        st.success("Digital Signature Verified")

        st.success("Application Activated")

    # ======================================================
    # FINAL STATUS
    # ======================================================

    st.divider()

    st.success("""
### Application Authenticated Successfully

✓ h₁ Integrity Verified

✓ Banking Module Downloaded

✓ Authentication KEY Generated

✓ Digital Signature Verified

✓ Banking Features Activated
""")