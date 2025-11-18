import tkinter as tk
from tkinter import messagebox, font, ttk
from datetime import datetime
import pyperclip
import re
import webbrowser

# CONSTANTES DE CORES 
CORES_ESCURO = {
    'bg_principal': '#000000',           # Preto puro
    'bg_secundario': '#0a0a0a',          # Preto profundo
    'bg_card': '#1c1c1e',                # Card escuro premium
    'bg_input': '#2c2c2e',               # Input escuro suave
    'bg_input_hover': '#3a3a3c',         # Input hover
    'vermelho_primario': '#ff3b30',      # Vermelho 
    'vermelho_hover': '#ff453a',         # Vermelho hover mais claro
    'vermelho_claro': '#ff6961',         # Vermelho claro suave
    'vermelho_suave': '#3a1a1a',         # Vermelho muito escuro
    'texto_principal': '#ffffff',        # Branco puro
    'texto_secundario': '#98989d',       # Cinza
    'texto_destaque': '#f5f5f7',         # Branco suave
    'borda': '#38383a',                  # Borda escura sutil
    'borda_ativa': '#ff3b30',            # Borda vermelha
    'sucesso': '#30d158',                # Verde 
    'aviso': '#ff9f0a',                  # Laranja 
    'accent': '#8e2a2a',                 # Vermelho escuro accent
    'sombra': '#00000040',               # Sombra suave
}

# CONSTANTES DE CORES - TEMA CLARO 
CORES_CLARO = {
    'bg_principal': '#f0f0f0',           # Cinza claro de fundo
    'bg_secundario': '#ffffff',          # Branco puro
    'bg_card': '#ffffff',                # Card branco
    'bg_input': '#ffffff',               # Input branco com borda
    'bg_input_hover': '#f8f8f8',         # Input hover
    'vermelho_primario': '#ff5722',      # Laranja/vermelho dos botões
    'vermelho_hover': '#e64a19',         # Laranja hover mais escuro
    'vermelho_claro': '#ff6961',         # Vermelho claro
    'vermelho_suave': '#e3f2fd',         # Azul claro para botão selecionar
    'texto_principal': '#000000',        # Preto para texto
    'texto_secundario': '#666666',       # Cinza para labels
    'texto_destaque': '#000000',         # Preto puro
    'borda': '#cccccc',                  # Borda cinza clara
    'borda_ativa': '#0078d7',            # Borda azul ao focar
    'sucesso': '#4caf50',                # Verde para sucesso
    'aviso': '#ff9800',                  # Laranja para avisos
    'accent': '#0078d7',                 # Azul para acentos
    'btn_selecionar_bg': '#e3f2fd',      # Fundo azul claro botão selecionar
    'btn_selecionar_fg': '#0078d7',      # Texto azul botão selecionar
    'btn_gerar_bg': '#4caf50',           # Verde para botão gerar
    'btn_gerar_hover': '#45a049',        # Verde hover
    'sombra': '#00000015',               # Sombra suave
}

# Tema atual (começa no escuro)
CORES = CORES_ESCURO.copy()
tema_escuro = True

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
    data_formatada = data.strftime('%d/%m')
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
    # Remove barras para processar
    data_limpa = data_str.replace("/", "").replace("-", "")
    
    if len(data_limpa) == 4 and data_limpa.isdigit():
        data_str = data_limpa[:2] + "-" + data_limpa[2:]
    
    try:
        data = datetime.strptime(data_str + "-2025", "%d-%m-%Y")
        return data
    except ValueError:
        return None

def formatar_data_entrada(event=None):
    """Formata automaticamente a data com barra enquanto digita."""
    texto = entry_data.get().replace("/", "").replace("-", "")
    
    # Remove qualquer caractere não numérico
    texto = ''.join(filter(str.isdigit, texto))
    
    # Limita a 4 dígitos
    if len(texto) > 4:
        texto = texto[:4]
    
    # Formata com barra
    if len(texto) >= 3:
        texto_formatado = texto[:2] + "/" + texto[2:]
    else:
        texto_formatado = texto
    
    # Atualiza o campo
    entry_data.delete(0, tk.END)
    entry_data.insert(0, texto_formatado)
    
    # Move cursor para o final
    entry_data.icursor(tk.END)

def calcular_quantidade_ajustada(quantidade_original, num_essenciais):
    """Calcula a quantidade ajustada subtraindo o número de essenciais selecionados."""
    try:
        quantidade_num = int(quantidade_original)
        quantidade_ajustada = quantidade_num - num_essenciais
        return max(0, quantidade_ajustada)
    except ValueError:
        return quantidade_original

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
        label_essenciais_display.config(text=f"{texto} ({len(selecionados)} selecionados)", 
                                       fg=CORES['vermelho_primario'])
    else:
        label_essenciais_display.config(text="Nenhum selecionado", fg=CORES['texto_secundario'])
    
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
                    fg=CORES['aviso']
                )
            else:
                label_quantidade_preview.config(text="", fg=CORES['texto_secundario'])
        else:
            label_quantidade_preview.config(text="", fg=CORES['texto_secundario'])
    except ValueError:
        label_quantidade_preview.config(text="", fg=CORES['texto_secundario'])

def mostrar_selecao_essenciais():
    """Mostra popup para seleção de essenciais."""
    popup = tk.Toplevel(root)
    popup.title("Selecionar Essenciais")
    popup.geometry("340x420")
    popup.resizable(False, False)
    popup.configure(bg=CORES['bg_card'])
    popup.transient(root)
    popup.grab_set()
    
    # Título
    titulo_popup = tk.Label(popup, text="⚡ Selecione os Essenciais", 
                           font=("Segoe UI", 13, "bold"), bg=CORES['bg_card'], 
                           fg=CORES['vermelho_primario'])
    titulo_popup.pack(pady=(20, 10))
    
    # Separador
    sep = tk.Frame(popup, height=2, bg=CORES['vermelho_suave'])
    sep.pack(fill='x', padx=30, pady=(0, 15))
    
    # Aviso
    aviso_popup = tk.Label(popup, text="⚠️ Cada essencial reduzirá a quantidade em 1", 
                          font=("Segoe UI", 9), bg=CORES['bg_card'], fg=CORES['aviso'],
                          justify='center')
    aviso_popup.pack(pady=(0, 15))
    
    # Frame principal
    main_popup_frame = tk.Frame(popup, bg=CORES['bg_card'])
    main_popup_frame.pack(fill='both', expand=True, padx=25, pady=(0, 20))
    
    # Frame para checkboxes
    frame_checks = tk.Frame(main_popup_frame, bg=CORES['bg_card'])
    frame_checks.pack(fill='x', pady=(0, 20))
    
    # Criar checkboxes estilizados
    for i, (var, nome) in enumerate(zip(essenciais_vars, essenciais)):
        cb = tk.Checkbutton(frame_checks, text=nome, variable=var,
                           font=("Segoe UI", 11), bg=CORES['bg_card'], 
                           fg=CORES['texto_principal'],
                           activebackground=CORES['bg_card'], 
                           activeforeground=CORES['vermelho_claro'],
                           selectcolor=CORES['bg_secundario'],
                           highlightthickness=0)
        cb.pack(anchor='w', pady=5, padx=5)
    
    # Frame para botões
    frame_botoes_popup = tk.Frame(main_popup_frame, bg=CORES['bg_card'])
    frame_botoes_popup.pack(side='bottom', fill='x', pady=(10, 0))
    
    buttons_container = tk.Frame(frame_botoes_popup, bg=CORES['bg_card'])
    buttons_container.pack()
    
    btn_ok = tk.Button(buttons_container, text="✓ Confirmar", 
                       font=("Segoe UI", 11, "bold"),
                       command=lambda: [atualizar_display_essenciais(), popup.destroy()],
                       relief='flat', bd=0, bg=CORES['vermelho_primario'], 
                       fg='white', cursor='hand2', padx=30, pady=12)
    btn_ok.pack(side="left", padx=5)
    btn_ok.bind("<Enter>", lambda e: btn_ok.config(bg=CORES['vermelho_hover']))
    btn_ok.bind("<Leave>", lambda e: btn_ok.config(bg=CORES['vermelho_primario']))
    
    btn_cancelar = tk.Button(buttons_container, text="✕ Cancelar", 
                            font=("Segoe UI", 11, "bold"),
                            command=popup.destroy,
                            relief='flat', bd=0, bg=CORES['bg_secundario'], 
                            fg=CORES['texto_principal'],
                            cursor='hand2', padx=30, pady=12)
    btn_cancelar.pack(side="left", padx=5)
    btn_cancelar.bind("<Enter>", lambda e: btn_cancelar.config(bg=CORES['borda']))
    btn_cancelar.bind("<Leave>", lambda e: btn_cancelar.config(bg=CORES['bg_secundario']))
    
    # Centralizar popup
    popup.update_idletasks()
    x = (popup.winfo_screenwidth() // 2) - (popup.winfo_width() // 2)
    y = (popup.winfo_screenheight() // 2) - (popup.winfo_height() // 2)
    popup.geometry(f"+{x}+{y}")

#FUNÇÕES PRINCIPAIS DA APLICAÇÃO
def gerar():
    """Função principal que gera o PES."""
    numero = entry_numero.get()
    cidade = entry_cidade.get()
    data_str = entry_data.get()
    quantidade_str = entry_quantidade.get()
    selecionados = obter_essenciais_selecionados()

    if not all([numero, cidade, data_str, quantidade_str]):
        messagebox.showwarning("Atenção", "Por favor, preencha todos os campos!")
        return

    data = parse_data(data_str)
    if not data:
        messagebox.showerror("Erro", "Data no formato errado! Use DD/MM ou DDMM")
        return

    num_essenciais = len(selecionados)
    quantidade_ajustada = calcular_quantidade_ajustada(quantidade_str, num_essenciais)
    
    try:
        if int(quantidade_str) < num_essenciais:
            messagebox.showwarning("Atenção", 
                f"A quantidade original ({quantidade_str}) é menor que o número de essenciais selecionados ({num_essenciais}).\n"
                f"A quantidade será ajustada para {quantidade_ajustada}.")
    except ValueError:
        pass

    nome_original = gerar_nome_arquivo(numero, cidade, data, str(quantidade_ajustada))
    nome_sem_quantidade = gerar_nome_arquivo(numero, cidade, data, "")

    if not selecionados:
        texto_final = nome_original
    else:
        texto_final = nome_original
        for essencial in selecionados:
            texto_final += f" \n\t{essencial} {nome_sem_quantidade}"

    pyperclip.copy(texto_final)
    label_resultado.config(text=texto_final, fg=CORES['vermelho_claro'])
    
    if num_essenciais > 0:
        status_msg = f"✓ Copiado! Quantidade ajustada: {quantidade_str} → {quantidade_ajustada}"
    else:
        status_msg = "✓ Copiado para área de transferência!"
    
    label_status.config(text=status_msg, fg=CORES['sucesso'])
    root.after(4000, lambda: label_status.config(text=""))

def apagar():
    """Limpa todos os campos do formulário."""
    entry_numero.delete(0, tk.END)
    entry_cidade.delete(0, tk.END)
    entry_data.delete(0, tk.END)
    entry_quantidade.delete(0, tk.END)
    
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

def alternar_tema():
    """Alterna entre tema escuro e claro."""
    global CORES, tema_escuro
    
    tema_escuro = not tema_escuro
    CORES = CORES_ESCURO.copy() if tema_escuro else CORES_CLARO.copy()
    
    # Atualizar o emoji do botão
    btn_tema.config(text="☀️" if tema_escuro else "🌙", 
                   bg=CORES['bg_card'], 
                   fg=CORES['texto_secundario'])
    
    # Atualizar cores de todos os elementos
    root.configure(bg=CORES['bg_principal'])
    main_frame.configure(bg=CORES['bg_card'])
    
    # Cabeçalho
    titulo_frame.configure(bg=CORES['bg_card'])
    titulo.configure(bg=CORES['bg_card'], fg=CORES['vermelho_primario'])
    subtitulo.configure(bg=CORES['bg_card'], fg=CORES['texto_secundario'])
    
    # Separador
    separator.configure(bg=CORES['borda'])
    
    # Labels
    for label in labels_list:
        label.configure(bg=CORES['bg_card'], fg=CORES['texto_secundario'])
    
    # Entries com efeito de hover
    for entry in entries_list:
        entry.configure(bg=CORES['bg_input'], fg=CORES['texto_principal'],
                       insertbackground=CORES['vermelho_primario'],
                       highlightbackground=CORES['borda'],
                       highlightcolor=CORES['borda_ativa'])
    
    # Frames
    frame_quantidade.configure(bg=CORES['bg_card'])
    frame_essenciais.configure(bg=CORES['bg_card'])
    frame_botoes.configure(bg=CORES['bg_card'])
    frame_resultado.configure(bg=CORES['bg_secundario'])
    rodape_frame.configure(bg=CORES['bg_card'])
    
    # Labels especiais
    label_quantidade_preview.configure(bg=CORES['bg_card'], fg=CORES['aviso'])
    label_essenciais_display.configure(bg=CORES['bg_card'])
    label_resultado.configure(bg=CORES['bg_secundario'], fg=CORES['vermelho_claro'])
    label_status.configure(bg=CORES['bg_card'])
    
    # Botões
    btn_selecionar.configure(bg=CORES['vermelho_suave'], fg=CORES['vermelho_primario'])
    btn_gerar.configure(bg=CORES['vermelho_primario'])
    btn_apagar.configure(bg=CORES['bg_input'], fg=CORES['texto_principal'])
    
    # Rodapé
    linha_rodape.configure(bg=CORES['borda'])
    rodape_texto.configure(bg=CORES['bg_card'], fg=CORES['texto_secundario'])
    rodape_link.configure(bg=CORES['bg_card'], fg=CORES['vermelho_primario'])
    
    # Atualizar display de essenciais
    atualizar_display_essenciais()

# =============================================================================
# CONFIGURAÇÃO DA INTERFACE GRÁFICA
# =============================================================================

def configurar_interface():
    """Configura toda a interface gráfica da aplicação."""
    global root, entry_numero, entry_cidade, entry_data, entry_quantidade
    global label_essenciais_display, label_resultado, label_status
    global label_quantidade_preview, essenciais_vars
    global main_frame, titulo_frame, titulo, subtitulo, separator
    global frame_quantidade, frame_essenciais, frame_botoes, frame_resultado, rodape_frame
    global btn_selecionar, btn_gerar, btn_apagar, btn_tema
    global labels_list, entries_list, linha_rodape, rodape_texto, rodape_link

    root = tk.Tk()
    root.title("Gerador de PES")
    root.geometry("520x850")
    root.minsize(500, 800)
    root.configure(bg=CORES['bg_principal'])
    root.eval('tk::PlaceWindow . center')

    essenciais_vars = [tk.BooleanVar() for _ in essenciais]

    # Fontes
    fonte_titulo = font.Font(family="Segoe UI", size=20, weight="bold")
    fonte_label = font.Font(family="Segoe UI", size=11)
    fonte_entry = font.Font(family="Segoe UI", size=11)
    fonte_botao = font.Font(family="Segoe UI", size=12, weight="bold")
    fonte_resultado = font.Font(family="Segoe UI", size=10, weight="bold")

    # Frame principal
    main_frame = tk.Frame(root, bg=CORES['bg_card'], relief='flat', bd=0)
    main_frame.pack(expand=True, fill='both', padx=25, pady=25)
    main_frame.grid_rowconfigure(11, weight=1)
    
    for i in range(2):
        main_frame.grid_columnconfigure(i, weight=1)

    # Título com efeito de borda
    titulo_frame = tk.Frame(main_frame, bg=CORES['bg_card'])
    titulo_frame.grid(row=0, column=0, columnspan=2, pady=(25, 20), sticky='ew')
    
    titulo = tk.Label(titulo_frame, text="🔥 GERADOR DE PES", font=fonte_titulo, 
                     bg=CORES['bg_card'], fg=CORES['vermelho_primario'])
    titulo.pack()
    
    subtitulo = tk.Label(titulo_frame, text="Sistema de Geração Automática", 
                        font=("Segoe UI", 9), bg=CORES['bg_card'], 
                        fg=CORES['texto_secundario'])
    subtitulo.pack(pady=(2, 0))
    
    # Botão de alternar tema (posicionado no canto direito do titulo_frame)
    btn_tema = tk.Button(titulo_frame, text="☀️", font=("Segoe UI", 18),
                        command=alternar_tema, relief='flat', bd=0,
                        bg=CORES['bg_card'], fg=CORES['texto_principal'],
                        cursor='hand2', padx=10, pady=6)
    btn_tema.place(relx=1.0, rely=0.5, anchor="e")

    # Separador vermelho
    separator = tk.Frame(main_frame, height=3, bg=CORES['vermelho_primario'])
    separator.grid(row=1, column=0, columnspan=2, sticky='ew', padx=25, pady=(0, 25))

    padxy = {"padx": 25, "pady": 10}

    # Campo Número
    label_numero = tk.Label(main_frame, text="PES:", font=fonte_label, bg=CORES['bg_card'], 
            fg=CORES['texto_destaque'])
    label_numero.grid(row=2, column=0, sticky="w", **padxy)
    
    entry_numero = tk.Entry(main_frame, font=fonte_entry, relief='flat', bd=0, 
                           bg=CORES['bg_input'], fg=CORES['texto_principal'],
                           insertbackground=CORES['vermelho_primario'],
                           highlightthickness=2, highlightbackground=CORES['borda'],
                           highlightcolor=CORES['vermelho_primario'])
    entry_numero.grid(row=2, column=1, sticky="ew", **padxy)
    entry_numero.bind("<Return>", lambda e: foco_proximo(e, entry_cidade))

    # Campo Cidade
    label_cidade = tk.Label(main_frame, text="Cidade:", font=fonte_label, bg=CORES['bg_card'], 
            fg=CORES['texto_destaque'])
    label_cidade.grid(row=3, column=0, sticky="w", **padxy)
    
    entry_cidade = tk.Entry(main_frame, font=fonte_entry, relief='flat', bd=0, 
                           bg=CORES['bg_input'], fg=CORES['texto_principal'],
                           insertbackground=CORES['vermelho_primario'],
                           highlightthickness=2, highlightbackground=CORES['borda'],
                           highlightcolor=CORES['vermelho_primario'])
    entry_cidade.grid(row=3, column=1, sticky="ew", **padxy)
    entry_cidade.bind("<Return>", lambda e: foco_proximo(e, entry_data))
    entry_cidade.bind("<Tab>", completar_cidade)

    # Campo Data
    label_data = tk.Label(main_frame, text="Data:", font=fonte_label, bg=CORES['bg_card'], 
            fg=CORES['texto_destaque'])
    label_data.grid(row=4, column=0, sticky="w", **padxy)
    
    entry_data = tk.Entry(main_frame, font=fonte_entry, relief='flat', bd=0, 
                         bg=CORES['bg_input'], fg=CORES['texto_principal'],
                         insertbackground=CORES['vermelho_primario'],
                         highlightthickness=2, highlightbackground=CORES['borda'],
                         highlightcolor=CORES['vermelho_primario'])
    entry_data.grid(row=4, column=1, sticky="ew", **padxy)
    entry_data.bind("<Return>", lambda e: foco_proximo(e, entry_quantidade))
    entry_data.bind("<KeyRelease>", formatar_data_entrada)

    # Campo Quantidade
    label_qtd = tk.Label(main_frame, text="Quantidade:", font=fonte_label, bg=CORES['bg_card'], 
            fg=CORES['texto_destaque'])
    label_qtd.grid(row=5, column=0, sticky="w", **padxy)
    
    frame_quantidade = tk.Frame(main_frame, bg=CORES['bg_card'])
    frame_quantidade.grid(row=5, column=1, sticky="ew", **padxy)
    frame_quantidade.grid_columnconfigure(0, weight=1)
    
    entry_quantidade = tk.Entry(frame_quantidade, font=fonte_entry, relief='flat', bd=0, 
                               bg=CORES['bg_input'], fg=CORES['texto_principal'],
                               insertbackground=CORES['vermelho_primario'],
                               highlightthickness=2, highlightbackground=CORES['borda'],
                               highlightcolor=CORES['vermelho_primario'])
    entry_quantidade.grid(row=0, column=0, sticky="ew")
    entry_quantidade.bind("<Return>", lambda e: gerar())
    entry_quantidade.bind("<KeyRelease>", on_quantidade_change)
    
    label_quantidade_preview = tk.Label(frame_quantidade, text="", 
                                       font=("Segoe UI", 9), bg=CORES['bg_card'], 
                                       fg=CORES['aviso'])
    label_quantidade_preview.grid(row=1, column=0, sticky="w", pady=(4, 0))

    # Seção de Essenciais
    label_ess = tk.Label(main_frame, text="Essenciais:", font=fonte_label, bg=CORES['bg_card'], 
            fg=CORES['texto_destaque'])
    label_ess.grid(row=6, column=0, sticky="w", **padxy)

    frame_essenciais = tk.Frame(main_frame, bg=CORES['bg_card'])
    frame_essenciais.grid(row=6, column=1, sticky="ew", **padxy)
    frame_essenciais.grid_columnconfigure(0, weight=1)

    btn_selecionar = tk.Button(frame_essenciais, text="⚡ Selecionar", 
                              font=("Segoe UI", 11, "bold"),
                              command=mostrar_selecao_essenciais, relief='flat', bd=0,
                              bg=CORES['vermelho_suave'], fg=CORES['texto_principal'], 
                              cursor='hand2', padx=20, pady=10)
    btn_selecionar.grid(row=0, column=1, sticky="e")
    btn_selecionar.bind("<Enter>", lambda e: btn_selecionar.config(bg=CORES['accent']))
    btn_selecionar.bind("<Leave>", lambda e: btn_selecionar.config(bg=CORES['vermelho_suave']))

    label_essenciais_display = tk.Label(frame_essenciais, text="Nenhum selecionado", 
                                       font=("Segoe UI", 10), bg=CORES['bg_card'], 
                                       fg=CORES['texto_secundario'], anchor='w')
    label_essenciais_display.grid(row=0, column=0, sticky="ew", padx=(0, 15))

    # Listas para facilitar atualização de tema
    labels_list = [label_numero, label_cidade, label_data, label_qtd, label_ess]
    entries_list = [entry_numero, entry_cidade, entry_data, entry_quantidade]

    # Botões principais
    frame_botoes = tk.Frame(main_frame, bg=CORES['bg_card'])
    frame_botoes.grid(row=7, column=0, columnspan=2, pady=30)

    btn_gerar = tk.Button(frame_botoes, text="🚀 GERAR PES", font=fonte_botao,
                          command=gerar, relief='flat', bd=0, 
                          bg=CORES['vermelho_primario'], fg='white',
                          cursor='hand2', padx=35, pady=14)
    btn_gerar.pack(side="left", padx=(0, 15))
    btn_gerar.bind("<Enter>", lambda e: btn_gerar.config(bg=CORES['vermelho_hover']))
    btn_gerar.bind("<Leave>", lambda e: btn_gerar.config(bg=CORES['vermelho_primario']))

    btn_apagar = tk.Button(frame_botoes, text="🗑️ LIMPAR", font=fonte_botao,
                           command=apagar, relief='flat', bd=0, 
                           bg=CORES['bg_secundario'], fg=CORES['texto_principal'],
                           cursor='hand2', padx=35, pady=14)
    btn_apagar.pack(side="left")
    btn_apagar.bind("<Enter>", lambda e: btn_apagar.config(bg=CORES['borda']))
    btn_apagar.bind("<Leave>", lambda e: btn_apagar.config(bg=CORES['bg_secundario']))

    # Labels de resultado e status
    # Frame para resultado com fundo destacado
    frame_resultado = tk.Frame(main_frame, bg=CORES['bg_secundario'], relief='flat')
    frame_resultado.grid(row=8, column=0, columnspan=2, sticky="ew", padx=25, pady=(15, 0))
    
    label_resultado = tk.Label(frame_resultado, text="", font=fonte_resultado, 
                              fg=CORES['vermelho_claro'], bg=CORES['bg_secundario'], 
                              wraplength=440, justify='left', padx=15, pady=15)
    label_resultado.pack(fill='both')

    label_status = tk.Label(main_frame, text="", font=("Segoe UI", 10, "bold"), 
                           fg=CORES['sucesso'], bg=CORES['bg_card'])
    label_status.grid(row=9, column=0, columnspan=2, sticky="n", padx=25, pady=(15, 15))

    # Labels de resultado e status
    # Frame para resultado com fundo destacado
    frame_resultado = tk.Frame(main_frame, bg=CORES['bg_secundario'], relief='flat')
    frame_resultado.grid(row=8, column=0, columnspan=2, sticky="ew", padx=25, pady=(15, 0))
    
    label_resultado = tk.Label(frame_resultado, text="", font=fonte_resultado, 
                              fg=CORES['vermelho_claro'], bg=CORES['bg_secundario'], 
                              wraplength=440, justify='left', padx=15, pady=15)
    label_resultado.pack(fill='both')

    label_status = tk.Label(main_frame, text="", font=("Segoe UI", 10, "bold"), 
                           fg=CORES['sucesso'], bg=CORES['bg_card'])
    label_status.grid(row=9, column=0, columnspan=2, sticky="n", padx=25, pady=(15, 15))

    # Rodapé
    rodape_frame = tk.Frame(main_frame, bg=CORES['bg_card'])
    rodape_frame.grid(row=12, column=0, columnspan=2, pady=(15, 25))

    # Linha decorativa acima do rodapé
    linha_rodape = tk.Frame(rodape_frame, height=2, bg=CORES['vermelho_suave'])
    linha_rodape.pack(fill='x', padx=50, pady=(0, 15))

    rodape_texto = tk.Label(rodape_frame, text="Desenvolvido por:", bg=CORES['bg_card'], 
                           fg=CORES['texto_secundario'], font=("Segoe UI", 9))
    rodape_texto.pack(side="left")

    rodape_link = tk.Label(rodape_frame, text="Gabriel Montenegro", bg=CORES['bg_card'], 
                          fg=CORES['vermelho_claro'], cursor="hand2",
                          font=("Segoe UI", 9, "underline"))
    rodape_link.pack(side="left", padx=(5, 0))
    rodape_link.bind("<Button-1>", abrir_link)
    rodape_link.bind("<Enter>", lambda e: rodape_link.config(fg=CORES['vermelho_primario']))
    rodape_link.bind("<Leave>", lambda e: rodape_link.config(fg=CORES['vermelho_claro']))

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