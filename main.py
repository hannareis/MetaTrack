# ======================================================
# Projeto: MetaTrack
# Autor: Hannna Nunes Reis
# Linguagem: Python
# Paradigmas: Imperativo, Funcional e Orientado a Objetos
# Descrição:
# Calcula quanto o estudante precisa tirar na próxima prova
# para alcançar a média mínima de aprovação.
# ======================================================

# --- Paradigma Orientado a Objetos ---
class Estudante:
    def __init__(self, nome, notas, media_minima):
        self.nome = nome
        self.notas = notas
        self.media_minima = media_minima

    def calcular_media_atual(self):
        return sum(self.notas) / len(self.notas) if self.notas else 0

    def precisa_para_passar(self, total_avaliacoes):
        """Retorna quanto o estudante precisa tirar na próxima avaliação."""
        # Paradigma funcional aplicado aqui:
        faltando = total_avaliacoes - len(self.notas)

        if faltando <= 0:
            return 0  # já fez todas as avaliações

        soma_atual = sum(self.notas)
        nota_necessaria = (self.media_minima * total_avaliacoes) - soma_atual
        return max(0, min(10, nota_necessaria))  # limita entre 0 e 10


# --- Paradigma Funcional ---
def filtrar_estudantes_aprovados(estudantes, media_minima):
    """Filtra os estudantes que já atingiram a média mínima."""
    return list(filter(lambda e: e.calcular_media_atual() >= media_minima, estudantes))


# --- Paradigma Imperativo ---
def main():
    print("=== Atingindo a Meta ===")
    nome = input("Digite o nome do estudante: ")

    total_avaliacoes = int(input("Quantas avaliações no total? "))
    media_minima = float(input("Qual é a média mínima para aprovação? "))

    notas = []
    while True:
        nota = input("Digite uma nota (ou pressione Enter para parar): ")
        if nota == "":
            break
        notas.append(float(nota))

    estudante = Estudante(nome, notas, media_minima)

    media_atual = estudante.calcular_media_atual()
    proxima_nota = estudante.precisa_para_passar(total_avaliacoes)

    print("\n=== Resultados ===")
    print(f"Estudante: {estudante.nome}")
    print(f"Média atual: {media_atual:.2f}")
    print(f"Nota necessária na próxima avaliação: {proxima_nota:.2f}")

    if media_atual >= media_minima:
        print("✅ Já atingiu a média mínima! Parabéns!")
    else:
        print("📘 Continue se esforçando — ainda dá tempo de alcançar a média!")


# Execução principal
if __name__ == "__main__":
    main()
