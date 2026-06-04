import streamlit as pd_stream
import random
from datetime import datetime

# Configuration de la page et application d'un thème sombre natif
pd_stream.set_page_config(
    page_title="GOLD SMC ALGO",
    page_icon="👑",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ---- DESIGN CSS AVANCÉ INJECTÉ (Pour casser le côté "plat") ----
pd_stream.markdown("""
    <style>
        /* Fond global et dégradé technologique */
        .stApp {
            background: linear-gradient(135deg, #0f111a 0%, #161925 100%);
            color: #e2e8f0;
        }
        /* Personnalisation des onglets (Tabs) */
        .stTabs [data-baseweb="tab-list"] {
            gap: 8px;
            background-color: #1e2235;
            padding: 8px;
            border-radius: 12px;
            border: 1px solid #2d334d;
        }
        .stTabs [data-baseweb="tab"] {
            height: 40px;
            white-space: pre;
            background-color: transparent;
            border-radius: 8px;
            color: #a0aec0;
            font-weight: 600;
            transition: all 0.3s;
        }
        .stTabs [aria-selected="true"] {
            background-color: #d4af37 !important; /* Couleur Or */
            color: #0f111a !important;
            box-shadow: 0px 4px 12px rgba(212, 175, 55, 0.3);
        }
        /* Boîtier premium pour les métriques et blocs */
        .metric-card {
            background: #1e2235;
            border: 1px solid #2d334d;
            border-left: 4px solid #d4af37; /* Ligne dorée à gauche */
            padding: 16px;
            border-radius: 12px;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
            margin-bottom: 12px;
        }
        .demand-card {
            background: rgba(16, 185, 129, 0.1);
            border: 1px solid #10b981;
            border-left: 5px solid #10b981;
            padding: 16px;
            border-radius: 12px;
            margin-bottom: 12px;
        }
        .supply-card {
            background: rgba(239, 68, 68, 0.1);
            border: 1px solid #ef4444;
            border-left: 5px solid #ef4444;
            padding: 16px;
            border-radius: 12px;
            margin-bottom: 12px;
        }
        /* Boutons personnalisés */
        div.stButton > button:first-child {
            background: linear-gradient(90deg, #ef4444 0%, #b91c1c 100%);
            color: white;
            border: none;
            font-weight: bold;
            border-radius: 8px;
            box-shadow: 0px 4px 15px rgba(239, 68, 68, 0.4);
        }
    </style>
""", unsafe_allow_html=True)

# ---- INITIALISATION DES VARIABLES SIMULÉES ----
if "capital" not in pd_stream.session_state:
    pd_stream.session_state.capital = 100450.0
if "risk_percent" not in pd_stream.session_state:
    pd_stream.session_state.risk_percent = 2.0
if "mode_entree" not in pd_stream.session_state:
    pd_stream.session_state.mode_entree = "Limite 50% (Agressif)"
if "bot_actif" not in pd_stream.session_state:
    pd_stream.session_state.bot_actif = True

# ---- ARCHITECTURE DE NAVIGATION AUTOMATIQUE ----
onglet1, onglet2, onglet3, onglet4 = pd_stream.tabs([
    "📊 Dashboard", 
    "🟩 Zones OB", 
    "🧠 Log ML", 
    "⚙️ Réglages"
])

# ==========================================
# 1. ONGLET : DASHBOARD (RE-STYLISÉ)
# ==========================================
with onglet1:
    col_statut1, col_statut2 = pd_stream.columns(2)
    with col_statut1:
        if pd_stream.session_state.bot_actif:
            pd_stream.markdown("<h3 style='color: #10b981; margin:0;'>🟢 BOT EN RECHERCHE</h3>", unsafe_allow_html=True)
        else:
            pd_stream.markdown("<h3 style='color: #ef4444; margin:0;'>⏸️ BOT EN PAUSE</h3>", unsafe_allow_html=True)
    with col_statut2:
        pd_stream.markdown(f"<p style='text-align:right; color:#a0aec0; margin:0;'>⏱️ M15 | {datetime.now().strftime('%H:%M GMT')}</p>", unsafe_allow_html=True)
    
    pd_stream.markdown("<br>", unsafe_allow_html=True)
    
    # Cartes Financières avec notre classe CSS premium
    col_fin1, col_fin2 = pd_stream.columns(2)
    with col_fin1:
        pd_stream.markdown(f"""
        <div class="metric-card">
            <p style="color: #a0aec0; margin: 0; font-size: 14px;">Capital Actuel</p>
            <h2 style="color: #fff; margin: 5px 0 0 0; font-size: 24px;">{pd_stream.session_state.capital:,.0f} XOF</h2>
            <span style="color: #10b981; font-size: 12px;">📈 +450 XOF aujourd'hui</span>
        </div>
        """, unsafe_allow_html=True)
        
    with col_fin2:
        pd_stream.markdown("""
        <div class="metric-card" style="border-left-color: #3182ce;">
            <p style="color: #a0aec0; margin: 0; font-size: 14px;">Win Rate Global</p>
            <h2 style="color: #fff; margin: 5px 0 0 0; font-size: 24px;">62.4 %</h2>
            <span style="color: #3182ce; font-size: 12px;">🎯 Algorithme stable</span>
        </div>
        """, unsafe_allow_html=True)
    
    # Données du Marché Gold
    pd_stream.markdown("<h4 style='color: #d4af37;'>⚡ Analyse Quantitative XAU/USD</h4>", unsafe_allow_html=True)
    
    col_mkt1, col_mkt2 = pd_stream.columns(2)
    with col_mkt1:
        pd_stream.metric(label="Prix du Gold", value="2 345.20 $", delta="-3.40 $ (M15)")
    with col_mkt2:
        pd_stream.markdown("<br>**Structure de Marché :**<br><span style='color:#10b981; font-weight:bold;'>📈 Bullish Structure (BOS Validé)</span>", unsafe_allow_html=True)
    
    # Indicateurs avancés
    pd_stream.markdown("<br>", unsafe_allow_html=True)
    col_ind1, col_ind2 = pd_stream.columns(2)
    with col_ind1:
        pd_stream.markdown("**Filtre Z-Score (VWAP)**")
        pd_stream.markdown("<h3 style='color: #10b981; margin:0;'>-2.15</h3>", unsafe_allow_html=True)
        pd_stream.progress(25)
        pd_stream.caption("🟢 Anomalie détectée : Prix sous-évalué")
    with col_ind2:
        pd_stream.markdown("**Volume Profile (CVD)**")
        pd_stream.markdown("<h3 style='color: #10b981; margin:0;'>+12,400</h3>", unsafe_allow_html=True)
        pd_stream.caption("🟢 Pression d'achat institutionnelle")

    pd_stream.markdown("<br><br>", unsafe_allow_html=True)
    if pd_stream.button("🚨 STOP: COUPER LE BOT ET LES TRADES", use_container_width=True):
        pd_stream.session_state.bot_actif = False
        pd_stream.warning("Bot mis en pause forcée. Ordres en attente purgés.")

# ==========================================
# 2. ONGLET : ZONES ORDER BLOCKS (DESIGNS INJECTÉS)
# ==========================================
with onglet2:
    pd_stream.markdown("<h3 style='color: #d4af37;'>🗺️ Cartographie des Blocs Institutionnels</h3>", unsafe_allow_html=True)
    
    pd_stream.markdown("#### 🟩 Zones de Demande (Achat / Ordres en attente)")
    pd_stream.markdown("""
    <div class="demand-card">
        <h4 style="margin:0 0 5px 0; color:#10b981;">Bullish Order Block #1 (Frais)</h4>
        <p style="margin:2px 0;"><b>Zone de prix :</b> 2 340.00 $ - 2 344.50 $</p>
        <p style="margin:2px 0; color:#fff;"><b>Seuil d'entrée 50% (Mean Threshold) : 2 342.25 $</b></p>
        <p style="margin:2px 0; font-size:13px; color:#a0aec0;">⏱️ Statut : Le prix approche de la zone de mitigation.</p>
    </div>
    """, unsafe_allow_html=True)
    
    pd_stream.markdown("#### 🟥 Zones d'Offre (Vente / Target Take Profit)")
    pd_stream.markdown("""
    <div class="supply-card">
        <h4 style="margin:0 0 5px 0; color:#ef4444;">Bearish Order Block #1 (Objectif)</h4>
        <p style="margin:2px 0;"><b>Zone de prix :</b> 2 368.00 $ - 2 372.00 $</p>
        <p style="margin:2px 0;"><b>Target idéal :</b> 2 370.00 $</p>
        <p style="margin:2px 0; font-size:13px; color:#a0aec0;">⏱️ Statut : En attente du déclenchement du bloc d'achat.</p>
    </div>
    """, unsafe_allow_html=True)

# ==========================================
# 3. ONGLET : JOURNAL ML
# ==========================================
with onglet3:
    pd_stream.markdown("### 🧠 Rapport d'Optimisation de la Perte")
    log_erreur = """[LOG - 2026-06-04 22:15 GMT]
--> Erreur détectée au Trade #34.
--> Ajustement de la matrice de poids acheteuse.
--> Décision automatique : Entrée stricte au seuil des 50% de l'OB M15 requise pour éviter les Drawdowns."""
    pd_stream.code(log_erreur, language="bash")

# ==========================================
# 4. ONGLET : PARAMÈTRES
# ==========================================
with onglet4:
    pd_stream.markdown("<h3 style='color: #d4af37;'>⚙️ Gestionnaire de Risque Pro</h3>", unsafe_allow_html=True)
    
    pd_stream.session_state.risk_percent = pd_stream.slider(
        "Risque par trade (%)", min_value=0.5, max_value=3.0, value=pd_stream.session_state.risk_percent, step=0.5
    )
    valeur_risque = (pd_stream.session_state.risk_percent / 100) * pd_stream.session_state.capital
    pd_stream.success(f"Risque max toléré par position : {valeur_risque:,.0f} XOF")
    
    pd_stream.session_state.mode_entree = pd_stream.radio(
        "Protocole d'entrée", ["Limite 50% (Agressif)", "Confirmation CHoCH M1 (Sécurisé)"]
                          )
        
