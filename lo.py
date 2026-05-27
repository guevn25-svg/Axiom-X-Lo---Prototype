
import streamlit as st

# Changed layout from 'wide' to 'centered' to fix stretching
st.set_page_config(
    page_title="Related Group Executive Dashboard",
    layout="centered", 
    initial_sidebar_state="collapsed"
)

# ---------- GLOBAL STYLES (Related Group Brand Identity) ----------
st.markdown("""
<style>
/* Import Core Typography: Luxury Serif + Clean Sans */
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,600;0,700;1,400&family=Inter:wght@300;400;500;600&display=swap');

/* Base Surfaces & Typography */
html, body, [class*="css"] {
    background-color: #FFFFFF !important; 
    color: #1A1A1A !important; 
    font-family: 'Inter', sans-serif !important;
    -webkit-font-smoothing: antialiased;
}

/* Custom UI Animations */
@keyframes fadeUp {
    from { opacity: 0; transform: translateY(16px); }
    to { opacity: 1; transform: translateY(0); }
}

/* Hero Section */
.hero-title {
    font-family: 'Playfair Display', serif;
    font-size: 52px;
    font-weight: 400;
    line-height: 1.1;
    letter-spacing: -0.01em;
    color: #111111;
    margin-bottom: 16px;
    animation: fadeUp 0.6s cubic-bezier(.16,1,.3,1) both;
}

.accent-text {
    /* Subtle champagne/bronze accent used in high-end real estate */
    color: #A68A61;
    font-style: italic;
}

.subtitle {
    color: #4A4A4A; 
    font-family: 'Inter', sans-serif;
    font-size: 16px;
    line-height: 1.6;
    max-width: 800px;
    font-weight: 300;
    animation: fadeUp 0.6s 0.1s cubic-bezier(.16,1,.3,1) both;
}

/* Data Cards - Minimalist, sharp corners, thin borders */
.glass-card {
    background: #FFFFFF;
    border: 1px solid #E5E5E5; 
    border-radius: 0px; 
    padding: 24px;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
    animation: fadeUp 0.6s 0.2s cubic-bezier(.16,1,.3,1) both;
    height: 100%;
}

.glass-card:hover {
    transform: translateY(-2px);
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.05);
    border-color: #A68A61;
}

.metric-value {
    font-family: 'Playfair Display', serif;
    font-size: 38px;
    font-weight: 400;
    color: #111111;
    line-height: 1.1;
    margin-bottom: 8px;
}

.metric-label {
    font-family: 'Inter', sans-serif;
    color: #767676;
    text-transform: uppercase;
    font-size: 10px;
    letter-spacing: 0.15em;
    font-weight: 500;
}

/* Section Labels */
.section-label {
    font-family: 'Inter', sans-serif;
    color: #A68A61;
    text-transform: uppercase;
    font-size: 11px;
    letter-spacing: 0.2em;
    font-weight: 500;
    margin-bottom: 12px;
    margin-top: 40px;
    border-top: 1px solid #E5E5E5;
    padding-top: 20px;
}

.section-title {
    font-family: 'Playfair Display', serif;
    font-size: 32px;
    font-weight: 400;
    color: #111111;
    margin-bottom: 16px;
}

/* Queue/Feed Items */
.feed-item {
    background: #FAFAFA;
    border-left: 3px solid #111111;
    padding: 20px 24px;
    margin-bottom: 16px;
    transition: background 0.2s ease;
}

.feed-item.border-crit { border-left-color: #8B0000; }
.feed-item.border-warn { border-left-color: #A68A61; }
.feed-item.border-info { border-left-color: #4A4A4A; }

.feed-item h3 {
    font-family: 'Playfair Display', serif;
    margin: 12px 0 6px 0;
    font-size: 18px;
    font-weight: 600;
    color: #111111;
}

.feed-item p {
    font-family: 'Inter', sans-serif;
    font-size: 13px;
    color: #4A4A4A;
    margin-bottom: 6px;
    line-height: 1.5;
}

/* Action Badges - Sharp monochrome */
.badge {
    display: inline-block;
    font-family: 'Inter', sans-serif;
    padding: 4px 10px;
    border: 1px solid #111111;
    color: #111111;
    font-size: 9px;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    font-weight: 600;
    background: transparent;
}

.badge-crit { border-color: #8B0000; color: #8B0000; }
.badge-warn { border-color: #A68A61; color: #A68A61; }

/* Phases / Roadmap */
.phase-card {
    background: #FFFFFF;
    border: 1px solid #E5E5E5;
    padding: 32px;
    height: 100%;
}

.phase-title {
    font-family: 'Inter', sans-serif;
    font-size: 10px;
    color: #A68A61;
    font-weight: 600;
    letter-spacing: 0.15em;
    margin-bottom: 12px;
    text-transform: uppercase;
}

.phase-heading {
    font-family: 'Playfair Display', serif;
    font-size: 20px;
    font-weight: 600;
    color: #111111;
    margin-bottom: 16px;
}

ul {
    padding-left: 16px;
    color: #4A4A4A;
    font-family: 'Inter', sans-serif;
    font-size: 13px;
    font-weight: 300;
}
li { margin-bottom: 8px; }

/* Custom Progress Bar Override - Minimalist Line */
.progress-container { margin-bottom: 24px; }
.progress-label-row { display: flex; justify-content: space-between; margin-bottom: 8px; font-family: 'Inter', sans-serif; font-size: 12px; font-weight: 400; color: #111111;}
.progress-percent { color: #A68A61; font-weight: 500;}
.progress-bg { width: 100%; background-color: #F0F0F0; height: 2px; }
.progress-fill { background-color: #111111; height: 100%; transition: width 0.8s ease; }

</style>
""", unsafe_allow_html=True)

# ---------- HERO ----------
st.markdown("""
<div class="hero-title" style="margin-top: 40px;">
The Operational Nervous System <br>for <span class="accent-text">Property Development</span>
</div>
<div class="subtitle">
A real-time optimization platform for Owners' Representatives and Developers. <br>
Built to replace static systems with live relational intelligence, multimodal AI ingestion, predictive procurement analysis, and operational continuity.
</div>
<br><br>
""", unsafe_allow_html=True)

# ---------- METRICS ----------
c1, c2, c3, c4 = st.columns(4)

metrics = [
    ("148", "Projects Monitored"),
    ("372", "Open RFIs"),
    ("$48.2M", "Subcontractor Quotes"),
    ("19", "Predicted Risk Flags"),
]

for col, metric in zip([c1, c2, c3, c4], metrics):
    with col:
        st.markdown(f"""
        <div class="glass-card">
            <div class="metric-value">{metric[0]}</div>
            <div class="metric-label">{metric[1]}</div>
        </div>
        """, unsafe_allow_html=True)

st.write("")
st.write("")

# ---------- EXECUTIVE DASHBOARD ----------
st.markdown("""
<div class="section-label">Live Operations</div>
<div class="section-title">Executive Command Dashboard</div>
<div style="font-family: 'Inter', sans-serif; font-size: 14px; font-weight: 300; color: #4A4A4A;">
Designed around the shift-start question.<br>
The system proactively surfaces what requires attention today without forcing workflow change.
</div>
<br>
""", unsafe_allow_html=True)

# ---------- PRIORITY SIGNALS ----------
s1, s2, s3 = st.columns(3)

signals = [
    ("12", "Critical Handover Deadlines", "Units at risk of turnover delay in the next 14 days."),
    ("28", "Pending Vendor Reviews", "AI extracted procurement entries awaiting human approval."),
    ("$1.8M", "Budget Variance Alerts", "Potential exposure detected across active developments.")
]

for col, signal in zip([s1, s2, s3], signals):
    with col:
        st.markdown(f"""
        <div class="glass-card">
            <div class="metric-label">Priority Signal</div>
            <div class="metric-value" style="font-size: 32px; margin-top: 12px;">{signal[0]}</div>
            <h3 style="font-family: 'Playfair Display', serif; font-size: 16px; margin: 8px 0; color: #111111;">{signal[1]}</h3>
            <p style="font-family: 'Inter', sans-serif; font-size: 12px; font-weight: 300; color: #767676;">{signal[2]}</p>
        </div>
        """, unsafe_allow_html=True)

st.write("")

# ---------- ATTENTION QUEUE ----------
st.markdown("""
<div class="section-title" style="margin-top: 32px;">Today's Attention Queue</div>
""", unsafe_allow_html=True)

queue = [
    ("Brickell Waterfront Residences", "Subcontractor submitted revised electrical pricing 11% above estimate.", "Critical", "Review before procurement lock tomorrow 8:00 AM.", "crit"),
    ("Coral Gables Tower Phase II", "AI detected discrepancy between CAD revision and structural quote.", "Review Required", "Human validation required before database commit.", "warn"),
    ("Miami Logistics Campus", "RFI response aging beyond contractual threshold.", "Operational Risk", "Escalate to consultant team within 24 hours.", "info")
]

for item in queue:
    border_class = f"border-{item[4]}"
    badge_class = f"badge-{item[4]}"
    
    st.markdown(f"""
    <div class="feed-item {border_class}">
        <div class="badge {badge_class}">{item[2]}</div>
        <h3>{item[0]}</h3>
        <p>{item[1]}</p>
        <p style="color: #A68A61; font-size: 11px; margin-top: 8px; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 500;">
            Action: {item[3]}
        </p>
    </div>
    """, unsafe_allow_html=True)

st.write("")

# ---------- AI INGESTION ----------
st.markdown("""
<div class="section-label">AI Ingestion Layer</div>
<div class="section-title">Multimodal Intelligence Pipeline</div>
<div style="font-family: 'Inter', sans-serif; font-size: 14px; font-weight: 300; color: #4A4A4A; margin-bottom: 24px;">
Reads PDF quotes, email chains, procurement revisions, and CAD updates into structured relational data.
</div>
""", unsafe_allow_html=True)

ai_items = [
    ("Electrical Scope Revision", 92),
    ("Insurance Expiration Detection", 99),
    ("Mechanical Equipment Schedule", 87),
    ("Change Order Exposure Detection", 95),
]

for item in ai_items:
    st.markdown(f"""
    <div class="progress-container">
        <div class="progress-label-row">
            <span>{item[0]}</span>
            <span class="progress-percent">{item[1]}% Accuracy</span>
        </div>
        <div class="progress-bg">
            <div class="progress-fill" style="width: {item[1]}%;"></div>
        </div>
    </div>
    """, unsafe_allow_html=True)

st.write("")

# ---------- MARKET POSITIONING ----------
st.markdown("""
<div class="section-label">Market Positioning</div>
<div class="section-title">Built Across the Generational Divide</div>
""", unsafe_allow_html=True)

g1, g2 = st.columns(2)

with g1:
    st.markdown("""
    <div class="glass-card">
        <div class="metric-label">Current Generation</div>
        <h2 style="font-family: 'Playfair Display', serif; font-size: 24px; margin: 16px 0; font-weight: 400;">Protect What They Built</h2>
        <ul>
            <li>Nothing falls through the cracks.</li>
            <li>Operational continuity and accountability.</li>
            <li>Trust earned through reliability.</li>
            <li>Minimal workflow disruption.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with g2:
    st.markdown("""
    <div class="glass-card">
        <div class="metric-label">Next Generation</div>
        <h2 style="font-family: 'Playfair Display', serif; font-size: 24px; margin: 16px 0; font-weight: 400;">Operate Above Their Years</h2>
        <ul>
            <li>Operate above your experience level.</li>
            <li>Leverage, automation, and speed.</li>
            <li>AI-native operational systems.</li>
            <li>Scalable decision-making.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

st.write("")

# ---------- CRAWL WALK RUN ----------
st.markdown("""
<div class="section-label">Adoption Strategy</div>
<div class="section-title">Crawl → Walk → Run</div>
""", unsafe_allow_html=True)

p1, p2, p3 = st.columns(3)

phases = [
    ("PHASE 1: CRAWL", "Operational Nervous System", ["Tracks RFIs and deadlines", "Answers the shift-start question", "Zero workflow behavior change"]),
    ("PHASE 2: WALK", "AI-Assisted Ingestion", ["Parses PDFs and CAD revisions", "Review Required AI outputs", "30-second error recovery"]),
    ("PHASE 3: RUN", "Predictive Intelligence", ["Behavioral pattern library", "Procurement anomaly detection", "Predictive operational scaling"]),
]

for col, phase in zip([p1, p2, p3], phases):
    with col:
        bullets = "".join([f"<li>{b}</li>" for b in phase[2]])
        st.markdown(f"""
        <div class="phase-card">
            <div class="phase-title">{phase[0]}</div>
            <div class="phase-heading">{phase[1]}</div>
            <ul>{bullets}</ul>
        </div>
        """, unsafe_allow_html=True)

st.write("")
st.write("")

# ---------- ROADMAP ----------
st.markdown("""
<div class="section-label">Execution Roadmap</div>
<div class="section-title">Validation → Adoption → Predictive Scale</div>
""", unsafe_allow_html=True)

roadmap = [
    ("Phase 0", "Weeks 1–4", "Validation & Pre-Launch"),
    ("Phase 1", "Months 1–3", "Foundation & Crawl MVP"),
    ("Phase 2", "Months 4–6", "AI Ingestion & Walk Rollout"),
    ("Phase 3", "Months 6–12+", "Predictive Intelligence & Scale"),
]

for item in roadmap:
    st.markdown(f"""
    <div class="glass-card" style="margin-bottom:16px; padding: 20px 24px; display: flex; justify-content: space-between; align-items: center;">
        <div>
            <div class="metric-label" style="margin-bottom: 4px;">{item[0]} · {item[1]}</div>
            <h2 style="font-family: 'Playfair Display', serif; font-size: 18px; margin: 0; font-weight: 600; color: #111111;">{item[2]}</h2>
        </div>
        <div style="color: #E5E5E5; font-family: 'Playfair Display', serif; font-size: 24px; font-style: italic;">
            {item[0].split(' ')[1]}
        </div>
    </div>
    """, unsafe_allow_html=True)
