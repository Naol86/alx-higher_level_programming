#!/usr/bin/python3
"""N queen problem"""
import sys


def start(n):
    col = []
    neg_digo = []
    pos_digo = []

    board = [True for i in range(n ** 2)]
    ans = []

    def back_tacking(r):
        if r == n:
            temp = board.copy()
            ans.append(temp)
            return

        for c in range(n):
            if c in col or (c + r) in pos_digo or (c - r) in neg_digo:
                continue

            col.append(c)
            neg_digo.append(c - r)
            pos_digo.append(c + r)
            board[(r * n) + c] = False

            back_tacking(r + 1)

            col.remove(c)
            neg_digo.remove(c - r)
            pos_digo.remove(c + r)
            board[(r * n) + c] = True

    back_tacking(0)
    return ans


def sol(n):
    ans = start(n)
    for i in range(len(ans)):
        temp = []
        for j in range(len(ans[i])):
            if not ans[i][j]:
                row = j // n
                col = j % n
                temp.append([row, col])
        print(temp)


def main():
    if __name__ == "__main__":
        if len(sys.argv) != 2:
            print("Usage: nqueens N")
            sys.exit(1)
        if sys.argv[1].isdigit() is False:
            print("N must be a number")
            sys.exit(1)
        if int(sys.argv[1]) < 4:
            print("N must be at least 4")
            sys.exit(1)
        a = int(sys.argv[1])
        sol(a)


main()
