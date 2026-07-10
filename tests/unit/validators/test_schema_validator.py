def test_should_accept_valid_uf():

    dataframe = pd.DataFrame(
        {
            "UF PRESTADOR": ["SP"],
            "STATUS": ["PENDENTE"],
            "AREA DA PENDENCIA": [
                "RELACIONAMENTO"
            ]
        }
    )

    validator.validate(dataframe)