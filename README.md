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
git clone https://github.com/jt19951014-maker/excel-file-organizer.git  /jt19951014-maker/weather-scraping-yahoo.git
cd weather-scraping-yahoo
```
