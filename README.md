# Excel_file_organization_tool
業務で作成されるExcelファイルを対象に、  
ファイル名に含まれる情報（ソフト名／案件名／工程名／機能名）をもとに  
フォルダ階層を自動生成し、ファイルを整理するPythonツールです。

## 概要
本ツールは、

【ソフト名】案件名_工程名_機能名.xlsx

という規則で命名されたエクセルファイルが混在するとき、  
ソフト名 → 案件名 → 工程名 の階層でフォルダを作成し、  
ファイルを自動的に振り分けます。

## デモ
### Before
- 1つのフォルダに複数案件・複数工程のExcelファイルが混在
- 手作業でフォルダ分けを行っていた
![Run Demo](image/Before.png)

### After
- スクリプトを実行するだけで
- 命名規則に基づいたフォルダ階層が自動生成され
- ファイルが整理される
![Run Demo](image/VSCode実行画面1.png)
![Run Demo](image/VSCode実行画面2.png)
![Run Demo](image/After1.png)
![Run Demo](image/After2.png)
![Run Demo](image/After3.png)
![Run Demo](image/After4.png)

## 使い方
### 1. リポジトリをクローン
```bash
git clone https://github.com/jt19951014-maker/Excel_file_organization_tool.git
cd Excel_file_organization_tool
```
### 2. フォルダ構成を準備

スクリプト実行前に、  
整理したいExcelファイルを格納する 「資料」 フォルダを  
実行環境と同じ階層に用意してください。
```bash
(例)
Excel_file_organization_tool/
├─ src/
│  └─ file_organizer2.py
├─ 資料/
   └─ 【ソフトA】_案件a_外部設計_ログイン.xlsx
```
### 3. スクリプトを実行
```bash
python src/file_organizer2.py
```
### 4. 出力結果の確認
実行後、「資料」フォルダ配下に
ソフト名／案件名／工程名ごとのフォルダが自動生成され、
Excelファイルが整理されます。

## 特徴
```bash
・命名規則に基づくファイル名の解析
・フォルダ階層の自動生成
・Excelファイルの自動振り分け
・業務での利用を想定したシンプルな構成
```

## 使用技術
```bash
・Python 3.12
・os
・shutil
```

## 構成
```bash
Excel_file_orgamization_tool/
├─ src/
│   └─ file_organizer2.py
├─ 資料/
│   └─ 【ソフトA】案件a_外部設計_ログイン.xlsx
└─ README.md
※資料フォルダは使用前に用意する必要あり
```

## 今後の拡張予定
```bash
・命名規則違反ファイルの検知
・dry-run モードの追加
・copy / move 切り替え機能
・CLI引数対応
・logging対応
```

## Lisence
MIT Lisence

