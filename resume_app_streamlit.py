from docxtpl import DocxTemplate
from datetime import datetime
import streamlit as st
import json
from io import BytesIO

st.title("職務経歴書作成アプリ（Streamlit版）")

uploaded_file = st.file_uploader("ステップ①：JSONファイルのアップロード", type="json")

if uploaded_file is not None:
    data = json.load(uploaded_file)
    data["作成日"] = datetime.today().strftime("%Y/%m/%d")

    doc = DocxTemplate("テンプレート.docx")  # 内蔵テンプレートを読み込む
    doc.render(data)

    output_filename = f"職務経歴書_{data['氏名']}.docx"
    buffer = BytesIO()
    doc.save(buffer)
    buffer.seek(0)

    st.download_button(
        label="📄 職務経歴書をダウンロード",
        data=buffer,
        file_name=output_filename,
        mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    )
