import tkinter as tk
from tkinter import messagebox, font
from datetime import datetime
import pyperclip
import re
import webbrowser

cidades_paraiba = [
    "Água Branca", "Aguiar", "Alagoa Grande", "Alagoa Nova", "Alagoinha",
    "Alcantil", "Algodão de Jandaíra", "Alhandra", "Amparo", "Aparecida",
    "Araçagi", "Arara", "Araruna", "Areia", "Areia de Baraúnas",
    "Areial", "Aroeiras", "Assunção", "Baía da Traição", "Bananeiras",
    "Baraúna", "Barra de Santana", "Barra de Santa Rosa", "Barra de São Miguel",
    "Bayeux", "Belém", "Belém do Brejo do Cruz", "Bernardino Batista",
    "Boa Ventura", "Boa Vista", "Bom Jesus", "Bom Sucesso", "Bonito de Santa Fé",
    "Boqueirão", "Borborema", "Brejo do Cruz", "Brejo dos Santos", "Caaporã",
    "Cabaceiras", "Cabedelo", "Cachoeira dos Índios", "Cacimba de Areia",
    "Cacimba de Dentro", "Cacimbas", "Caicó", "Cajazeiras", "Cajazeirinhas",
    "Caldas Brandão", "Camalaú", "Campina Grande", "Capim", "Caraúbas",
    "Carrapateira", "Casserengue", "Catingueira", "Catolé do Rocha",
    "Caturité", "Conceição", "Condado", "Conde", "Congo", "Coremas",
    "Coxixola", "Cruz do Espírito Santo", "Cubati", "Cuité", "Cuitegi",
    "Cuité de Mamanguape", "Curral de Cima", "Curral Velho", "Damião",
    "Desterro", "Diamante", "Dona Inês", "Duas Estradas", "Emas", "Esperança",
    "Fagundes", "Frei Martinho", "Gado Bravo", "Guarabira", "Gurinhém",
    "Gurjão", "Ibiara", "Igaracy", "Imaculada", "Ingá", "Itabaiana", "Itaporanga",
    "Itapororoca", "Itatuba", "Jacaraú", "Jericó", "João Pessoa", "Juarez Távora",
    "Juazeirinho", "Junco do Seridó", "Juripiranga", "Juru", "Lagoa", "Lagoa de Dentro",
    "Lagoa Seca", "Lastro", "Livramento", "Logradouro", "Lucena", "Mãe d'Água",
    "Malta", "Mamanguape", "Manaíra", "Marcação", "Mari", "Marizópolis",
    "Massaranduba", "Mataraca", "Matinhas", "Mato Grosso", "Maturéia",
    "Mogeiro", "Montadas", "Monte Horebe", "Monteiro", "Mulungu", "Natuba",
    "Nazarezinho", "Nova Floresta", "Nova Olinda", "Nova Palmeira",
    "Olho d'Água", "Olivedos", "Ouro Velho", "Parari", "Passagem",
    "Patos", "Paulista", "Pedra Branca", "Pedra Lavrada", "Pedras de Fogo",
    "Pedro Régis", "Piancó", "Picuí", "Pilar", "Pilões", "Pilõezinhos",
    "Pirpirituba", "Pitimbu", "Pocinhos", "Poço Dantas", "Poço de José de Moura",
    "Pombal", "Prata", "Princesa Isabel", "Puxinanã", "Queimadas",
    "Quixabá", "Remígio", "Riachão", "Riachão do Bacamarte", "Riachão do Poço",
    "Riacho de Santo Antônio", "Riacho dos Cavalos", "Rio Tinto", "Salgadinho",
    "Salgado de São Félix", "Santa Cecília", "Santa Cruz", "Santa Helena",
    "Santa Inês", "Santa Luzia", "Santa Rita", "Santa Teresinha", "Santana de Mangueira",
    "Santana dos Garrotes", "Santarém", "Santo André", "São Bentinho",
    "São Bento", "São Domingos de Pombal", "São Domingos do Cariri",
    "São Francisco", "São João do Cariri", "São João do Rio do Peixe",
    "São João do Tigre", "São José da Lagoa Tapada", "São José de Caiana",
    "São José de Espinharas", "São José de Piranhas", "São José de Princesa",
    "São José do Bonfim", "São José do Brejo do Cruz", "São José do Sabugi",
    "São José dos Cordeiros", "São José dos Ramos", "São Mamede",
    "São Miguel de Taipu", "São Sebastião de Lagoa de Roça",
    "São Sebastião do Umbuzeiro", "Sapé", "Serra Branca", "Serra da Raiz",
    "Serra Grande", "Serra Redonda", "Serraria", "Sertãozinho", "Sobrado",
    "Solânea", "Soledade", "Sossêgo", "Sousa", "Sumé", "Taperoá",
    "Tavares", "Teixeira", "Tenório", "Triunfo", "Uiraúna", "Umbuzeiro",
    "Vieirópolis", "Vista Serrana", "Zabelê"
]

def limpar_espacos(texto):
    texto = texto.strip()
    texto = re.sub(r'\s+', ' ', texto)
    return texto

def gerar_nome_arquivo(numero, cidade, data, quantidade):
    data_formatada = data.strftime('%d-%m')
    cidade_limpa = limpar_espacos(cidade).upper()
    numero_limpo = numero.strip()
    quantidade_limpa = quantidade.strip()
    nome_arquivo = f"PES {numero_limpo} {cidade_limpa} {data_formatada} ({quantidade_limpa})"
    return nome_arquivo

def parse_data(data_str):
    if len(data_str) == 4 and data_str.isdigit():
        data_str = data_str[:2] + "-" + data_str[2:]
    try:
        data = datetime.strptime(data_str + "-2025", "%d-%m-%Y")
        return data
    except ValueError:
        return None

def gerar():
    numero = entry_numero.get()
    cidade = entry_cidade.get()
    data_str = entry_data.get()
    quantidade = entry_quantidade.get()

    # Validação de campos obrigatórios
    if not all([numero, cidade, data_str, quantidade]):
        messagebox.showwarning("Atenção", "Por favor, preencha todos os campos!")
        return

    data = parse_data(data_str)
    if not data:
        messagebox.showerror("Erro", "Data no formato errado! Use DD-MM ou DDMM")
        return

    nome_arquivo = gerar_nome_arquivo(numero, cidade, data, quantidade)
    pyperclip.copy(nome_arquivo)
    
    # Feedback visual
    label_resultado.config(text=nome_arquivo, fg="#2E7D32")
    label_status.config(text="✓ Copiado para área de transferência!", fg="#2E7D32")
    
    # Limpar status após 3 segundos
    root.after(3000, lambda: label_status.config(text=""))

def apagar():
    entry_numero.delete(0, tk.END)
    entry_cidade.delete(0, tk.END)
    entry_data.delete(0, tk.END)
    entry_quantidade.delete(0, tk.END)
    label_resultado.config(text="")
    label_status.config(text="")
    entry_numero.focus()

def foco_proximo(event, proximo_widget):
    proximo_widget.focus()
    return "break"

def on_enter_button(button, hover_color):
    button.config(bg=hover_color)

def on_leave_button(button, original_color):
    button.config(bg=original_color)

def completar_cidade(event):
    texto_atual = entry_cidade.get().lower()
    if not texto_atual:
        return "break"

    # Buscar as cidades que começam com o texto digitado
    correspondencias = [cidade for cidade in cidades_paraiba if cidade.lower().startswith(texto_atual)]
    if correspondencias:
        # Completa com a primeira correspondência
        entry_cidade.delete(0, tk.END)
        entry_cidade.insert(0, correspondencias[0])
        # Seleciona o texto a partir do ponto digitado até o fim para facilitar substituição
        entry_cidade.select_range(len(texto_atual), tk.END)
    return "break"

def abrir_link(event):
    webbrowser.open_new("https://www.linkedin.com/in/gabriel-montenegro7/")

# Configuração da janela principal
root = tk.Tk()
root.title("Gerador de PES")
root.geometry("500x650")
root.minsize(480, 600)
root.configure(bg='#f5f5f5')

# Centralizar janela na tela
root.eval('tk::PlaceWindow . center')

# Fontes modernas
fonte_titulo = font.Font(family="Segoe UI", size=18, weight="bold")
fonte_label = font.Font(family="Segoe UI", size=11, weight="normal")
fonte_entry = font.Font(family="Segoe UI", size=11)
fonte_botao = font.Font(family="Segoe UI", size=11, weight="bold")
fonte_resultado = font.Font(family="Segoe UI", size=10, weight="bold")
fonte_status = font.Font(family="Segoe UI", size=9)

# Frame principal centralizado
main_frame = tk.Frame(root, bg='#ffffff', relief='raised', bd=1)
main_frame.pack(expand=True, fill='both', padx=30, pady=30)

# Configurar grid do frame principal
main_frame.grid_rowconfigure(8, weight=1)  # Espaço para resultado
for i in range(2):
    main_frame.grid_columnconfigure(i, weight=1)

# Título
titulo = tk.Label(main_frame, text="📁 GERADOR DE PES", 
                 font=fonte_titulo, bg='#ffffff', fg='#1976D2')
titulo.grid(row=0, column=0, columnspan=2, pady=(20, 30), sticky='n')

# Separador visual
separator = tk.Frame(main_frame, height=2, bg='#e0e0e0')
separator.grid(row=1, column=0, columnspan=2, sticky='ew', padx=20, pady=(0, 20))

# Configuração dos campos
padxy = {"padx": 20, "pady": 8}

# Campo Número
tk.Label(main_frame, text="Número:", font=fonte_label, bg='#ffffff', fg='#424242').grid(
    row=2, column=0, sticky="w", **padxy)
entry_numero = tk.Entry(main_frame, font=fonte_entry, relief='solid', bd=1, 
                       highlightthickness=2, highlightcolor='#1976D2')
entry_numero.grid(row=2, column=1, sticky="ew", **padxy)
entry_numero.bind("<Return>", lambda e: foco_proximo(e, entry_cidade))

# Campo Cidade
tk.Label(main_frame, text="Cidade:", font=fonte_label, bg='#ffffff', fg='#424242').grid(
    row=3, column=0, sticky="w", **padxy)
entry_cidade = tk.Entry(main_frame, font=fonte_entry, relief='solid', bd=1,
                       highlightthickness=2, highlightcolor='#1976D2')
entry_cidade.grid(row=3, column=1, sticky="ew", **padxy)
entry_cidade.bind("<Return>", lambda e: foco_proximo(e, entry_data))
entry_cidade.bind("<Tab>", completar_cidade)

# Campo Data
tk.Label(main_frame, text="Data:", font=fonte_label, bg='#ffffff', fg='#424242').grid(
    row=4, column=0, sticky="w", **padxy)
entry_data = tk.Entry(main_frame, font=fonte_entry, relief='solid', bd=1,
                     highlightthickness=2, highlightcolor='#1976D2')
entry_data.grid(row=4, column=1, sticky="ew", **padxy)
entry_data.bind("<Return>", lambda e: foco_proximo(e, entry_quantidade))

# Campo Quantidade
tk.Label(main_frame, text="Quantidade:", font=fonte_label, bg='#ffffff', fg='#424242').grid(
    row=6, column=0, sticky="w", **padxy)
entry_quantidade = tk.Entry(main_frame, font=fonte_entry, relief='solid', bd=1,
                           highlightthickness=2, highlightcolor='#1976D2')
entry_quantidade.grid(row=6, column=1, sticky="ew", **padxy)
entry_quantidade.bind("<Return>", lambda e: gerar())

# Frame para botões
frame_botoes = tk.Frame(main_frame, bg='#ffffff')
frame_botoes.grid(row=7, column=0, columnspan=2, pady=25)

# Botão Gerar (principal)
btn_gerar = tk.Button(frame_botoes, text="🚀 Gerar PES", font=fonte_botao, 
                     command=gerar, relief='flat', bd=0, bg='#4CAF50', fg='white',
                     cursor='hand2', padx=25, pady=10)
btn_gerar.pack(side="left", padx=(0, 15))

# Efeitos hover para botão gerar
btn_gerar.bind("<Enter>", lambda e: on_enter_button(btn_gerar, '#45A049'))
btn_gerar.bind("<Leave>", lambda e: on_leave_button(btn_gerar, '#4CAF50'))
btn_gerar.bind("<Return>", lambda e: gerar())

# Botão Apagar (secundário)
btn_apagar = tk.Button(frame_botoes, text="🗑️ Limpar", font=fonte_botao, 
                      command=apagar, relief='flat', bd=0, bg='#FF5722', fg='white',
                      cursor='hand2', padx=25, pady=10)
btn_apagar.pack(side="left")

btn_apagar.bind("<Enter>", lambda e: on_enter_button(btn_apagar, '#E64A19'))
btn_apagar.bind("<Leave>", lambda e: on_leave_button(btn_apagar, '#FF5722'))
btn_apagar.bind("<Return>", lambda e: apagar())

# Label resultado
label_resultado = tk.Label(main_frame, text="", font=fonte_resultado, fg="#333333", bg='#ffffff', wraplength=420)
label_resultado.grid(row=8, column=0, columnspan=2, sticky="n", padx=20, pady=(0, 5))

# Label status (feedback)
label_status = tk.Label(main_frame, text="", font=fonte_status, fg="#4CAF50", bg='#ffffff')
label_status.grid(row=9, column=0, columnspan=2, sticky="n", padx=20, pady=(10, 10))

# Rodapé centralizado dentro da caixa branca
rodape_frame = tk.Frame(main_frame, bg='#ffffff')
rodape_frame.grid(row=10, column=0, columnspan=2, pady=(10, 20))

rodape_texto = tk.Label(rodape_frame, text="Desenvolvido por:", bg='#ffffff', fg='#555555', font=("Segoe UI", 9))
rodape_texto.pack(side="left")

rodape_link = tk.Label(rodape_frame, text="Gabriel Montenegro", bg='#ffffff', fg="blue", cursor="hand2",
                       font=("Segoe UI", 9, "underline"))
rodape_link.pack(side="left")
rodape_link.bind("<Button-1>", abrir_link)

# Foco inicial no campo número
entry_numero.focus()

root.mainloop()