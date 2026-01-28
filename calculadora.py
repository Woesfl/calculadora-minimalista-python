import customtkinter as ctk

# Configurações iniciais do visual
ctk.set_appearance_mode("dark")  # Começa no dark mode pq é mais estiloso
ctk.set_default_color_theme("blue") 

class CalculadoraMinimalista(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Título e tamanho da janela
        self.title("Minha Calc")
        self.geometry("300x450")

        # Variável que guarda o que a gente digita
        self.equacao = ""

        # --- O Visor da Calculadora ---
        self.visor = ctk.CTkEntry(self, width=280, height=70, 
                                  font=("Arial", 30), 
                                  justify="right",
                                  border_width=0,
                                  fg_color="transparent")
        self.visor.pack(pady=20)

        # --- O Botão de Trocar Tema ---
        # Fiz aqui em cima pra ficar fácil de achar
        self.btn_tema = ctk.CTkButton(self, text="Mudar Tema", 
                                      command=self.trocar_tema,
                                      height=20, width=100,
                                      fg_color="gray", hover_color="#555")
        self.btn_tema.pack(pady=5)

        # --- Grid de Botões ---
        self.frame_botoes = ctk.CTkFrame(self, fg_color="transparent")
        self.frame_botoes.pack(expand=True, fill="both", padx=10, pady=10)

        # Lista com os textos dos botões
        botoes = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'C', '0', '=', '+'
        ]

        # Criando os botões com um loop pra não cansar a mão
        row = 0
        col = 0
        for texto in botoes:
            comando = lambda t=texto: self.clique_botao(t)
            btn = ctk.CTkButton(self.frame_botoes, text=texto, 
                                width=60, height=60, 
                                font=("Arial", 18, "bold"),
                                command=comando)
            btn.grid(row=row, column=col, padx=5, pady=5)
            
            col += 1
            if col > 3:
                col = 0
                row += 1

    # Lógica de quando a gente clica em algo
    def clique_botao(self, tecla):
        if tecla == "=":
            try:
                # O eval faz a mágica da matemática pra gente
                resultado = str(eval(self.equacao))
                self.visor.delete(0, "end")
                self.visor.insert(0, resultado)
                self.equacao = resultado
            except:
                self.visor.delete(0, "end")
                self.visor.insert(0, "Erro")
                self.equacao = ""
        
        elif tecla == "C":
            # Limpa tudo se eu errar
            self.visor.delete(0, "end")
            self.equacao = ""
        
        else:
            # Vai juntando os números na "memória"
            self.equacao += tecla
            self.visor.delete(0, "end")
            self.visor.insert(0, self.equacao)

    # Função que troca do claro pro escuro e vice-versa
    def trocar_tema(self):
        if ctk.get_appearance_mode() == "Dark":
            ctk.set_appearance_mode("light")
        else:
            ctk.set_appearance_mode("dark")

# Rodando o projeto
if __name__ == "__main__":
    app = CalculadoraMinimalista()
    app.mainloop()