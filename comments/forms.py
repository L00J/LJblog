
from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment # form 关联的 Model
        fields = ['name', 'email', 'url', 'text']
        # fields 表示需要渲染的字段，这里需要渲染user_name、user_email、body
        # 这样渲染后表单会有三个文本输入框，分别是输入user_name、user_email、body的输入框


        widgets = {
            # 为各个需要渲染的字段指定渲染成什么html组件，主要是为了添加css样式。
            # 例如 user_name 渲染后的html组件如下：
            # <input type="text" class="form-control" placeholder="Username" aria-describedby="sizing-addon1">

            'name': forms.TextInput(attrs={
                'placeholder': "请输入昵称",
            }),
            'email': forms.TextInput(attrs={

                'placeholder': "邮箱信息不会被公开",
            }),
            'url': forms.TextInput(attrs={

                'placeholder': " 个人网站地址(选填)",
            }),
            'text': forms.Textarea(attrs={

                'placeholder': '我来说两句~',
                'cols':85,
            }),
        }
