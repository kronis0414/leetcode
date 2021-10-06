class Solution:
    def solveSudoku(self, board):
        rows = []
        columns = []
        squares = []
        for i in range(9):
            rows.append({})
            columns.append({})
            squares.append({})
            
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    rows[i][board[i][j]] = True
                    columns[j][board[i][j]] = True
                    idx = (i//3) * 3 + j // 3
                    squares[idx][board[i][j]] = True
                    
        self.f = False
        def run():
            if sum([len(t) for t in rows]) == 81:
                self.f = True
                return
            for i in range(9):
                for j in range(9):
                    if board[i][j] == '.':
                        idx = (i//3) * 3 + j // 3
                        c = 1
                        while c < 10: 
                            d = str(c)
                            if d not in rows[i] and d not in columns[j] \
                                and d not in squares[idx]:
                                rows[i][d] = True
                                columns[j][d] = True
                                squares[idx][d] = True
                                board[i][j] = d
                                run()
                                if self.f:
                                    return
                                rows[i].pop(d)
                                columns[j].pop(d)
                                squares[idx].pop(d)
                                board[i][j] = '.'
                            c += 1
                        if c > 9:
                            return
        run()
#使用back tracking, 
#建立3個資料結構, rows, columns, squares, 用來判斷要填入的數字是否有重複
#每個資料結構分別儲存第i rows/columns/squares, 已經存在的數字
#其中squares, 從左到右從上到下, 編號是0-8
#運作方式如下
#1.從頭到尾掃board, 若遇到".", 表示該空格還沒有數字, 
#   嘗試數字1-9, 且不跟該空格所在的row, column, square裡面的數字重複
#2.填入數字後, 並在rows, column, square記錄下來, 遞迴1.
#3.若在該空格, 找不到可以填入的數字, 那麼可以提早結束, 不用在判斷後面的空格