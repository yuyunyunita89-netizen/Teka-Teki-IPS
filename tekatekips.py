import streamlit as st

def validasi_angka(angka):
    return 1 <= angka <= 50

def main():
    st.title("🧮 Aplikasi Operasi Hitung (Skala 1 - 50)")

    st.write("### Pilih Operasi:")
    operasi = st.selectbox("Operasi", ["Penjumlahan (+)", "Pengurangan (-)", "Perkalian (*)", "Pembagian (/)"])

    angka1 = st.number_input("Masukkan angka pertama (1-50):", min_value=1, max_value=50, step=1)
    angka2 = st.number_input("Masukkan angka kedua (1-50):", min_value=1, max_value=50, step=1)

    if st.button("Hitung"):
        if not (validasi_angka(angka1) and validasi_angka(angka2)):
            st.error("Angka harus dalam rentang 1 sampai 50!")
            return

        if operasi == "Penjumlahan (+)":
            hasil = angka1 + angka2
            st.success(f"Hasil penjumlahan: {angka1} + {angka2} = {hasil}")
        elif operasi == "Pengurangan (-)":
            hasil = angka1 - angka2
            st.success(f"Hasil pengurangan: {angka1} - {angka2} = {hasil}")
        elif operasi == "Perkalian (*)":
            hasil = angka1 * angka2
            st.success(f"Hasil perkalian: {angka1} * {angka2} = {hasil}")
        elif operasi == "Pembagian (/)":
            if angka2 == 0:
                st.error("Error: Pembagian dengan nol tidak diperbolehkan!")
            else:
                hasil = angka1 / angka2
                st.success(f"Hasil pembagian: {angka1} / {angka2} = {hasil:.2f}")

if __name__ == "__main__":
    main()
