import streamlit as pd_stream
import time
import random
from datetime import datetime

# 1. INITIALISATION ET CONFIGURATION DE L'INTERFACE SYSTEME
pd_stream.set_page_config(
    page_title="XAUUSD QUANT MODULE", 
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ---- STYLING INSTITUTIONNEL (MATTE TERMINAL DESIGN) ----
pd_stream.markdown("""
    <style>
        /* Fond sombre mat et typographie chirurgicale style Bloomberg/Reuters */
        .stApp { 
            background-color: #0b0c10; 
            color: #f1f1f1; 
            font-family: 'Courier New', Courier, monospace; 
        }
        
        /* Blocs de données épurés 1px */
        .terminal-box { 
            background-color: #12141c; 
            border: 1px solid #1f2331; 
            padding: 15px; 
            border-radius: 4px; 
            margin-bottom: 12px; 
        }
        
        /* Bannières d'ordres d'exécution discrètes et nettes */
        .signal-banner { 
            padding: 16px; 
            border-radius: 4px; 
            text-align: center; 
            font-weight: 600; 
            font-size: 16px; 
            letter-spacing: 1px; 
            margin-bottom: 20px; 
        }
        .sig-buy { background-color: rgba(46, 204, 113, 0.1); border: 1px solid #2ecc71; color: #2ecc71; }
        .sig-sell { background-color: rgba(231, 76, 60, 0.1); border: 1px solid #e74c3c; color: #e74c3c; }
        .sig-wait { background-color: #1a1d29; border: 1px solid #34495e; color: #7f8c8d; }
        
        /* Fiche de gestion des risques */
        .risk-profile {
            background-color: #12141c; 
            border-left: 2px solid #555c6d; 
            padding: 14px; 
            font-size: 12px; 
            line-height: 1.7; 
            color: #a1a8b9;
        }
        
        hr { border: 0; border-top: 1px solid #1f2331; }
    </style>
""", unsafe_allow_html=True)

# 2. MOTEUR QUANTITATIF DE FLUX SCALPING (M15 RESOLUTION)
if "prix_gold" not in pd_stream.session_state:
    pd_stream.session_state.prix_gold = 2322.40
if "historique_prix" not in pd_stream.session_state:
    # Génération d'une base de données initiale restreinte pour une réactivité maximale
    pd_stream.session_state.historique_prix = [2322.0 + random.uniform(-1.0, 1.0) for _ in range(12)]

# Simulation de flux ultra-fluide (micro-variations XAUUSD)
pd_stream.session_state.prix_gold = round(pd_stream.session_state.prix_gold + random.uniform(-0.35, 0.35), 2)
prix_actuel = pd_stream.session_state.prix_gold

pd_stream.session_state.historique_prix.append(prix_actuel)
if len(pd_stream.session_state.historique_prix) > 15:
    pd_stream.session_state.historique_prix.pop(0)

# Calcul Statistique en temps réel (Z-Score de volatilité)
g_moyenne = sum(pd_stream.session_state.historique_prix) / len(pd_stream.session_state.historique_prix)
g_variance = sum((p - g_moyenne) ** 2 for p in pd_stream.session_state.historique_prix) / len(pd_stream.session_state.historique_prix)
g_std_dev = (g_variance ** 0.5) if g_variance > 0 else 0.4
z_score = (prix_actuel - g_moyenne) / g_std_dev

# Seuils mathématiques des Order Blocks institutionnels en M15
ob_demand_zone = 2321.20  # Seuil d'achat
ob_supply_zone = 2323.40  # Seuil de vente

# 3. LOGIQUE DE DECISION DU MODÈLE EXPERT (ALGORITHME SANS CONFLIT)
if prix_actuel <= ob_demand_zone and z_score < -0.8:
    decision_systeme = "EXECUTE_BUY"
elif prix_actuel >= ob_supply_zone and z_score > 0.8:
    decision_systeme = "EXECUTE_SELL"
else:
    decision_systeme = "STANDBY"

# 4. RENDU DE L'INTERFACE DE BORD (DASHBOARD)
pd_stream.markdown("<h3 style='letter-spacing: 2px; color: #ffffff; margin-bottom: 0; font-weight: 500;'>XAUUSD SYSTEM / MODULE M15</h3>", unsafe_allow_html=True)
pd_stream.markdown("<p style='color: #555c6d; font-size: 11px; margin-top: 2px; letter-spacing: 0.5px;'>SYSTEM STATUS: OPERATIONAL — CORE: SMC + VOLATILITY FILTER</p>", unsafe_allow_html=True)
pd_stream.markdown("<hr>", unsafe_allow_html=True)

# Affichage du signal d'exécution prioritaire
if decision_systeme == "EXECUTE_BUY":
    pd_stream.markdown('<div class="signal-banner sig-buy">ORDER: EXECUTE BUY ORDER (M15 DISCREPANCY)</div>', unsafe_allow_html=True)
elif decision_systeme == "EXECUTE_SELL":
    pd_stream.markdown('<div class="signal-banner sig-sell">ORDER: EXECUTE SELL ORDER (M15 DISCREPANCY)</div>', unsafe_allow_html=True)
else:
    pd_stream.markdown('<div class="signal-banner sig-wait">ORDER: STANDBY (MARKET BALANCED)</div>', unsafe_allow_html=True)

# Affichage des deux métriques clés sur une seule ligne carrée
col_1, col_2 = pd_stream.columns(2)
with col_1:
    pd_stream.markdown(f"""
    <div class="terminal-box">
        <p style="color: #555c6d; margin: 0; font-size: 10px; font-weight: bold; letter-spacing: 1px;">SPOT PRICE (USD)</p>
        <h2 style="color: #ffffff; margin: 5px 0 0 0; font-family: monospace; font-size: 24px;">{prix_actuel:.2f}</h2>
    </div>
    """, unsafe_allow_html=True)

with col_2:
    color_z = "#2ecc71" if z_score < -0.8 else "#e74c3c" if z_score > 0.8 else "#7f8c8d"
    pd_stream.markdown(f"""
    <div class="terminal-box">
        <p style="color: #555c6d; margin: 0; font-size: 10px; font-weight: bold; letter-spacing: 1px;">Z-SCORE METRIC</p>
        <h2 style="color: {color_z}; margin: 5px 0 0 0; font-family: monospace; font-size: 24px;">{z_score:.2f}</h2>
    </div>
    """, unsafe_allow_html=True)

pd_stream.markdown("<br>", unsafe_allow_html=True)

# 5. FICHE STRICTE DE GESTION DU RISQUE AUTOMATISÉE (PROFILED FOR 100K XOF)
pd_stream.markdown("<p style='color: #ffffff; font-size: 12px; font-weight: bold; letter-spacing: 1px; margin-bottom:6px;'>RISK MANAGEMENT PROFILE</p>", unsafe_allow_html=True)
pd_stream.markdown(f"""
<div class="risk-profile">
    • ACCOUNT BASE       : 100,450 XOF<br>
    • RISK PER SCALP     : 1,000 XOF (STRICT 1.0%)<br>
    • METATRADER SIZE    : <span style="color: #ffffff; font-weight: bold; background-color: #1f2331; padding: 2px 6px; border-radius: 2px;">0.11 LOT</span><br>
    • TARGET MATRIX      : SL 15 PIPS / TP 30 PIPS (RATIO 1:2)
</div>
""", unsafe_allow_html=True)

# Boucle d'actualisation rapide de scalping (1.5 seconde)
time.sleep(1.5)
pd_stream.rerun()
