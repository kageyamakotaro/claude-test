"""じゃんけんゲーム

使い方:
    python janken.py          # 対話モードで遊ぶ
    python janken.py グー      # 1回だけ勝負する
"""
import random
import sys

HANDS = ["グー", "チョキ", "パー"]
# キーの手が、値の手に勝つ
WINS = {"グー": "チョキ", "チョキ": "パー", "パー": "グー"}


def judge(player, computer):
    if player == computer:
        return "あいこ"
    return "あなたの勝ち！" if WINS[player] == computer else "あなたの負け…"


def play(player):
    computer = random.choice(HANDS)
    print(f"あなた: {player}  /  コンピュータ: {computer}")
    print(judge(player, computer))


def main():
    if len(sys.argv) > 1:
        hand = sys.argv[1]
        if hand not in HANDS:
            print("グー・チョキ・パーのどれかを指定してください")
            sys.exit(1)
        play(hand)
        return

    print("じゃんけんゲーム！(やめるときは q)")
    while True:
        choice = input("1:グー 2:チョキ 3:パー > ").strip()
        if choice == "q":
            print("またね！")
            break
        if choice not in ("1", "2", "3"):
            print("1, 2, 3 か q を入力してください")
            continue
        play(HANDS[int(choice) - 1])


if __name__ == "__main__":
    main()
