from flask import Flask, request, jsonify, send_file, render_template
import qrcode
from io import BytesIO
import base64

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_qr():
    data = request.get_json()
    url = data.get('url', '').strip()
    fg_color = data.get('fg_color', '#000000')
    bg_color = data.get('bg_color', '#ffffff')
    
    if not url:
        return jsonify({'error': 'No URL provided'}), 400
    
    # Your original QR code logic
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4
    )
    qr.add_data(url)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color=fg_color, back_color=bg_color)
    
    # Convert to base64
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode()
    
    return jsonify({
        'image': f'data:image/png;base64,{img_str}'
    })

if __name__ == '__main__':
    app.run(debug=True)
