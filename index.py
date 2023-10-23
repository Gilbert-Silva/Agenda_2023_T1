from templates.inicioUI import InicioUI
from templates.equacaoUI import EquacaoUI
from templates.manterclienteUI import ManterClienteUI
from templates.manterservicoUI import ManterServicoUI
import streamlit as st

class IndexUI:
      
    @classmethod
    def sidebar(cls):
      op = st.sidebar.selectbox("Menu", ["Equação", "Manter Clientes", "Manter Serviços"])
      if op == "Equação": st.session_state["page"] = "equacaoUI"
      if op == "Manter Clientes": st.session_state["page"] = "manter_clienteUI"
      if op == "Manter Serviços": st.session_state["page"] = "manter_servicoUI"

    @classmethod
    def main(cls):
      IndexUI.sidebar()
      if "page" not in st.session_state: st.session_state["page"] = "equacaoUI"
      if st.session_state["page"] == "equacaoUI": EquacaoUI.main()
      if st.session_state["page"] == "manter_clienteUI": ManterClienteUI.main()
      if st.session_state["page"] == "manter_servicoUI": ManterServicoUI.main()

      #InicioUI.main()
      #EquacaoUI.main()
      #ManterClienteUI.main()
      #ManterServicoUI.main()

IndexUI.main()



