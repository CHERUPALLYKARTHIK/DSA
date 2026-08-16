class Solution:
    def stoneGameIX(self, stones):
        count = [0, 0, 0]

        for x in stones:
            count[x % 3] += 1

        def check(a):
            if a[1] == 0:
                return False

            a[1] -= 1
            moves = 1 + min(a[1], a[2]) * 2 + a[0]

            if a[1] > a[2]:
                a[1] -= 1
                moves += 1

            return moves % 2 == 1 and a[1] != a[2]

        return check(count[:]) or check([count[0], count[2], count[1]])