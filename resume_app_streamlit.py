import streamlit as st
import json
import datetime
from docxtpl import DocxTemplate
from io import BytesIO

st.title("職務経歴書作成アプリ（Streamlit版）")

st.markdown("### ステップ①：JSONファイルのアップロード")
json_file = st.file_uploader("ChatGPTなどで作成された職務経歴書データ（JSON）をアップロードしてください", type="json")

if json_file:
    data = json.load(json_file)
    data["作成日"] = datetime.date.today().strftime("%Y/%m/%d")

    # ✅ GitHubに保存されたテンプレートを直接読み込む
    doc = DocxTemplate("template.docx")
    doc.render(data)

    output_filename = f"職務経歴書_{data.get('氏名', 'noname')}.docx"
    buffer = BytesIO()
    doc.save(buffer)
    buffer.seek(0)

    st.success("✅ 職務経歴書が完成しました！以下からダウンロードできます：")
    st.download_button(
        label="📄 職務経歴書をダウンロード",
        data=buffer,
        file_name=output_filename,
        mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    )
else:
    st.info("📂 JSONファイルをアップロードしてください。")
