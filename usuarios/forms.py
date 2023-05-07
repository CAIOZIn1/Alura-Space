from django import forms


class LoginForms(forms.Form):
    nome_login = forms.CharField(
        label="Nome de login:",
        required=True,
        max_length=50,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ex.: Caio Lindo"
            }
        )
    )
    senha = forms.CharField(
        label="Senha:",
        required=True,
        max_length=20,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Digite sua senha"
            }
        )
    )


class CadastroForms(forms.Form):
    nome_cadastro = forms.CharField(
        label="Nome de Cadastro:",
        required=True,
        max_length=50,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ex.: CaioLindo"
            }
        )
    )
    email = forms.EmailField(
        label="Email:",
        required=True,
        max_length=70,
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ex.: caiolindo@gmail.com"
            }
        )
    )
    senha1 = forms.CharField(
        label="senha:",
        required=True,
        max_length=20,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Digite sua senha"
            }
        )
    )
    senha2 = forms.CharField(
        label="Confirme sua senha:",
        required=True,
        max_length=20,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Digite sua senha novamente"
            }
        )
    )

    def clean_nome_cadastro(self):
        nome = self.cleaned_data.get('nome_cadastro')

        if nome:
            nome = nome.strip()

            if not ' ' in nome:
                return nome

            raise forms.ValidationError(
                "Não é possível inserir espaços dentro do campo nome!")

    def clean_senha2(self):
        senha_1 = self.cleaned_data.get('senha1')
        senha_2 = self.cleaned_data.get('senha2')

        if senha_1 and senha_2:
            if senha_1 != senha_2:
                raise forms.ValidationError('Senhas não são iguais')
            else:
                return senha_2
