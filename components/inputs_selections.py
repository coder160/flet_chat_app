import flet as ft

class Input:
    def textfield(lbl:str, f=False, fn=None, h=None,se=False,miL=1,mxL=None,fill=True,xp=True):
        return ft.TextField(label=lbl, autofocus=f, on_submit=fn,filled=fill,expand=xp,
                            hint_text=h,shift_enter=se,min_lines=miL,max_lines=mxL)
