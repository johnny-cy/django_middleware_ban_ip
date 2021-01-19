# django_middleware_ban_ip
透過自訂義的中間件，設定3秒內發送10次請求的IP將被Ban 30秒
1. 創建middleware.py
2. 添加到settings.py
3. request.META可獲得REMOTE_ADDR 表示請求來自IP
4. 利用紀錄每次請求的當前時間跟上一次時間比較
5. 每次請求判斷是否在3秒內，是的話增加次數1
6. 若請求不在3秒內，則將IP紀錄刪除，重新計算。
