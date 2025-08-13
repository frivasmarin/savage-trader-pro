from flask import Flask, render_template_string

app = Flask(__name__)

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SAVAGE TRADER PRO</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet">
    <style>
        body {
            background: linear-gradient(135deg, #1a1a1a 0%, #2d2d2d 100%);
            color: white;
            font-family: 'Arial', sans-serif;
        }
        .hero { padding: 80px 0; text-align: center; }
        .logo {
            width: 120px; height: 120px; margin: 0 auto 30px;
            background: linear-gradient(45deg, #ff6b35, #f7931e);
            border-radius: 50%; display: flex; align-items: center;
            justify-content: center; font-size: 50px; color: white;
            animation: pulse 2s infinite;
        }
        @keyframes pulse {
            0% { transform: scale(1); }
            50% { transform: scale(1.05); }
            100% { transform: scale(1); }
        }
        .btn-premium {
            background: linear-gradient(45deg, #ff6b35, #f7931e);
            border: none; padding: 15px 30px; border-radius: 50px;
            color: white; font-weight: bold; text-decoration: none;
            display: inline-block; margin: 10px; transition: all 0.3s;
        }
        .btn-premium:hover {
            transform: translateY(-3px);
            box-shadow: 0 10px 25px rgba(255, 107, 53, 0.3);
            color: white;
        }
        .price-card {
            background: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.2);
            border-radius: 20px; padding: 40px; margin: 20px 0;
            transition: transform 0.3s;
        }
        .price-card:hover { transform: translateY(-10px); }
    </style>
</head>
<body>
    <div class="container">
        <div class="hero">
            <div class="logo"><i class="fas fa-chart-line"></i></div>
            <h1 class="display-4 fw-bold mb-4">SAVAGE TRADER PRO</h1>
            <p class="lead mb-5">Bot de Trading con IA - Señales Premium</p>
            
            <div class="row justify-content-center">
                <div class="col-md-5">
                    <div class="price-card">
                        <h3>Plan Basic</h3>
                        <div class="display-5 fw-bold text-warning">€29/mes</div>
                        <a href="https://paypal.me/savagetrader/29" class="btn-premium">
                            <i class="fab fa-paypal"></i> Suscribirse Basic
                        </a>
                    </div>
                </div>
                <div class="col-md-5">
                    <div class="price-card">
                        <h3>Plan Premium</h3>
                        <div class="display-5 fw-bold text-warning">€99/mes</div>
                        <a href="https://paypal.me/savagetrader/99" class="btn-premium">
                            <i class="fab fa-paypal"></i> Suscribirse Premium
                        </a>
                    </div>
                </div>
            </div>
        </div>
    </div>
</body>
</html>"""

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE)

@app.route('/health')
def health():
    return {'status': 'healthy', 'service': 'SAVAGE TRADER PRO'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
