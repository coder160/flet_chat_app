import flet as ft


class Display:

    def texto(t:str, s=24, c= ft.colors.WHITE, bgc= ft.colors.GREEN_700, w=ft.FontWeight.BOLD, i=False):
        return ft.Text(value = t, size= s, color= c, 
                       bgcolor= bgc, weight= w, italic=i)
    

