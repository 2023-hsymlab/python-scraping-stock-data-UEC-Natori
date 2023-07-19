from flask import render_template, request  # 追加
from flask_testapp import app

from random import randint


@app.route('/')
def index():
    data = 'insertテスト中...'
    my_dict = {
        'insert_something1': 'views.pyのinsert_something1部分です。',
        'insert_something2': 'views.pyのinsert_something2部分です。',
        'test_titles': ['aaa', 'bbb', 'ccc']
    }
    return render_template('pages/index.html', insert_test=data, dict_test=my_dict)

@app.route('/sampleform', methods=['GET', 'POST'])
def sample_form():
    if request.method == 'GET':
        return render_template('pages/form.html')
    if request.method == 'POST':
        # ジャンケンの手を文字列の数字0~2で受け取る
        hands = {
            '0': 'グー',
            '1': 'チョキ',
            '2': 'パー',
        }
        janken_mapping = {
            'draw': '引き分け',
            'win': '勝ち',
            'lose': '負け',
        }

        player_hand_ja = hands[request.form['janken']]  # 日本語表示用
        player_hand = int(request.form['janken'])  # str型→数値に変換必要
        enemy_hand = randint(0, 2)  # 相手は0~2の乱数
        enemy_hand_ja = hands[str(enemy_hand)]  # 日本語表示用
        if player_hand == enemy_hand:
            judgement = 'draw'
        elif (player_hand == 0 and enemy_hand == 1) or (player_hand == 1 and enemy_hand == 2) or (player_hand == 2 and enemy_hand == 0):
            judgement = 'win'
        else:
            judgement = 'lose'
        # print(f'じゃんけん開始: enemy_hand: {enemy_hand}, player_hand: {player_hand}, judgement: {judgement}')
        # return f'相手： {enemy_hand_ja}, あなた: {player_hand_ja}, 判定：{janken_mapping[judgement]}'
    

        result = {
            'enemy_hand_ja': enemy_hand_ja,
            'player_hand_ja': player_hand_ja,
            'judgement': janken_mapping[judgement],
        }
        return render_template('pages/janken_result.html', result=result)
