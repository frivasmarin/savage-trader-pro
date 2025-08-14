#!/usr/bin/env python3
"""
SAVAGE TRADER PRO - Railway Production
Bot de Trading con IA, Copy-Trading, Market Mood Indicator
Versión optimizada para Railway con todos los sistemas integrados
"""

from flask import Flask, render_template_string, jsonify, request, session
import os
from datetime import datetime, timedelta
import logging
import json
import random

# Configuración de logging para Railway
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Inicializar Flask
app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET", "savage_trader_pro_2024")

# Puerto para Railway (CRÍTICO)
PORT = int(os.environ.get("PORT", 5000))

logger.info(f"🚀 SAVAGE TRADER PRO iniciando en puerto {PORT}")

# SISTEMA DE ANÁLISIS DE MERCADO
class MarketAnalyzer:
    def __init__(self):
        self.indicators = {
            'fear_greed': random.randint(65, 85),
            'volatility': random.randint(20, 35),
            'trend_strength': random.randint(75, 95),
            'ai_confidence': random.randint(85, 95),
            'social_sentiment': 'Bullish',
            'institutional_flow': 'Buying Strong'
        }
    
    def get_market_mood(self):
        score = (self.indicators['fear_greed'] + 
                (100 - self.indicators['volatility']) + 
                self.indicators['trend_strength']) / 3
        
        if score >= 80:
            return {
                'mood': '🚀 Extremadamente Optimista',
                'color': '#10b981',
                'score': int(score),
                'recommendation': 'LONG AGRESIVO'
            }
        elif score >= 70:
            return {
                'mood': '📈 Muy Optimista', 
                'color': '#059669',
                'score': int(score),
                'recommendation': 'BUY FUERTE'
            }
        elif score >= 50:
            return {
                'mood': '⚡ Optimista',
                'color': '#3b82f6', 
                'score': int(score),
                'recommendation': 'BUY MODERADO'
            }
        else:
            return {
                'mood': '⚖️ Neutral',
                'color': '#f59e0b',
                'score': int(score),
                'recommendation': 'ESPERAR'
            }
    
    def get_live_signals(self):
        return [
            {
                'symbol': 'NVDA',
                'action': 'BUY FUERTE',
                'price': 892.50,
                'change': '+2.8%',
                'target1': 925.00,
                'target2': 950.00,
                'stop_loss': 875.00,
                'confidence': 94,
                'reasoning': 'AI Catalyst: Earnings beat + GPU demand surge',
                'timeframe': '4H',
                'volume': 'High'
            },
            {
                'symbol': 'TAO/USDT',
                'action': 'LONG AGRESIVO',
                'price': 345.80,
                'change': '+5.2%',
                'target1': 380.00,
                'target2': 420.00,
                'stop_loss': 330.00,
                'confidence': 91,
                'reasoning': 'Bittensor ecosystem expansion + institutional adoption',
                'timeframe': '1H',
                'volume': 'Extreme'
            },
            {
                'symbol': 'PLTR',
                'action': 'BUY',
                'price': 24.75,
                'change': '+1.9%',
                'target1': 27.50,
                'target2': 30.00,
                'stop_loss': 23.20,
                'confidence': 87,
                'reasoning': 'Government contracts + AI defense applications',
                'timeframe': '1D',
                'volume': 'Medium'
            }
        ]

# SISTEMA COPY-TRADING
class CopyTradingEngine:
    def __init__(self):
        self.elite_traders = {
            'CRYPTO_KING': {
                'name': 'CryptoKing Elite',
                'specialty': 'AI Tokens & DeFi',
                'success_rate': 89.5,
                'avg_profit': 15.2,
                'followers': 1247,
                'risk_level': 'Medio',
                'monthly_return': 28.7,
                'description': 'Especialista en tokens de IA con enfoque en análisis on-chain',
                'assets': ['BTC-USD', 'TAO-USD', 'RENDER-USD', 'FET-USD'],
                'status': 'Activo'
            },
            'AI_STOCKS_MASTER': {
                'name': 'AI Stock Master',
                'specialty': 'Tech Stocks IA',
                'success_rate': 92.1,
                'avg_profit': 12.8,
                'followers': 892,
                'risk_level': 'Bajo',
                'monthly_return': 22.3,
                'description': 'Experto en acciones de IA con análisis fundamental profundo',
                'assets': ['NVDA', 'PLTR', 'SOUN', 'APP'],
                'status': 'Activo'
            },
            'FOREX_ELITE': {
                'name': 'Forex Master Elite',
                'specialty': 'Forex Professional',
                'success_rate': 94.2,
                'avg_profit': 17.3,
                'followers': 2847,
                'risk_level': 'Bajo',
                'monthly_return': 31.5,
                'description': 'Trader institucional de forex con 15+ años de experiencia',
                'assets': ['EUR/USD', 'GBP/USD', 'USD/JPY', 'AUD/USD'],
                'status': 'Activo'
            }
        }
    
    def get_active_trades(self):
        return [
            {
                'trader': 'CryptoKing Elite',
                'asset': 'TAO/USDT',
                'action': 'LONG',
                'entry': 345.80,
                'current': 348.20,
                'target': 380.00,
                'stop_loss': 330.00,
                'pnl': '+0.7%',
                'confidence': 91,
                'time': '14:23'
            },
            {
                'trader': 'AI Stock Master',
                'asset': 'NVDA',
                'action': 'HOLD',
                'entry': 889.30,
                'current': 892.50,
                'target': 925.00,
                'stop_loss': 875.00,
                'pnl': '+0.4%',
                'confidence': 94,
                'time': '13:45'
            }
        ]

# SISTEMA DE GAMIFICACIÓN
class GamificationSystem:
    def __init__(self):
        self.badges = {
            'first_win': {'name': '🎯 Primera Victoria', 'rarity': 'Común', 'points': 100},
            'streak_master': {'name': '🔥 Racha Master', 'rarity': 'Raro', 'points': 300},
            'risk_manager': {'name': '🛡️ Gestor de Riesgo', 'rarity': 'Épico', 'points': 500},
            'diamond_hands': {'name': '💎 Manos de Diamante', 'rarity': 'Legendario', 'points': 1000},
            'ai_expert': {'name': '🤖 Experto IA', 'rarity': 'Raro', 'points': 400},
            'copy_master': {'name': '🔄 Master Copy-Trading', 'rarity': 'Épico', 'points': 600},
            'profit_king': {'name': '👑 Rey de Ganancias', 'rarity': 'Mítico', 'points': 2000}
        }
    
    def get_leaderboard(self):
        return [
            {'rank': 1, 'username': 'TradingKing', 'profit': 28.7, 'badges': 8, 'points': 3420, 'plan': 'Elite'},
            {'rank': 2, 'username': 'AITrader', 'profit': 25.3, 'badges': 6, 'points': 2890, 'plan': 'Premium'},
            {'rank': 3, 'username': 'CryptoWolf', 'profit': 22.8, 'badges': 7, 'points': 2650, 'plan': 'Elite'},
            {'rank': 4, 'username': 'DiamondHands', 'profit': 19.4, 'badges': 5, 'points': 2180, 'plan': 'Premium'},
            {'rank': 5, 'username': 'MarketMaster', 'profit': 17.2, 'badges': 4, 'points': 1940, 'plan': 'Basic'}
        ]

# Inicializar sistemas
market_analyzer = MarketAnalyzer()
copy_trading = CopyTradingEngine()
gamification = GamificationSystem()
