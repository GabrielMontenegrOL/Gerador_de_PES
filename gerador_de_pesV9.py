import tkinter as tk
from tkinter import messagebox, font, ttk
from datetime import datetime
import pyperclip
import re
import webbrowser

# CONSTANTES E DADOS
cidades_paraiba = [
    "Agua Branca", "Aguiar", "Alagoa Grande", "Alagoa Nova", "Alagoinha",
    "Alcantil", "Algodao de Jandaira", "Alhandra", "Amparo", "Aparecida",
    "Aracagi", "Arara", "Araruna", "Areia", "Areia de Baraunas",
    "Areial", "Aroeiras", "Assuncao", "Baia da Traicao", "Bananeiras",
    "Barauna", "Barra de Santana", "Barra de Santa Rosa", "Barra de Sao Miguel",
    "Bayeux", "Belem", "Belem do Brejo do Cruz", "Bernardino Batista",
    "Boa Ventura", "Boa Vista", "Bom Jesus", "Bom Sucesso", "Bonito de Santa Fe",
    "Boqueirao", "Borborema", "Brejo do Cruz", "Brejo dos Santos", "Caapora",
    "Cabaceiras", "Cabedelo", "Cachoeira dos Indios", "Cacimba de Areia",
    "Cacimba de Dentro", "Cacimbas", "Caico", "Cajazeiras", "Cajazeirinhas",
    "Caldas Brandao", "Camalau", "Campina Grande", "Capim", "Caraubas",
    "Carrapateiras", "Casserengue", "Catingueira", "Catole do Rocha",
    "Caturite", "Conceicao", "Condado", "Conde", "Congo", "Coremas",
    "Coxixola", "Cruz do Espirito Santo", "Cubati", "Cuie", "Cuitegi",
    "Cuie de Mamanguape", "Curral de Cima", "Curral Velho", "Damiao",
    "Desterro", "Diamante", "Dona Ines", "Duas Estradas", "Emas", "Esperanca",
    "Fagundes", "Frei Martinho", "Gado Bravo", "Guarabira", "Gurinhem",
    "Gurjao", "Ibiara", "Igaracy", "Imaculada", "Inga", "Itabaiana", "Itaporanga",
    "Itapororoca", "Itatuba", "Jacarau", "Jerico", "Joao Pessoa", "Juarez Tavora",
    "Juazeirinho", "Junco do Serido", "Juripiranga", "Juru", "Lagoa", "Lagoa de Dentro",
    "Lagoa Seca", "Lastro", "Livramento", "Logradouro", "Lucena", "Mae d Agua",
    "Malta", "Mamanguape", "Manaira", "Marcacao", "Mari", "Marizopolis",
    "Massaranduba", "Mataraca", "Matinhas", "Mato Grosso", "Matureia",
    "Mogeiro", "Montadas", "Monte Horebe", "Monteiro", "Mulungu", "Natuba",
    "Nazarezinho", "Nova Floresta", "Nova Olinda", "Nova Palmeira",
    "Olho d Agua", "Olivedos", "Ouro Velho", "Parari", "Passagem",
    "Patos", "Paulista", "Pedra Branca", "Pedra Lavrada", "Pedras de Fogo",
    "Pedro Regis", "Pianco", "Picui", "Pilar", "Piloes", "Piloenzinhos",
    "Pirpirituba", "Pitimbu", "Pocinhos", "Poco Dantas", "Poco de Jose de Moura",
    "Pombal", "Prata", "Princesa Isabel", "Puxinana", "Queimadas",
    "Quixaba", "Remigio", "Riachao", "Riachao do Bacamarte", "Riachao do Poco",
    "Riacho de Santo Antonio", "Riacho dos Cavalos", "Rio Tinto", "Salgadinho",
    "Salgado de Sao Felix", "Santa Rita", "Santa Cecilia", "Santa Cruz", "Santa Helena",
    "Santa Ines", "Santa Luzia", "Santa Teresinha", "Santana de Mangueira",
    "Santana dos Garrotes", "Santarem", "Santo Andre", "Sao Bentinho",
    "Sao Bento", "Sao Domingos de Pombal", "Sao Domingos do Cariri",
    "Sao Francisco", "Sao Joao do Cariri", "Sao Joao do Rio do Peixe",
    "Sao Joao do Tigre", "Sao Jose da Lagoa Tapada", "Sao Jose de Caiana",
    "Sao Jose de Espinharas", "Sao Jose de Piranhas", "Sao Jose de Princesa",
    "Sao Jose do Bonfim", "Sao Jose do Brejo do Cruz", "Sao Jose do Sabugi",
    "Sao Jose dos Cordeiros", "Sao Jose dos Ramos", "Sao Mamede",
    "Sao Miguel de Taipu", "Sao Sebastiao de Lagoa de Roca",
    "Sao Sebastiao do Umbuzeiro", "Sape", "Serra Branca", "Serra da Raiz",
    "Serra Grande", "Serra Redonda", "Serraria", "Sertaozinho", "Sobrado",
    "Solanea", "Soledade", "Sossego", "Sousa", "Sume", "Taperoa",
    "Tavares", "Teixeira", "Tenorio", "Triunfo", "Uirauna", "Umbuzeiro",
    "Vieiropolis", "Vista Serrana", "Zabele"
]

essenciais = ["CAGEPA", "CLARO", "TIM", "VIVO", "ENERGISA", "ANE"]

# FUNÇÕES UTILITÁRIAS
def limpar_espacos(texto):
    """Remove espaços extras e normaliza o texto."""
    texto = texto.strip()
    texto = re.sub(r'\s+', ' ', texto)
    return texto

def gerar_nome_arquivo(numero, cidade, data, quantidade):
    """Gera o nome do arquivo seguindo o padrão definido."""
    data_formatada = data.strftime('%d-%m')
    cidade_limpa = limpar_espacos(cidade).upper()
    numero_limpo = numero.strip()
    quantidade_limpa = quantidade.strip()
    
    if quantidade_limpa:
        nome_arquivo = f"PES {numero_limpo} {cidade_limpa} {data_formatada} ({quantidade_limpa})"
    else:
        nome_arquivo = f"PES {numero_limpo} {cidade_limpa} {data_formatada}"
    
    return nome_arquivo

def parse_data(data_str):
    """Converte string de data para objeto datetime."""
    if len(data_str) == 4 and data_str.isdigit():
        data_str = data_str[:2] + "-" + data_str[2:]
    
    try:
        data = datetime.strptime(data_str + "-2025", "%d-%m-%Y")
        return data
    except ValueError:
        return None

def calcular_quantidade_ajustada(quantidade_original, num_essenciais):
    """Calcula a quantidade ajustada subtraindo o número de essenciais selecionados."""
    try:
        quantidade_num = int(quantidade_original)
        quantidade_ajustada = quantidade_num - num_essenciais
        return max(0, quantidade_ajustada)  # Não permite valores negativos
    except ValueError:
        return quantidade_original  # Retorna o valor original se não for um número

#FUNÇÕES PARA GERENCIAMENTO DE ESSENCIAIS
def obter_essenciais_selecionados():
    """Retorna lista de essenciais selecionados."""
    selecionados = []
    for var, nome in zip(essenciais_vars, essenciais):
        if var.get():
            selecionados.append(nome)
    return selecionados

def toggle_essencial(nome):
    """Alterna o estado de seleção de um essencial."""
    index = essenciais.index(nome)
    essenciais_vars[index].set(not essenciais_vars[index].get())
    atualizar_display_essenciais()

def atualizar_display_essenciais():
    """Atualiza o display dos essenciais selecionados."""
    selecionados = obter_essenciais_selecionados()
    
    if selecionados:
        texto = ", ".join(selecionados)
        if len(texto) > 30:
            texto = texto[:27] + "..."
        label_essenciais_display.config(text=f"{texto} ({len(selecionados)} selecionados)", fg="#1976D2")
    else:
        label_essenciais_display.config(text="Nenhum selecionado", fg="#757575")
    
    # Atualizar preview da quantidade ajustada
    atualizar_preview_quantidade()

def atualizar_preview_quantidade():
    """Atualiza o preview da quantidade que será usada após os ajustes."""
    quantidade_str = entry_quantidade.get().strip()
    if not quantidade_str:
        label_quantidade_preview.config(text="")
        return
    
    try:
        quantidade_original = int(quantidade_str)
        num_essenciais = len(obter_essenciais_selecionados())
        
        if num_essenciais > 0:
            quantidade_ajustada = max(0, quantidade_original - num_essenciais)
            if quantidade_ajustada != quantidade_original:
                label_quantidade_preview.config(
                    text=f"(Quantidade ajustada: {quantidade_ajustada})",
                    fg="#FF9800"
                )
            else:
                label_quantidade_preview.config(text="", fg="#757575")
        else:
            label_quantidade_preview.config(text="", fg="#757575")
    except ValueError:
        label_quantidade_preview.config(text="", fg="#757575")

def mostrar_selecao_essenciais():
    """Mostra popup para seleção de essenciais."""
    # Criar janela popup
    popup = tk.Toplevel(root)
    popup.title("Selecionar Essenciais")
    popup.geometry("320x400")
    popup.resizable(False, False)
    popup.configure(bg='#ffffff')
    popup.transient(root)
    popup.grab_set()
    
    # Título
    titulo_popup = tk.Label(popup, text="Selecione os Essenciais:", 
                           font=("Segoe UI", 12, "bold"), bg='#ffffff', fg='#1976D2')
    titulo_popup.pack(pady=(15, 10))
    
    #Aviso sobre subtração
    aviso_popup = tk.Label(popup, text="⚠️ Cada essencial selecionado reduzirá\na quantidade total em 1 unidade", 
                          font=("Segoe UI", 9), bg='#ffffff', fg='#FF5722',
                          justify='center')
    aviso_popup.pack(pady=(0, 15))
    
    # Frame principal com scrollbar (caso necessário)
    main_popup_frame = tk.Frame(popup, bg='#ffffff')
    main_popup_frame.pack(fill='both', expand=True, padx=20, pady=(0, 15))
    
    # Frame para checkboxes
    frame_checks = tk.Frame(main_popup_frame, bg='#ffffff')
    frame_checks.pack(fill='x', pady=(0, 20))
    
    # Criar checkboxes
    for i, (var, nome) in enumerate(zip(essenciais_vars, essenciais)):
        cb = tk.Checkbutton(frame_checks, text=nome, variable=var,
                           font=("Segoe UI", 11), bg='#ffffff', fg='#424242',
                           activebackground='#ffffff', activeforeground='#1976D2')
        cb.pack(anchor='w', pady=4, padx=5)
    
    # Frame para botões na parte inferior
    frame_botoes_popup = tk.Frame(main_popup_frame, bg='#ffffff')
    frame_botoes_popup.pack(side='bottom', fill='x')
    
    # Centralizar os botões
    buttons_container = tk.Frame(frame_botoes_popup, bg='#ffffff')
    buttons_container.pack()
    
    btn_ok = tk.Button(buttons_container, text="OK", font=("Segoe UI", 11, "bold"),
                       command=lambda: [atualizar_display_essenciais(), popup.destroy()],
                       relief='flat', bd=0, bg='#4CAF50', fg='white',
                       cursor='hand2', padx=25, pady=8)
    btn_ok.pack(side="left", padx=8)
    
    btn_cancelar = tk.Button(buttons_container, text="Cancelar", font=("Segoe UI", 11, "bold"),
                            command=popup.destroy,
                            relief='flat', bd=0, bg='#757575', fg='white',
                            cursor='hand2', padx=25, pady=8)
    btn_cancelar.pack(side="left", padx=8)
    
    # Centralizar popup
    popup.update_idletasks()
    x = (popup.winfo_screenwidth() // 2) - (popup.winfo_width() // 2)
    y = (popup.winfo_screenheight() // 2) - (popup.winfo_height() // 2)
    popup.geometry(f"+{x}+{y}")
    
    # Garantir que a janela seja atualizada
    popup.update()

#FUNÇÕES PRINCIPAIS DA APLICAÇÃO
def gerar():
    """Função principal que gera o PES."""
    numero = entry_numero.get()
    cidade = entry_cidade.get()
    data_str = entry_data.get()
    quantidade_str = entry_quantidade.get()
    selecionados = obter_essenciais_selecionados()

    # Validação dos campos obrigatórios
    if not all([numero, cidade, data_str, quantidade_str]):
        messagebox.showwarning("Atenção", "Por favor, preencha todos os campos!")
        return

    # Validação da data
    data = parse_data(data_str)
    if not data:
        messagebox.showerror("Erro", "Data no formato errado! Use DD-MM ou DDMM")
        return

    # Calcular quantidade ajustada
    num_essenciais = len(selecionados)
    quantidade_ajustada = calcular_quantidade_ajustada(quantidade_str, num_essenciais)
    
    # Verificar se a quantidade ficou negativa ou zero
    try:
        if int(quantidade_str) < num_essenciais:
            messagebox.showwarning("Atenção", 
                f"A quantidade original ({quantidade_str}) é menor que o número de essenciais selecionados ({num_essenciais}).\n"
                f"A quantidade será ajustada para {quantidade_ajustada}.")
    except ValueError:
        pass  # Se não for um número, mantém o comportamento original

    # Gerar nomes dos arquivos
    nome_original = gerar_nome_arquivo(numero, cidade, data, str(quantidade_ajustada))
    nome_sem_quantidade = gerar_nome_arquivo(numero, cidade, data, "")

    # Montar texto final
    if not selecionados:
        texto_final = nome_original
    else:
        texto_final = nome_original
        for essencial in selecionados:
            texto_final += f" \n\t{essencial} {nome_sem_quantidade}"

    # Copiar para área de transferência e exibir resultado
    pyperclip.copy(texto_final)
    label_resultado.config(text=texto_final, fg="#2E7D32")
    
    # Mensagem de status mais informativa
    if num_essenciais > 0:
        status_msg = f"✓ Copiado! Quantidade ajustada: {quantidade_str} → {quantidade_ajustada}"
    else:
        status_msg = "✓ Copiado para área de transferência!"
    
    label_status.config(text=status_msg, fg="#2E7D32")
    root.after(4000, lambda: label_status.config(text=""))

def apagar():
    """Limpa todos os campos do formulário."""
    entry_numero.delete(0, tk.END)
    entry_cidade.delete(0, tk.END)
    entry_data.delete(0, tk.END)
    entry_quantidade.delete(0, tk.END)
    
    # Desmarcar todos os essenciais
    for var in essenciais_vars:
        var.set(False)
    atualizar_display_essenciais()
    
    label_resultado.config(text="")
    label_status.config(text="")
    label_quantidade_preview.config(text="")
    entry_numero.focus()


#FUNÇÕES DE EVENTOS E INTERAÇÃO
def foco_proximo(event, proximo_widget):
    """Move o foco para o próximo widget."""
    proximo_widget.focus()
    return "break"

def on_enter_button(button, hover_color):
    """Efeito hover para botões."""
    button.config(bg=hover_color)

def on_leave_button(button, original_color):
    """Remove efeito hover dos botões."""
    button.config(bg=original_color)

def completar_cidade(event):
    """Autocompletar cidade baseado na lista de cidades da Paraíba."""
    texto_atual = entry_cidade.get().lower()
    if not texto_atual:
        return "break"
    
    correspondencias = [cidade for cidade in cidades_paraiba 
                       if cidade.lower().startswith(texto_atual)]
    
    if correspondencias:
        entry_cidade.delete(0, tk.END)
        entry_cidade.insert(0, correspondencias[0])
        entry_cidade.select_range(len(texto_atual), tk.END)
    
    return "break"

def abrir_link(event):
    """Abre o link do LinkedIn."""
    webbrowser.open_new("https://www.linkedin.com/in/gabriel-montenegro7/")

def on_quantidade_change(event=None):
    """Atualiza o preview quando a quantidade muda."""
    atualizar_preview_quantidade()

# =============================================================================
# CONFIGURAÇÃO DA INTERFACE GRÁFICA
# =============================================================================

def configurar_interface():
    """Configura toda a interface gráfica da aplicação."""
    global root, entry_numero, entry_cidade, entry_data, entry_quantidade
    global label_essenciais_display, label_resultado, label_status
    global label_quantidade_preview, essenciais_vars

    # Configuração da janela principal
    root = tk.Tk()
    root.title("Gerador de PES")
    root.geometry("500x800")
    root.minsize(480, 750)
    root.configure(bg='#f5f5f5')
    root.eval('tk::PlaceWindow . center')

    # Variáveis para controlar os essenciais selecionados
    essenciais_vars = [tk.BooleanVar() for _ in essenciais]

    # Configuração de fontes
    fonte_titulo = font.Font(family="Segoe UI", size=18, weight="bold")
    fonte_label = font.Font(family="Segoe UI", size=11)
    fonte_entry = font.Font(family="Segoe UI", size=11)
    fonte_botao = font.Font(family="Segoe UI", size=11, weight="bold")
    fonte_resultado = font.Font(family="Segoe UI", size=10, weight="bold")
    fonte_status = font.Font(family="Segoe UI", size=9)

    # Frame principal
    main_frame = tk.Frame(root, bg='#ffffff', relief='raised', bd=1)
    main_frame.pack(expand=True, fill='both', padx=30, pady=30)
    main_frame.grid_rowconfigure(11, weight=1)
    
    for i in range(2):
        main_frame.grid_columnconfigure(i, weight=1)

    # Título
    titulo = tk.Label(main_frame, text="📁 GERADOR DE PES", font=fonte_titulo, 
                     bg='#ffffff', fg='#1976D2')
    titulo.grid(row=0, column=0, columnspan=2, pady=(20, 30), sticky='n')

    # Separador
    separator = tk.Frame(main_frame, height=2, bg='#e0e0e0')
    separator.grid(row=1, column=0, columnspan=2, sticky='ew', padx=20, pady=(0, 20))

    padxy = {"padx": 20, "pady": 8}

    # Campo Número
    tk.Label(main_frame, text="PES:", font=fonte_label, bg='#ffffff', 
            fg='#424242').grid(row=2, column=0, sticky="w", **padxy)
    entry_numero = tk.Entry(main_frame, font=fonte_entry, relief='solid', bd=1, 
                           highlightthickness=2, highlightcolor='#1976D2')
    entry_numero.grid(row=2, column=1, sticky="ew", **padxy)
    entry_numero.bind("<Return>", lambda e: foco_proximo(e, entry_cidade))

    # Campo Cidade
    tk.Label(main_frame, text="Cidade:", font=fonte_label, bg='#ffffff', 
            fg='#424242').grid(row=3, column=0, sticky="w", **padxy)
    entry_cidade = tk.Entry(main_frame, font=fonte_entry, relief='solid', bd=1, 
                           highlightthickness=2, highlightcolor='#1976D2')
    entry_cidade.grid(row=3, column=1, sticky="ew", **padxy)
    entry_cidade.bind("<Return>", lambda e: foco_proximo(e, entry_data))
    entry_cidade.bind("<Tab>", completar_cidade)

    # Campo Data
    tk.Label(main_frame, text="Data:", font=fonte_label, bg='#ffffff', 
            fg='#424242').grid(row=4, column=0, sticky="w", **padxy)
    entry_data = tk.Entry(main_frame, font=fonte_entry, relief='solid', bd=1, 
                         highlightthickness=2, highlightcolor='#1976D2')
    entry_data.grid(row=4, column=1, sticky="ew", **padxy)
    entry_data.bind("<Return>", lambda e: foco_proximo(e, entry_quantidade))

    # Campo Quantidade
    tk.Label(main_frame, text="Quantidade:", font=fonte_label, bg='#ffffff', 
            fg='#424242').grid(row=5, column=0, sticky="w", **padxy)
    
    frame_quantidade = tk.Frame(main_frame, bg='#ffffff')
    frame_quantidade.grid(row=5, column=1, sticky="ew", **padxy)
    frame_quantidade.grid_columnconfigure(0, weight=1)
    
    entry_quantidade = tk.Entry(frame_quantidade, font=fonte_entry, relief='solid', bd=1, 
                               highlightthickness=2, highlightcolor='#1976D2')
    entry_quantidade.grid(row=0, column=0, sticky="ew")
    entry_quantidade.bind("<Return>", lambda e: gerar())
    entry_quantidade.bind("<KeyRelease>", on_quantidade_change)
    
    # Label para mostrar a quantidade ajustada
    label_quantidade_preview = tk.Label(frame_quantidade, text="", 
                                       font=("Segoe UI", 9), bg='#ffffff', fg='#FF9800')
    label_quantidade_preview.grid(row=1, column=0, sticky="w", pady=(2, 0))

    # Seção de Essenciais
    tk.Label(main_frame, text="Essenciais:", font=fonte_label, bg='#ffffff', 
            fg='#424242').grid(row=6, column=0, sticky="w", **padxy)

    frame_essenciais = tk.Frame(main_frame, bg='#ffffff')
    frame_essenciais.grid(row=6, column=1, sticky="ew", **padxy)
    frame_essenciais.grid_columnconfigure(0, weight=1)

    btn_selecionar = tk.Button(frame_essenciais, text="🔧 Selecionar", 
                              font=("Segoe UI", 11, "bold"),
                              command=mostrar_selecao_essenciais, relief='flat', bd=1,
                              bg='#E3F2FD', fg='#1976D2', cursor='hand2', 
                              padx=20, pady=10)
    btn_selecionar.grid(row=0, column=1, sticky="e")

    label_essenciais_display = tk.Label(frame_essenciais, text="Nenhum selecionado", 
                                       font=("Segoe UI", 10), bg='#ffffff', fg='#757575',
                                       anchor='w')
    label_essenciais_display.grid(row=0, column=0, sticky="ew", padx=(0, 10))

    # Botões principais
    frame_botoes = tk.Frame(main_frame, bg='#ffffff')
    frame_botoes.grid(row=7, column=0, columnspan=2, pady=25)

    btn_gerar = tk.Button(frame_botoes, text="🚀 Gerar PES", font=fonte_botao,
                          command=gerar, relief='flat', bd=0, bg='#4CAF50', fg='white',
                          cursor='hand2', padx=25, pady=10)
    btn_gerar.pack(side="left", padx=(0, 15))
    btn_gerar.bind("<Enter>", lambda e: on_enter_button(btn_gerar, '#45A049'))
    btn_gerar.bind("<Leave>", lambda e: on_leave_button(btn_gerar, '#4CAF50'))
    btn_gerar.bind("<Return>", lambda e: gerar())

    btn_apagar = tk.Button(frame_botoes, text="🗑️ Limpar", font=fonte_botao,
                           command=apagar, relief='flat', bd=0, bg='#FF5722', fg='white',
                           cursor='hand2', padx=25, pady=10)
    btn_apagar.pack(side="left")
    btn_apagar.bind("<Enter>", lambda e: on_enter_button(btn_apagar, '#E64A19'))
    btn_apagar.bind("<Leave>", lambda e: on_leave_button(btn_apagar, '#FF5722'))
    btn_apagar.bind("<Return>", lambda e: apagar())

    # Labels de resultado e status
    label_resultado = tk.Label(main_frame, text="", font=fonte_resultado, fg="#333333", 
                              bg='#ffffff', wraplength=420, justify='left')
    label_resultado.grid(row=8, column=0, columnspan=2, sticky="n", 
                        padx=20, pady=(0, 5))

    label_status = tk.Label(main_frame, text="", font=fonte_status, fg="#4CAF50", 
                           bg='#ffffff')
    label_status.grid(row=9, column=0, columnspan=2, sticky="n", 
                     padx=20, pady=(10, 10))

    # Rodapé
    rodape_frame = tk.Frame(main_frame, bg='#ffffff')
    rodape_frame.grid(row=12, column=0, columnspan=2, pady=(10, 20))

    rodape_texto = tk.Label(rodape_frame, text="Desenvolvido por:", bg='#ffffff', 
                           fg='#555555', font=("Segoe UI", 9))
    rodape_texto.pack(side="left")

    rodape_link = tk.Label(rodape_frame, text="Gabriel Montenegro", bg='#ffffff', 
                          fg="blue", cursor="hand2",
                          font=("Segoe UI", 9, "underline"))
    rodape_link.pack(side="left")
    rodape_link.bind("<Button-1>", abrir_link)

    # Foco inicial
    entry_numero.focus()

# =============================================================================
# EXECUÇÃO PRINCIPAL
# =============================================================================

def main():
    """Função principal da aplicação."""
    configurar_interface()
    root.mainloop()

if __name__ == "__main__":
    main()