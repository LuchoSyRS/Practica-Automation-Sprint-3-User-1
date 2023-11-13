cd /d %~dp0
python -m pytest Tests/tst_001.py Tests/tst_002.py Tests/tst_003.py --html=Results/OnetoLucianoOmar.html --self-contained-html
pause
