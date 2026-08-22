"""Streamlit frontend for the Plant Disease Detection API."""

import codecs
import os

import altair as alt
import pandas as pd
import requests
import streamlit as st

API_URL = os.environ.get("API_URL", "http://localhost:8000")

st.set_page_config(page_title="Plant Disease Detection", page_icon="🌿", layout="wide")

if "prediction" not in st.session_state:
    st.session_state.prediction = None
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Design tokens
ACCENT = "#4ADE80"  # brighter accent for text/highlights that need to pop on dark
INK = "#E5E9F0"  # matches config.toml textColor
MUTED = "#8B98B0"
BORDER = "#263048"
SURFACE = "#151F32"  # matches config.toml secondaryBackgroundColor
CHART_BAR = "#33415C"  # non-highlighted chart bars

SEVERITY_COLORS = {
    "none": ("#4ADE80", "rgba(34, 197, 94, 0.15)"),  # healthy
    "low": ("#22D3EE", "rgba(34, 211, 238, 0.15)"),
    "moderate": ("#FBBF24", "rgba(251, 191, 36, 0.15)"),
    "high": ("#FB923C", "rgba(251, 146, 60, 0.15)"),
    "very high": ("#F87171", "rgba(248, 113, 113, 0.15)"),
}


def severity_colors(severity_text: str) -> tuple[str, str]:
    text = (severity_text or "").lower()
    for key in ("very high", "high", "moderate", "low", "none"):
        if key in text:
            return SEVERITY_COLORS[key]
    return MUTED, "rgba(255, 255, 255, 0.06)"


st.markdown(
    f"""
    <style>
        #MainMenu, footer {{visibility: hidden;}}
        .block-container {{ padding-top: 1.5rem; max-width: 1200px; }}

        .hero {{
            background: linear-gradient(135deg, #065F46 0%, #0E7490 100%);
            border-radius: 16px;
            padding: 2rem 2.25rem;
            margin-bottom: 1.75rem;
            color: white;
            box-shadow: 0 10px 25px -10px rgba(0, 0, 0, 0.5);
        }}
        .hero h1 {{
            margin: 0 0 0.35rem 0;
            font-size: 1.9rem;
            font-weight: 750;
            color: white;
        }}
        .hero p {{
            margin: 0;
            opacity: 0.92;
            font-size: 1rem;
            color: white;
        }}

        .status-pill {{
            display: inline-flex;
            align-items: center;
            gap: 0.4rem;
            padding: 0.3rem 0.75rem;
            border-radius: 999px;
            font-size: 0.82rem;
            font-weight: 600;
        }}
        .status-online {{ background: rgba(34, 197, 94, 0.15); color: {ACCENT}; }}
        .status-offline {{ background: rgba(248, 113, 113, 0.15); color: #F87171; }}
        .status-warn {{ background: rgba(251, 191, 36, 0.15); color: #FBBF24; }}

        .card {{
            background: {SURFACE};
            border: 1px solid {BORDER};
            border-radius: 14px;
            padding: 1.25rem 1.4rem;
            box-shadow: 0 4px 14px rgba(0, 0, 0, 0.25);
        }}

        .result-header {{ display: flex; align-items: center; justify-content: space-between; }}
        .result-title {{ font-size: 1.35rem; font-weight: 700; color: {INK}; margin: 0; }}
        .result-sub {{ color: {MUTED}; font-size: 0.9rem; margin-top: 0.15rem; }}

        .confidence-badge {{
            font-size: 1.6rem;
            font-weight: 800;
            color: {ACCENT};
        }}

        .severity-badge {{
            display: inline-block;
            padding: 0.25rem 0.7rem;
            border-radius: 8px;
            font-weight: 650;
            font-size: 0.85rem;
        }}

        .section-title {{
            font-weight: 700;
            font-size: 0.95rem;
            color: {INK};
            margin: 1.1rem 0 0.5rem 0;
            display: flex;
            align-items: center;
            gap: 0.4rem;
        }}

        .info-list {{ margin: 0; padding-left: 1.1rem; color: {INK}; font-size: 0.92rem; }}
        .info-list li {{ margin-bottom: 0.3rem; }}

        .placeholder-card {{
            text-align: center;
            padding: 3rem 1rem;
            color: {MUTED};
        }}

        .footer-note {{
            text-align: center;
            color: {MUTED};
            font-size: 0.8rem;
            margin-top: 2.5rem;
            padding-top: 1rem;
            border-top: 1px solid {BORDER};
        }}
        .footer-note code {{
            background: rgba(255, 255, 255, 0.06);
            color: {INK};
            padding: 0.1rem 0.4rem;
            border-radius: 4px;
        }}
    </style>
    """,
    unsafe_allow_html=True,
)


def check_health() -> dict | None:
    try:
        r = requests.get(f"{API_URL}/health", timeout=5)
        r.raise_for_status()
        return r.json()
    except requests.RequestException:
        return None


def predict(image_bytes: bytes, filename: str, content_type: str) -> dict | None:
    try:
        r = requests.post(
            f"{API_URL}/predict",
            files={"file": (filename, image_bytes, content_type)},
            timeout=30,
        )
        r.raise_for_status()
        return r.json()
    except requests.RequestException as exc:
        st.error(f"Prediction request failed: {exc}")
        return None


def _chat_payload(message: str) -> dict:
    return {
        "message": message,
        "conversation_history": st.session_state.chat_history,
        "disease_context": (
            st.session_state.prediction["class_name"] if st.session_state.prediction else None
        ),
        "confidence": (
            st.session_state.prediction["confidence"] if st.session_state.prediction else None
        ),
    }


def send_chat_message(message: str) -> str:
    try:
        r = requests.post(f"{API_URL}/chat", json=_chat_payload(message), timeout=30)
        r.raise_for_status()
        return r.json()["response"]
    except requests.RequestException as exc:
        return f"⚠️ Chat request failed: {exc}"


def stream_chat_message(message: str):
    """Yield the AI reply incrementally, like ChatGPT's typing effect."""
    try:
        with requests.post(
            f"{API_URL}/chat/stream", json=_chat_payload(message), timeout=60, stream=True
        ) as r:
            r.raise_for_status()
            decoder = codecs.getincrementaldecoder("utf-8")()
            for chunk in r.iter_content(chunk_size=64):
                if chunk:
                    text = decoder.decode(chunk)
                    if text:
                        yield text
            tail = decoder.decode(b"", final=True)
            if tail:
                yield tail
    except requests.RequestException as exc:
        yield f"⚠️ Chat request failed: {exc}"


def render_info_section(icon: str, title: str, items: list[str]) -> None:
    if not items:
        return
    st.markdown(f'<div class="section-title">{icon} {title}</div>', unsafe_allow_html=True)
    st.markdown(
        "<ul class='info-list'>" + "".join(f"<li>{i}</li>" for i in items) + "</ul>",
        unsafe_allow_html=True,
    )


def render_predictions_chart(all_predictions: dict) -> None:
    df = pd.DataFrame(
        {"class": list(all_predictions.keys()), "confidence": list(all_predictions.values())}
    ).sort_values("confidence", ascending=True)
    top_class = df.iloc[-1]["class"]
    df["is_top"] = df["class"] == top_class

    chart = (
        alt.Chart(df)
        .mark_bar(cornerRadiusEnd=4, height=16)
        .encode(
            x=alt.X("confidence:Q", title="Confidence (%)", scale=alt.Scale(domain=[0, 100])),
            y=alt.Y("class:N", title=None, sort=None),
            color=alt.condition(alt.datum.is_top, alt.value(ACCENT), alt.value(CHART_BAR)),
            tooltip=[
                alt.Tooltip("class:N", title="Class"),
                alt.Tooltip("confidence:Q", title="Confidence", format=".2f"),
            ],
        )
        .properties(height=max(220, len(df) * 24), background="transparent")
        .configure_axis(labelColor=MUTED, titleColor=MUTED, gridColor=BORDER, domainColor=BORDER)
        .configure_view(strokeWidth=0)
    )
    st.altair_chart(chart, use_container_width=True)


# ── Header ───────────────────────────────────────────────────────────────
st.markdown(
    """
    <div class="hero">
        <h1>🌿 Plant Disease Detection</h1>
        <p>AI-powered leaf diagnosis across 14 crops — upload a photo for an
        instant assessment, treatment guidance, and an expert chat assistant.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

with st.sidebar:
    st.markdown("### System Status")
    health = check_health()
    if health and health.get("model_loaded"):
        version = health.get("version", "?")
        st.markdown(
            f'<span class="status-pill status-online">● API online · v{version}</span>',
            unsafe_allow_html=True,
        )
    elif health:
        st.markdown(
            '<span class="status-pill status-warn">● Online, model not loaded</span>',
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            '<span class="status-pill status-offline">● API unreachable</span>',
            unsafe_allow_html=True,
        )
    st.caption(f"Backend: `{API_URL}`")

    st.markdown("---")
    st.markdown("### Coverage")
    st.markdown(
        "🍎 **Apple** — Scab, Black Rot, Cedar Rust, Healthy\n\n"
        "🫐 **Blueberry** — Healthy\n\n"
        "🍒 **Cherry** — Powdery Mildew, Healthy\n\n"
        "🌽 **Corn** — Gray Leaf Spot, Common Rust, N. Leaf Blight, Healthy\n\n"
        "🍇 **Grape** — Black Rot, Esca, Leaf Blight, Healthy\n\n"
        "🍊 **Orange** — Citrus Greening (HLB)\n\n"
        "🍑 **Peach** — Bacterial Spot, Healthy\n\n"
        "🫑 **Pepper** — Bacterial Spot, Healthy\n\n"
        "🥔 **Potato** — Early/Late Blight, Healthy\n\n"
        "🍇 **Raspberry** — Healthy\n\n"
        "🌱 **Soybean** — Healthy\n\n"
        "🎃 **Squash** — Powdery Mildew\n\n"
        "🍓 **Strawberry** — Leaf Scorch, Healthy\n\n"
        "🍅 **Tomato** — 9 diseases + Healthy"
    )
    st.markdown("---")
    st.caption("38 disease classes + not-a-leaf rejection · MobileNetV2 transfer learning · MLflow-tracked model")

tab_detect, tab_chat = st.tabs(["🔍  Detect Disease", "💬  Ask the AI"])

with tab_detect:
    col_upload, col_result = st.columns([1, 1.3], gap="large")

    with col_upload:
        st.markdown("#### Upload a leaf photo")
        uploaded = st.file_uploader(
            "Potato, tomato or pepper leaf image",
            type=["jpg", "jpeg", "png"],
            label_visibility="collapsed",
        )

        if uploaded is not None:
            st.image(uploaded, use_container_width=True)
            if st.button("🔬 Analyze Leaf", type="primary", use_container_width=True):
                uploaded.seek(0)
                with st.spinner("Analyzing leaf..."):
                    st.session_state.prediction = predict(
                        uploaded.read(), uploaded.name, uploaded.type or "image/jpeg"
                    )
        else:
            st.caption("Supported formats: JPG, JPEG, PNG")

    with col_result:
        result = st.session_state.prediction
        if not result:
            st.markdown(
                '<div class="card placeholder-card">'
                "Upload a leaf photo and click <b>Analyze Leaf</b> to see results here."
                "</div>",
                unsafe_allow_html=True,
            )
        else:
            info = result.get("disease_info") or {}
            confidence = result["confidence"]
            sev_text = info.get("severity", "Unknown")
            sev_color, sev_bg = severity_colors(sev_text)

            st.markdown(
                f"""
                <div class="card">
                    <div class="result-header">
                        <div>
                            <p class="result-title">{result["display_name"]}</p>
                            <p class="result-sub">Predicted class</p>
                        </div>
                        <div class="confidence-badge">{confidence:.1f}%</div>
                    </div>
                    <div style="margin-top:0.75rem;">
                        <span class="severity-badge"
                              style="color:{sev_color}; background:{sev_bg};">
                            Severity: {sev_text}
                        </span>
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )

            with st.expander("📊 Confidence across all 39 classes", expanded=False):
                render_predictions_chart(result["all_predictions"])

            if info:
                render_info_section("🔍", "Symptoms", info.get("symptoms", []))
                render_info_section("💊", "Treatment", info.get("treatment", []))
                render_info_section("🛡️", "Prevention", info.get("prevention", []))
                render_info_section("🌱", "Care Tips", info.get("care_tips", []))

                pesticides = info.get("recommended_pesticides", [])
                if pesticides:
                    st.markdown(
                        '<div class="section-title">🧪 Recommended Pesticides</div>',
                        unsafe_allow_html=True,
                    )
                    st.markdown(
                        "<ul class='info-list'>"
                        + "".join(
                            f"<li><b>{p['name']}</b> "
                            f"<span style='color:{MUTED};'>({p['type']})</span> "
                            f"— {p['usage']}</li>"
                            for p in pesticides
                        )
                        + "</ul>",
                        unsafe_allow_html=True,
                    )

with tab_chat:
    if st.session_state.prediction:
        st.markdown(
            '<div class="card" style="margin-bottom:1rem;">'
            "💬 Chatting with context from your last scan: "
            f"<b>{st.session_state.prediction['display_name']}</b></div>",
            unsafe_allow_html=True,
        )
    else:
        st.caption("Tip: scan a leaf in the **Detect Disease** tab first for personalised answers.")

    for msg in st.session_state.chat_history:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    if user_message := st.chat_input("Ask about treatment, prevention, symptoms..."):
        st.session_state.chat_history.append({"role": "user", "content": user_message})
        with st.chat_message("user"):
            st.markdown(user_message)
        with st.chat_message("assistant"):
            reply = st.write_stream(stream_chat_message(user_message))
        st.session_state.chat_history.append({"role": "assistant", "content": reply})
        st.rerun()

st.markdown(
    '<div class="footer-note">Built with <code>FastAPI</code> · <code>TensorFlow</code> · '
    "<code>MLflow</code> · <code>DVC</code> · <code>Streamlit</code></div>",
    unsafe_allow_html=True,
)
