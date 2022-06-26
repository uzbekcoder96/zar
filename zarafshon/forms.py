from django import forms

from django.contrib.auth.models import User


from zarafshon.models import Messages

class MessagesForm(forms.Form):

    sender_email = forms.EmailField(max_length=100,label='', widget=forms.EmailInput(attrs={'placeholder': 'Emailingiz *', 'class': 'form-control col-sm-6 mb-3'}))
    sender_name = forms.CharField(max_length=200, label='', widget=forms.TextInput(attrs={'placeholder': 'Ismingiz *', 'class': 'form-control  col-sm-6 mb-3'}))
    sender_message = forms.CharField(max_length=500, label='', widget=forms.Textarea(attrs={'class': 'form-control textarea col-sm-12'}))

    def save(self):

        sender_email = self.cleaned_data['sender_email']
        sender_name = self.cleaned_data['sender_name']
        sender_message = self.cleaned_data['sender_message']

        message = Messages.objects.create(
            sender_email = sender_email,
            sender_name = sender_name,
            sender_message = sender_message
        )

        message.save()
    




class SignUpForm(forms.ModelForm):
    username = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'placeholder': 'Ismingiz *', 'class': 'input100'}))
    email = forms.EmailField(max_length=200,help_text='Iltimos to\'g\'ri email kiriting.', widget=forms.TextInput(attrs={'placeholder': 'Emailingiz *', 'class': 'input100'}))
    password = forms.CharField(max_length=200, widget=forms.PasswordInput(attrs={'placeholder': 'Password *', 'class': 'input100'}))
    password_confirmation = forms.CharField(max_length=200, widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password *', 'class': 'input100'}))
    
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password_confirmation', )    


    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('Bu nomdagi foydalanuvchi allaqochon ro\'yxatdan o\'tgan')
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Ushbu email sistemada ro\'yxatdan o\'tkazilgan.')
        return email

    def clean_password(self):
        password = self.cleaned_data['password']
        if len(password) < 8:
            raise forms.ValidationError('Parol end kamida 8 ta belgidan iborat bo\'lishi kerak') 
        if password.isnumeric():
            raise forms.ValidationError('Parolda eng kamida bitta harf ishtirok etishi kerak')
        if password.isalpha():
            raise forms.ValidationError('Parolda end kamida bitta son ishtirok etishi kerak')  

        return password                 
    
    def clean_confirm_password(self):
        password = self.data['password']
        confirm_password = self.cleaned_data['password_confirmation']
        if password != confirm_password:
            raise forms.ValidationError('Tasdiqlash paroli notog\'ri')

        return confirm_password

    def save(self):

        username = self.cleaned_data['username']
        email = self.cleaned_data['email']
        password = self.cleaned_data['password']

        user = User.objects.create(
            username = username,
            email = email,
            
        )
        user.set_password(password)
        user.save()    

class LoginForm(forms.Form):
    username = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'placeholder': 'Ismingiz *', 'class': 'input100'})) # error_messages={"required": "", "invalid": ""}
    password = forms.CharField(max_length=200, widget=forms.PasswordInput(attrs={'placeholder': 'Password *', 'class': 'input100'}))

    def clean_username(self):
        username = self.cleaned_data['username']
        if not User.objects.filter(username=username).exists():
            raise forms.ValidationError('Ushbu username tizimda ro\'yxatdan o\'tkazilmagan.')
        return username
    
    def clean_password(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data['password']
        if username:
            user = User.objects.filter(username=username).first()
            if user:
                if not user.check_password(password):
                    raise forms.ValidationError('Parol notog\'ri kiritildi.')
        return password
