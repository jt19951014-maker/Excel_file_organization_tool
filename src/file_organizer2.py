import os
import shutil
from glob import glob

#資料フォルダ内の全てのエクセルファイルのリストを作成する。
list_of_file = glob("資料/*.xlsx")

#リスト内の1つ1つのファイルに対して実施
for path_of_file in list_of_file:
    #パス名からファイル名のみを抽出
    file_name = path_of_file.split("\\")[1]

    #ファイル名から、フォルダ情報のみを残して余計な記号や文字は削除
    #ソフト名と案件名の間には_を入れ、それぞれの名称を識別できるようにしておく
    base_name = file_name.replace(".xlsx", "").replace("【", "").replace("】", "_").strip()

    #ソフト名、案件名、工程名を各変数に格納
    soft_name = base_name.split("_")[0]
    project_name = base_name.split("_")[1]
    process_name = base_name.split("_")[2]
    #所定のフォルダが存在しなかった場合
    if not os.path.exists(f"資料/{soft_name}/{project_name}/{process_name}"):
        #新しくフォルダを作成
        os.makedirs(f"資料/{soft_name}/{project_name}/{process_name}")

    #移動前と移動先のファイルパスを設定し、ファイルを移動する。
    file_path_before_move = f"資料/{file_name}"
    file_path_after_move = f"資料/{soft_name}/{project_name}/{process_name}/{file_name}"
    shutil.move(file_path_before_move, file_path_after_move)

print("フォルダ整理が完了しました")





