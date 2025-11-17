import json

def to_dict(obj):
    """Converte qualquer objeto em dicionário, incluindo objetos aninhados."""
    if isinstance(obj, (str, int, float, bool, type(None))):
        return obj

    if isinstance(obj, dict):
        return {k: to_dict(v) for k, v in obj.items()}

    if isinstance(obj, list):
        return [to_dict(i) for i in obj]

    # Caso seja um objeto com atributos
    if hasattr(obj, "__dict__"):
        return {k: to_dict(v) for k, v in obj.__dict__.items()}

    return str(obj)  # fallback

def salvar_personagem(personagem, caminho="personagem.json"):
    data = to_dict(personagem)
    with open(caminho, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
