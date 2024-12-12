from flask import Flask, render_template_string, request

app = Flask(__name__)

best_score = 0

@app.route('/')
def home():
    return render_template_string('''
        <!DOCTYPE html>
        <html lang="tr">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Codeland</title>
            <style>
                body {
                    font-family: 'Arial', sans-serif;
                    background-color: #f4f4f9;
                    margin: 0;
                    padding: 0;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                }
                .container {
                    width: 100%;
                    max-width: 500px;
                    background-color: #ffffff;
                    padding: 40px;
                    border-radius: 8px;
                    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                    text-align: center;
                }
                h1 {
                    color: #333;
                    font-size: 36px;
                    margin-bottom: 20px;
                    font-weight: 600;
                }
                p {
                    color: #666;
                    font-size: 18px;
                    margin-bottom: 30px;
                }
                .button {
                    display: inline-block;
                    padding: 12px 30px;
                    margin: 10px 0;
                    background-color: #007bff;
                    color: #fff;
                    font-size: 18px;
                    font-weight: bold;
                    text-decoration: none;
                    border-radius: 5px;
                    transition: background-color 0.3s ease;
                }
                .button:hover {
                    background-color: #0056b3;
                }
                .button-secondary {
                    background-color: #28a745;
                }
                .button-secondary:hover {
                    background-color: #218838;
                }
            </style>
        </head>
        <body>
        <div class="container">
            <h1>Hoşgeldiniz!</h1>
            <p>Codeland platformunda sınavınızı başlatmak için aşağıdaki butonlara tıklayabilirsiniz.</p>
            <form action="/quiz" method="POST">
                <button type="submit" class="button">Sınava Başla</button>
            </form>
            <a href="https://github.com/TrKes/Codeland" class="button button-secondary">Proje Kodları</a>
        </div>
        </body>
        </html>
    ''')


@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    global best_score
    score = 0
    if request.method == 'POST':

        answers = {
            'question1': 'D', 'question2': 'A', 'question3': 'A',
            'question4': 'D', 'question5': 'B'
        }

        for question, correct_answer in answers.items():
            if request.form.get(question) == correct_answer:
                score += 1

        # Update best score if necessary
        if score > best_score:
            best_score = score

        return render_template_string("""
            <!DOCTYPE html>
            <html lang="tr">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Python Quiz - Sınav</title>
                <style>
                    body {
                        font-family: 'Arial', sans-serif;
                        background-color: #f4f4f9;
                        margin: 0;
                        padding: 0;
                        display: flex;
                        justify-content: center;
                        align-items: center;
                        height: 100%;
                    }
                    .container {
                        width: 100%;
                        max-width: 800px;
                        background-color: #ffffff;
                        padding: 40px;
                        border-radius: 10px;
                        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.1);
                        text-align: center;
                    }
                    h1 {
                        color: #333;
                        font-size: 36px;
                        margin-bottom: 20px;
                        font-weight: 600;
                    }
                    p {
                        color: #666;
                        font-size: 18px;
                        margin-bottom: 30px;
                    }
                   .score {
                        font-size: 18px;
                        position: absolute;
                        top: 10px;
                        right: 435px;
                    }

                    .question {
                        text-align: left;
                        margin-bottom: 20px;
                    }
                    label {
                        font-size: 16px;
                        color: #333;
                    }
                    .options {
                        display: flex;
                        align-items: flex-start;
                    }
                    .options input {
                        margin-bottom: 10px;
                    }
                    button {
                        padding: 12px 30px;
                        background-color: #007bff;
                        color: white;
                        border: none;
                        border-radius: 5px;
                        font-size: 18px;
                        cursor: pointer;
                        transition: background-color 0.3s;
                    }
                    button:hover {
                        background-color: #0056b3;
                    }
                    .result {
                        font-size: 24px;
                        font-weight: bold;
                        color: #333;
                        margin-top: 20px;
                    }
                    .back-button {
                        padding: 10px 20px;
                        background-color: #28a745;
                        color: white;
                        border: none;
                        border-radius: 5px;
                        font-size: 18px;
                        cursor: pointer;
                        transition: background-color 0.3s;
                    }
                    .back-button:hover {
                        background-color: #218838;
                    }
                     .username {
                        font-size: 18px;
                        margin-bottom: 20px;
                    }

                </style>
            </head>
            <body>
            <div class="container">
                <div class="score">
                    <strong>En Yüksek Skor: {{ best_score }}</strong>
                </div>

                <h1>Sınav: Python Bilgisi</h1>

                  <div class="username">
                        <label for="username">Adınızı Giriniz:</label><br>
                        <input type="text" id="username" name="username" placeholder="Adınız" required><br><br>
                </div>
                <form method="POST">
                    <div class="question">
                        <label for="question1">Python'da makine öğrenmesi ve yapay zeka modellerini geliştirmek için hangi kütüphane/araç kullanılmaz?</label><br>
                        <div>
                            <input type="radio" id="question1_a" name="question1" value="A">
                            <label for="question1_a">A) TensorFlow</label><br>
                            <input type="radio" id="question1_b" name="question1" value="B">
                            <label for="question1_b">B) scikit-learn</label><br>
                            <input type="radio" id="question1_c" name="question1" value="C">
                            <label for="question1_c">C) PyTorch</label><br>
                            <input type="radio" id="question1_d" name="question1" value="D">
                            <label for="question1_d">D) Microsoft Excel</label>
                        </div>
                    </div>

                    <div class="question">
                        <label for="question2">Python'da bilgisayar görüşü (computer vision) uygulamaları için en yaygın kullanılan kütüphanelerden hangisi doğru verilmiştir?</label><br>
                        <div >
                            <input type="radio" id="question2_a" name="question2" value="A">
                            <label for="question2_a">A) OpenCV</label><br>
                            <input type="radio" id="question2_b" name="question2" value="B">
                            <label for="question2_b">B) Matplotlib</label><br>
                            <input type="radio" id="question2_c" name="question2" value="C">
                            <label for="question2_c">C) Pandas</label><br>
                            <input type="radio" id="question2_d" name="question2" value="D">
                            <label for="question2_d">D) NumPy</label>
                        </div>
                    </div>

                    <div class="question">
                        <label for="question3">Aşağıdaki işlemlerden hangisi doğal dil işleme (NLP) alanında genellikle "tokenization" adıyla bilinir?</label><br>
                        <div >
                            <input type="radio" id="question3_a" name="question3" value="A">
                            <label for="question3_a">A) Cümleleri kelimelere ayırma</label><br>
                            <input type="radio" id="question3_b" name="question3" value="B">
                            <label for="question3_b">B) Cümledeki bağlaçları çıkartma</label><br>
                            <input type="radio" id="question3_c" name="question3" value="C">
                            <label for="question3_c">C) Kelimelerin kök hallerine dönüştürülmesi</label><br>
                            <input type="radio" id="question3_d" name="question3" value="D">
                            <label for="question3_d">D) Metni sesli hale getirme</label>
                        </div>
                    </div>

                    <div class="question">
                        <label for="question4">Aşağıdakilerden hangisi, Python'da bir yapay zeka modelinin eğitiminde kullanılan temel algoritmalardan biri değildir?</label><br>
                        <div >
                            <input type="radio" id="question4_a" name="question4" value="A">
                            <label for="question4_a">A) Karar Ağaçları</label><br>
                            <input type="radio" id="question4_b" name="question4" value="B">
                            <label for="question4_b">B) K-Nearest Neighbors (KNN)</label><br>
                            <input type="radio" id="question4_c" name="question4" value="C">
                            <label for="question4_c">C) Lojistik Regresyon</label><br>
                            <input type="radio" id="question4_d" name="question4" value="D">
                            <label for="question4_d">D) SSH (Secure Shell)</label>
                        </div>
                    </div>

                    <div class="question">
                        <label for="question5">Python'da nesne tanıma için kullanılan "Haar Cascade" sınıflandırma yöntemi, hangi tür nesnelerin tespiti için kullanılır?</label><br>
                        <div >
                            <input type="radio" id="question5_a" name="question5" value="A">
                            <label for="question5_a">A) Yalnızca yazı karakterlerini tanımak</label><br>
                            <input type="radio" id="question5_b" name="question5" value="B">
                            <label for="question5_b">B) Yüz tanıma ve göz algılama</label><br>
                            <input type="radio" id="question5_c" name="question5" value="C">
                            <label for="question5_c">C) Ses tanıma</label><br>
                            <input type="radio" id="question5_d" name="question5" value="D">
                            <label for="question5_d">D) Sesli komutlar</label>
                        </div>
                    </div>

                    <button type="submit">Sonuçları Göster</button>
                </form>

                  {% if score is not none %}
                    <div class="result">
                        <p>Skorunuz: {{ score }} / 5</p>
                    </div>
                {% endif %}

                <button class="back-button" onclick="window.location.href='/'">Ana Sayfaya Dön</button>

                 <h4 class="result">Bu site Halil İbrahim Kes tarafından hazırlanmıştır.</h4>

            </div>
            </body>
            </html>
        """, score=score, best_score=best_score)


if __name__ == "__main__":
    app.run(debug=True)
