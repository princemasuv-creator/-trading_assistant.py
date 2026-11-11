import streamlit as st
import datetime
st.set_page_config(page_title="Forex Trading Assistant", layout="wide")
st.markdown("# 📈 FOREX TRADING ASSISTANT")
st.caption("Pre-trade analysis • Trade planning • Performance journal")

# Top action buttons
col_btn1, col_btn2 = st.columns(2)
with col_btn1:
    st.button("Print plan", use_container_width=True)
with col_btn2:
    st.button("Save trade", use_container_width=True, type="primary")

tab1, tab2 = st.tabs(["📋 Pre-trade planner", "📓 Trade journal"])

with tab1:
    # Section 1: Trade Details
    st.header("1. Trade details")
    c1, c2, c3 = st.columns(3)
    with c1:
        instrument = st.selectbox("Currency pair / instrument", [
            "EURUSD", "GBPUSD", "USDJPY", "USDCHF", "AUDUSD", "NZDUSD", 
            "USDCAD", "EURGBP", "GBPJPY", "EURJPY", "XAUUSD (Gold)", "Other"
        ])
        direction = st.radio("Trade direction", ["Buy / Long", "Sell / Short", "Watch only"])
    with c2:
        trade_date = st.date_input("Date of analysis", datetime.date.today())
        session = st.selectbox("Trading session", ["London", "New York", "London / New York overlap", "Asian", "Other"])
    with c3:
        tf = st.selectbox("Execution timeframe", ["M1", "M5", "M15", "M30", "H1", "H4", "D1"])
        ttype = st.selectbox("Trade type", ["Day trade", "Swing trade", "Scalp"])

    # Section 2: Market Structure & Momentum
    st.header("2. Market structure & momentum")
    st.subheader("Higher timeframe market condition (weekly / daily)")
    c4, c5, c6 = st.columns(3)
    with c4:
        w_trend = st.selectbox("Weekly trend", ["Uptrend", "Sideways", "Downtrend", "Unclear"])
        d_trend = st.selectbox("Daily trend", ["Uptrend", "Sideways", "Downtrend", "Unclear"])
    with c5:
        momentum = st.selectbox("Price momentum", ["High", "Low", "Neutral", "Fading"])
        fib = st.selectbox("Fibonacci zone", ["Not identified", "23.6%", "38.2%", "50.0%", "61.8%", "78.6%", "Other"])
    with c6:
        st.text_area("Trendline / structure observations", height=100)

    st.subheader("Important price levels")
    c7, c8, c9 = st.columns(3)
    with c7:
        st.text_input("Support level")
    with c8:
        st.text_input("Resistance level")
    with c9:
        st.text_input("Trendline level / note")
    near_key = st.radio("Price near key level?", ["Yes", "No", "Not sure"], horizontal=True)

    # Section 3: Entry Signal
    st.header("3. Entry signal")
    c10, c11 = st.columns(2)
    with c10:
        pattern = st.selectbox("Chart pattern", ["Continuation", "Reversal", "Breakout", "Range / consolidation", "No clear pattern", "Other"])
        candle = st.selectbox("Candlestick signal", ["Pin bar", "Inside bar", "Engulfing", "Doji", "Evening star", "Morning star", "Other", "No clear signal"])
    with c11:
        st.text_area("Entry explanation / confirmation", height=110)

    # Section 4: Risk Management & Trade Levels
    st.header("4. Risk management & trade levels")
    c12, c13, c14 = st.columns(3)
    with c12:
        balance = st.number_input("Account balance (optional)", min_value=0.0, step=100.0, value=10000.0)
        risk_pct = st.number_input("Risk per trade (%)", min_value=0.0, max_value=100.0, step=0.1, value=1.0)
        lot_size = st.number_input("Lot size", min_value=0.0, step=0.01, value=0.1)
    with c13:
        ep = st.number_input("Entry price", min_value=0.0, step=0.0001, format="%.5f")
        sl = st.number_input("Stop loss (SL)", min_value=0.0, step=0.0001, format="%.5f")
        tp = st.number_input("Take profit (TP)", min_value=0.0, step=0.0001, format="%.5f")
    with c14:
        pip_val = st.number_input("Estimated pip / point value (optional)", min_value=0.0, step=0.1)
        outcome = st.selectbox("Trade outcome (after closing)", ["Pending", "Win", "Loss", "Break-even", "Cancelled"])

    # Calculations
    risk_amt = balance * (risk_pct / 100.0) if balance > 0 else 0.0
    pips_sl = abs(ep - sl) if ep > 0 and sl > 0 else 0.0
    pips_tp = abs(tp - ep) if ep > 0 and tp > 0 else 0.0
    rr_ratio = (pips_tp / pips_sl) if pips_sl > 0 else 0.0

    st.info(f"📊 **Risk amount:** ${risk_amt:,.2f}  |  **Reward : Risk Ratio:** {rr_ratio:.2f}:1")
    st.caption("Calculations use price distance. Verify contract specifications with your broker, especially for gold and JPY pairs.")

    # Section 5: Economic News
    st.header("5. Economic news & market conditions")
    c15, c16 = st.columns(2)
    with c15:
        news_near = st.selectbox("High-impact news near trade?", ["No known high-impact news", "Yes — within 30 minutes", "Yes — within 1–2 hours", "Yes — later today", "Not checked"])
        st.text_input("News affecting this pair")
    with c16:
        st.text_area("News / calendar notes", height=100)

    # Section 6: Pre-Trade Discipline Checklist
    st.header("6. Pre-trade discipline checklist")
    st.caption("Tick each item only after you have checked it.")
    col_chk1, col_chk2 = st.columns(2)
    with col_chk1:
        ch1 = st.checkbox("Weekly and daily trend assessed")
        ch2 = st.checkbox("Momentum supports my trade direction")
        ch3 = st.checkbox("Support / resistance / key levels marked")
        ch4 = st.checkbox("Clear chart and candlestick signal confirmed")
        ch5 = st.checkbox("Entry, stop loss and take profit planned")
    with col_chk2:
        ch6 = st.checkbox("Risk is within my trading limit")
        ch7 = st.checkbox("Economic calendar checked")
        ch8 = st.checkbox("I am calm; not revenge trading or chasing price")
        ch9 = st.checkbox("Reward-to-risk meets my trading rules")
        ch10 = st.checkbox("I can explain why this trade is valid")

    all_checked = all([ch1, ch2, ch3, ch4, ch5, ch6, ch7, ch8, ch9, ch10])
    if all_checked:
        st.success("✅ **Ready Status:** Checklist Complete. You are disciplined and ready to trade your plan!")
    else:
        st.warning("⚠️ Complete the checklist and enter your trade levels to review readiness.")

    # Section 7: Notes
    st.header("7. Trade notes & review")
    st.text_area("Why am I taking this trade?", height=100)
    st.text_area("Post-trade lesson (complete after closing)", height=100)

    # Bottom Actions
    st.markdown("---")
    c_b1, c_b2, c_b3 = st.columns(3)
    c_b1.button("Save to journal", use_container_width=True, key="save_bottom")
    c_b2.button("Print this trade plan", use_container_width=True, key="print_bottom")
    c_b3.button("Clear form", use_container_width=True, key="clear_bottom")

with tab2:
    st.header("📓 Historical Journal Entries")
    st.write("No closed trades in your history yet. Fill out the pre-trade planner to save your first entry.")

st.markdown("---")
st.caption("Educational tool only — not financial advice or a signal service.")
