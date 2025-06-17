
import streamlit as st
import json
import datetime
from docxtpl import DocxTemplate
import pandas as pd

st.title("職務経歴書作成アプリ（Streamlit版）")

st.markdown("### ステップ①：JSONファイルのアップロード")
json_file = st.file_uploader("ChatGPTなどで作成された職務経歴書データ（JSON）をアップロードしてください", type="json")

st.markdown("### ステップ②：Wordテンプレート（.docx）のアップロード")
template_file = st.file_uploader("Jinjaタグ付きの職務経歴書テンプレート（Word）をアップロードしてください", type="docx")

if json_file and template_file:
    # JSON読み込み
    data = json.load(json_file)

    # 作成日を追加（自動で今日）
    data["作成日"] = datetime.date.today().strftime("%Y/%m/%d")

    # Wordテンプレートに差し込み
    doc = DocxTemplate(template_file)
    doc.render(data)

    output_filename = f"職務経歴書_{data.get('氏名', 'noname')}.docx"
    doc.save(output_filename)

    with open(output_filename, "rb") as file:
        st.success("職務経歴書が完成しました！以下からダウンロードできます：")
        st.download_button("📄 ダウンロードする", file, file_name=output_filename)
else:
    st.info("上記2つのファイルをアップロードしてください。")
