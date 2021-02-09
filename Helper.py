def formata_moeda(valor: float):
    """
    Cdds
    onverte o valor float para o padrao BR com duas casa deicmas
    :param valor: no formato float
    :return: uma string do valor no formata padrao do br
    """
    return f'R$ {valor:,.2f}'

