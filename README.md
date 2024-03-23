### Install and Run
```
pip install -r requirements.txt
```

To scrape all available links in Finra and save to a .txt file:
```
python maain.py
```

Once you have the links text file, to read each link and save to a dataset, run:
```
python data.py
```

### Additional links and resources

https://chat.openai.com/share/07588606-fb71-4af2-bcfc-9de566ec9bc4<br>

https://github.com/mozilla/geckodriver/?tab=readme-ov-file<br>

Install geckodrivers
```
wget https://github.com/mozilla/geckodriver/releases/download/v0.34.0/geckodriver-v0.34.0-linux64.tar.gz  
# or similar latest for linux64
tar -zxvf geckodriver-v0.34.0-linux64.tar.gz
sudo mv geckodriver /usr/local/bin/
chmod +x /usr/local/bin/geckodriver
geckodriver --version
```

https://www.finra.org/finra-data/browse-catalog/short-sale-volume-data/daily-short-sale-volume-files<br>
https://www.finra.org/sites/default/files/2021-07/DailyShortSaleVolumeFileLayout.pdf<br>
<br>
https://www.omgubuntu.co.uk/2022/04/how-to-install-firefox-deb-apt-ubuntu-22-04#:%7E:text=Installing%20Firefox%20via%20Apt%20(Not%20Snap)&text=You%20add%20the%20Mozilla%20Team,%2C%20bookmarks%2C%20and%20other%20data.<br>

`pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu`
