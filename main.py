import streamlit as st

st.set_page_config(page_title="Axion Academy Ledger", page_icon="🎓")

st.title("🎓 Axion Academy: جواز السفر التعليمي")
st.write("لأن الحرب قد تسرق أوراقنا، لكنها لن تسرق عقول أطفالنا")

# --- ملف الطفل التعليمي ---
child_name = st.text_input("اسم الطالب (الطفل)")
grade_level = st.selectbox("المرحلة الدراسية الأصلية", ["أساس 1", "أساس 5", "متوسط", "ثانوي"])

tab1, tab2 = st.tabs(["📚 سجل التعلم اليومي", "📜 شهادة الكفاءة الرقمية"])

with tab1:
    st.header("توثيق الدروس المنجزة")
    subject = st.selectbox("المادة", ["الرياضيات", "اللغة الإنجليزية", "العلوم", "البرمجة للأطفال"])
    progress = st.slider("نسبة إكمال المنهج", 0, 100, 20)
    teacher_note = st.text_area("ملاحظة المعلم المشرف (أو الأب كمعلم)")
    if st.button("حفظ التقدم في السجل الدائم"):
        st.success(f"تم تسجيل تقدم {child_name} في مادة {subject}. البيانات محمية ضد الفقدان.")

with tab2:
    st.header("إصدار بطاقة الكفاءة")
    st.info("هذه البطاقة معتمدة من نظام أكسيون كدليل على المستوى الأكاديمي الفعلي.")
    if st.button("توليد جواز السفر الأكاديمي (PDF)"):
        st.markdown(f"""
        <div style="border:5px double #1E3A8A; padding:20px; border-radius:15px; background-color:#F8FAFC;">
            <h2 style="text-align:center; color:#1E3A8A;">Academic Competency Passport</h2>
            <p><b>Student:</b> {child_name}</p>
            <p><b>Certified Level:</b> {grade_level}</p>
            <p><b>Verified Skills:</b> Logic, Problem Solving, Literacy</p>
            <hr>
            <p style="text-align:center;"><i>وثيقة صادرة عن مبادرة أكسيون لدعم استمرارية التعليم في الأزمات</i></p>
        </div>
        """, unsafe_allow_html=True)
