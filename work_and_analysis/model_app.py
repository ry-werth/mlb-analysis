import streamlit as st
import numpy as np
import pandas as pd

# Run this with streamlit run model_app.py

complete_df = pd.read_pickle("full_comined_baseball_stats.pkl")

singles = st.sidebar.slider("Singles Per Game", 3.0, 9.0, 5.0, 0.1)
doubles = st.sidebar.slider("Doubles Per Game", 0.5, 3.5, 1.0, 0.1)
triples = st.sidebar.slider("Triples Per Game", 0.0, 1.2, .2, 0.1)
homeruns = st.sidebar.slider("Home Runs Per Game", 0.0, 2.5, 1.2, 0.1)
walks = st.sidebar.slider("Walks Per Game", 0.0, 6.0, 3.0, 0.1)
sbs = st.sidebar.slider("Stolen Bases Per Game", 0.0, 2.5, 0.8, 0.1)
sos = st.sidebar.slider("Strike Outs Per Game", 1.0, 12.0, 7.0, 0.1)

singles_a = st.sidebar.slider("Singles Per Game Against", 3.0, 9.0, 5.0, 0.1)
doubles_a = st.sidebar.slider("Doubles Per Game Against", 0.5, 3.5, 1.0, 0.1)
triples_a = st.sidebar.slider("Triples Per Game Against", 0.0, 1.2, .2, 0.1)
homeruns_a = st.sidebar.slider("Home Runs Per Game Against", 0.0, 2.5, 1.2, 0.1)
walks_a = st.sidebar.slider("Walks Per Game Against", 0.0, 6.0, 3.0, 0.1)
sbs_a = st.sidebar.slider("Stolen Bases Per Game Against", 0.0, 2.5, 0.8, 0.1)
sos_a = st.sidebar.slider("Strike Outs Per Game Against", 1.0, 12.0, 7.0, 0.1)

stats_dict = {
    "Singles" : float(singles),
    "Doubles" : float(doubles),
    "Triples" : float(triples),
    "Homeruns" : float(homeruns),
    "Walks" : float(walks),
    "Stolen_Bases": float(sbs),
    "Strike_Outs" : float(sos),
    "Singles_Against" : float(singles),
    "Doubles_Against" : float(doubles),
    "Triples_Against" : float(triples),
    "Homeruns_Against" : float(homeruns),
    "Walks_Against" : float(walks),
    "Stolen_Bases_Against": float(sbs),
    "Strike_Outs_Against" : float(sos),
}

st.markdown("** MLB Win Calculator **")
st.markdown("Adjust Your Team's Stats on the Left To See How Many Games You Should Win")
st.markdown("Or select some of baseball's most iconic seasons of the early 2000's")

selected_team = ""

if st.button('2001 Seattle Mariners'):
    doubles = 1.91
    triples = 0.23
    homeruns = 1.04
    singles = 10.10 - doubles - triples - homeruns
    sbs = 1.07
    walks = 3.79
    sos = 6.10

    singles_a = 5.259259
    doubles_a = 1.598765
    triples_a = 0.135802
    homeruns_a = 0.987654
    walks = 2.87037
    sbs_a = 0.450617
    sos_a = 6.487654

    selected_team = "mariners"

if st.button("2002 Oakland A's"):

    singles=5.79
    doubles=1.72
    triples=0.17
    homereuns=1.27
    walks=3.76
    sbs=0.28
    sos=6.22
    singles_a = 5.919753
    doubles_a = 1.660494
    triples_a = 0.17284
    homeruns_a = 0.833333
    walks = 2.925926
    sbs_a = 0.419753
    sos_a = 6.302469

    selected_team = "athletics"

if st.button('2004 Boston Red Sox'):
    singles=6.14
    doubles=2.3
    triples=0.15
    homereuns=1.37
    walks=4.07
    sbs=0.42
    sos=7.34
    singles_a = 5.691358
    doubles_a = 1.962963
    triples_a = 0.191358
    homeruns_a = 0.981481
    walks = 2.759259
    sbs_a = 0.759259
    sos_a = 6.987654

    selected_team = "redsox"

stats_list = [round(singles, 2), round(doubles,2), round(triples,2), round(homeruns,2), round(walks,2), round(sbs,2), round(sos,2),
            round(singles_a,2), round(doubles_a,2), round(triples_a,2), round(homeruns_a,2), round(walks_a,2), round(sbs_a,2), round(sos_a,2)]

headers = ["Singles", "Doubles", "Triples", "Homeruns", "Walks", "Stolen Bases", "Strike Outs",
            "Singles Against", "Doubles Against", "Triples Against", "Homeruns Against", "Walks Against", "Stolen Bases Against", "Strike Outs Against"]

df = pd.DataFrame([stats_list], columns=headers)

st.write(df.style)

wins = 88.03 + 8.46548619*singles +  doubles*10.90153133 +  triples*10.31579342 + homeruns*25.49726365 + walks*5.2875412 + sbs*4.99142514 - sos*1.14114248 \
- singles_a*8.4076169 - doubles_a*11.28754979 - triples_a*18.29526589 - homeruns_a*23.87520359 - walks_a*6.83247114 - sbs_a*5.00346649 + sos_a*0.83890628


st.markdown('This team should win **{}** games'.format(round(wins,2)))
if selected_team == "mariners":
    st.markdown("They actually won an MLB record 116 games! I'll blame the discrepency on it being an outlier...")

if selected_team == "athletics":
    st.markdown("They actually won 103 games. This was the famous money ball season.")

if selected_team == "redsox":
    st.markdown("They actually won 98 games and went on to win their first world series in over a century. It was a better prediction than the mariners...")


