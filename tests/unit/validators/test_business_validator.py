def test_should_accept_valid_schema():

    dataframe = pd.DataFrame(
        columns=[
            "USUARIO",
            "PROCEDIMENTO",
            "NOME DO PRESTADOR",
            "UF PRESTADOR",
            "CIDADE PRESTADOR",
            "VALOR DEPOSITO",
            "DATA DEPOSITO",
            "OBRIGACAO",
            "AREA DA PENDENCIA",
            "STATUS"
        ]
    )

    validator.validate(dataframe)