from flask import Flask, render_template_string, jsonify, request, redirect, url_for, session
import os
from datetime import datetime, timedelta
import logging
import json
import random

# Configurar logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET", "savage_trader_secret")

# Puerto para Railway (CRÍTICO)
PORT = int(os.environ.get("PORT", 5000))

logger.info(f"🚀 SAVAGE TRADER PRO iniciando en puerto {PORT}")

# SISTEMA DE GAMIFICACIÓN Y RETENCIÓN AVANZADO
class GamificationSystem:
    def __init__(self):
        self.badges = {
            'first_win': {'name': '🎯 Primera Victoria', 'description': 'Tu primera operación exitosa', 'rarity': 'común'},
            'streak_master': {'name': '🔥 Racha Master', 'description': '5 operaciones consecutivas exitosas', 'rarity': 'raro'},
            'risk_manager': {'name': '🛡️ Gestor de Riesgo', 'description': 'Nunca perdiste más del 2%', 'rarity': 'épico'},
            'diamond_hands': {'name': '💎 Manos de Diamante', 'description': '1 mes sin cerrar posiciones por pánico', 'rarity': 'legendario'},
            'ai_expert': {'name': '🤖 Experto IA', 'description': 'Siguió 50+ señales de IA', 'rarity': 'raro'},
            'copy_master': {'name': '🔄 Master Copy-Trading', 'description': 'Siguió a 3+ traders durante 1 mes', 'rarity': 'épico'},
            'profit_king': {'name': '👑 Rey de Ganancias', 'description': '+50% profit en un mes', 'rarity': 'mítico'},
            'early_adopter': {'name': '🌟 Early Adopter', 'description': 'Usuario desde el plan Starter', 'rarity': 'especial'}
        }
        
    def get_user_badges(self, user_id):
        return ['first_win', 'ai_expert', 'early_adopter']
        
    def get_leaderboard(self):
        return [
            {'username': 'TradingKing', 'profit': 28.7, 'badges': 6, 'streak': 15, 'plan': 'Elite'},
            {'username': 'AITrader', 'profit': 25.3, 'badges': 5, 'streak': 12, 'plan': 'Premium'},
            {'username': 'CryptoWolf', 'profit': 22.8, 'badges': 7, 'streak': 18, 'plan': 'Elite'},
            {'username': 'DiamondHands', 'profit': 19.4, 'badges': 4, 'streak': 9, 'plan': 'Premium'},
            {'username': 'MarketMaster', 'profit': 17.2, 'badges': 5, 'streak': 11, 'plan': 'Basic'}
        ]

# SISTEMA DE ANÁLISIS AVANZADO CON IA
class AdvancedAnalytics:
    def __init__(self):
        self.market_indicators = {
            'fear_greed_index': random.randint(65, 85),
            'volatility_index': random.randint(20, 35),
            'trend_strength': random.randint(75, 95),
            'social_sentiment': 'Bullish',
            'institutional_flow': 'Buying',
            'ai_confidence': random.randint(85, 95)
        }
    
    def get_market_mood(self):
        mood_score = (self.market_indicators['fear_greed_index'] + 
                     (100 - self.market_indicators['volatility_index']) + 
                     self.market_indicators['trend_strength']) / 3
        
        if mood_score >= 80:
            return {'mood': '🚀 Extremadamente Optimista', 'color': '#10b981', 'score': int(mood_score)}
        elif mood_score >= 70:
            return {'mood': '📈 Muy Optimista', 'color': '#059669', 'score': int(mood_score)}
        elif mood_score >= 50:
            return {'mood': '⚡ Optimista', 'color': '#3b82f6', 'score': int(mood_score)}
        elif mood_score >= 30:
            return {'mood': '⚖️ Neutral', 'color': '#f59e0b', 'score': int(mood_score)}
        else:
            return {'mood': '📉 Pesimista', 'color': '#ef4444', 'score': int(mood_score)}
    
    def get_live_signals(self):
        signals = [
            {
                'symbol': 'NVDA',
                'action': 'BUY FUERTE',
                'price': 892.50,
                'change': '+2.3%',
                'target1': 920.00,
                'target2': 945.00,
                'stop_loss': 875.00,
                'confidence': 94,
                'ai_reasoning': 'Momentum alcista + flujo institucional + sentiment positivo'
            },
            {
                'symbol': 'TAO/USDT',
                'action': 'LONG AGRESIVO',
                'price': 342.50,
                'change': '+4.7%',
                'target1': 378.00,
                'target2': 410.00,
                'stop_loss': 325.00,
                'confidence': 89,
                'ai_reasoning': 'AI Catalyst: Partnership + volumen institucional x3'
            }
        ]
        return signals

# SISTEMA DE EDUCACIÓN PREMIUM
class EducationSystem:
    def __init__(self):
        self.micro_courses = [
            {
                'id': 1,
                'title': 'Fundamentos del Trading con IA',
                'duration': '5 min',
                'level': 'Principiante',
                'completion_rate': '92%',
                'lessons': ['¿Qué es el trading algorítmico?', 'Cómo funciona la IA en trading', 'Primeros pasos']
            },
            {
                'id': 2,
                'title': 'Gestión de Riesgo Avanzada',
                'duration': '8 min',
                'level': 'Intermedio',
                'completion_rate': '87%',
                'lessons': ['Stop-loss inteligente', 'Diversificación de portfolio', 'Ratio Riesgo/Beneficio']
            },
            {
                'id': 3,
                'title': 'Psicología del Trading',
                'duration': '6 min',
                'level': 'Avanzado',
                'completion_rate': '79%',
                'lessons': ['Control emocional', 'FOMO y FUD', 'Disciplina en trading']
            },
            {
                'id': 4,
                'title': 'Copy-Trading Profesional',
                'duration': '10 min',
                'level': 'Premium',
                'completion_rate': '95%',
                'lessons': ['Selección de traders', 'Gestión de capital', 'Diversificación automática']
            }
        ]
        
        self.master_class = {
            'title': 'Master Class Trading con IA',
            'price': 299,
            'duration': '20 horas',
            'modules': 12,
            'certification': True,
            'lifetime_access': True,
            'students': 1247
        }

# SISTEMA DE REFERIDOS Y MONETIZACIÓN
class ReferralSystem:
    def __init__(self):
        self.commission_rate = 0.30  # 30%
        self.referral_bonuses = {
            'starter_to_basic': {'discount': 0.50, 'duration': '1 month'},
            'basic_to_premium': {'free_weeks': 2, 'discount': 0.00},
            'premium_to_elite': {'free_month': 1, 'alpha_access': True}
        }
    
    def calculate_earnings(self, referrals, plan_prices):
        total = 0
        for plan, count in referrals.items():
            total += plan_prices.get(plan, 0) * count * self.commission_rate
        return total

# Inicializar sistemas avanzados
gamification = GamificationSystem()
analytics = AdvancedAnalytics()
education = EducationSystem()
referrals = ReferralSystem()

# TEMPLATE HTML COMPLETO Y MEJORADO
COMPLETE_ENHANCED_TEMPLATE = """<!DOCTYPE html>
<html lang="es" data-bs-theme="dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no">
    <title>SAVAGE TRADER PRO - Bot de Trading con IA</title>
    
    <!-- PWA Configuration -->
    <link rel="manifest" href="/manifest.json">
    <meta name="theme-color" content="#ffd700">
    <meta name="apple-mobile-web-app-capable" content="yes">
    <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
    <meta name="apple-mobile-web-app-title" content="SAVAGE TRADER PRO">
    
    <link href="https://cdn.replit.com/agent/bootstrap-agent-dark-theme.min.css" rel="stylesheet">
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
    <style>
        :root {
            --primary-gold: #ffd700;
            --aggressive-red: #ff0040;
            --blood-red: #8b0000;
            --elite-black: #000000;
            --steel-gray: #2a2a2a;
            --neon-blue: #00d4ff;
            --neon-purple: #b847ff;
            --neon-green: #00ff88;
            --neon-pink: #ff0080;
            --gradient-primary: linear-gradient(135deg, #ffd700 0%, #ff8c00 30%, #dc143c 70%, #8b0000 100%);
            --gradient-aggressive: linear-gradient(135deg, #ff0040 0%, #8b0000 50%, #000000 100%);
            --gradient-bg: linear-gradient(135deg, #000000 0%, #1a0000 25%, #000a1a 50%, #1a0010 75%, #0a0a0a 100%);
            --gradient-neon: linear-gradient(45deg, #ff0040, #ffd700, #00d4ff, #b847ff);
            --gradient-professional: linear-gradient(135deg, #2a2a2a 0%, #1a1a1a 50%, #0a0a0a 100%);
            --shadow-gold: 0 0 50px rgba(255, 215, 0, 0.8), 0 0 100px rgba(255, 215, 0, 0.4);
            --shadow-aggressive: 0 0 40px rgba(255, 0, 64, 0.9), 0 0 80px rgba(139, 0, 0, 0.6);
            --shadow-neon-blue: 0 0 30px rgba(0, 212, 255, 0.8), 0 0 60px rgba(0, 212, 255, 0.4);
            --shadow-neon-purple: 0 0 30px rgba(184, 71, 255, 0.8), 0 0 60px rgba(184, 71, 255, 0.4);
            --shadow-neon-green: 0 0 30px rgba(0, 255, 136, 0.8), 0 0 60px rgba(0, 255, 136, 0.4);
            --gradient-glass: linear-gradient(135deg, rgba(255,255,255,0.12) 0%, rgba(255,255,255,0.06) 100%);
            --gradient-hologram: linear-gradient(45deg, 
                transparent 0%, 
                rgba(255,0,64,0.15) 25%, 
                rgba(255,215,0,0.15) 50%, 
                rgba(0,212,255,0.15) 75%, 
                transparent 100%);
        }
        
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Exo+2:wght@300;400;600;700;800;900&display=swap');
        
        body {
            background: var(--gradient-bg);
            color: white;
            font-family: 'Exo 2', sans-serif;
            overflow-x: hidden;
            line-height: 1.6;
            position: relative;
        }
        
        body::before {
            content: '';
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: 
                radial-gradient(circle at 20% 80%, rgba(255,0,64,0.15) 0%, transparent 50%),
                radial-gradient(circle at 80% 20%, rgba(255,215,0,0.12) 0%, transparent 50%),
                radial-gradient(circle at 40% 40%, rgba(139,0,0,0.1) 0%, transparent 50%),
                linear-gradient(180deg, transparent 0%, rgba(0,0,0,0.4) 100%);
            pointer-events: none;
            z-index: -2;
            animation: backgroundShift 25s ease-in-out infinite;
        }
        
        @keyframes backgroundShift {
            0%, 100% { 
                background: 
                    radial-gradient(circle at 20% 80%, rgba(255,0,64,0.15) 0%, transparent 50%),
                    radial-gradient(circle at 80% 20%, rgba(255,215,0,0.12) 0%, transparent 50%),
                    linear-gradient(180deg, transparent 0%, rgba(0,0,0,0.4) 100%);
            }
            33% { 
                background: 
                    radial-gradient(circle at 80% 80%, rgba(139,0,0,0.15) 0%, transparent 50%),
                    radial-gradient(circle at 20% 20%, rgba(255,215,0,0.12) 0%, transparent 50%),
                    linear-gradient(180deg, transparent 0%, rgba(20,0,0,0.4) 100%);
            }
            66% { 
                background: 
                    radial-gradient(circle at 50% 50%, rgba(255,215,0,0.15) 0%, transparent 50%),
                    radial-gradient(circle at 10% 90%, rgba(139,0,0,0.12) 0%, transparent 50%),
                    linear-gradient(180deg, transparent 0%, rgba(10,5,0,0.4) 100%);
            }
        }
        
        /* Cielo estrellado animado */
        body::after {
            content: '';
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-image: 
                radial-gradient(2px 2px at 20px 30px, #fff, transparent),
                radial-gradient(1px 1px at 40px 70px, rgba(255,255,255,0.8), transparent),
                radial-gradient(1px 1px at 90px 40px, #fff, transparent),
                radial-gradient(1px 1px at 130px 80px, rgba(255,255,255,0.6), transparent),
                radial-gradient(2px 2px at 160px 30px, #fff, transparent),
                radial-gradient(1px 1px at 200px 90px, rgba(255,255,255,0.7), transparent),
                radial-gradient(2px 2px at 240px 20px, rgba(255,255,255,0.9), transparent),
                radial-gradient(1px 1px at 280px 60px, #fff, transparent),
                radial-gradient(1px 1px at 320px 100px, rgba(255,255,255,0.8), transparent),
                radial-gradient(2px 2px at 360px 50px, #fff, transparent),
                radial-gradient(3px 3px at 80px 120px, #ffd700, transparent),
                radial-gradient(4px 4px at 220px 160px, rgba(255,215,0,0.8), transparent),
                radial-gradient(3px 3px at 350px 80px, #fff, transparent),
                radial-gradient(2px 2px at 150px 200px, rgba(255,255,255,0.9), transparent),
                radial-gradient(4px 4px at 300px 140px, rgba(255,215,0,0.7), transparent),
                radial-gradient(3px 3px at 50px 180px, #fff, transparent);
            background-repeat: repeat;
            background-size: 400px 250px;
            animation: starryNight 30s linear infinite;
            pointer-events: none;
            z-index: -1;
            opacity: 0.7;
        }
        
        @keyframes starryNight {
            0% { 
                transform: translateX(0px) translateY(0px);
                opacity: 0.7;
            }
            25% { 
                opacity: 0.9;
            }
            50% { 
                transform: translateX(-100px) translateY(-50px);
                opacity: 0.6;
            }
            75% { 
                opacity: 0.8;
            }
            100% { 
                transform: translateX(-200px) translateY(-100px);
                opacity: 0.7;
            }
        }
        
        /* Estrellas parpadeantes adicionales */
        .starry-overlay {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: 
                radial-gradient(1px 1px at 15% 25%, #fff, transparent),
                radial-gradient(2px 2px at 75% 15%, rgba(255,215,0,0.9), transparent),
                radial-gradient(1px 1px at 35% 75%, #fff, transparent),
                radial-gradient(3px 3px at 85% 85%, rgba(255,255,255,0.8), transparent),
                radial-gradient(2px 2px at 25% 45%, rgba(255,215,0,0.7), transparent),
                radial-gradient(1px 1px at 65% 35%, #fff, transparent),
                radial-gradient(2px 2px at 95% 55%, rgba(255,255,255,0.9), transparent);
            animation: twinkle 8s ease-in-out infinite;
            pointer-events: none;
            z-index: -1;
            opacity: 0.5;
        }
        
        @keyframes twinkle {
            0%, 100% { opacity: 0.5; }
            25% { opacity: 0.8; }
            50% { opacity: 0.3; }
            75% { opacity: 0.9; }
        }
        
        .container-fluid {
            padding: 0;
        }
        
        .logo-container {
            text-align: center;
            margin: 30px 0;
            position: relative;
        }
        
        .logo-svg {
            width: 300px;
            height: 300px;
            max-width: 90vw;
            margin: 0 auto;
            animation: logoFloat 6s ease-in-out infinite, logoGlow 4s ease-in-out infinite alternate;
            filter: drop-shadow(0 0 30px rgba(255,215,0,0.8)) 
                    drop-shadow(0 0 60px rgba(255,0,64,0.6)) 
                    drop-shadow(0 0 90px rgba(139,0,0,0.4));
        }
        
        @keyframes logoFloat {
            0%, 100% { transform: translateY(0px) scale(1); }
            50% { transform: translateY(-20px) scale(1.05); }
        }
        
        @keyframes logoGlow {
            0% { filter: drop-shadow(0 0 30px rgba(255,215,0,0.8)) drop-shadow(0 0 60px rgba(255,0,64,0.6)); }
            100% { filter: drop-shadow(0 0 50px rgba(255,215,0,1)) drop-shadow(0 0 100px rgba(255,0,64,0.8)); }
        }
        
        .hero-title {
            font-family: 'Orbitron', monospace;
            font-size: clamp(2.5rem, 8vw, 5rem);
            font-weight: 900;
            background: var(--gradient-primary);
            -webkit-background-clip: text;
            background-clip: text;
            -webkit-text-fill-color: transparent;
            text-align: center;
            margin: 30px 0;
            text-shadow: 0 0 50px rgba(255, 215, 0, 0.8);
            animation: titlePulse 3s ease-in-out infinite alternate;
            letter-spacing: 2px;
        }
        
        @keyframes titlePulse {
            0% { 
                transform: scale(1);
                text-shadow: 0 0 50px rgba(255, 215, 0, 0.8), 0 0 100px rgba(255, 0, 64, 0.4);
            }
            100% { 
                transform: scale(1.02);
                text-shadow: 0 0 70px rgba(255, 215, 0, 1), 0 0 140px rgba(255, 0, 64, 0.6);
            }
        }
        
        .hero-subtitle {
            font-family: 'Exo 2', sans-serif;
            font-size: clamp(1.2rem, 4vw, 2rem);
            font-weight: 700;
            color: #ffffff;
            text-align: center;
            margin-bottom: 40px;
            text-shadow: 0 0 20px rgba(255, 255, 255, 0.8);
            opacity: 0.95;
        }
        
        .status-online {
            color: var(--neon-green);
            font-weight: 700;
            text-align: center;
            margin: 20px 0;
            animation: statusPulse 2s ease-in-out infinite;
            text-shadow: 0 0 20px rgba(0, 255, 136, 0.8);
        }
        
        @keyframes statusPulse {
            0%, 100% { opacity: 0.8; }
            50% { opacity: 1; }
        }
        
        .market-mood-card {
            background: var(--gradient-glass);
            border: 2px solid rgba(255, 215, 0, 0.3);
            border-radius: 20px;
            padding: 25px;
            margin: 20px 0;
            backdrop-filter: blur(20px);
            box-shadow: var(--shadow-gold);
            position: relative;
            overflow: hidden;
            transition: all 0.3s ease;
        }
        
        .market-mood-card:hover {
            transform: translateY(-5px);
            border-color: rgba(255, 215, 0, 0.6);
            box-shadow: 
                0 0 60px rgba(255, 215, 0, 0.9), 
                0 0 120px rgba(255, 215, 0, 0.5),
                0 20px 40px rgba(0, 0, 0, 0.3);
        }
        
        .market-mood-card::before {
            content: '';
            position: absolute;
            top: -50%;
            left: -50%;
            width: 200%;
            height: 200%;
            background: var(--gradient-hologram);
            animation: hologramSweep 8s linear infinite;
            opacity: 0.1;
            pointer-events: none;
        }
        
        @keyframes hologramSweep {
            0% { transform: translateX(-100%) translateY(-100%) rotate(45deg); }
            100% { transform: translateX(100%) translateY(100%) rotate(45deg); }
        }
        
        .mood-score {
            font-size: 3rem;
            font-weight: 900;
            font-family: 'Orbitron', monospace;
            margin: 10px 0;
        }
        
        .mood-indicator {
            font-size: 1.5rem;
            font-weight: 700;
            margin: 15px 0;
            padding: 15px;
            border-radius: 15px;
            background: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.2);
            text-align: center;
        }
        
        .signal-item {
            background: var(--gradient-professional);
            border: 1px solid rgba(255, 215, 0, 0.3);
            border-radius: 15px;
            padding: 20px;
            margin: 15px 0;
            transition: all 0.3s ease;
            position: relative;
            overflow: hidden;
        }
        
        .signal-item:hover {
            transform: translateY(-3px);
            border-color: rgba(255, 215, 0, 0.6);
            box-shadow: 0 10px 30px rgba(255, 215, 0, 0.3);
        }
        
        .signal-item::before {
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 2px;
            background: var(--gradient-primary);
            animation: signalSweep 3s ease-in-out infinite;
        }
        
        @keyframes signalSweep {
            0% { left: -100%; }
            50% { left: 100%; }
            100% { left: -100%; }
        }
        
        .signal-symbol {
            font-size: 1.8rem;
            font-weight: 900;
            color: var(--primary-gold);
            margin-bottom: 10px;
        }
        
        .signal-action {
            font-size: 1.3rem;
            font-weight: 800;
            padding: 8px 15px;
            border-radius: 20px;
            display: inline-block;
            margin: 10px 0;
        }
        
        .action-buy {
            background: linear-gradient(135deg, #10b981 0%, #059669 100%);
            box-shadow: var(--shadow-neon-green);
        }
        
        .action-sell {
            background: linear-gradient(135deg, #ef4444 0%, #dc2626 100%);
            box-shadow: var(--shadow-aggressive);
        }
        
        .action-long {
            background: linear-gradient(135deg, #3b82f6 0%, #1d4ed8 100%);
            box-shadow: var(--shadow-neon-blue);
        }
        
        .confidence-bar {
            width: 100%;
            height: 8px;
            background: rgba(255, 255, 255, 0.1);
            border-radius: 10px;
            overflow: hidden;
            margin: 15px 0;
            position: relative;
        }
        
        .confidence-fill {
            height: 100%;
            border-radius: 10px;
            background: var(--gradient-primary);
            transition: width 2s ease-in-out;
            animation: confidencePulse 2s ease-in-out infinite alternate;
        }
        
        @keyframes confidencePulse {
            0% { box-shadow: 0 0 10px rgba(255, 215, 0, 0.5); }
            100% { box-shadow: 0 0 20px rgba(255, 215, 0, 0.8); }
        }
        
        .price-card {
            background: var(--gradient-glass);
            border: 2px solid rgba(255, 0, 64, 0.3);
            border-radius: 20px;
            padding: 25px;
            margin: 20px 0;
            backdrop-filter: blur(20px);
            box-shadow: var(--shadow-aggressive);
            transition: all 0.3s ease;
            position: relative;
            overflow: hidden;
        }
        
        .price-card:hover {
            transform: translateY(-5px) scale(1.02);
            border-color: rgba(255, 0, 64, 0.8);
            box-shadow: 
                0 0 60px rgba(255, 0, 64, 0.9),
                0 0 120px rgba(255, 0, 64, 0.5),
                0 20px 40px rgba(0, 0, 0, 0.3);
        }
        
        .price-card::before {
            content: '';
            position: absolute;
            top: -2px;
            left: -2px;
            right: -2px;
            bottom: -2px;
            background: var(--gradient-primary);
            border-radius: 22px;
            z-index: -1;
            opacity: 0;
            transition: opacity 0.3s ease;
        }
        
        .price-card:hover::before {
            opacity: 1;
        }
        
        .plan-title {
            font-family: 'Orbitron', monospace;
            font-size: 2rem;
            font-weight: 900;
            margin-bottom: 20px;
            text-align: center;
        }
        
        .plan-price {
            font-size: 3.5rem;
            font-weight: 900;
            text-align: center;
            margin: 20px 0;
            font-family: 'Orbitron', monospace;
        }
        
        .plan-features {
            list-style: none;
            padding: 0;
        }
        
        .plan-features li {
            padding: 10px 0;
            border-bottom: 1px solid rgba(255, 255, 255, 0.1);
            font-weight: 600;
        }
        
        .plan-features li:before {
            content: '✓ ';
            color: var(--neon-green);
            font-weight: 900;
            margin-right: 10px;
        }
        
        .btn-savage {
            background: var(--gradient-primary);
            border: none;
            padding: 18px 40px;
            border-radius: 50px;
            font-weight: 900;
            font-size: 1.2rem;
            color: #000000;
            text-transform: uppercase;
            letter-spacing: 2px;
            transition: all 0.3s ease;
            box-shadow: var(--shadow-gold);
            position: relative;
            overflow: hidden;
        }
        
        .btn-savage::before {
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, transparent, rgba(255,255,255,0.4), transparent);
            transition: left 0.6s;
        }
        
        .btn-savage:hover::before {
            left: 100%;
        }
        
        .btn-savage:hover {
            transform: translateY(-3px) scale(1.05);
            box-shadow: 
                0 0 60px rgba(255, 215, 0, 1),
                0 0 120px rgba(255, 215, 0, 0.6),
                0 15px 35px rgba(0, 0, 0, 0.3);
        }
        
        .trader-card {
            background: var(--gradient-professional);
            border: 2px solid rgba(0, 212, 255, 0.3);
            border-radius: 20px;
            padding: 25px;
            margin: 20px 0;
            backdrop-filter: blur(20px);
            box-shadow: var(--shadow-neon-blue);
            transition: all 0.3s ease;
            position: relative;
        }
        
        .trader-card:hover {
            transform: translateY(-5px);
            border-color: rgba(0, 212, 255, 0.8);
            box-shadow: 
                0 0 60px rgba(0, 212, 255, 0.9),
                0 0 120px rgba(0, 212, 255, 0.5);
        }
        
        .trader-name {
            font-size: 1.5rem;
            font-weight: 900;
            color: var(--neon-blue);
            margin-bottom: 10px;
            font-family: 'Orbitron', monospace;
        }
        
        .trader-stats {
            display: flex;
            justify-content: space-between;
            flex-wrap: wrap;
            gap: 15px;
            margin: 20px 0;
        }
        
        .stat-item {
            text-align: center;
            padding: 15px;
            background: rgba(255, 255, 255, 0.05);
            border-radius: 10px;
            border: 1px solid rgba(255, 255, 255, 0.1);
            flex: 1;
            min-width: 120px;
        }
        
        .stat-value {
            font-size: 1.8rem;
            font-weight: 900;
            color: var(--neon-green);
            display: block;
            margin-bottom: 5px;
            font-family: 'Orbitron', monospace;
        }
        
        .stat-label {
            font-size: 0.9rem;
            color: rgba(255, 255, 255, 0.8);
            font-weight: 600;
        }
        
        .badge-container {
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
            margin: 20px 0;
            justify-content: center;
        }
        
        .badge-item {
            background: var(--gradient-glass);
            border: 1px solid rgba(255, 215, 0, 0.3);
            padding: 8px 16px;
            border-radius: 25px;
            font-size: 0.9rem;
            font-weight: 700;
            backdrop-filter: blur(10px);
            transition: all 0.3s ease;
        }
        
        .badge-item:hover {
            border-color: rgba(255, 215, 0, 0.8);
            transform: scale(1.05);
            box-shadow: 0 0 20px rgba(255, 215, 0, 0.5);
        }
        
        .badge-rarity-común {
            border-color: rgba(128, 128, 128, 0.5);
            color: #a0a0a0;
        }
        
        .badge-rarity-raro {
            border-color: rgba(0, 212, 255, 0.5);
            color: var(--neon-blue);
            box-shadow: 0 0 15px rgba(0, 212, 255, 0.3);
        }
        
        .badge-rarity-épico {
            border-color: rgba(184, 71, 255, 0.5);
            color: var(--neon-purple);
            box-shadow: 0 0 15px rgba(184, 71, 255, 0.3);
        }
        
        .badge-rarity-legendario {
            border-color: rgba(255, 215, 0, 0.8);
            color: var(--primary-gold);
            box-shadow: 0 0 20px rgba(255, 215, 0, 0.5);
            animation: legendaryGlow 2s ease-in-out infinite alternate;
        }
        
        .badge-rarity-mítico {
            border-color: rgba(255, 0, 128, 0.8);
            color: var(--neon-pink);
            box-shadow: 0 0 25px rgba(255, 0, 128, 0.6);
            animation: mythicPulse 1.5s ease-in-out infinite;
        }
        
        @keyframes legendaryGlow {
            0% { box-shadow: 0 0 20px rgba(255, 215, 0, 0.5); }
            100% { box-shadow: 0 0 40px rgba(255, 215, 0, 0.8), 0 0 60px rgba(255, 215, 0, 0.4); }
        }
        
        @keyframes mythicPulse {
            0%, 100% { 
                transform: scale(1);
                box-shadow: 0 0 25px rgba(255, 0, 128, 0.6);
            }
            50% { 
                transform: scale(1.05);
                box-shadow: 0 0 35px rgba(255, 0, 128, 0.9), 0 0 50px rgba(255, 0, 128, 0.5);
            }
        }
        
        .leaderboard-item {
            background: var(--gradient-professional);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 15px;
            padding: 20px;
            margin: 15px 0;
            display: flex;
            align-items: center;
            gap: 20px;
            transition: all 0.3s ease;
        }
        
        .leaderboard-item:hover {
            border-color: rgba(255, 215, 0, 0.5);
            transform: translateX(10px);
            background: rgba(255, 215, 0, 0.05);
        }
        
        .leaderboard-rank {
            font-size: 2rem;
            font-weight: 900;
            color: var(--primary-gold);
            min-width: 60px;
            text-align: center;
            font-family: 'Orbitron', monospace;
        }
        
        .leaderboard-info {
            flex: 1;
        }
        
        .leaderboard-username {
            font-size: 1.3rem;
            font-weight: 900;
            margin-bottom: 5px;
            color: var(--neon-blue);
        }
        
        .leaderboard-stats {
            font-size: 0.9rem;
            color: rgba(255, 255, 255, 0.8);
            display: flex;
            gap: 15px;
            flex-wrap: wrap;
        }
        
        .responsive-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 20px;
            margin: 30px 0;
        }
        
        /* Responsive Design */
        @media (max-width: 768px) {
            .hero-title {
                font-size: 3rem;
                margin: 20px 0;
            }
            
            .hero-subtitle {
                font-size: 1.5rem;
                margin-bottom: 30px;
            }
            
            .logo-svg {
                width: 250px;
                height: 250px;
            }
            
            .plan-price {
                font-size: 2.5rem;
            }
            
            .trader-stats {
                flex-direction: column;
            }
            
            .stat-item {
                min-width: auto;
            }
            
            .leaderboard-item {
                flex-direction: column;
                text-align: center;
                gap: 10px;
            }
            
            .leaderboard-stats {
                justify-content: center;
            }
            
            .responsive-grid {
                grid-template-columns: 1fr;
                gap: 15px;
            }
        }
        
        @media (max-width: 480px) {
            .hero-title {
                font-size: 2.2rem;
            }
            
            .hero-subtitle {
                font-size: 1.2rem;
            }
            
            .logo-svg {
                width: 200px;
                height: 200px;
            }
            
            .market-mood-card,
            .price-card,
            .trader-card {
                padding: 20px;
                margin: 15px 0;
            }
            
            .btn-savage {
                padding: 15px 30px;
                font-size: 1rem;
            }
        }
        
        /* Animaciones adicionales para elementos interactivos */
        .interactive-element {
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        }
        
        .interactive-element:hover {
            transform: translateY(-2px);
        }
        
        .interactive-element:active {
            transform: translateY(0);
        }
        
        /* Efectos de carga */
        .loading-shimmer {
            background: linear-gradient(90deg, 
                rgba(255,255,255,0.1) 0%, 
                rgba(255,255,255,0.3) 50%, 
                rgba(255,255,255,0.1) 100%);
            background-size: 200% 100%;
            animation: shimmer 1.5s infinite;
        }
        
        @keyframes shimmer {
            0% { background-position: -200% 0; }
            100% { background-position: 200% 0; }
        }
        
        /* Scroll suave */
        html {
            scroll-behavior: smooth;
        }
        
        /* Mejoras de accesibilidad */
        .sr-only {
            position: absolute;
            width: 1px;
            height: 1px;
            padding: 0;
            margin: -1px;
            overflow: hidden;
            clip: rect(0, 0, 0, 0);
            white-space: nowrap;
            border: 0;
        }
        
        /* Focus states para accesibilidad */
        .btn-savage:focus,
        .interactive-element:focus {
            outline: 2px solid var(--primary-gold);
            outline-offset: 2px;
        }
    </style>
</head>
<body>
    <div class="starry-overlay"></div>
    
    <div class="container-fluid">
        <!-- Logo y Título Principal -->
        <div class="logo-container">
            <svg class="logo-svg" viewBox="0 0 300 300" xmlns="http://www.w3.org/2000/svg">
                <!-- Fondo circular con gradiente -->
                <defs>
                    <radialGradient id="bgGradient" cx="50%" cy="50%" r="50%">
                        <stop offset="0%" style="stop-color:#ffd700;stop-opacity:0.3" />
                        <stop offset="50%" style="stop-color:#ff0040;stop-opacity:0.2" />
                        <stop offset="100%" style="stop-color:#8b0000;stop-opacity:0.1" />
                    </radialGradient>
                    <linearGradient id="wolfGradient" x1="0%" y1="0%" x2="100%" y2="100%">
                        <stop offset="0%" style="stop-color:#ffd700" />
                        <stop offset="30%" style="stop-color:#ff8c00" />
                        <stop offset="70%" style="stop-color:#dc143c" />
                        <stop offset="100%" style="stop-color:#8b0000" />
                    </linearGradient>
                    <filter id="glow">
                        <feGaussianBlur stdDeviation="4" result="coloredBlur"/>
                        <feMerge> 
                            <feMergeNode in="coloredBlur"/>
                            <feMergeNode in="SourceGraphic"/>
                        </feMerge>
                    </filter>
                </defs>
                
                <!-- Círculo de fondo -->
                <circle cx="150" cy="150" r="145" fill="url(#bgGradient)" opacity="0.6"/>
                
                <!-- Círculo principal -->
                <circle cx="150" cy="150" r="140" fill="none" stroke="url(#wolfGradient)" stroke-width="6" opacity="0.8"/>
                
                <!-- Cara del lobo estilizada -->
                <g transform="translate(150,150)" filter="url(#glow)">
                    <!-- Orejas -->
                    <path d="M-40,-80 L-20,-100 L-15,-75 Z" fill="url(#wolfGradient)"/>
                    <path d="M40,-80 L20,-100 L15,-75 Z" fill="url(#wolfGradient)"/>
                    
                    <!-- Cabeza principal -->
                    <ellipse cx="0" cy="-20" rx="45" ry="55" fill="url(#wolfGradient)" opacity="0.9"/>
                    
                    <!-- Hocico -->
                    <ellipse cx="0" cy="10" rx="25" ry="35" fill="url(#wolfGradient)" opacity="0.8"/>
                    
                    <!-- Ojos -->
                    <circle cx="-18" cy="-35" r="8" fill="#ffd700"/>
                    <circle cx="18" cy="-35" r="8" fill="#ffd700"/>
                    <circle cx="-18" cy="-35" r="4" fill="#000"/>
                    <circle cx="18" cy="-35" r="4" fill="#000"/>
                    
                    <!-- Nariz -->
                    <ellipse cx="0" cy="-5" rx="4" ry="6" fill="#000"/>
                    
                    <!-- Boca -->
                    <path d="M0,5 Q-8,15 -15,10 Q-8,20 0,15 Q8,20 15,10 Q8,15 0,5" fill="#000" opacity="0.6"/>
                    
                    <!-- Colmillos -->
                    <path d="M-8,10 L-6,20 L-10,20 Z" fill="#fff"/>
                    <path d="M8,10 L6,20 L10,20 Z" fill="#fff"/>
                </g>
                
                <!-- Texto "SAVAGE" curvado -->
                <path id="topCurve" d="M 50,150 A 100,100 0 0,1 250,150" fill="none"/>
                <text font-family="Orbitron, monospace" font-size="24" font-weight="900" fill="url(#wolfGradient)">
                    <textPath href="#topCurve" startOffset="50%" text-anchor="middle">
                        SAVAGE TRADER
                    </textPath>
                </text>
                
                <!-- Texto "PRO" curvado -->
                <path id="bottomCurve" d="M 250,150 A 100,100 0 0,1 50,150" fill="none"/>
                <text font-family="Orbitron, monospace" font-size="20" font-weight="900" fill="url(#wolfGradient)">
                    <textPath href="#bottomCurve" startOffset="50%" text-anchor="middle">
                        • PRO •
                    </textPath>
                </text>
                
                <!-- Elementos decorativos -->
                <g opacity="0.6">
                    <circle cx="80" cy="80" r="3" fill="#ffd700"/>
                    <circle cx="220" cy="80" r="2" fill="#ff0040"/>
                    <circle cx="80" cy="220" r="2" fill="#8b0000"/>
                    <circle cx="220" cy="220" r="3" fill="#ffd700"/>
                </g>
            </svg>
        </div>
        
        <h1 class="hero-title">SAVAGE TRADER PRO</h1>
        <p class="hero-subtitle">💎 Bot de Trading con IA Avanzada 💎</p>
        
        <div class="status-online">
            <i class="fas fa-circle" style="color: #00ff88;"></i> 
            Sistema Online 24/7 • IA GPT-4 Activa • Copy-Trading Elite
        </div>
        
        <!-- Market Mood Indicator -->
        <div class="market-mood-card">
            <h3 style="text-align: center; margin-bottom: 25px; font-family: 'Orbitron', monospace;">
                🎯 Market Mood Indicator
            </h3>
            <div class="mood-score" style="color: {{ market_mood.color }}; text-align: center;">
                {{ market_mood.score }}%
            </div>
            <div class="mood-indicator" style="color: {{ market_mood.color }};">
                {{ market_mood.mood }}
            </div>
            <div class="row mt-4">
                <div class="col-6">
                    <div class="text-center">
                        <div style="font-size: 2rem; color: #ffd700;">{{ market_indicators.fear_greed_index }}</div>
                        <div style="font-size: 0.9rem; color: rgba(255,255,255,0.8);">Fear & Greed</div>
                    </div>
                </div>
                <div class="col-6">
                    <div class="text-center">
                        <div style="font-size: 2rem; color: #00d4ff;">{{ market_indicators.ai_confidence }}%</div>
                        <div style="font-size: 0.9rem; color: rgba(255,255,255,0.8);">IA Confidence</div>
                    </div>
                </div>
            </div>
        </div>
        
        <!-- Señales en Vivo -->
        <section class="my-5">
            <h3 style="text-align: center; margin-bottom: 30px; font-family: 'Orbitron', monospace; color: var(--primary-gold);">
                🚀 Señales Elite en Vivo
            </h3>
            {% for signal in live_signals %}
            <div class="signal-item">
                <div class="signal-symbol">{{ signal.symbol }}</div>
                <div class="signal-action {% if 'BUY' in signal.action %}action-buy{% elif 'LONG' in signal.action %}action-long{% else %}action-sell{% endif %}">
                    {{ signal.action }}
                </div>
                <div class="row mt-3">
                    <div class="col-md-6">
                        <div><strong>Precio:</strong> ${{ "%.2f"|format(signal.price) }}</div>
                        <div><strong>Cambio:</strong> <span style="color: #10b981;">{{ signal.change }}</span></div>
                        <div><strong>Target 1:</strong> ${{ "%.2f"|format(signal.target1) }}</div>
                        <div><strong>Target 2:</strong> ${{ "%.2f"|format(signal.target2) }}</div>
                        <div><strong>Stop Loss:</strong> ${{ "%.2f"|format(signal.stop_loss) }}</div>
                    </div>
                    <div class="col-md-6">
                        <div><strong>Confianza IA:</strong></div>
                        <div class="confidence-bar">
                            <div class="confidence-fill" style="width: {{ signal.confidence }}%;"></div>
                        </div>
                        <div style="text-align: center; font-weight: 700;">{{ signal.confidence }}%</div>
                        <div style="margin-top: 10px; font-size: 0.9rem; color: rgba(255,255,255,0.8);">
                            {{ signal.ai_reasoning }}
                        </div>
                    </div>
                </div>
            </div>
            {% endfor %}
        </section>
        
        <!-- Copy-Trading Elite -->
        <section class="my-5">
            <h3 style="text-align: center; margin-bottom: 30px; font-family: 'Orbitron', monospace; color: var(--neon-blue);">
                🔄 Copy-Trading Elite
            </h3>
            <div class="responsive-grid">
                {% for trader_id, trader in elite_traders.items() %}
                <div class="trader-card">
                    <div class="trader-name">{{ trader.name }}</div>
                    <div style="color: var(--neon-purple); font-weight: 700; margin-bottom: 15px;">
                        {{ trader.specialty }}
                    </div>
                    <div class="trader-stats">
                        <div class="stat-item">
                            <span class="stat-value">{{ trader.success_rate }}%</span>
                            <span class="stat-label">Éxito</span>
                        </div>
                        <div class="stat-item">
                            <span class="stat-value">{{ trader.monthly_return }}%</span>
                            <span class="stat-label">Retorno</span>
                        </div>
                        <div class="stat-item">
                            <span class="stat-value">{{ trader.followers }}</span>
                            <span class="stat-label">Seguidores</span>
                        </div>
                    </div>
                    <div style="text-align: center; margin: 15px 0; padding: 10px; background: rgba(0,255,136,0.1); border-radius: 10px;">
                        <strong>{{ trader.description }}</strong>
                    </div>
                    <button class="btn btn-savage w-100">Seguir Trader</button>
                </div>
                {% endfor %}
            </div>
        </section>
        
        <!-- Sistema de Gamificación -->
        <section class="my-5">
            <h3 style="text-align: center; margin-bottom: 30px; font-family: 'Orbitron', monospace; color: var(--neon-purple);">
                🏆 Sistema de Gamificación
            </h3>
            
            <!-- Badges -->
            <div style="text-align: center; margin-bottom: 30px;">
                <h4 style="color: var(--primary-gold); margin-bottom: 20px;">Tus Badges</h4>
                <div class="badge-container">
                    {% for badge_id in ['first_win', 'ai_expert', 'early_adopter'] %}
                        {% set badge = badges[badge_id] %}
                        <div class="badge-item badge-rarity-{{ badge.rarity }}">
                            {{ badge.name }}
                        </div>
                    {% endfor %}
                </div>
            </div>
            
            <!-- Leaderboard -->
            <div>
                <h4 style="color: var(--neon-blue); text-align: center; margin-bottom: 25px;">🥇 Leaderboard Elite</h4>
                {% for leader in leaderboard[:5] %}
                <div class="leaderboard-item">
                    <div class="leaderboard-rank">#{{ loop.index }}</div>
                    <div class="leaderboard-info">
                        <div class="leaderboard-username">{{ leader.username }}</div>
                        <div class="leaderboard-stats">
                            <span><strong>Profit:</strong> +{{ leader.profit }}%</span>
                            <span><strong>Badges:</strong> {{ leader.badges }}</span>
                            <span><strong>Racha:</strong> {{ leader.streak }}</span>
                            <span><strong>Plan:</strong> {{ leader.plan }}</span>
                        </div>
                    </div>
                </div>
                {% endfor %}
            </div>
        </section>
        
        <!-- Planes de Precio -->
        <section class="my-5">
            <h3 style="text-align: center; margin-bottom: 40px; font-family: 'Orbitron', monospace; color: var(--aggressive-red);">
                💰 Planes Elite SAVAGE TRADER
            </h3>
            <div class="responsive-grid">
                <!-- Plan Starter -->
                <div class="price-card" style="border-color: rgba(128, 128, 128, 0.5);">
                    <div class="plan-title" style="color: #a0a0a0;">🚀 STARTER</div>
                    <div class="plan-price" style="color: #a0a0a0;">€5.99<small>/semana</small></div>
                    <ul class="plan-features">
                        <li>5 señales IA diarias</li>
                        <li>Market Mood básico</li>
                        <li>1 trader copy-trading</li>
                        <li>Soporte por email</li>
                        <li>Análisis técnico básico</li>
                    </ul>
                    <button class="btn btn-savage w-100 mt-4">Empezar</button>
                </div>
                
                <!-- Plan Basic -->
                <div class="price-card" style="border-color: rgba(0, 212, 255, 0.5);">
                    <div class="plan-title" style="color: var(--neon-blue);">⚡ BASIC</div>
                    <div class="plan-price" style="color: var(--neon-blue);">€29<small>/mes</small></div>
                    <ul class="plan-features">
                        <li>Señales IA ilimitadas</li>
                        <li>Market Mood avanzado</li>
                        <li>3 traders copy-trading</li>
                        <li>Análisis de sentimiento</li>
                        <li>Alerts personalizadas</li>
                        <li>Soporte prioritario</li>
                    </ul>
                    <button class="btn btn-savage w-100 mt-4">Ser Basic</button>
                </div>
                
                <!-- Plan Premium -->
                <div class="price-card" style="border-color: rgba(255, 215, 0, 0.8); box-shadow: 0 0 60px rgba(255, 215, 0, 0.4);">
                    <div class="plan-title" style="color: var(--primary-gold);">👑 PREMIUM</div>
                    <div class="plan-price" style="color: var(--primary-gold);">€99<small>/mes</small></div>
                    <ul class="plan-features">
                        <li>Todo de Basic +</li>
                        <li>Todos los traders elite</li>
                        <li>IA GPT-4 avanzada</li>
                        <li>Análisis macro económico</li>
                        <li>Risk management IA</li>
                        <li>Señales pre-market</li>
                        <li>Webinars exclusivos</li>
                        <li>Telegram VIP</li>
                    </ul>
                    <button class="btn btn-savage w-100 mt-4">Ser Premium</button>
                </div>
                
                <!-- Plan Elite -->
                <div class="price-card" style="border-color: rgba(255, 0, 64, 0.8); box-shadow: 0 0 60px rgba(255, 0, 64, 0.6);">
                    <div class="plan-title" style="color: var(--aggressive-red);">🔥 ELITE</div>
                    <div class="plan-price" style="color: var(--aggressive-red);">€199<small>/mes</small></div>
                    <ul class="plan-features">
                        <li>Todo de Premium +</li>
                        <li>Acceso a Alpha Signals</li>
                        <li>1-on-1 con traders pro</li>
                        <li>API trading automation</li>
                        <li>Portfolio management IA</li>
                        <li>Backtesting avanzado</li>
                        <li>Academia SAVAGE completa</li>
                        <li>Master Class €299 GRATIS</li>
                        <li>WhatsApp directo</li>
                    </ul>
                    <button class="btn btn-savage w-100 mt-4">Ser Elite</button>
                </div>
            </div>
        </section>
        
        <!-- Footer Status -->
        <footer class="text-center py-4">
            <div class="status-online mb-3">
                <i class="fas fa-circle"></i> Sistema Online • 
                <i class="fas fa-robot"></i> IA GPT-4 Activa • 
                <i class="fas fa-chart-line"></i> 20 Mercados Monitoreados •
                <i class="fas fa-copy"></i> Copy-Trading Activo
            </div>
            <p>
                <strong>© 2024 SAVAGE TRADER PRO</strong><br>
                <small>Bot de Trading con IA • Wolf of Wall Street Design • Railway Production 24/7</small>
            </p>
        </footer>
    </div>
    
    <!-- Bootstrap JS -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
    
    <script>
        document.addEventListener('DOMContentLoaded', function() {
            console.log('🚀 SAVAGE TRADER PRO - GitHub/Railway Production v1.0');
            console.log('🐺 Wolf of Wall Street Design System');
            console.log('💎 Premium Trading Bot con IA Avanzada');
            console.log('📊 4 Planes: Starter €5.99/sem, Basic €29, Premium €99, Elite €199');
            console.log('🏆 Sistema de Gamificación Completo');
            console.log('📚 Academia de Trading con Master Class');
            console.log('🤝 Programa de Referidos 30%');
            console.log('🎯 Market Mood Indicator + Analytics');
            console.log('🤖 Demo con IA GPT-4 avanzada');
            console.log('✨ Todas las mejoras implementadas');
            
            // Auto-refresh de datos cada 30 segundos
            setInterval(() => {
                fetch('/api/market_mood')
                    .then(response => response.json())
                    .then(data => {
                        console.log('📊 Market mood updated:', data);
                    })
                    .catch(error => console.log('Operating in offline mode'));
            }, 30000);
            
            // Efectos de hover
            document.querySelectorAll('.price-card, .trader-card, .signal-item').forEach(card => {
                card.addEventListener('mouseenter', function() {
                    this.style.transition = 'all 0.3s ease';
                });
            });
        });
    </script>
</body>
</html>"""

# RUTAS DE LA APLICACIÓN
@app.route('/')
def index():
    return render_template_string(COMPLETE_ENHANCED_TEMPLATE,
        market_mood=analytics.get_market_mood(),
        market_indicators=analytics.market_indicators,
        live_signals=analytics.get_live_signals(),
        elite_traders={'CRYPTO_KING': {'name': 'CryptoKing Elite', 'specialty': 'AI Tokens & DeFi', 'success_rate': 89.5, 'monthly_return': 28.7, 'followers': 1247, 'description': 'Especialista en tokens de IA con enfoque en análisis on-chain'}},
        badges=gamification.badges,
        leaderboard=gamification.get_leaderboard()
    )

# API ENDPOINTS
@app.route('/api/status')
def api_status():
    return jsonify({
        'status': 'online',
        'version': '1.0-github',
        'timestamp': datetime.now().isoformat(),
        'github': True,
        'railway': True,
        'services': {
            'analytics': True,
            'gamification': True,
            'education': True,
            'referrals': True
        }
    })

@app.route('/api/market_mood')
def api_market_mood():
    return jsonify(analytics.get_market_mood())

@app.route('/api/signals')
def api_signals():
    return jsonify(analytics.get_live_signals())

@app.route('/api/leaderboard')
def api_leaderboard():
    return jsonify(gamification.get_leaderboard())

@app.route('/manifest.json')
def manifest():
    return jsonify({
        "name": "SAVAGE TRADER PRO",
        "short_name": "SavageTrader",
        "description": "Bot de Trading con IA, Copy-Trading Elite y Market Mood Indicator",
        "start_url": "/",
        "display": "standalone",
        "theme_color": "#ffd700",
        "background_color": "#000000",
        "icons": [
            {
                "src": "data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTkyIiBoZWlnaHQ9IjE5MiIgdmlld0JveD0iMCAwIDE5MiAxOTIiIGZpbGw9Im5vbmUiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CjxyZWN0IHdpZHRoPSIxOTIiIGhlaWdodD0iMTkyIiByeD0iOTYiIGZpbGw9InVybCgjZ3JhZGllbnQwX2xpbmVhcikiLz4KPHRleHQgeD0iOTYiIHk9IjEyMCIgZm9udC1mYW1pbHk9IkFyaWFsLCBzYW5zLXNlcmlmIiBmb250LXNpemU9IjgwIiBmaWxsPSIjMDAwIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIj7wn5C6PC90ZXh0Pgo8ZGVmcz4KPGxpbmVhckdyYWRpZW50IGlkPSJncmFkaWVudDBfbGluZWFyIiB4MT0iMCIgeTE9IjAiIHgyPSIxOTIiIHkyPSIxOTIiIGdyYWRpZW50VW5pdHM9InVzZXJTcGFjZU9uVXNlIj4KPHN0b3Agb2Zmc2V0PSIwJSIgc3RvcC1jb2xvcj0iI0ZGRDcwMCIvPgo8c3RvcCBvZmZzZXQ9IjUwJSIgc3RvcC1jb2xvcj0iI0ZGOENGRCIKAPXRVCB9ZmZzZXQ9IjEwMCUiIHN0b3AtY29sb3I9IiNEQzE0M0MiLz4KPC9saW5lYXJHcmFkaWVudD4KPC9kZWZzPgo8L3N2Zz4K",
                "sizes": "192x192",
                "type": "image/svg+xml"
            }
        ]
    })

@app.route('/health')
def health():
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat()
    })

# MANEJO DE ERRORES
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Endpoint not found'}), 404

@app.errorhandler(500)
def server_error(error):
    return jsonify({'error': 'Internal server error'}), 500

# EJECUTAR APLICACIÓN
if __name__ == '__main__':
    logger.info(f"🚀 SAVAGE TRADER PRO starting on port {PORT}")
    logger.info("✅ GitHub/Railway Production Ready")
    logger.info("🌟 All systems ready")
    
    app.run(host='0.0.0.0', port=PORT, debug=False)
from flask import Flask, render_template_string, jsonify, request, redirect, url_for, session
import os
from datetime import datetime, timedelta
import logging
import json
import random

# Configurar logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET", "savage_trader_secret")

# Puerto para Railway (CRÍTICO)
PORT = int(os.environ.get("PORT", 5000))

logger.info(f"🚀 SAVAGE TRADER PRO iniciando en puerto {PORT}")

# SISTEMA DE GAMIFICACIÓN Y RETENCIÓN AVANZADO
class GamificationSystem:
    def __init__(self):
        self.badges = {
            'first_win': {'name': '🎯 Primera Victoria', 'description': 'Tu primera operación exitosa', 'rarity': 'común'},
            'streak_master': {'name': '🔥 Racha Master', 'description': '5 operaciones consecutivas exitosas', 'rarity': 'raro'},
            'risk_manager': {'name': '🛡️ Gestor de Riesgo', 'description': 'Nunca perdiste más del 2%', 'rarity': 'épico'},
            'diamond_hands': {'name': '💎 Manos de Diamante', 'description': '1 mes sin cerrar posiciones por pánico', 'rarity': 'legendario'},
            'ai_expert': {'name': '🤖 Experto IA', 'description': 'Siguió 50+ señales de IA', 'rarity': 'raro'},
            'copy_master': {'name': '🔄 Master Copy-Trading', 'description': 'Siguió a 3+ traders durante 1 mes', 'rarity': 'épico'},
            'profit_king': {'name': '👑 Rey de Ganancias', 'description': '+50% profit en un mes', 'rarity': 'mítico'},
            'early_adopter': {'name': '🌟 Early Adopter', 'description': 'Usuario desde el plan Starter', 'rarity': 'especial'}
        }
        
    def get_user_badges(self, user_id):
        return ['first_win', 'ai_expert', 'early_adopter']
        
    def get_leaderboard(self):
        return [
            {'username': 'TradingKing', 'profit': 28.7, 'badges': 6, 'streak': 15, 'plan': 'Elite'},
            {'username': 'AITrader', 'profit': 25.3, 'badges': 5, 'streak': 12, 'plan': 'Premium'},
            {'username': 'CryptoWolf', 'profit': 22.8, 'badges': 7, 'streak': 18, 'plan': 'Elite'},
            {'username': 'DiamondHands', 'profit': 19.4, 'badges': 4, 'streak': 9, 'plan': 'Premium'},
            {'username': 'MarketMaster', 'profit': 17.2, 'badges': 5, 'streak': 11, 'plan': 'Basic'}
        ]

# SISTEMA DE ANÁLISIS AVANZADO CON IA
class AdvancedAnalytics:
    def __init__(self):
        self.market_indicators = {
            'fear_greed_index': random.randint(65, 85),
            'volatility_index': random.randint(20, 35),
            'trend_strength': random.randint(75, 95),
            'social_sentiment': 'Bullish',
            'institutional_flow': 'Buying',
            'ai_confidence': random.randint(85, 95)
        }
    
    def get_market_mood(self):
        mood_score = (self.market_indicators['fear_greed_index'] + 
                     (100 - self.market_indicators['volatility_index']) + 
                     self.market_indicators['trend_strength']) / 3
        
        if mood_score >= 80:
            return {'mood': '🚀 Extremadamente Optimista', 'color': '#10b981', 'score': int(mood_score)}
        elif mood_score >= 70:
            return {'mood': '📈 Muy Optimista', 'color': '#059669', 'score': int(mood_score)}
        elif mood_score >= 50:
            return {'mood': '⚡ Optimista', 'color': '#3b82f6', 'score': int(mood_score)}
        elif mood_score >= 30:
            return {'mood': '⚖️ Neutral', 'color': '#f59e0b', 'score': int(mood_score)}
        else:
            return {'mood': '📉 Pesimista', 'color': '#ef4444', 'score': int(mood_score)}
    
    def get_live_signals(self):
        signals = [
            {
                'symbol': 'NVDA',
                'action': 'BUY FUERTE',
                'price': 892.50,
                'change': '+2.3%',
                'target1': 920.00,
                'target2': 945.00,
                'stop_loss': 875.00,
                'confidence': 94,
                'ai_reasoning': 'Momentum alcista + flujo institucional + sentiment positivo'
            },
            {
                'symbol': 'TAO/USDT',
                'action': 'LONG AGRESIVO',
                'price': 342.50,
                'change': '+4.7%',
                'target1': 378.00,
                'target2': 410.00,
                'stop_loss': 325.00,
                'confidence': 89,
                'ai_reasoning': 'AI Catalyst: Partnership + volumen institucional x3'
            }
        ]
        return signals

# SISTEMA DE EDUCACIÓN PREMIUM
class EducationSystem:
    def __init__(self):
        self.micro_courses = [
            {
                'id': 1,
                'title': 'Fundamentos del Trading con IA',
                'duration': '5 min',
                'level': 'Principiante',
                'completion_rate': '92%',
                'lessons': ['¿Qué es el trading algorítmico?', 'Cómo funciona la IA en trading', 'Primeros pasos']
            },
            {
                'id': 2,
                'title': 'Gestión de Riesgo Avanzada',
                'duration': '8 min',
                'level': 'Intermedio',
                'completion_rate': '87%',
                'lessons': ['Stop-loss inteligente', 'Diversificación de portfolio', 'Ratio Riesgo/Beneficio']
            },
            {
                'id': 3,
                'title': 'Psicología del Trading',
                'duration': '6 min',
                'level': 'Avanzado',
                'completion_rate': '79%',
                'lessons': ['Control emocional', 'FOMO y FUD', 'Disciplina en trading']
            },
            {
                'id': 4,
                'title': 'Copy-Trading Profesional',
                'duration': '10 min',
                'level': 'Premium',
                'completion_rate': '95%',
                'lessons': ['Selección de traders', 'Gestión de capital', 'Diversificación automática']
            }
        ]
        
        self.master_class = {
            'title': 'Master Class Trading con IA',
            'price': 299,
            'duration': '20 horas',
            'modules': 12,
            'certification': True,
            'lifetime_access': True,
            'students': 1247
        }

# SISTEMA DE REFERIDOS Y MONETIZACIÓN
class ReferralSystem:
    def __init__(self):
        self.commission_rate = 0.30  # 30%
        self.referral_bonuses = {
            'starter_to_basic': {'discount': 0.50, 'duration': '1 month'},
            'basic_to_premium': {'free_weeks': 2, 'discount': 0.00},
            'premium_to_elite': {'free_month': 1, 'alpha_access': True}
        }
    
    def calculate_earnings(self, referrals, plan_prices):
        total = 0
        for plan, count in referrals.items():
            total += plan_prices.get(plan, 0) * count * self.commission_rate
        return total

# Inicializar sistemas avanzados
gamification = GamificationSystem()
analytics = AdvancedAnalytics()
education = EducationSystem()
referrals = ReferralSystem()

# TEMPLATE HTML COMPLETO Y MEJORADO
COMPLETE_ENHANCED_TEMPLATE = """<!DOCTYPE html>
<html lang="es" data-bs-theme="dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no">
    <title>SAVAGE TRADER PRO - Bot de Trading con IA</title>
    
    <!-- PWA Configuration -->
    <link rel="manifest" href="/manifest.json">
    <meta name="theme-color" content="#ffd700">
    <meta name="apple-mobile-web-app-capable" content="yes">
    <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
    <meta name="apple-mobile-web-app-title" content="SAVAGE TRADER PRO">
    
    <link href="https://cdn.replit.com/agent/bootstrap-agent-dark-theme.min.css" rel="stylesheet">
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
    <style>
        :root {
            --primary-gold: #ffd700;
            --aggressive-red: #ff0040;
            --blood-red: #8b0000;
            --elite-black: #000000;
            --steel-gray: #2a2a2a;
            --neon-blue: #00d4ff;
            --neon-purple: #b847ff;
            --neon-green: #00ff88;
            --neon-pink: #ff0080;
            --gradient-primary: linear-gradient(135deg, #ffd700 0%, #ff8c00 30%, #dc143c 70%, #8b0000 100%);
            --gradient-aggressive: linear-gradient(135deg, #ff0040 0%, #8b0000 50%, #000000 100%);
            --gradient-bg: linear-gradient(135deg, #000000 0%, #1a0000 25%, #000a1a 50%, #1a0010 75%, #0a0a0a 100%);
            --gradient-neon: linear-gradient(45deg, #ff0040, #ffd700, #00d4ff, #b847ff);
            --gradient-professional: linear-gradient(135deg, #2a2a2a 0%, #1a1a1a 50%, #0a0a0a 100%);
            --shadow-gold: 0 0 50px rgba(255, 215, 0, 0.8), 0 0 100px rgba(255, 215, 0, 0.4);
            --shadow-aggressive: 0 0 40px rgba(255, 0, 64, 0.9), 0 0 80px rgba(139, 0, 0, 0.6);
            --shadow-neon-blue: 0 0 30px rgba(0, 212, 255, 0.8), 0 0 60px rgba(0, 212, 255, 0.4);
            --shadow-neon-purple: 0 0 30px rgba(184, 71, 255, 0.8), 0 0 60px rgba(184, 71, 255, 0.4);
            --shadow-neon-green: 0 0 30px rgba(0, 255, 136, 0.8), 0 0 60px rgba(0, 255, 136, 0.4);
            --gradient-glass: linear-gradient(135deg, rgba(255,255,255,0.12) 0%, rgba(255,255,255,0.06) 100%);
            --gradient-hologram: linear-gradient(45deg, 
                transparent 0%, 
                rgba(255,0,64,0.15) 25%, 
                rgba(255,215,0,0.15) 50%, 
                rgba(0,212,255,0.15) 75%, 
                transparent 100%);
        }
        
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Exo+2:wght@300;400;600;700;800;900&display=swap');
        
        body {
            background: var(--gradient-bg);
            color: white;
            font-family: 'Exo 2', sans-serif;
            overflow-x: hidden;
            line-height: 1.6;
            position: relative;
        }
        
        body::before {
            content: '';
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: 
                radial-gradient(circle at 20% 80%, rgba(255,0,64,0.15) 0%, transparent 50%),
                radial-gradient(circle at 80% 20%, rgba(255,215,0,0.12) 0%, transparent 50%),
                radial-gradient(circle at 40% 40%, rgba(139,0,0,0.1) 0%, transparent 50%),
                linear-gradient(180deg, transparent 0%, rgba(0,0,0,0.4) 100%);
            pointer-events: none;
            z-index: -2;
            animation: backgroundShift 25s ease-in-out infinite;
        }
        
        @keyframes backgroundShift {
            0%, 100% { 
                background: 
                    radial-gradient(circle at 20% 80%, rgba(255,0,64,0.15) 0%, transparent 50%),
                    radial-gradient(circle at 80% 20%, rgba(255,215,0,0.12) 0%, transparent 50%),
                    linear-gradient(180deg, transparent 0%, rgba(0,0,0,0.4) 100%);
            }
            33% { 
                background: 
                    radial-gradient(circle at 80% 80%, rgba(139,0,0,0.15) 0%, transparent 50%),
                    radial-gradient(circle at 20% 20%, rgba(255,215,0,0.12) 0%, transparent 50%),
                    linear-gradient(180deg, transparent 0%, rgba(20,0,0,0.4) 100%);
            }
            66% { 
                background: 
                    radial-gradient(circle at 50% 50%, rgba(255,215,0,0.15) 0%, transparent 50%),
                    radial-gradient(circle at 10% 90%, rgba(139,0,0,0.12) 0%, transparent 50%),
                    linear-gradient(180deg, transparent 0%, rgba(10,5,0,0.4) 100%);
            }
        }
        
        /* Cielo estrellado animado */
        body::after {
            content: '';
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-image: 
                radial-gradient(2px 2px at 20px 30px, #fff, transparent),
                radial-gradient(1px 1px at 40px 70px, rgba(255,255,255,0.8), transparent),
                radial-gradient(1px 1px at 90px 40px, #fff, transparent),
                radial-gradient(1px 1px at 130px 80px, rgba(255,255,255,0.6), transparent),
                radial-gradient(2px 2px at 160px 30px, #fff, transparent),
                radial-gradient(1px 1px at 200px 90px, rgba(255,255,255,0.7), transparent),
                radial-gradient(2px 2px at 240px 20px, rgba(255,255,255,0.9), transparent),
                radial-gradient(1px 1px at 280px 60px, #fff, transparent),
                radial-gradient(1px 1px at 320px 100px, rgba(255,255,255,0.8), transparent),
                radial-gradient(2px 2px at 360px 50px, #fff, transparent),
                radial-gradient(3px 3px at 80px 120px, #ffd700, transparent),
                radial-gradient(4px 4px at 220px 160px, rgba(255,215,0,0.8), transparent),
                radial-gradient(3px 3px at 350px 80px, #fff, transparent),
                radial-gradient(2px 2px at 150px 200px, rgba(255,255,255,0.9), transparent),
                radial-gradient(4px 4px at 300px 140px, rgba(255,215,0,0.7), transparent),
                radial-gradient(3px 3px at 50px 180px, #fff, transparent);
            background-repeat: repeat;
            background-size: 400px 250px;
            animation: starryNight 30s linear infinite;
            pointer-events: none;
            z-index: -1;
            opacity: 0.7;
        }
        
        @keyframes starryNight {
            0% { 
                transform: translateX(0px) translateY(0px);
                opacity: 0.7;
            }
            25% { 
                opacity: 0.9;
            }
            50% { 
                transform: translateX(-100px) translateY(-50px);
                opacity: 0.6;
            }
            75% { 
                opacity: 0.8;
            }
            100% { 
                transform: translateX(-200px) translateY(-100px);
                opacity: 0.7;
            }
        }
        
        /* Estrellas parpadeantes adicionales */
        .starry-overlay {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: 
                radial-gradient(1px 1px at 15% 25%, #fff, transparent),
                radial-gradient(2px 2px at 75% 15%, rgba(255,215,0,0.9), transparent),
                radial-gradient(1px 1px at 35% 75%, #fff, transparent),
                radial-gradient(3px 3px at 85% 85%, rgba(255,255,255,0.8), transparent),
                radial-gradient(2px 2px at 25% 45%, rgba(255,215,0,0.7), transparent),
                radial-gradient(1px 1px at 65% 35%, #fff, transparent),
                radial-gradient(2px 2px at 95% 55%, rgba(255,255,255,0.9), transparent);
            animation: twinkle 8s ease-in-out infinite;
            pointer-events: none;
            z-index: -1;
            opacity: 0.5;
        }
        
        @keyframes twinkle {
            0%, 100% { opacity: 0.5; }
            25% { opacity: 0.8; }
            50% { opacity: 0.3; }
            75% { opacity: 0.9; }
        }
        
        .container-fluid {
            padding: 0;
        }
        
        .logo-container {
            text-align: center;
            margin: 30px 0;
            position: relative;
        }
        
        .logo-svg {
            width: 300px;
            height: 300px;
            max-width: 90vw;
            margin: 0 auto;
            animation: logoFloat 6s ease-in-out infinite, logoGlow 4s ease-in-out infinite alternate;
            filter: drop-shadow(0 0 30px rgba(255,215,0,0.8)) 
                    drop-shadow(0 0 60px rgba(255,0,64,0.6)) 
                    drop-shadow(0 0 90px rgba(139,0,0,0.4));
        }
        
        @keyframes logoFloat {
            0%, 100% { transform: translateY(0px) scale(1); }
            50% { transform: translateY(-20px) scale(1.05); }
        }
        
        @keyframes logoGlow {
            0% { filter: drop-shadow(0 0 30px rgba(255,215,0,0.8)) drop-shadow(0 0 60px rgba(255,0,64,0.6)); }
            100% { filter: drop-shadow(0 0 50px rgba(255,215,0,1)) drop-shadow(0 0 100px rgba(255,0,64,0.8)); }
        }
        
        .hero-title {
            font-family: 'Orbitron', monospace;
            font-size: clamp(2.5rem, 8vw, 5rem);
            font-weight: 900;
            background: var(--gradient-primary);
            -webkit-background-clip: text;
            background-clip: text;
            -webkit-text-fill-color: transparent;
            text-align: center;
            margin: 30px 0;
            text-shadow: 0 0 50px rgba(255, 215, 0, 0.8);
            animation: titlePulse 3s ease-in-out infinite alternate;
            letter-spacing: 2px;
        }
        
        @keyframes titlePulse {
            0% { 
                transform: scale(1);
                text-shadow: 0 0 50px rgba(255, 215, 0, 0.8), 0 0 100px rgba(255, 0, 64, 0.4);
            }
            100% { 
                transform: scale(1.02);
                text-shadow: 0 0 70px rgba(255, 215, 0, 1), 0 0 140px rgba(255, 0, 64, 0.6);
            }
        }
        
        .hero-subtitle {
            font-family: 'Exo 2', sans-serif;
            font-size: clamp(1.2rem, 4vw, 2rem);
            font-weight: 700;
            color: #ffffff;
            text-align: center;
            margin-bottom: 40px;
            text-shadow: 0 0 20px rgba(255, 255, 255, 0.8);
            opacity: 0.95;
        }
        
        .status-online {
            color: var(--neon-green);
            font-weight: 700;
            text-align: center;
            margin: 20px 0;
            animation: statusPulse 2s ease-in-out infinite;
            text-shadow: 0 0 20px rgba(0, 255, 136, 0.8);
        }
        
        @keyframes statusPulse {
            0%, 100% { opacity: 0.8; }
            50% { opacity: 1; }
        }
        
        .market-mood-card {
            background: var(--gradient-glass);
            border: 2px solid rgba(255, 215, 0, 0.3);
            border-radius: 20px;
            padding: 25px;
            margin: 20px 0;
            backdrop-filter: blur(20px);
            box-shadow: var(--shadow-gold);
            position: relative;
            overflow: hidden;
            transition: all 0.3s ease;
        }
        
        .market-mood-card:hover {
            transform: translateY(-5px);
            border-color: rgba(255, 215, 0, 0.6);
            box-shadow: 
                0 0 60px rgba(255, 215, 0, 0.9), 
                0 0 120px rgba(255, 215, 0, 0.5),
                0 20px 40px rgba(0, 0, 0, 0.3);
        }
        
        .market-mood-card::before {
            content: '';
            position: absolute;
            top: -50%;
            left: -50%;
            width: 200%;
            height: 200%;
            background: var(--gradient-hologram);
            animation: hologramSweep 8s linear infinite;
            opacity: 0.1;
            pointer-events: none;
        }
        
        @keyframes hologramSweep {
            0% { transform: translateX(-100%) translateY(-100%) rotate(45deg); }
            100% { transform: translateX(100%) translateY(100%) rotate(45deg); }
        }
        
        .mood-score {
            font-size: 3rem;
            font-weight: 900;
            font-family: 'Orbitron', monospace;
            margin: 10px 0;
        }
        
        .mood-indicator {
            font-size: 1.5rem;
            font-weight: 700;
            margin: 15px 0;
            padding: 15px;
            border-radius: 15px;
            background: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.2);
            text-align: center;
        }
        
        .signal-item {
            background: var(--gradient-professional);
            border: 1px solid rgba(255, 215, 0, 0.3);
            border-radius: 15px;
            padding: 20px;
            margin: 15px 0;
            transition: all 0.3s ease;
            position: relative;
            overflow: hidden;
        }
        
        .signal-item:hover {
            transform: translateY(-3px);
            border-color: rgba(255, 215, 0, 0.6);
            box-shadow: 0 10px 30px rgba(255, 215, 0, 0.3);
        }
        
        .signal-item::before {
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 2px;
            background: var(--gradient-primary);
            animation: signalSweep 3s ease-in-out infinite;
        }
        
        @keyframes signalSweep {
            0% { left: -100%; }
            50% { left: 100%; }
            100% { left: -100%; }
        }
        
        .signal-symbol {
            font-size: 1.8rem;
            font-weight: 900;
            color: var(--primary-gold);
            margin-bottom: 10px;
        }
        
        .signal-action {
            font-size: 1.3rem;
            font-weight: 800;
            padding: 8px 15px;
            border-radius: 20px;
            display: inline-block;
            margin: 10px 0;
        }
        
        .action-buy {
            background: linear-gradient(135deg, #10b981 0%, #059669 100%);
            box-shadow: var(--shadow-neon-green);
        }
        
        .action-sell {
            background: linear-gradient(135deg, #ef4444 0%, #dc2626 100%);
            box-shadow: var(--shadow-aggressive);
        }
        
        .action-long {
            background: linear-gradient(135deg, #3b82f6 0%, #1d4ed8 100%);
            box-shadow: var(--shadow-neon-blue);
        }
        
        .confidence-bar {
            width: 100%;
            height: 8px;
            background: rgba(255, 255, 255, 0.1);
            border-radius: 10px;
            overflow: hidden;
            margin: 15px 0;
            position: relative;
        }
        
        .confidence-fill {
            height: 100%;
            border-radius: 10px;
            background: var(--gradient-primary);
            transition: width 2s ease-in-out;
            animation: confidencePulse 2s ease-in-out infinite alternate;
        }
        
        @keyframes confidencePulse {
            0% { box-shadow: 0 0 10px rgba(255, 215, 0, 0.5); }
            100% { box-shadow: 0 0 20px rgba(255, 215, 0, 0.8); }
        }
        
        .price-card {
            background: var(--gradient-glass);
            border: 2px solid rgba(255, 0, 64, 0.3);
            border-radius: 20px;
            padding: 25px;
            margin: 20px 0;
            backdrop-filter: blur(20px);
            box-shadow: var(--shadow-aggressive);
            transition: all 0.3s ease;
            position: relative;
            overflow: hidden;
        }
        
        .price-card:hover {
            transform: translateY(-5px) scale(1.02);
            border-color: rgba(255, 0, 64, 0.8);
            box-shadow: 
                0 0 60px rgba(255, 0, 64, 0.9),
                0 0 120px rgba(255, 0, 64, 0.5),
                0 20px 40px rgba(0, 0, 0, 0.3);
        }
        
        .price-card::before {
            content: '';
            position: absolute;
            top: -2px;
            left: -2px;
            right: -2px;
            bottom: -2px;
            background: var(--gradient-primary);
            border-radius: 22px;
            z-index: -1;
            opacity: 0;
            transition: opacity 0.3s ease;
        }
        
        .price-card:hover::before {
            opacity: 1;
        }
        
        .plan-title {
            font-family: 'Orbitron', monospace;
            font-size: 2rem;
            font-weight: 900;
            margin-bottom: 20px;
            text-align: center;
        }
        
        .plan-price {
            font-size: 3.5rem;
            font-weight: 900;
            text-align: center;
            margin: 20px 0;
            font-family: 'Orbitron', monospace;
        }
        
        .plan-features {
            list-style: none;
            padding: 0;
        }
        
        .plan-features li {
            padding: 10px 0;
            border-bottom: 1px solid rgba(255, 255, 255, 0.1);
            font-weight: 600;
        }
        
        .plan-features li:before {
            content: '✓ ';
            color: var(--neon-green);
            font-weight: 900;
            margin-right: 10px;
        }
        
        .btn-savage {
            background: var(--gradient-primary);
            border: none;
            padding: 18px 40px;
            border-radius: 50px;
            font-weight: 900;
            font-size: 1.2rem;
            color: #000000;
            text-transform: uppercase;
            letter-spacing: 2px;
            transition: all 0.3s ease;
            box-shadow: var(--shadow-gold);
            position: relative;
            overflow: hidden;
        }
        
        .btn-savage::before {
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, transparent, rgba(255,255,255,0.4), transparent);
            transition: left 0.6s;
        }
        
        .btn-savage:hover::before {
            left: 100%;
        }
        
        .btn-savage:hover {
            transform: translateY(-3px) scale(1.05);
            box-shadow: 
                0 0 60px rgba(255, 215, 0, 1),
                0 0 120px rgba(255, 215, 0, 0.6),
                0 15px 35px rgba(0, 0, 0, 0.3);
        }
        
        .trader-card {
            background: var(--gradient-professional);
            border: 2px solid rgba(0, 212, 255, 0.3);
            border-radius: 20px;
            padding: 25px;
            margin: 20px 0;
            backdrop-filter: blur(20px);
            box-shadow: var(--shadow-neon-blue);
            transition: all 0.3s ease;
            position: relative;
        }
        
        .trader-card:hover {
            transform: translateY(-5px);
            border-color: rgba(0, 212, 255, 0.8);
            box-shadow: 
                0 0 60px rgba(0, 212, 255, 0.9),
                0 0 120px rgba(0, 212, 255, 0.5);
        }
        
        .trader-name {
            font-size: 1.5rem;
            font-weight: 900;
            color: var(--neon-blue);
            margin-bottom: 10px;
            font-family: 'Orbitron', monospace;
        }
        
        .trader-stats {
            display: flex;
            justify-content: space-between;
            flex-wrap: wrap;
            gap: 15px;
            margin: 20px 0;
        }
        
        .stat-item {
            text-align: center;
            padding: 15px;
            background: rgba(255, 255, 255, 0.05);
            border-radius: 10px;
            border: 1px solid rgba(255, 255, 255, 0.1);
            flex: 1;
            min-width: 120px;
        }
        
        .stat-value {
            font-size: 1.8rem;
            font-weight: 900;
            color: var(--neon-green);
            display: block;
            margin-bottom: 5px;
            font-family: 'Orbitron', monospace;
        }
        
        .stat-label {
            font-size: 0.9rem;
            color: rgba(255, 255, 255, 0.8);
            font-weight: 600;
        }
        
        .badge-container {
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
            margin: 20px 0;
            justify-content: center;
        }
        
        .badge-item {
            background: var(--gradient-glass);
            border: 1px solid rgba(255, 215, 0, 0.3);
            padding: 8px 16px;
            border-radius: 25px;
            font-size: 0.9rem;
            font-weight: 700;
            backdrop-filter: blur(10px);
            transition: all 0.3s ease;
        }
        
        .badge-item:hover {
            border-color: rgba(255, 215, 0, 0.8);
            transform: scale(1.05);
            box-shadow: 0 0 20px rgba(255, 215, 0, 0.5);
        }
        
        .badge-rarity-común {
            border-color: rgba(128, 128, 128, 0.5);
            color: #a0a0a0;
        }
        
        .badge-rarity-raro {
            border-color: rgba(0, 212, 255, 0.5);
            color: var(--neon-blue);
            box-shadow: 0 0 15px rgba(0, 212, 255, 0.3);
        }
        
        .badge-rarity-épico {
            border-color: rgba(184, 71, 255, 0.5);
            color: var(--neon-purple);
            box-shadow: 0 0 15px rgba(184, 71, 255, 0.3);
        }
        
        .badge-rarity-legendario {
            border-color: rgba(255, 215, 0, 0.8);
            color: var(--primary-gold);
            box-shadow: 0 0 20px rgba(255, 215, 0, 0.5);
            animation: legendaryGlow 2s ease-in-out infinite alternate;
        }
        
        .badge-rarity-mítico {
            border-color: rgba(255, 0, 128, 0.8);
            color: var(--neon-pink);
            box-shadow: 0 0 25px rgba(255, 0, 128, 0.6);
            animation: mythicPulse 1.5s ease-in-out infinite;
        }
        
        @keyframes legendaryGlow {
            0% { box-shadow: 0 0 20px rgba(255, 215, 0, 0.5); }
            100% { box-shadow: 0 0 40px rgba(255, 215, 0, 0.8), 0 0 60px rgba(255, 215, 0, 0.4); }
        }
        
        @keyframes mythicPulse {
            0%, 100% { 
                transform: scale(1);
                box-shadow: 0 0 25px rgba(255, 0, 128, 0.6);
            }
            50% { 
                transform: scale(1.05);
                box-shadow: 0 0 35px rgba(255, 0, 128, 0.9), 0 0 50px rgba(255, 0, 128, 0.5);
            }
        }
        
        .leaderboard-item {
            background: var(--gradient-professional);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 15px;
            padding: 20px;
            margin: 15px 0;
            display: flex;
            align-items: center;
            gap: 20px;
            transition: all 0.3s ease;
        }
        
        .leaderboard-item:hover {
            border-color: rgba(255, 215, 0, 0.5);
            transform: translateX(10px);
            background: rgba(255, 215, 0, 0.05);
        }
        
        .leaderboard-rank {
            font-size: 2rem;
            font-weight: 900;
            color: var(--primary-gold);
            min-width: 60px;
            text-align: center;
            font-family: 'Orbitron', monospace;
        }
        
        .leaderboard-info {
            flex: 1;
        }
        
        .leaderboard-username {
            font-size: 1.3rem;
            font-weight: 900;
            margin-bottom: 5px;
            color: var(--neon-blue);
        }
        
        .leaderboard-stats {
            font-size: 0.9rem;
            color: rgba(255, 255, 255, 0.8);
            display: flex;
            gap: 15px;
            flex-wrap: wrap;
        }
        
        .responsive-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 20px;
            margin: 30px 0;
        }
        
        /* Responsive Design */
        @media (max-width: 768px) {
            .hero-title {
                font-size: 3rem;
                margin: 20px 0;
            }
            
            .hero-subtitle {
                font-size: 1.5rem;
                margin-bottom: 30px;
            }
            
            .logo-svg {
                width: 250px;
                height: 250px;
            }
            
            .plan-price {
                font-size: 2.5rem;
            }
            
            .trader-stats {
                flex-direction: column;
            }
            
            .stat-item {
                min-width: auto;
            }
            
            .leaderboard-item {
                flex-direction: column;
                text-align: center;
                gap: 10px;
            }
            
            .leaderboard-stats {
                justify-content: center;
            }
            
            .responsive-grid {
                grid-template-columns: 1fr;
                gap: 15px;
            }
        }
        
        @media (max-width: 480px) {
            .hero-title {
                font-size: 2.2rem;
            }
            
            .hero-subtitle {
                font-size: 1.2rem;
            }
            
            .logo-svg {
                width: 200px;
                height: 200px;
            }
            
            .market-mood-card,
            .price-card,
            .trader-card {
                padding: 20px;
                margin: 15px 0;
            }
            
            .btn-savage {
                padding: 15px 30px;
                font-size: 1rem;
            }
        }
        
        /* Animaciones adicionales para elementos interactivos */
        .interactive-element {
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        }
        
        .interactive-element:hover {
            transform: translateY(-2px);
        }
        
        .interactive-element:active {
            transform: translateY(0);
        }
        
        /* Efectos de carga */
        .loading-shimmer {
            background: linear-gradient(90deg, 
                rgba(255,255,255,0.1) 0%, 
                rgba(255,255,255,0.3) 50%, 
                rgba(255,255,255,0.1) 100%);
            background-size: 200% 100%;
            animation: shimmer 1.5s infinite;
        }
        
        @keyframes shimmer {
            0% { background-position: -200% 0; }
            100% { background-position: 200% 0; }
        }
        
        /* Scroll suave */
        html {
            scroll-behavior: smooth;
        }
        
        /* Mejoras de accesibilidad */
        .sr-only {
            position: absolute;
            width: 1px;
            height: 1px;
            padding: 0;
            margin: -1px;
            overflow: hidden;
            clip: rect(0, 0, 0, 0);
            white-space: nowrap;
            border: 0;
        }
        
        /* Focus states para accesibilidad */
        .btn-savage:focus,
        .interactive-element:focus {
            outline: 2px solid var(--primary-gold);
            outline-offset: 2px;
        }
    </style>
</head>
<body>
    <div class="starry-overlay"></div>
    
    <div class="container-fluid">
        <!-- Logo y Título Principal -->
        <div class="logo-container">
            <svg class="logo-svg" viewBox="0 0 300 300" xmlns="http://www.w3.org/2000/svg">
                <!-- Fondo circular con gradiente -->
                <defs>
                    <radialGradient id="bgGradient" cx="50%" cy="50%" r="50%">
                        <stop offset="0%" style="stop-color:#ffd700;stop-opacity:0.3" />
                        <stop offset="50%" style="stop-color:#ff0040;stop-opacity:0.2" />
                        <stop offset="100%" style="stop-color:#8b0000;stop-opacity:0.1" />
                    </radialGradient>
                    <linearGradient id="wolfGradient" x1="0%" y1="0%" x2="100%" y2="100%">
                        <stop offset="0%" style="stop-color:#ffd700" />
                        <stop offset="30%" style="stop-color:#ff8c00" />
                        <stop offset="70%" style="stop-color:#dc143c" />
                        <stop offset="100%" style="stop-color:#8b0000" />
                    </linearGradient>
                    <filter id="glow">
                        <feGaussianBlur stdDeviation="4" result="coloredBlur"/>
                        <feMerge> 
                            <feMergeNode in="coloredBlur"/>
                            <feMergeNode in="SourceGraphic"/>
                        </feMerge>
                    </filter>
                </defs>
                
                <!-- Círculo de fondo -->
                <circle cx="150" cy="150" r="145" fill="url(#bgGradient)" opacity="0.6"/>
                
                <!-- Círculo principal -->
                <circle cx="150" cy="150" r="140" fill="none" stroke="url(#wolfGradient)" stroke-width="6" opacity="0.8"/>
                
                <!-- Cara del lobo estilizada -->
                <g transform="translate(150,150)" filter="url(#glow)">
                    <!-- Orejas -->
                    <path d="M-40,-80 L-20,-100 L-15,-75 Z" fill="url(#wolfGradient)"/>
                    <path d="M40,-80 L20,-100 L15,-75 Z" fill="url(#wolfGradient)"/>
                    
                    <!-- Cabeza principal -->
                    <ellipse cx="0" cy="-20" rx="45" ry="55" fill="url(#wolfGradient)" opacity="0.9"/>
                    
                    <!-- Hocico -->
                    <ellipse cx="0" cy="10" rx="25" ry="35" fill="url(#wolfGradient)" opacity="0.8"/>
                    
                    <!-- Ojos -->
                    <circle cx="-18" cy="-35" r="8" fill="#ffd700"/>
                    <circle cx="18" cy="-35" r="8" fill="#ffd700"/>
                    <circle cx="-18" cy="-35" r="4" fill="#000"/>
                    <circle cx="18" cy="-35" r="4" fill="#000"/>
                    
                    <!-- Nariz -->
                    <ellipse cx="0" cy="-5" rx="4" ry="6" fill="#000"/>
                    
                    <!-- Boca -->
                    <path d="M0,5 Q-8,15 -15,10 Q-8,20 0,15 Q8,20 15,10 Q8,15 0,5" fill="#000" opacity="0.6"/>
                    
                    <!-- Colmillos -->
                    <path d="M-8,10 L-6,20 L-10,20 Z" fill="#fff"/>
                    <path d="M8,10 L6,20 L10,20 Z" fill="#fff"/>
                </g>
                
                <!-- Texto "SAVAGE" curvado -->
                <path id="topCurve" d="M 50,150 A 100,100 0 0,1 250,150" fill="none"/>
                <text font-family="Orbitron, monospace" font-size="24" font-weight="900" fill="url(#wolfGradient)">
                    <textPath href="#topCurve" startOffset="50%" text-anchor="middle">
                        SAVAGE TRADER
                    </textPath>
                </text>
                
                <!-- Texto "PRO" curvado -->
                <path id="bottomCurve" d="M 250,150 A 100,100 0 0,1 50,150" fill="none"/>
                <text font-family="Orbitron, monospace" font-size="20" font-weight="900" fill="url(#wolfGradient)">
                    <textPath href="#bottomCurve" startOffset="50%" text-anchor="middle">
                        • PRO •
                    </textPath>
                </text>
                
                <!-- Elementos decorativos -->
                <g opacity="0.6">
                    <circle cx="80" cy="80" r="3" fill="#ffd700"/>
                    <circle cx="220" cy="80" r="2" fill="#ff0040"/>
                    <circle cx="80" cy="220" r="2" fill="#8b0000"/>
                    <circle cx="220" cy="220" r="3" fill="#ffd700"/>
                </g>
            </svg>
        </div>
        
        <h1 class="hero-title">SAVAGE TRADER PRO</h1>
        <p class="hero-subtitle">💎 Bot de Trading con IA Avanzada 💎</p>
        
        <div class="status-online">
            <i class="fas fa-circle" style="color: #00ff88;"></i> 
            Sistema Online 24/7 • IA GPT-4 Activa • Copy-Trading Elite
        </div>
        
        <!-- Market Mood Indicator -->
        <div class="market-mood-card">
            <h3 style="text-align: center; margin-bottom: 25px; font-family: 'Orbitron', monospace;">
                🎯 Market Mood Indicator
            </h3>
            <div class="mood-score" style="color: {{ market_mood.color }}; text-align: center;">
                {{ market_mood.score }}%
            </div>
            <div class="mood-indicator" style="color: {{ market_mood.color }};">
                {{ market_mood.mood }}
            </div>
            <div class="row mt-4">
                <div class="col-6">
                    <div class="text-center">
                        <div style="font-size: 2rem; color: #ffd700;">{{ market_indicators.fear_greed_index }}</div>
                        <div style="font-size: 0.9rem; color: rgba(255,255,255,0.8);">Fear & Greed</div>
                    </div>
                </div>
                <div class="col-6">
                    <div class="text-center">
                        <div style="font-size: 2rem; color: #00d4ff;">{{ market_indicators.ai_confidence }}%</div>
                        <div style="font-size: 0.9rem; color: rgba(255,255,255,0.8);">IA Confidence</div>
                    </div>
                </div>
            </div>
        </div>
        
        <!-- Señales en Vivo -->
        <section class="my-5">
            <h3 style="text-align: center; margin-bottom: 30px; font-family: 'Orbitron', monospace; color: var(--primary-gold);">
                🚀 Señales Elite en Vivo
            </h3>
            {% for signal in live_signals %}
            <div class="signal-item">
                <div class="signal-symbol">{{ signal.symbol }}</div>
                <div class="signal-action {% if 'BUY' in signal.action %}action-buy{% elif 'LONG' in signal.action %}action-long{% else %}action-sell{% endif %}">
                    {{ signal.action }}
                </div>
                <div class="row mt-3">
                    <div class="col-md-6">
                        <div><strong>Precio:</strong> ${{ "%.2f"|format(signal.price) }}</div>
                        <div><strong>Cambio:</strong> <span style="color: #10b981;">{{ signal.change }}</span></div>
                        <div><strong>Target 1:</strong> ${{ "%.2f"|format(signal.target1) }}</div>
                        <div><strong>Target 2:</strong> ${{ "%.2f"|format(signal.target2) }}</div>
                        <div><strong>Stop Loss:</strong> ${{ "%.2f"|format(signal.stop_loss) }}</div>
                    </div>
                    <div class="col-md-6">
                        <div><strong>Confianza IA:</strong></div>
                        <div class="confidence-bar">
                            <div class="confidence-fill" style="width: {{ signal.confidence }}%;"></div>
                        </div>
                        <div style="text-align: center; font-weight: 700;">{{ signal.confidence }}%</div>
                        <div style="margin-top: 10px; font-size: 0.9rem; color: rgba(255,255,255,0.8);">
                            {{ signal.ai_reasoning }}
                        </div>
                    </div>
                </div>
            </div>
            {% endfor %}
        </section>
        
        <!-- Copy-Trading Elite -->
        <section class="my-5">
            <h3 style="text-align: center; margin-bottom: 30px; font-family: 'Orbitron', monospace; color: var(--neon-blue);">
                🔄 Copy-Trading Elite
            </h3>
            <div class="responsive-grid">
                {% for trader_id, trader in elite_traders.items() %}
                <div class="trader-card">
                    <div class="trader-name">{{ trader.name }}</div>
                    <div style="color: var(--neon-purple); font-weight: 700; margin-bottom: 15px;">
                        {{ trader.specialty }}
                    </div>
                    <div class="trader-stats">
                        <div class="stat-item">
                            <span class="stat-value">{{ trader.success_rate }}%</span>
                            <span class="stat-label">Éxito</span>
                        </div>
                        <div class="stat-item">
                            <span class="stat-value">{{ trader.monthly_return }}%</span>
                            <span class="stat-label">Retorno</span>
                        </div>
                        <div class="stat-item">
                            <span class="stat-value">{{ trader.followers }}</span>
                            <span class="stat-label">Seguidores</span>
                        </div>
                    </div>
                    <div style="text-align: center; margin: 15px 0; padding: 10px; background: rgba(0,255,136,0.1); border-radius: 10px;">
                        <strong>{{ trader.description }}</strong>
                    </div>
                    <button class="btn btn-savage w-100">Seguir Trader</button>
                </div>
                {% endfor %}
            </div>
        </section>
        
        <!-- Sistema de Gamificación -->
        <section class="my-5">
            <h3 style="text-align: center; margin-bottom: 30px; font-family: 'Orbitron', monospace; color: var(--neon-purple);">
                🏆 Sistema de Gamificación
            </h3>
            
            <!-- Badges -->
            <div style="text-align: center; margin-bottom: 30px;">
                <h4 style="color: var(--primary-gold); margin-bottom: 20px;">Tus Badges</h4>
                <div class="badge-container">
                    {% for badge_id in ['first_win', 'ai_expert', 'early_adopter'] %}
                        {% set badge = badges[badge_id] %}
                        <div class="badge-item badge-rarity-{{ badge.rarity }}">
                            {{ badge.name }}
                        </div>
                    {% endfor %}
                </div>
            </div>
            
            <!-- Leaderboard -->
            <div>
                <h4 style="color: var(--neon-blue); text-align: center; margin-bottom: 25px;">🥇 Leaderboard Elite</h4>
                {% for leader in leaderboard[:5] %}
                <div class="leaderboard-item">
                    <div class="leaderboard-rank">#{{ loop.index }}</div>
                    <div class="leaderboard-info">
                        <div class="leaderboard-username">{{ leader.username }}</div>
                        <div class="leaderboard-stats">
                            <span><strong>Profit:</strong> +{{ leader.profit }}%</span>
                            <span><strong>Badges:</strong> {{ leader.badges }}</span>
                            <span><strong>Racha:</strong> {{ leader.streak }}</span>
                            <span><strong>Plan:</strong> {{ leader.plan }}</span>
                        </div>
                    </div>
                </div>
                {% endfor %}
            </div>
        </section>
        
        <!-- Planes de Precio -->
        <section class="my-5">
            <h3 style="text-align: center; margin-bottom: 40px; font-family: 'Orbitron', monospace; color: var(--aggressive-red);">
                💰 Planes Elite SAVAGE TRADER
            </h3>
            <div class="responsive-grid">
                <!-- Plan Starter -->
                <div class="price-card" style="border-color: rgba(128, 128, 128, 0.5);">
                    <div class="plan-title" style="color: #a0a0a0;">🚀 STARTER</div>
                    <div class="plan-price" style="color: #a0a0a0;">€5.99<small>/semana</small></div>
                    <ul class="plan-features">
                        <li>5 señales IA diarias</li>
                        <li>Market Mood básico</li>
                        <li>1 trader copy-trading</li>
                        <li>Soporte por email</li>
                        <li>Análisis técnico básico</li>
                    </ul>
                    <button class="btn btn-savage w-100 mt-4">Empezar</button>
                </div>
                
                <!-- Plan Basic -->
                <div class="price-card" style="border-color: rgba(0, 212, 255, 0.5);">
                    <div class="plan-title" style="color: var(--neon-blue);">⚡ BASIC</div>
                    <div class="plan-price" style="color: var(--neon-blue);">€29<small>/mes</small></div>
                    <ul class="plan-features">
                        <li>Señales IA ilimitadas</li>
                        <li>Market Mood avanzado</li>
                        <li>3 traders copy-trading</li>
                        <li>Análisis de sentimiento</li>
                        <li>Alerts personalizadas</li>
                        <li>Soporte prioritario</li>
                    </ul>
                    <button class="btn btn-savage w-100 mt-4">Ser Basic</button>
                </div>
                
                <!-- Plan Premium -->
                <div class="price-card" style="border-color: rgba(255, 215, 0, 0.8); box-shadow: 0 0 60px rgba(255, 215, 0, 0.4);">
                    <div class="plan-title" style="color: var(--primary-gold);">👑 PREMIUM</div>
                    <div class="plan-price" style="color: var(--primary-gold);">€99<small>/mes</small></div>
                    <ul class="plan-features">
                        <li>Todo de Basic +</li>
                        <li>Todos los traders elite</li>
                        <li>IA GPT-4 avanzada</li>
                        <li>Análisis macro económico</li>
                        <li>Risk management IA</li>
                        <li>Señales pre-market</li>
                        <li>Webinars exclusivos</li>
                        <li>Telegram VIP</li>
                    </ul>
                    <button class="btn btn-savage w-100 mt-4">Ser Premium</button>
                </div>
                
                <!-- Plan Elite -->
                <div class="price-card" style="border-color: rgba(255, 0, 64, 0.8); box-shadow: 0 0 60px rgba(255, 0, 64, 0.6);">
                    <div class="plan-title" style="color: var(--aggressive-red);">🔥 ELITE</div>
                    <div class="plan-price" style="color: var(--aggressive-red);">€199<small>/mes</small></div>
                    <ul class="plan-features">
                        <li>Todo de Premium +</li>
                        <li>Acceso a Alpha Signals</li>
                        <li>1-on-1 con traders pro</li>
                        <li>API trading automation</li>
                        <li>Portfolio management IA</li>
                        <li>Backtesting avanzado</li>
                        <li>Academia SAVAGE completa</li>
                        <li>Master Class €299 GRATIS</li>
                        <li>WhatsApp directo</li>
                    </ul>
                    <button class="btn btn-savage w-100 mt-4">Ser Elite</button>
                </div>
            </div>
        </section>
        
        <!-- Footer Status -->
        <footer class="text-center py-4">
            <div class="status-online mb-3">
                <i class="fas fa-circle"></i> Sistema Online • 
                <i class="fas fa-robot"></i> IA GPT-4 Activa • 
                <i class="fas fa-chart-line"></i> 20 Mercados Monitoreados •
                <i class="fas fa-copy"></i> Copy-Trading Activo
            </div>
            <p>
                <strong>© 2024 SAVAGE TRADER PRO</strong><br>
                <small>Bot de Trading con IA • Wolf of Wall Street Design • Railway Production 24/7</small>
            </p>
        </footer>
    </div>
    
    <!-- Bootstrap JS -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
    
    <script>
        document.addEventListener('DOMContentLoaded', function() {
            console.log('🚀 SAVAGE TRADER PRO - GitHub/Railway Production v1.0');
            console.log('🐺 Wolf of Wall Street Design System');
            console.log('💎 Premium Trading Bot con IA Avanzada');
            console.log('📊 4 Planes: Starter €5.99/sem, Basic €29, Premium €99, Elite €199');
            console.log('🏆 Sistema de Gamificación Completo');
            console.log('📚 Academia de Trading con Master Class');
            console.log('🤝 Programa de Referidos 30%');
            console.log('🎯 Market Mood Indicator + Analytics');
            console.log('🤖 Demo con IA GPT-4 avanzada');
            console.log('✨ Todas las mejoras implementadas');
            
            // Auto-refresh de datos cada 30 segundos
            setInterval(() => {
                fetch('/api/market_mood')
                    .then(response => response.json())
                    .then(data => {
                        console.log('📊 Market mood updated:', data);
                    })
                    .catch(error => console.log('Operating in offline mode'));
            }, 30000);
            
            // Efectos de hover
            document.querySelectorAll('.price-card, .trader-card, .signal-item').forEach(card => {
                card.addEventListener('mouseenter', function() {
                    this.style.transition = 'all 0.3s ease';
                });
            });
        });
    </script>
</body>
</html>"""

# RUTAS DE LA APLICACIÓN
@app.route('/')
def index():
    return render_template_string(COMPLETE_ENHANCED_TEMPLATE,
        market_mood=analytics.get_market_mood(),
        market_indicators=analytics.market_indicators,
        live_signals=analytics.get_live_signals(),
        elite_traders={'CRYPTO_KING': {'name': 'CryptoKing Elite', 'specialty': 'AI Tokens & DeFi', 'success_rate': 89.5, 'monthly_return': 28.7, 'followers': 1247, 'description': 'Especialista en tokens de IA con enfoque en análisis on-chain'}},
        badges=gamification.badges,
        leaderboard=gamification.get_leaderboard()
    )

# API ENDPOINTS
@app.route('/api/status')
def api_status():
    return jsonify({
        'status': 'online',
        'version': '1.0-github',
        'timestamp': datetime.now().isoformat(),
        'github': True,
        'railway': True,
        'services': {
            'analytics': True,
            'gamification': True,
            'education': True,
            'referrals': True
        }
    })

@app.route('/api/market_mood')
def api_market_mood():
    return jsonify(analytics.get_market_mood())

@app.route('/api/signals')
def api_signals():
    return jsonify(analytics.get_live_signals())

@app.route('/api/leaderboard')
def api_leaderboard():
    return jsonify(gamification.get_leaderboard())

@app.route('/manifest.json')
def manifest():
    return jsonify({
        "name": "SAVAGE TRADER PRO",
        "short_name": "SavageTrader",
        "description": "Bot de Trading con IA, Copy-Trading Elite y Market Mood Indicator",
        "start_url": "/",
        "display": "standalone",
        "theme_color": "#ffd700",
        "background_color": "#000000",
        "icons": [
            {
                "src": "data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTkyIiBoZWlnaHQ9IjE5MiIgdmlld0JveD0iMCAwIDE5MiAxOTIiIGZpbGw9Im5vbmUiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CjxyZWN0IHdpZHRoPSIxOTIiIGhlaWdodD0iMTkyIiByeD0iOTYiIGZpbGw9InVybCgjZ3JhZGllbnQwX2xpbmVhcikiLz4KPHRleHQgeD0iOTYiIHk9IjEyMCIgZm9udC1mYW1pbHk9IkFyaWFsLCBzYW5zLXNlcmlmIiBmb250LXNpemU9IjgwIiBmaWxsPSIjMDAwIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIj7wn5C6PC90ZXh0Pgo8ZGVmcz4KPGxpbmVhckdyYWRpZW50IGlkPSJncmFkaWVudDBfbGluZWFyIiB4MT0iMCIgeTE9IjAiIHgyPSIxOTIiIHkyPSIxOTIiIGdyYWRpZW50VW5pdHM9InVzZXJTcGFjZU9uVXNlIj4KPHN0b3Agb2Zmc2V0PSIwJSIgc3RvcC1jb2xvcj0iI0ZGRDcwMCIvPgo8c3RvcCBvZmZzZXQ9IjUwJSIgc3RvcC1jb2xvcj0iI0ZGOENGRCIKAPXRVCB9ZmZzZXQ9IjEwMCUiIHN0b3AtY29sb3I9IiNEQzE0M0MiLz4KPC9saW5lYXJHcmFkaWVudD4KPC9kZWZzPgo8L3N2Zz4K",
                "sizes": "192x192",
                "type": "image/svg+xml"
            }
        ]
    })

@app.route('/health')
def health():
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat()
    })

# MANEJO DE ERRORES
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Endpoint not found'}), 404

@app.errorhandler(500)
def server_error(error):
    return jsonify({'error': 'Internal server error'}), 500

# EJECUTAR APLICACIÓN
if __name__ == '__main__':
    logger.info(f"🚀 SAVAGE TRADER PRO starting on port {PORT}")
    logger.info("✅ GitHub/Railway Production Ready")
    logger.info("🌟 All systems ready")
    
    app.run(host='0.0.0.0', port=PORT, debug=False)
