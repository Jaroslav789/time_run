import streamlit as st

def vypocitej_cas(t1, d1, d2):
    # Riegelův vzorec: T2 = T1 * (d2/d1)^1.06
    t2 = t1 * (d2 / d1)**1.06
    return t2

def formatuj_cas(sekundy):
    hodiny = int(sekundy // 3600)
    minuty = int((sekundy % 3600) // 60)
    vteriny = int(sekundy % 60)
    if hodiny > 0:
        return f"{hodiny}h {minuty}m {vteriny}s"
    return f"{minuty}m {vteriny}s"

st.title("🏃 Běžecký Prediktor 1.0")
st.write("Zadejte svůj nejlepší čas na známé vzdálenosti a zjistěte, za kolik uběhnete maraton.")

# Vstupy od uživatele
col1, col2 = st.columns(2)
with col1:
    vzdalenost_zname = st.number_input("Vaše známá vzdálenost (km)", value=5.0)
    cas_v_minutach = st.number_input("Váš čas (celkem v minutách)", value=25.0)

# Výpočty pro standardní tratě
trate = {"10 km": 10, "Půlmaraton": 21.097, "Maraton": 42.195}

st.subheader("Vaše odhadované časy:")

for nazev, d2 in trate.items():
    predikce_sekundy = vypocitej_cas(cas_v_minutach * 60, vzdalenost_zname, d2)
    tempo_sekundy = predikce_sekundy / d2

    col_a, col_b = st.columns(2)
    col_a.metric(nazev, formatuj_cas(predikce_sekundy))
    col_b.write(f"Tempo: {formatuj_cas(tempo_sekundy)} / km")

st.info("TIP: Tento výpočet předpokládá, že máte na danou vzdálenost natrénováno.")
