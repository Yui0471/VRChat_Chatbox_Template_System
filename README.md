# VRChat Chatbox Template System

「いちいちキーボードで入力するのもアレだし、定型文そのまま送信してくれるのあればいいよね」

それだけ。


# DEMO

- アバターのExpressionParametersに"chattext"というintパラメータを設定します
- アバターのExpressionMenuに使うだけchattextのintを変更するbuttonを追加します
- template.pyの辞書を書き換えます. ここに入力した文字がテンプレートとして扱われます
- main.pyを起動します
- VRChat内でEXMenuを操作します
- おわり

[![thumbnail](https://pbs.twimg.com/ext_tw_video_thumb/1560097540246163456/pu/img/n7KWthtDBgcEneuB.jpg)](https://twitter.com/i/status/1560097636127875073)


# Requirement

* Windows 10 以降想定


## Python

* Python 3.8以上
* python-osc 1.8.0

```bash
pip install python-osc
```

# Development Environment

* Windows 10 Home 21H1
* Python 3.8.2
* python-osc 1.8.0
* Visual Studio Code 1.65.2  


# Author

* 風庭ゆい

# License

* いまのところMITlicenseです。