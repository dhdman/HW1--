# [課程規劃表](https://docs.google.com/spreadsheets/d/e/2PACX-1vQcKCGPuZqbmiXOrpkkxfx364vEgpuej5v-Td94xIXXuK7rguBYTcMlXjgL5zvquecvM_Kt3U21TPAW/pubhtml)

# [與教授說明與討論時間安排](https://docs.google.com/spreadsheets/d/1ihrqutmwi0KU2XMlVvTUxCk4JECk-no_hmo4Wt6y90c/edit#gid=0)


# 作業流程
* 你選擇用甚麼樣的套件來做網路爬蟲?為什麼要用這個套件
	* selenium: 可以自動爬取動態式資料(須填入爬取年分、爬取日期區間)，例如yahoo_finance。
    * request: 方便且快速獲取非動態式網頁內文
    * beautifulsoup: 方便且快速獲取非動態式網頁內文
 * 請用流程圖的方式告訴我們你是怎麼抓到你的目標資料，流程圖的畫法不拘，主要易懂就好:  
   [流程圖](https://drive.google.com/file/d/16q2AWJ3wPwgKP_qlCzlIt5zXhwKm_pv-/view?usp=sharing)
 * 完整的範例程式
 * Demo的示範畫面以及解說
 * 至少設想並列出5種當別人使用你的程式最有可能會遇到的錯誤情況，並提供解決辦法
 	1. 使用selenium時: 需將瀏覽器的自動開啟檔(web_dirver)放在同個資料夾裡面(EX:Chrome_driver,Gecko_driver)。
 	2. 若開啟web_driver有錯誤，可能要檢查一下driver版本，目前資料夾提供(MAC : Chrome_driver , Windows : Chrome_driver , firefox_driver)
 	   可以嘗試使用不同的driver來解決此問題
 	3. 使用selenium時: 記得如果有讀取或更新頁面的步驟時，記得輸入time.sleep 讓程式稍微暫停，否則容易出現爬取錯誤或者重複爬取的情況
 	4. 自動點擊下載時: 如果太早將driver關起來，可能會出現資料沒下載的情形。
		* Sol:使用time.sleep暫停一下畫面(同上稍微暫停等站程式執行)。
	5. 在使用selenium時: 若找不到自己執行得路徑可以透過 (Katalon Recoder) 來輔助執行
	    此適用於Chrome and Firfox 套件
	6. 在使用個個檔案讀取時 : 請將路徑改成網路github_dataset或者將Data自行下載至自己路徑，並且確實指定完整路徑，否則容易發生找不到路徑的狀況
	    (../這格語法是指在此Python(Juptyer) check point下的檔案位置，通常會在user中) 




