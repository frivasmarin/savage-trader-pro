#!/usr/bin/env python3
"""SAVAGE TRADER PRO - Compact Production Server"""

from flask import Flask, v
    <title>SAVAGE TRADER PRO</title>
    <link href="https://cdn.replit.com/agent/bootstrap-agent-dark-theme.min.css" rel="stylesheet">
    <style>
        body { background: linear-gradient(135deg, #0f0f0f, #2d1810); min-height: 100vh; }
        .hero { background: linear-gradient(135deg, rgba(255,215,0,0.1), rgba(255,255,255,0.05)); 
                border-radius: 30px; padding: 60px 40px; margin: 40px 0; border: 2px solid rgba(255,215,0,0.3); text-align: center; }
        .wolf-logo { width: 120px; height: 120px; background: linear-gradient(45deg, #ffd700, #ffed4e);
                     border-radius: 50%; display: flex; align-items: center; justify-content: center;
                     margin: 0 auto 30px; font-size: 4rem; color: #1a1a1a; animation: pulse 2s infinite; }
        @keyframes pulse { 0%, 100% { transform: scale(1); } 50% { transform: scale(1.05); } }
        .price-tag { background: linear-gradient(45deg, #ffd700, #ffed4e); color: #1a1a1a; padding: 15px 30px;
                     border-radius: 25px; font-weight: 900; font-size: 1.3rem; text-decoration: none; }
    </style>
</head>
<body>
    <div class="container">
        <div class="hero">
            <div class="wolf-logo">🐺</div>
            <h1 style="font-size: 3.5rem; font-weight: 900; background: linear-gradient(45deg, #ffd700, #ffed4e); 
                       -webkit-background-clip: text; -webkit-text-fill-color: transparent; margin-bottom: 20px;">
                SAVAGE TRADER PRO
            </h1>
            <p style="font-size: 1.4rem; color: #fff; margin-bottom: 30px;">
                🤖 Trading Bot con IA • 📊 Señales Premium • 🚀 24/7 Autónomo
            </p>
            <div style="margin: 30px 0;">
                <a href="https://paypal.me/savagetrader/29" class="price-tag" style="margin: 10px;">
                    📱 PLAN BÁSICO - €29/mes
                </a>
                <a href="https://paypal.me/savagetrader/99" class="price-tag" style="margin: 10px;">
                    👑 PLAN ELITE - €99/mes
                </a>
            </div>
            <div style="margin-top: 40px;">
                <a href="https://t.me/savagetrader_signals" style="color: #10b981; text-decoration: none; font-size: 1.2rem;">
                    <i class="fab fa-telegram"></i> Únete al Canal VIP
                </a>
            </div>
        </div>
        
        <div style="text-align: center; margin: 60px 0; opacity: 0.7;">
            <p>© 2024 SAVAGE TRADER PRO - Desplegado en Railway 🚀</p>
            <a href="/health" style="color: #10b981; text-decoration: none;">Estado del Sistema</a>
        </div>
    </div>
</body>
</html>''')

@app.route('/health')
def health():
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'platform': 'Railway Production',
        'message': 'SAVAGE TRADER PRO operativo 24/7',
        'version': 'v2.0-compact'
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
