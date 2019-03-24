# [課程規劃表](https://docs.google.com/spreadsheets/d/e/2PACX-1vQcKCGPuZqbmiXOrpkkxfx364vEgpuej5v-Td94xIXXuK7rguBYTcMlXjgL5zvquecvM_Kt3U21TPAW/pubhtml)

# [與教授說明與討論時間安排](https://docs.google.com/spreadsheets/d/1ihrqutmwi0KU2XMlVvTUxCk4JECk-no_hmo4Wt6y90c/edit#gid=0)

# 作業說明:
1. 請各組在所指定的ETF資料中，先篩選出於2015年年底既已存在的ETF(可從EXCEL檔中的W欄看到起始時間)，並以此子集合重新建立一個EXCEL檔。

2. 承上，請利用爬蟲方法整理出此子集合中的每一檔ETF，其每月月底的基金淨值(NAV)。

3. 承上，為求統一，只收集2015年12月至2018年12月，故共有1+36 = 37筆的月底基金淨值。

4. 有關每組找尋怎樣的ETF，請每組請參考"ETF分組.rar"中的檔案 HW1作業分組.xlsx，並根據檔案內「HW1_爬蟲與指標選定」欄位在"ETF分組.rar"中找到你們所屬的資料夾，裡面會有你們要找尋的ETF清單 。例如在HW1_爬蟲與指標選定欄位中第一組要找的是BOND，打開路徑為"ETF分組\BOND (第一組~第五組)\第1組"的資料夾後，請參考"Total Bond Market ETF List (82).csv"的檔案。

5. 請小組成員互相合作，比較會寫程式的人請「踴躍積極」幫助另一半，另一半也請不要害羞提問，越多互動越好，在繳交期限前小組記得將檔案fork到你們成員的github中。有關爬蟲的部分請以小組為單位繳交作業，但我們會去github中看你們每個成員的貢獻度，以及更改紀錄XD。

6. 另外有關找尋評比績效指標的部分，請每組繳交兩頁的word檔案，說明使用的指標，並上傳到作業區中，有關小組介紹指標的部分，請包涵下面三點:
    * 介紹指標的由來，例如發明人或是提出的機構
    * 介紹這個指標的內涵，包含如何計算
    * 介紹指標的依據，根據甚麼樣的財務理論或是邏輯來建立    
    * (optional不強迫)指標的應用面，例如有那些著名的機構有採用你這個指標

7. 爬蟲的教學可以參考YOUTUB，可以輸入SELENIUM TUTORIAL就會有(看你用哪個套件)下面網站也可以讓大家參考，但希望理工的同學可以互相合作指導對方，不行的話可以約OFFICE HOUR跟我們討論

[Selenium install Tutorial](https://medium.com/@NorthBei/%E5%9C%A8windows%E4%B8%8A%E5%AE%89%E8%A3%9Dpython-selenium-%E7%B0%A1%E6%98%93%E6%95%99%E5%AD%B8-eade1cd2d12d)

[Selenium Tutorial on youtube](https://www.youtube.com/watch?v=o6yzNaRAzW8&list=PLRxMjOjh7Y5fi4ID2YCkcA2vLlD-JNC9i)

[Morvanzhou **GitHub** 連結](https://morvanzhou.github.io/tutorials/data-manipulation/scraping/5-01-selenium/)
 
-----
* HW1

1. 請各組在所指定的ETF資料中，先篩選出於2015年年底既已存在的ETF(可從EXCEL檔中的W欄看到起始時間)，並以此子集合重新建立一個EXCEL檔。

2. 承上，請利用爬蟲方法整理出此子集合中的每一檔ETF，其每月月底的基金淨值(NAV)。

3. 承上，為求統一，只收集2015年12月至2018年12月，故共有1+36 = 37筆的月底基金淨值。

4. 在Github上的呈現方式請符合下面要求:

	* 請將程式碼放上Github上，用網路教學的方式來撰寫作業，讓有基礎Python經驗的人可以根據你的教案做出同樣的功能來，
	  或是在未來你想用這份作業的程式時，你可以根據這份教案快速上手，小組完成後成員互相fork一份。內容至少要包含下列幾項:

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
	    (../這是相對路徑語法，若自行下載此打法是指在此Python(Juptyer) check point下的檔案位置，通常會在user中) 




